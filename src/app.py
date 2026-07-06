import os
import streamlit as st
import requests
from utils import (
    montar_mensagens_sistema,
    detectar_intent,
    aplicar_guardrails_produto,
    aviso_legal,
)

# ----------------------------
# Configurações da OpenRouter
# ----------------------------
OPENROUTER_API_KEY=os.getenv("OPENROUTER_API_KEY", "")  # Defina no ambiente
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
MODEL_NAME = "openai/gpt-4o-mini"   # Pode trocar por qualquer modelo OpenRouter
TEMPERATURE = 0.2                   # Baixa criatividade → mais segurança
MAX_TOKENS = 512

def query_openrouter(messages: list[dict]) -> str:
    """Envia a lista de mensagens para a API da OpenRouter e retorna o texto."""
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "temperature": TEMPERATURE,
        "max_tokens": MAX_TOKENS,
    }
    try:
        resp = requests.post(
            f"{OPENROUTER_BASE_URL}/chat/completions",
            headers=headers,
            json=payload,
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        return f"⚠️ Erro ao consultar a LLM: {e}"

# ----------------------------
# Interface Streamlit
# ----------------------------
st.set_page_config(
    page_title="Agente Financeiro Jaime",
    page_icon="💰",
    layout="centered",
)

st.title("🤖 Agente Financeiro Inteligente – Jaime")
st.caption("Desafio DIO • Powered by OpenRouter + Streamlit")

# Histórico de chat (apenas user/assistant; o system vem de utils)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe o histórico
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input do usuário
if prompt := st.chat_input("Digite sua pergunta sobre finanças..."):
    # 1️⃣ Registra a pergunta do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2️⃣ (Opcional) detecta intenção - pode ser usado para logging ou ações específicas
    intencao = detectar_intent(prompt)
    # st.sidebar.write(f"Intenção detectada: {intencao}")  # descomente se quiser ver

    # 3️⃣ Monta as mensagens para a LLM: system + histórico
    mensagens = montar_mensagens_sistema() + [
        {"role": m["role"], "content": m["content"]} for m in st.session_state.messages
    ]

    # 4️⃣ Consulta a LLM
    with st.chat_message("assistant"):
        with st.spinner("Consultando o modelo..."):
            resposta_raw = query_openrouter(mensagens)
        # 5️⃣ Aplica guardrails de produto
        resposta_segura = aplicar_guardrails_produto(resposta_raw)
        # 6️⃣ Anexa aviso legal
        resposta_final = resposta_segura + aviso_legal()
        st.markdown(resposta_final)

    # 7️⃣ Armazena a resposta no histórico
    st.session_state.messages.append({"role": "assistant", "content": resposta_final})

# Rodapé com créditos
st.markdown("---\n")
st.markdown(
    """
    **Desenvolvido para o desafio DIO**
    *Base de conhecimento:* `data/` (transações, histórico, perfil, produtos)
    *LLM:* OpenRouter (`{model}`)
    *Interface:* Streamlit
    """
    .format(model=MODEL_NAME)
)
