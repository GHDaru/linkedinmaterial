# Proposta · Série de IA avançada

Status: **proposta**, aguardando o orquestrador e o Darú. Pedido `20261025T123528Z-orquestrador-4bc0`.

## 1. Nome

**Por dentro do agente**

Explica o que a série faz: abre o agente e mostra as peças que ficam em volta do modelo. Para quem acompanhou "IA do básico ao avançado", é a continuação natural do Ep. 8 (Harness).

Alternativas: *Agente em operação* · *O agente no turno* · *IA avançada na prática*.

## 2. Episódios

Cada episódio abre com uma **cena de operação** e só depois dá o nome técnico. Cada um tem um paralelo com algo que o leitor de supply chain já conhece.

| # | Episódio | Paralelo na operação | Ângulo | Pré-requisito (fundamentos) | Formato |
|---|---|---|---|---|---|
| 1 | **AGENTS.md** | Manual de integração do funcionário novo | O arquivo de instruções que todo agente lê ao entrar no projeto. Estudo da ETH Zurich (2026): arquivos gerados por IA *pioraram* o agente e encareceram ~20%, e os escritos por humanos ajudaram pouco. A lição é escrever menos e melhor. | Ep. 4 Contexto | Animação + Colab curto (custo em tokens do arquivo por sessão) |
| 2 | **Skills** | POP guardado na gaveta, aberto só quando precisa | Um SKILL.md é um procedimento reutilizável. O agente vê só a descrição (~100 tokens) e carrega o resto quando a tarefa pede: *divulgação progressiva*. É padrão aberto, com mais de 30 ferramentas compatíveis. | Eps. 4 e 5 | Animação + Colab (mini carregador de skills com contagem de tokens) |
| 3 | **Memória** | Passagem de turno | Instruções fixas, memória durável e resumo de contexto (*compaction*) são três coisas diferentes. Mostra o risco de uma memória errada que persiste e vira "verdade". | Ep. 4 | Animação + Colab (memória em arquivo, um erro que persiste, como corrigir) |
| 4 | **Hooks e permissões** | Poka-yoke e limite de alçada | Uma instrução é um pedido. Um hook é uma garantia: código que roda antes ou depois de cada ação do agente e pode bloqueá-la. Inclui permissões e sandbox. | Eps. 5 e 8 | Animação + Colab (agente tenta alterar um pedido acima da alçada, o hook bloqueia) |
| 5 | **Subagentes** | Coordenador e equipe de turno | Um agente coordenador distribui tarefas para subagentes com contexto próprio. Quando vale a pena e quando só multiplica o custo. | Eps. 6 e 8 | Animação + diagrama |
| 6 | **Mods e plugins** | Customizar a máquina, não só a ordem de serviço | Lançados em out/2026 no Claude Code, os mods mudam a própria ferramenta: interface, comandos, chamadas de ferramenta. Plugins empacotam skills, hooks e mods para instalar de uma vez. | Ep. 4 desta série | Diagrama + arte (sem Colab: mods rodam na máquina do usuário) |
| 7 | **A cadeia de suprimentos do agente** | Homologação de fornecedor | Skills e servidores MCP de terceiros são fornecedores: já houve campanhas de skills maliciosas em 2026, e a OWASP criou um Top 10 específico. Você audita fornecedor de embalagem; audita a skill que instalou? | Eps. 2 e 6 desta série | Diagrama + checklist (o ângulo mais forte para este público) |
| 8 | **Evals de agente** | Auditoria do processo, não só do produto | Avaliar um agente é avaliar a trajetória (que ferramentas usou, quantos passos, quanto custou), não só a resposta final. | Ep. 7 Evals | Colab (comparar duas trajetórias para a mesma tarefa) |
| 9 | **Agente fala com agente** | EDI entre empresas | Protocolos para agentes conversarem entre si (MCP, ACP, A2A). Exemplo real: o canal `msg/1` deste repositório, onde o orquestrador e o Claude trocam pedidos por git. | Ep. 5 | Animação + diagrama + o próprio canal como exemplo |
| 10 | **Harness mínimo** | Montar a linha inteira | Episódio final: junta AGENTS.md, skill, memória e hook num agente de ~100 linhas, que roda no Colab. Um estudo de 11 agentes de código (jul/2026) mostrou que um loop simples rende parecido com sistemas muito maiores. | Todos acima | Colab (o principal entregável) + animação |

## 3. Ordem e por quê

`1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10`

- **1 a 3 (o que o agente sabe):** instrução fixa, procedimento e memória. São a base de tudo e dependem só de Contexto (Ep. 4 dos fundamentos).
- **4 (o que o agente pode fazer):** hooks e permissões precisam do agente já entendido como alguém que age (Eps. 5 e 6).
- **5 e 6 (como se organiza e se estende):** subagentes e mods supõem que hooks já foram explicados. Os mods são construídos sobre hooks.
- **7 (segurança):** só faz sentido depois que skills, plugins e MCP foram apresentados como coisas que se instalam.
- **8 e 9 (medir e conectar):** pedem a visão do agente completo.
- **10 (capstone):** cada notebook anterior acrescenta uma peça ao mesmo `mini_agente.py`, e o Ep. 10 monta a versão final.

## 4. Lacunas além dos exemplos

Incluídas na lista: **permissões e sandbox** (dentro do Ep. 4), **subagentes**, **segurança de skills e MCP**, **evals de trajetória** e **protocolos entre agentes (ACP, A2A)**.

Deixadas de fora por já estarem nos fundamentos ou serem básicas: tool calling simples (Ep. 5), RAG (Ep. 1), prompt (Ep. 4), MCP introdutório (Ep. 5).

Candidatos a episódio extra:
- **Compaction e contexto longo em agentes** (como o agente "esquece" com segurança numa tarefa de horas).
- **Meta-harness:** orquestrar agentes de fornecedores diferentes atrás de uma mesma interface.

## 5. Formato: o que fica e o que muda

**Fica igual:** cena concreta na abertura, animação com régua de etapas, Colab com botão no README, post no LinkedIn, números reais sempre que possível e ilustrativos marcados como tal.

**Muda:**
- **Animação mais curta** (10 a 12 s, 3 a 4 etapas, 4:5). Os temas são estruturais, e um "antes × depois" funciona melhor que um fluxo longo.
- **O notebook vira laboratório incremental.** Cada episódio acrescenta uma peça a um mesmo mini agente, e o leitor que acompanha a série termina com um agente funcionando.
- **O LLM é plugável.** Por padrão, um "modelo roteirizado" determinístico (o foco é a estrutura, não a qualidade do modelo), com a opção de trocar por um modelo aberto ou pelo Claude com chave. Isso mantém a regra de rodar sem chave de API.
- **Densidade maior no texto do post**, com um quadro "o que isso muda na sua operação" no fim.

## 6. Risco de jargão (chapéu do leitor de operação)

| Termo | Risco | Como abrir |
|---|---|---|
| AGENTS.md | Parece coisa de programador | "O agente novo chegou e ninguém deu o manual" |
| Skill | Confunde com "habilidade" genérica | "O POP de devolução por avaria, que só sai da gaveta quando chega uma avaria" |
| Memória / compaction | Abstrato | "O turno da noite não sabia o que o dia combinou com o fornecedor" |
| Hook | Palavra sem tradução | "Poka-yoke: a peça que não deixa montar errado" |
| Subagente | Ficção científica | "O coordenador de turno que distribui as tarefas" |
| Mod / plugin | Ambíguo | "Customizar a empilhadeira, não só a ordem de serviço" |
| MCP, ACP, A2A | Sopa de letras | "EDI entre agentes": o leitor de supply chain já entende EDI |
| Trajetória (evals) | Abstrato | "Auditar o processo, não só inspecionar o produto final" |

**Regra:** o termo técnico aparece só depois da cena, uma vez, com o paralelo ao lado. O título do post usa a cena, não a sigla.

## 7. Estimativa e entrega

**Por episódio:** ~1 dia de construção.
- Animação: 3 a 4 h, reaproveitando `tools/motion` e o padrão visual.
- Notebook: 4 a 6 h, incluindo o teste completo.
- README e revisão técnica do texto: ~1 h.
- O Ep. 10 (capstone) leva ~2 dias.

**Início:** depois que os fundamentos publicarem o Ep. 6 (Agente ou automação), porque os Eps. 4 e 5 desta série dependem dele.

**Ritmo:** 1 episódio por semana, intercalado com os fundamentos enquanto as duas séries correm juntas. As datas exatas ficam com o orquestrador, a partir do calendário dos fundamentos.

**Entrega:** o material de cada episódio fica pronto até a segunda-feira 12:00 da semana de publicação, o mesmo combinado do Ep. 2.

## Fontes

- [AGENTS.md como padrão aberto sob a Linux Foundation (AAIF)](https://codex.danielvaughan.com/2026/04/07/agents-md-open-standard-cross-tool-portability)
- [Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents? (ETH Zurich, 2026)](https://arxiviq.substack.com/p/evaluating-agentsmd-are-repository)
- [SKILL.md Open Standard Reaches 30+ AI Coding Tools](https://noqta.tn/en/news/skill-md-open-standard-30-ai-coding-tools-adoption-2026)
- [Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents (arXiv 2609.00006)](https://arxiv.org/pdf/2609.00006)
- [Claude Code gets mods (The New Stack, out/2026)](https://thenewstack.io/anthropic-claude-code-mods-plugins/?p=22839147)
- [The Agent Skill Supply Chain Crisis](https://codex.danielvaughan.com/2026/06/07/agent-skill-supply-chain-crisis-clawhavoc-toxicskills-skillsieve-codex-cli-defence/)
- [OWASP Agentic Skills Top 10 · AST01 Malicious Skills](https://owasp.org/www-project-agentic-skills-top-10/ast01.html)
- [Don't rely on instructions; use Agent Hooks to enforce guardrails](https://bitbytebit.substack.com/p/agent-hooks-deterministic-guardrails)
