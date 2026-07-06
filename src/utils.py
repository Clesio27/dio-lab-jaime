import os
import json
import pandas as pd
from typing import List, Dict

# ----------------------------------------------------------------------
# Caminhos dos dados (relativos à pasta src/)
# ----------------------------------------------------------------------
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
TRANSACOES_PATH   = os.path.join(DATA_DIR, "transacoes.csv")
HISTORICO_PATH    = os.path.join(DATA_DIR, "historico_atendimento.csv")
PERFIL_PATH       = os.path.join(DATA_DIR, "perfil_investidor.json")
PRODUTOS_PATH     = os.path.join(DATA_DIR, "produtos_financeiros.json")


# ----------------------------------------------------------------------
# Leitura dos dados mockados
# ----------------------------------------------------------------------
def load_transacoes() -> pd.DataFrame:
    try:
        return pd.read_csv(TRANSACOES_PATH, parse_dates=["data"])
    except Exception as e:
        raise RuntimeError(f"Erro ao ler transacoes.csv: {e}")


def load_historico() -> pd.DataFrame:
    try:
        return pd.read_csv(HISTORICO_PATH, parse_dates=["data"])
    except Exception as e:
        raise RuntimeError(f"Erro ao ler historico_atendimento.csv: {e}")


def load_perfil() -> Dict:
    try:
        with open(PERFIL_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        raise RuntimeError(f"Erro ao ler perfil_investidor.json: {e}")


def load_produtos() -> List[Dict]:
    try:
        with open(PRODUTOS_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        raise RuntimeError(f"Erro ao ler produtos_financeiros.json: {e}")


# ----------------------------------------------------------------------
# Construção do contexto (enviado como "system" ao LLM)
# ----------------------------------------------------------------------
def montar_mensagens_sistema() -> list[dict]:
    """
    Retorna a lista de mensagens que será usada como "system" no prompt da LLM.
    Inclui:
    - Persona do agente Jaime
    - Contexto resumido (últimas transações, histórico, perfil, produtos)
    """
    persona = (
        "Você é Jaime, um agente financeiro prestativo, claro e objetivo. "
        "Seu papel é ajudar o usuário a organizar suas finanças, entender seus gastos, "
        "sugerir produtos de investimento conservadores e garantir que ele esteja ciente "
        "dos riscos envolvidos. Sempre responda em português do Brasil, de forma amigável "
        "e profissional. Nunca recomende produtos de alto risco sem deixar claro o aviso."
    )

    # Construir contexto resumido
    partes = [persona]

    # Transações (últimas 10 linhas)
    df_tx = load_transacoes()
    if not df_tx.empty:
        partes.append(
            "### Histórico de Transações (últimas linhas)\n"
            + df_tx.tail(10).to_csv(index=False)
        )

    # Histórico de atendimentos
    df_hist = load_historico()
    if not df_hist.empty:
        partes.append(
            "### Histórico de Atendimentos\n" + df_hist.to_csv(index=False)
        )

    # Perfil do investidor
    perfil = load_perfil()
    if perfil:
        partes.append(
            "### Perfil do Investidor\n"
            + json.dumps(perfil, indent=2, ensure_ascii=False)
        )

    # Produtos financeiros
    produtos = load_produtos()
    if produtos:
        partes.append(
            "### Produtos Financeiros Disponíveis\n"
            + json.dumps(produtos, indent=2, ensure_ascii=False)
        )

    return [{"role": "system", "content": "\n\n".join(partes)}]


# ----------------------------------------------------------------------
# Detecção simples de intenção (para logging interno)
# ----------------------------------------------------------------------
INTENT_KEYWORDS = {
    "reserva": ["reserva", "emergência", "fundo de emergência"],
    "meta": ["meta", "objetivo", "apartamento", "casa", "carro", "viagem"],
    "extrato": ["extrato", "saldo", "gastos", "receitas"],
    "produto": ["cdb", "tesouro", "lc", "lci", "lca", "renda fixa"],
    "aporte": ["aporte", "investir", "alocar", "depositar"],
}


def detectar_intent(texto: str) -> list[str]:
    """Retorna a lista de intenções encontradas no texto (baseado em palavras‑chave)."""
    texto_low = texto.lower()
    encontradas = []
    for intent, palavras in INTENT_KEYWORDS.items():
        if any(p in texto_low for p in palavras):
            encontradas.append(intent)
    return encontradas or ["geral"]


# ----------------------------------------------------------------------
# Guardrails de produto (evita menção a produtos não listados)
# ----------------------------------------------------------------------
def aplicar_guardrails_produto(resposta: str) -> str:
    """
    Verifica se a resposta menciona algum produto que não esteja na lista
    de produtos_financeiros.json. Se encontrar, substitui por mensagem de segurança.
    """
    produtos = load_produtos()  # utils.py precisa ser importado para isso funcionar
    nomes_validos = {p.get("nome", "").lower() for p in produtos}

    # Heurística simples: procura por termos comuns de produto
    palavras = resposta.lower().split()
    suspeitas = [w.strip(",.!?:;") for w in palavras if w in {"cdb", "tesouro", "lci", "lca", "lc", "renda fixa"}]

    for p in suspeitas:
        if p not in nomes_validos:
            # Se o agente inventou um produto não listado, bloqueamos e avisamos
            return (
                "Desculpe, mas não há registro desse produto na lista de opções disponíveis "
                "para seu perfil. Vamos focar nos produtos que preservam seu capital, como o "
                "Tesouro Selic ou o CDB de liquidez diária."
            )
    return resposta


# ----------------------------------------------------------------------
# Avisos legais
# ----------------------------------------------------------------------
def aviso_legal() -> str:
    """Retorna o aviso legal padrão a ser acrescentado ao final de cada resposta."""
    return (
        "\n\n---\n"
        "*Aviso:* Esta conversa é meramente informativa e não constitui recomendação de investimento. "
        "Consulte um profissional qualificado antes de tomar qualquer decisão financeira."
    )


# ----------------------------------------------------------------------
# Funções auxiliares de dados (caso precisem ser usadas diretamente nos utils)
# ----------------------------------------------------------------------
def get_usuario_id() -> str:
    """Retorna o ID do usuário a partir do perfil (se existir)."""
    perfil = load_perfil()
    return str(perfil.get("id", "desconhecido"))


def get_limite_risco() -> float:
    """Retorna o limite de risco aceitável do perfil (ex: 0.02 para 2%)."""
    perfil = load_perfil()
    return float(perfil.get("limite_risco", 0.02))
