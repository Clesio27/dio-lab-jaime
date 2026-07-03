# Código da Aplicação

Esta pasta contém o código do seu agente financeiro.

## Estrutura Jaime

```
src/
├── app.py              # Aplicação principal; Configurações (API keys, etc.)
├── utils.py            # Funções de apoio ao agente Jaime: (Leitura dos arquivos mockados, etc)
└── requirements.txt    # Dependências
```

## Exemplo de requirements.txt

```
streamlit
openai
python-dotenv
```

## Como Rodar

```bash
# Instalar dependências
pip install -r requirements.txt

# Rodar a aplicação
streamlit run app.py
```
