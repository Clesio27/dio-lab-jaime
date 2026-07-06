# Código da Aplicação

Esta pasta contém o código do seu agente de vendas.

## Estrutura Jaime

```
src/
├── app.py              # Aplicação principal (interface Streamlit)
│                       # - Carrega as variáveis de ambiente (OPENROUTER_API_KEY, etc.)
│                       # - Define o layout da página, os componentes de input e output
│                       # - Orquestra a chamada ao modelo LLM via OpenRouter
│                       # - Aplica guardrails e formata a resposta final
│
├── utils.py            # Módulo de funções de apoio
│                       # - load_mock_data(): lê os arquivos JSON/CSV da pasta data/
│                       # - build_prompt(transacao, historico, perfil, produto): monta o prompt
│                       # - call_openrouter(messages): envia a requisição à API da OpenRouter
│                       # - aplicar_guardrails(resposta): filtra e ajusta o texto de saída
│                       # - helpers de logging, tratamento de erros e formatação de moeda/data
│
└── requirements.txt    # Dependências necessárias

```

## Exemplo de requirements.txt

```
streamlit
openai
python-dotenv
pandas   # (opcional, caso utilize DataFrames nos utils)

```

## Como Rodar o agente Jaime

1. Clone ou copie o repositório para a sua máquina/local de desenvolvimento.  
2. Instale as dependências (recomenda‑se usar um virtualenv):

```
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   
```
3. Configure a chave da OpenRouter  
   - Crie um arquivo .env na raiz do projeto (ou defina a variável de ambiente diretamente):


```
   OPENROUTER_API_KEY=sk-or-...sua_chave_aqui...
   
```


   - Se preferir, exporte no terminal antes de iniciar o app:

```
   export OPENROUTER_API_KEY="sk-or-...sua_chave_aqui..."
   
```

4. Inicie a aplicação Streamlit:

```
   streamlit run src/app.py
   
```
   - O Streamlit imprimirá algo como:
```
     You can now view your Streamlit app in your browser.
     Local URL: http://localhost:8501
     Network URL: http://192.168.x.x:8501
   
```

 - Abra o Local URL no navegador para interagir com o Jaime.

5. Parar a aplicação  
   Pressione Ctrl+C no terminal onde o streamlit run está em execução.

---

Dicas rápidas de manutenção

⚠️ Erro ao consultar a LLM: 401

• Sintoma: ⚠️ Erro ao consultar a LLM: 401

• Causa provável: Chave da OpenRouter ausente ou inválida

• Solução: Verifique OPENROUTER_API_KEY no .env ou no ambiente.

ModuleNotFoundError: No module named 'streamlit'

• Sintoma: ModuleNotFoundError: No module named 'streamlit'
