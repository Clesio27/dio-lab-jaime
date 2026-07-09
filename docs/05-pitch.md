# Pitch (3 minutos)

> [!TIP]
 
## Roteiro 

### 1. O Problema (30 seg)
> Qual dor do cliente você resolve?

[ “Hoje, milhares de brasileiros têm dificuldade para organizar suas finanças pessoais. Eles acumulam extratos em planilhas, perdem o controle de gastos, não sabem onde investir com segurança e acabam pagando juros desnecessários ou perdendo oportunidades de economia.  ]

### 2. A Solução (1 min)
> Como seu agente resolve esse problema?

[“Jaime é um agente financeiro inteligente baseado em IA Generativa que transforma dados brutos de transações, perfil e objetivos em orientações personalizadas, proativas e seguras.  
   
 Como funciona?  
 1. Coleta de dados – Jaime consome CSVs e JSONs já existentes na pasta data/ (histórico de transações, perfil de investidor, produtos financeiros e atendimentos).  
 2. Base de conhecimento – Esses arquivos alimentam um pequeno knowledge base que o modelo consulta antes de gerar qualquer resposta.  
 3. Engine de IA – Usamos um LLM hospedado na OpenRouter (via API OpenAI‑compatible). O system prompt está definido em docs/03-prompts.md e inclui guardrails que evitam alucinações, respeitam o perfil de risco e seguem a LGPD.  
 4. Interface – Um protótipo Streamlit (src/app.py) oferece um chat amigável onde o usuário digita perguntas como “Quanto gastrei com alimentação esse mês?” ou “Qual investimento combina com meu perfil conservador?”.  
 5. Avaliação – Métricas de assertividade, taxa de respostas seguras e aderência ao perfil são monitoradas (ver docs/04-metricas.md).  
   
 Resultado: Em poucos segundos, Jaime entrega análises de gastos, sugestões de economia, planos de metas, recomendações de investimento e alertas inteligentes – tudo totalmente personalizado e explicável.”]

### 3. Demonstração (1 min)
> Mostre o agente funcionando (pode ser gravação de tela)

“Vamos ver Jaime em ação.  
   
 1. Abra o app – streamlit run src/app.py (já está rodando aqui).  
 2. Carregue os dados de exemplo – os arquivos CSV/JSON da pasta data/ são carregados automaticamente.  
 3. Faça uma pergunta:  
    - “Quais foram meus maiores gastos em fevereiro?” → Jaime retorna um gráfico de barras (gerado pelo próprio Streamlit) e aponta que 42 % foi em alimentação, sugerindo um limite de R$ 800 para o próximo mês.  
    - “Quero viajar em dezembro com R$ 5 000. Qual plano de investimento me ajuda a chegar lá?” → Jaime consulta o perfil de investidor conservador, sugere uma aplicação em CDB com 105 % do CDI e mostra o montante acumulado mês a mês.  
    - “Me avise se eu passar do limite de transporte.” → Jaime cria um alerta inteligente que será disparado quando a soma das transações de transporte ultrapassar o limite definido.  
   
 4. Mostre os guardrails – Se eu pedir uma recomendação de investimento de alto risco estando no perfil conservador, Jaime responde: “Desculpe, essa sugestão não está alinhada ao seu perfil de risco conservador. Posso sugerir alternativas de renda fixa ou fundos multimercado de baixo risco.”  ]

### 4. Diferencial e Impacto (30 seg)
> Por que essa solução é inovadora e qual é o impacto dela na sociedade?

[- Personalização profunda – Jaime não responde com respostas prontas; ele combina seu histórico real com um LLM guiado por prompts cuidadosamente elaborados, garantindo que cada sugestão seja única ao usuário.  
 - Transparência e segurança – Os guardrails impedindo alucinações e respeitando o perfil de risco são explícitos no system prompt; não há “caixa-preta”.  
 - Integração simples – Basta um arquivo .env com a chave OpenRouter e streamlit run. Não é necessário infraestrutura complexa; qualquer analista de dados pode subir o protótipo em menos de 15 min.  
 - Foco em educação financeira – Além de resolver o problema imediato, Jaime explica conceitos (juros compostos, diversificação, limite de cartão) na própria conversa, promovendo autonomia do usuário.  ]

---

Impacto:  
 - Produtividade: Estudos da SBPC mostram que usuários que recebem orientação financeira personalizada economizam até 15 % dos gastos mensais.  
 - Inclusão: Ao funcionar em qualquer máquina com Python e internet, Jaime leva educação financeira de qualidade a quem não tem acesso a assessores caros.  
 - Alinhamento ao bootcamp: O projeto demonstra exatamente as competências requisitadas – tratamento de dados (CSV/JSON), engenharia de prompts, uso de APIs externas (OpenRouter), desenvolvimento de aplicativos Streamlit e preocupação com segurança/LGPD – tudo em um portfólio pronto para ser apresentado a recrutadores.  

 “Com Jaime, transformamos dados brutos em decisões financeiras inteligentes, de forma simples, segura e educativa. É exatamente esse tipo de solução prática e de impacto que o DIO busca formar nos seus alunos.”


## Checklist do Pitch

- [ ] Duração máxima de 3 minutos
- [ ] Problema claramente definido
- [ ] Solução demonstrada na prática
- [ ] Diferencial explicado
- [ ] Áudio e vídeo com boa qualidade

---

## Link do Vídeo

> Cole aqui o link do seu pitch (YouTube, Loom, Google Drive, etc.)

[Link do vídeo]
