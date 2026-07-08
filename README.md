# 🤖 Jaime - Agente Financeiro Inteligente com IA Generativa

Jaime é um agente financeiro inteligente baseado em IA Generativa, projetado para auxiliar usuários na gestão pessoal de finanças, oferecendo:

- **Análise de gastos**: identificação de padrões e sugestões de economia.  
- **Planejamento de metas**: criação de planos personalizados para alcançar objetivos financeiros.  
- **Recomendações de investimento**: sugestões alinhadas ao perfil de risco e objetivos do usuário.  
- **Alertas inteligentes**: notificações proativas sobre limites de gasto, vencimentos e oportunidades.  
- **Educação financeira**: explicações simples e personalizadas sobre conceitos e produtos.

## Como funciona

1. **Coleta de dados** – Jaime consome os dados fornecidos pelo usuário (transações, perfil, objetivos) contidos na pasta `data/`.  
2. **Base de conhecimento** – Utiliza arquivos CSV e JSON com informações de produtos, histórico e perfil.  
3. **Engine de IA** – Um modelo de linguagem (LLM) recebe um *system prompt* que define o comportamento de Jaime, garantindo respostas seguras, alinhadas ao perfil e livres de alucinações.  
4. **Interface** – Protótipo desenvolvido com Streamlit (pasta `src/`), permitindo interação via chat.  
5. **Avaliação** – Métricas de assertividade, taxa de respostas seguras e aderência ao perfil são monitoradas (ver `docs/04-metricas.md`).

## Estrutura do repositório

```
📁 dio-lab-jaime/
│
├── 📄 README.md
│
├── 📁 data/                          # Dados mockados para o agente
│   ├── historico_atendimento.csv     # Histórico de atendimentos (CSV)
│   ├── perfil_investidor.json        # Perfil do cliente (JSON)
│   ├── produtos_financeiros.json     # Produtos disponíveis (JSON)
│   └── transacoes.csv                # Histórico de transações (CSV)
│
├── 📁 docs/                          # Documentação do projeto
│   ├── 01-documentacao-agente.md     # Caso de uso e arquitetura
│   ├── 02-base-conhecimento.md       # Estratégia de dados
│   ├── 03-prompts.md                 # Engenharia de prompts
│   ├── 04-metricas.md                # Avaliação e métricas
│   └── 05-pitch.md                   # Roteiro do pitch
│
├── 📁 src/                           # protótipo funcional (Streamlit)
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
├── 📁 assets/                        # Imagens e screenshots
│   └── ...
│
└── 📁 examples/                      # Referências e exemplos
    └── README.md
```
Exemplo de requirements.txt
---

```
streamlit
openai
python-dotenv
pandas   # (opcional, caso utilize DataFrames nos utils)

```
Como rodar o agente Jaime
---

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

• Causa provável: Dependência não instalada

• Solução: Rode pip install -r requirements.txt.

Página em branco ou “connection refused”

• Sintoma: Página em branco ou “connection refused”

• Causa provável: Streamlit não está rodando ou porta ocupada

• Solução: Confira o output do terminal; libere a porta 8501 ou use --server.port 8502.

ScriptRunContext warnings

• Sintoma: ScriptRunContext warnings

• Causa provável: Execução via python src/app.py ao invés de streamlit run

• Solução: Sempre use streamlit run src/app.py.

Arquivos de dados não encontrados (FileNotFoundError)

• Sintoma: Arquivos de dados não encontrados (FileNotFoundError)

• Causa provável: Caminho relativo incorreto

• Solução: Execute a partir da raiz do projeto ou ajuste os paths em utils.py usando os.path.join(os.path.dirname(__file__), "..", "data", "arquivo.csv").

Com essas instruções você terá o agente Jaime totalmente funcional, pronto para demonstrar o fluxo de atendimento de vendas utilizando a LLM da OpenRouter dentro de uma interface Streamlit amigável. Boa experimentação! 🚀
