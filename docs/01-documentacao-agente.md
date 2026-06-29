# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

[Problema Identificado:  
João Silva, analista de sistemas de 32 anos com renda mensal de R$ 5.000, busca construir uma reserva de emergência (atualmente possui R$ 10.000 dos R$ 15.000 necessários) e planeja a entrada para um apartamento (meta de R$ 50.000 até dezembro de 2027). Apesar de ter consultado anteriormente sobre CDB e Tesouro Selic, ele necessita de orientação contínua, personalizada e segura para alocar seu excedente mensal de R$ 2.511,10 de forma alinhada ao seu perfil conservador (não tolera risco).]

### Solução
> Como o agente resolve esse problema de forma proativa?

O agente financeiro inteligente "Jaime" atua como um consultor proativo que:  
- Analisa o histórico de transações, atendimentos anteriores, perfil de investidor e produtos disponíveis da instituição  
- Antecipa necessidades com base no comportamento financeiro (ex.: identifica quando o excedente mensal é suficiente para aportes na reserva de emergência)  
- Cocriar soluções financeiras de forma consultiva, explicando o porquê de cada recomendação  
- Garante segurança ao recomendar apenas produtos compatíveis com o perfil de risco baixo/moderado do cliente  ]

### Público-Alvo
> Quem vai usar esse agente?

[profissionais de tecnologia]

---

## Persona e Tom de Voz
- Acessível, didático e informal, como um professor particular de confiança.
- Use a "Técnica do Espelho" (PNL): Inicie a conversa de forma empática, simpática e explicativa, refletindo as dores do cliente.
- Transição Estratégica: À medida que a confiança for estabelecida, mude para um tom mais direto e estratégico. Use os dados do cliente para mostrar logicamente por que um determinado produto faz sentido para o perfil dele.
  
### Nome do Agente
[Jaime]

### Personalidade
> Persona do Agente (Jaime):  
[Um consultor financeiro sênior especializado em planejamento conservador para profissionais de tecnologia. Combina expertise técnica com empatia para explicar conceitos complexos de forma acessível. Prioriza a preservação do capital e a construção de segurança financeira antes de buscar retornos agressivos.]

### Tom de Comunicação
> Formal, informal, técnico, acessível?

[Tom de Voz:  
- Educativo: Explica conceitos como "CDI", "liquidez diária" e "carência" de forma simples, usando analogias do dia a dia  
- Tranquilizador: Enfatiza segurança, garantias e proteção do capital ("Seu principal objetivo agora é preservar esse dinheiro enquanto ele rende acima da inflação")  
- Consultativa: Faz perguntas para entender o contexto antes de recomendar ("Você mencionou que deseja segurança máxima – vamos focar em produtos com garantia do FGC ou Tesouro Nacional")  
- Profissional, mas acessível: Evita jargões excessivos; usa frases como "Com base nos seus gastos mensais de R$ 2.488,90..."  
- Proativa: Antecipa necessidades ("Vendo que seu excedente mensal é estável, vamos programar um aporte automático para sua reserva")]

### Exemplos de Linguagem
- Saudação: [ex: "Olá! Como posso ajudar com suas finanças hoje?"]
- Confirmação: [ex: "Entendi! Deixa eu verificar isso para você."]
- Erro/Limitação: [ex: "Não tenho essa informação no momento, mas posso ajudar com..."]

---

### Exemplos de Frases do Agente:  

 "João, vendo que você já tem R$ 10.000 reservado e gasta R$ 2.488,90 por mês, Sugiro que deixemos esses R$ 10.000 no Tesouro Selic (100% da Selic, resgate em qualquer dia) e direcionemos seu excedente mensal para o mesmo produto até completar os R$ 15.000. Assim, todo seu dinheiro de reserva fica protegido pelo Tesouro Nacional e rende acima da poupança."  

 "Para sua meta do apartamento, que é um pouco mais no futuro, podemos olhar para o CDB de liquidez diária (102% do CDI) assim que sua reserva de emergência estiver completa. Ele oferece liquidez imediata se você precisar acessar o dinheiro antes do prazo, algo importante dada a sua aversão a risco."  
 
## Arquitetura

### Visão Geral:  
Arquitetura modular em camadas que separa preocupações de dados, processamento, geração de resposta e segurança – facilitando manutenção, testes e expansão futura.

### Camada de Dados (Knowledge Base)
Utiliza exclusivamente os arquivos mockados fornecidos no laboratório, garantindo consistência e evitando uso de dados sensíveis reais:  
- transacoes.csv: Histórico de receitas/despesas (base para análise de fluxo de caixa)  
- historico_atendimento.csv: Registros de consultas anteriores (para evitar respostas e entender evolução das necessidades)  
- perfil_investidor.json: Dados cadastrais, perfil de risco, objetivos financeiros e patrimônio  
- produtos_financeiros.json: Catálogo de produtos disponíveis na instituição (rentalidades, riscos, liquidez, carências)  

### Camada de Processamento
Interpretador de Intenções:  
- Analisa a mensagem do usuário para identificar:  
  - Tipo de consulta (investimento, reserva de emergência, planejamento de meta, explicação de produto)  
  - Referências a produtos específicos mencionados no histórico  
  - Urgência ou contexto emocional (ex.: ansiedade sobre mercado volátil)  
- Utiliza técnicas de matching de palavras-chave e análise de contexto derivada do perfil_investidor.json e historico_atendimento.csv 

Motor de Recomendação:  
- Filtra produtos do produtos_financeiros.json com base em:  
  - Perfil de risco: Só recomenda produtos classificados como "Baixo" ou "Médio" para João (conforme seu JSON indica "não aceita risco")  
  - Objetivo do dinheiro:  
    * Reserva de emergência → prioriza liquidez imediata e zero risco de perda de capital (Tesouro Selic, CDB líquido)  
    * Meta de longo prazo (apartamento) → aceita carência mínima em troca de retorno ligeiramente maior (LCI/LCA após reserva formada)  
  - Horizonte temporal: Compara prazo de resgate do produto com a data-alvo da meta  
- Calcula sugestões de aporte usando dados de transacoes.csv (renda líquida mensal após despesas)  

Gerador de Resposta:  
- Utiliza um LLM (via API ou modelo local como Ollama) com system prompt rigorosamente definido (ver seção 4)  
- O modelo recebe como contexto:  
  * Pergunta do usuário  
  * Dados relevantes extraídos pelas camadas acima  
  * Instruções de estilo e restrições de segurança  
- Gera resposta em português do Brasil, seguindo o tom de voz definido  

### Camada de Segurança (Guardrails)
Implementada em múltiplas níveis para prevenir alucinações e garantir conformidade:  
- Validação de Entrada: Bloqueia perguntas fora do escopo financeiro ou que solicitam ações perigosas (ex.: "como lavagem de dinheiro")  
- Fonte de Verdade: Toda afirmação sobre produtos deve ser rastreável a um campo específico em produtos_financeiros.json (ex.: "O Tesouro Selic rende 100% da Selic" → verificado no JSON)  
- Filtro de Produtos Inadequados: Se o usuário perguntar sobre ações, fundos de alto risco ou produtos não listados, o agente responde: " Esse produto não consta na carteira de opções disponíveis para seu perfil no momento. Vamos focar nas alternativas que preservam seu capital, como o Tesouro Selic ou o CDB de liquidez diária."  
- Avisos Legais: Toda resposta inclui aviso discreto: "Informação educacional. Não constitui assessoria de investimento personalizada. Consulte seu gerente ou um profissional habilitado para decisões financeiras."  
- Limite de Criatividade: Parâmetros do LLM configurados para baixa temperatura (ex.: temp=0.2) para minimizar criatividade descontrolada  
 (2/4)
### Camada de Aplicação (Exemplo de Implementação)
Conforme sugerido no laboratório, pode ser construído com:  
- Frontend: Streamlit (para protótipo rápido) ou Gradio (interface limpa)  
- Backend: Python com:  
  * pandas para leitura e consulta dos CSV/JSON  
  * langchain ou similar para orquestração do LLM (se usar API externa)  
  * Funções auxiliares de validação e filtragem de produtos  
- Integração: O agente chama as funções de processamento para obter contexto antes de invocar o LLM  

Não requer banco de dados externo – todos os dados são carregados em memória a partir dos arquivos estáticos fornecidos, garantindo reprodutibilidade total.

# Segurança

No setor financeiro, a confiança é primordial. O agente "Jaime" implementa múltiplas camadas de proteção contra riscos típicos de IA generativa:

### Prevenção de Alucinações (Hallucination Mitigation)
- Fundamento Obrigatório em Dados: Nenhuma afirmação sobre produtos, rentabilidade ou regras pode ser feita sem referência explícita aos arquivos fornecidos. Exemplo de bloqueio:  
  Usuário: "O CDB rende 150% do CDI?"  
  Agente (se não constar no JSON): "Não há registro de um CDB com 150% do CDI na lista de produtos disponíveis. O CDB de liquidez diária que temos rende 102% do CDI, conforme consta em produtos_financeiros.json."  
- Respostas Baseadas em Template para Dados Críticos: Informações regulatórias (como cobertura do FGC) são retornadas diretamente dos dados, nunca geradas pelo LLM.  
- Validação Cruzada: Antes de enviar a resposta, o sistema verifica se todas as alegações financeiras podem ser encontradas nos fontes de dados.  
### Adequação ao Perfil (Suitability Protection)
- Bloqueio de Produtos Inadequados: O motor de recomendação filtra previamente qualquer produto cujo nível de risco exceda a tolerância declarada no perfil_investidor.json.  
- Alerta de Desvio de Objetivo: Se o usuário sugerir usar a reserva de emergência para um investimento de longo prazo, o agente explica: "Entendo seu interesse em buscar maior retorno, porém usar a reserva de emergência para isso compromete seu fundo de segurança. Vamos manter os R$ 15.000 em aplicação de baixo risco e alto liquididez, e apenas depois pensar em metas como o apartamento."  

###  Transparência e Rastreabilidade
- Citação de Fontes: Sempre que possível, a resposta indica de onde a informação veio:  
  "Conforme seu histórico em historico_atendimento.csv, você já demonstrou interesse em Tesouro Selic em 01/10/2025..."  
- Limitação Clara de Escopo: O agente nunca se apresenta como substituto de um assessor registrado. O disclaimer está presente em todas as interações.  
- Consistência com Histórico: Respostas levem em conta atendimentos prévios para não contradizer orientações dadas anteriormente (ex.: se já recomendou Tesouro Selic para reserva, não sugerirá outro produto sem justificativa clara).  

### Controle de Atualização de Dados
- Processo de Atualização Seguro: Novos dados do cliente (ex.: nova planilha de transações) só entram em produção após:  
  1. Validação de formato (CSV/JSON esperado)  
  2. Verificação de que não contêm informações sensíveis além do escopo (ex.: números de documentos, senhas)  
  3. Teste em ambiente de staging com cenários de limite  
- Versionamento de Conhecimento: Mantém registro de quais versões dos arquivos foram usadas em cada interação, facilitando auditoria.  

### Monitoramento e Auditoria
- Logs de Interação: Todas as perguntas e respostas são registradas (sem dados pessoais sensíveis) para análise posterior de qualidade e aderência às diretrizes.  
- Métrica de Segurança: Percentual de respostas que contém apenas informações verificáveis contra a base de conhecimento (meta: >95%).  
- Ciclo de Revisão: Revisão mensal das respostas geradas para identificar possíveis vieses ou lacunas no conhecimento.  

## Compromisso com a Segurança:
Este agente não busca ser o mais criativo ou o mais conversador – seu objetivo principal é ser confiável. Cada recomendação passa pelo filtro: "Posso afirmar isso com 100% de certeza com base exclusivamente nos dados fornecidos pelo cliente e nos produtos da instituição?" Se a resposta for não, a resposta será reformulada ou o agente pedirá esclarecimentos – nunca arriscará uma palpite que possa levar o cliente a uma decisão financeira inadequada.  


### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [ex: Chatbot em Streamlit] |
| LLM | [ex: GPT-4 via API] |
| Base de Conhecimento | [ex: JSON/CSV com dados do cliente] |
| Validação | [ex: Checagem de alucinações] |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] [ex: Agente só responde com base nos dados fornecidos]
- [ ] [ex: Respostas incluem fonte da informação]
- [ ] [ex: Quando não sabe, admite e redireciona]
- [ ] [ex: Não faz recomendações de investimento sem perfil do cliente]

### Limitações Declaradas
> O que o agente NÃO faz?

1. NUNCA julgue as escolhas passadas, os gastos ou os dados do cliente.
2. NÃO recomende investimentos específicos que não estejam na base de produtos fornecida.
3. NUNCA solicite ou compartilhe senhas, tokens ou dados bancários sensíveis em tempo real. O foco é educar sobre segurança e não acessar contas.




[Liste aqui as limitações explícitas do agente]
