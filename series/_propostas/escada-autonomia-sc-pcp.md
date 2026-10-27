# Proposta · Escada da autonomia e série "IA na operação"

Status: **v2, revisada por três especialistas independentes** (operações e TOC; automação e governança; adoção de IA e conteúdo). Pedido do Darú em 27/10/2026. Os pareceres estão resumidos na seção 9.

> **A tese em uma frase:** escolha a decisão pela restrição, prove a IA em modo sombra e meça em throughput. O nível de autonomia é da decisão, nunca da empresa.

## 1. O problema

Empresas tratam "implantar IA" como um projeto só, com ponto de chegada. Na prática, cada **decisão** de um processo está num grau diferente de automação, e quem não separa os graus erra de dois jeitos. Ou compra autonomia para uma decisão que ainda não tem dado confiável, ou põe um humano para carimbar aprovações que ele já não consegue avaliar.

O Gartner publicou em setembro de 2026 uma pesquisa com 243 líderes de empresas com receita de US$ 500 milhões ou mais, feita no fim de 2025. A conclusão: até 2030, só 5% das organizações com automação de planejamento vão deixar a tecnologia tomar ao menos 10% das decisões de planejamento sem humano. E isso apesar de 83% já terem gasto US$ 3 milhões ou mais. Na frase da analista Buse Aras, faltam fundações de "decisão, talento e tecnologia".

## 2. A escada: quem autoriza a execução, e quando

A escada tem **um eixo só: quem autoriza a execução da decisão, e em que momento**. Escopo, reversibilidade e risco não são degraus: são **atributos** de cada decisão (seção 3) e definem até onde ela pode subir.

| Nível | Nome | Quem autoriza | O que a máquina faz | Papel do humano |
|---|---|---|---|---|
| **N0** | Manual | O humano faz tudo | Nada | Decide e executa |
| **N1** | Informa | O humano | Junta, organiza e explica os dados | Decide e executa |
| **N2** | Recomenda | O humano escolhe | Sugere uma ou poucas opções, com justificativa e fonte | Escolhe e executa |
| **N3** | Age com OK | O humano aprova **antes**, caso a caso | Prepara a ação completa e executa após o OK | Aprova cada caso |
| **N4** | Age no envelope | Uma **regra escrita** autoriza; o humano trata a exceção | Age sozinha dentro do envelope, informa e escala o que sai dele. Variante: janela de veto antes de executar | Trata exceções, audita amostras |
| **N5** | Autônoma no domínio | A regra autoriza; o humano não intervém caso a caso | Decide, age e registra | Observa indicadores, tem o botão de parar |

**Para o leitor de operação, a versão curta tem quatro degraus:** Informa · Recomenda · Age com OK · Age no envelope. N0 e N5 ficam como os extremos.

**Regra não é IA.** Um N4 pode ser 100% determinístico, como o gerenciamento de pulmão pela regra do DBM. A IA entra onde a regra não alcança: explicar, tratar exceção, sugerir o ajuste.

### Paralelos com as escalas conhecidas

| Nível | Sheridan & Verplank (1978) | Parasuraman et al. (2000) | Feng et al. (2025) | Gartner (Downard, 2017) |
|---|---|---|---|---|
| N1 | 1–2 | Aquisição e análise da informação | — | 1 · informação geral |
| N2 | 2–4 | Decisão: sugere | Operador | 2 · informação específica, com recomendação |
| N3 | 5 · executa se o humano aprovar | Decisão e ação | Operador (não age sem aprovação) | — |
| N4 | 6 · veto com prazo antes · 7 · executa e informa | Ação | Aprovador | 5 · automação que se pode sobrescrever |
| N5 | 8–9 | Ação | Observador (só o botão de desligar) | 6 · automação sem revisão |

A **SAE J3016** (revisão 2021 com a ISO, níveis 0–5 do carro autônomo) não entra na tabela. Comparar os níveis um a um seria forçado, porque eles descrevem controle contínuo de um veículo. Dela vêm duas lições:
1. **O nível vale para uma função, dentro de um domínio operacional declarado (ODD).** Por isso não existe "empresa nível 4".
2. **Todo sistema precisa de um estado seguro para onde voltar** (a *minimal risk condition*). Aqui, é o rebaixamento automático para N2 (seção 5).

O nível 5 do SAE, autonomia sem domínio limitado, não tem equivalente aqui. É de propósito.

## 3. Inventário de decisões: por onde começar

O método começa por um **inventário das decisões** do processo, não por uma ferramenta. Cada decisão recebe uma linha:

| Atributo | Exemplo |
|---|---|
| Decisão | Liberar ordem para o chão |
| Ligação com a restrição | Governa a carga do gargalo (sim/não) |
| Volume | 400 por mês |
| Custo de um erro | Atraso de pedido + hora extra no gargalo |
| Reversibilidade | Alta antes do início da ordem; baixa depois |
| Qualidade do dado | Lead time real medido? cadastro limpo? |
| Dono | Nome do responsável pela decisão |
| Nível atual / nível-alvo | N1 / N3 |

**O nível-alvo sai dos atributos, não da vontade de subir.** O teto vem da reversibilidade e do custo do erro: uma decisão irreversível e cara fica em N2 ou N3, por mais que o modelo acerte. O volume diz se vale o esforço: decisão rara não paga a automação.

**A decisão a trabalhar primeiro é a que governa a restrição.** A restrição em si é um recurso, o mercado ou uma política, não uma decisão.

## 4. A sequência: os cinco passos da TOC, decisão por decisão

1. **Identificar a restrição.** A IA já entra aqui, em **N1**: carga × capacidade, mineração do processo, histórico de penetração do pulmão. Isso é diagnóstico.
2. **Explorar a restrição.** Tirar o máximo dela com regra e política certas. Muitas vezes a restrição é a própria política. Aqui entram as **seis perguntas de Goldratt sobre tecnologia** (*Necessária, mas não suficiente*, 2000), aplicadas à IA:
   - qual é o poder da tecnologia;
   - que limitação ela remove;
   - que regras existiam para conviver com essa limitação;
   - que regras novas devem valer agora;
   - que mudanças a tecnologia precisa ter;
   - como fazer a mudança.

   Otimizar a sequência do gargalo também é explorar, mesmo com algoritmo.
3. **Subordinar.** Todo o resto segue o ritmo da restrição: liberação pela corda, prioridade pela cor do pulmão e folga proposital nos não-gargalos.
4. **Elevar.** Só aqui a decisão sobe para N2 em diante, passando pelos portões (seção 5). A regra é: **N1 em qualquer passo; N2 ou mais só depois de explorar e subordinar.**
5. **Não deixar a inércia virar a restrição.** Quando o gargalo muda de lugar, o envelope do N4 e a regra codificada viram a próxima restrição de política. A cada volta do ciclo, **revise o envelope e o nível de cada decisão**, e rebaixe se for preciso.

Resumo para a arte: **Restrição → Regra → Ferramenta → Throughput**.

## 5. Portões: para subir e para descer

Os valores numéricos abaixo são **pontos de partida propostos**, para calibrar decisão por decisão. Não são norma.

| Para chegar a | Precisa ter |
|---|---|
| **N1** | Dono da decisão nomeado. Dado acessível. Processo estável: cadastro e estoque com acurácia medida, lead time real conhecido |
| **N2** | Métrica de **resultado** da decisão: throughput, ruptura, OTIF, % do tempo no vermelho, estoque, despesa operacional. Concordância com o humano não basta. Monitoramento de deriva ligado. Registro de cada recomendação |
| **N3** | Modo sombra com volume suficiente (ponto de partida: 30 ciclos de decisão ou 8 semanas, o que for maior), com resultado igual ou melhor que o humano. A decisão humana é registrada antes de ver a sugestão, para não contaminar a comparação. Aderência do chão ao plano medida. A ação grava de volta no ERP. **Incentivo revisto:** o planejador não pode ser cobrado por fazer override |
| **N4** | Envelope escrito (alçada, faixas, tipos de item, exceções). Testes com casos fora do envelope. Custo de desfazer explícito, porque cancelar um pedido emitido não é grátis. Log de cada ação. Auditoria por amostragem e casos-sentinela. Plano de contingência manual com treino periódico |
| **N5** | Meses em N4 com taxa de exceção estável (ponto de partida: 3 meses). Teto permitido pela reversibilidade. Auditoria externa à equipe que opera |

**Gatilhos de rebaixamento (o caminho de descer):** deriva acima do limiar, aumento da taxa de exceção ou de reversão, incidente, mudança de regra, de sortimento ou de fornecedor, troca de modelo, mudança de lugar da restrição. O estado seguro padrão é **voltar para N2**, em que a máquina recomenda e o humano decide.

## 6. Os dois alertas

**N3, o aprovador que carimba.** Quem aprova centenas de casos quase sempre certos passa a confiar sem olhar. A literatura chama isso de complacência e viés de automação (Bainbridge, 1983; Parasuraman e Manzey, 2010), e o EU AI Act exige, no art. 14, que a supervisão humana considere esse viés. Há três saídas:
- ficar em N2, em que o humano decide de verdade;
- manter o N3 com **amostragem auditada e casos-sentinela** (erros plantados para ver se o aprovador ainda distingue o certo do errado);
- ir para N4 com envelope estreito.

Para decisões de baixo risco e reversíveis, o N3 com amostragem é aceitável.

**N4, o humano fora do circuito.** A exceção chega justamente a quem deixou de praticar a decisão, que é a ironia de Bainbridge. É aqui que está o análogo do nível 3 do carro: o sistema pede ajuda e o humano precisa reassumir. A saída é treinar a operação manual periodicamente e não deixar o envelope crescer além do que a equipe consegue cobrir.

## 7. A série: "IA na operação" (método + casos, alternados)

Os revisores recomendaram **uma série só**, alternando um post de **método** e um **caso** que o aplica, com a cena como título do post. São 14 episódios:

| # | Tipo | Título (cena) | O que ensina | Nível |
|---|---|---|---|---|
| 1 | Método | "Só 5% vão deixar a IA decidir 10% do planejamento" | O nível é da decisão, não da empresa | — |
| 2 | Caso | "Todo mundo ocupado e o pedido atrasa" | Achar o gargalo com dados | N1 |
| 3 | Método | "Informa, recomenda, age com OK, age no envelope" | A escada e quem autoriza | — |
| 4 | Caso | "O produto que mais vende é o que menos dá lucro" | Mix por throughput por hora de gargalo | N1 → N2 |
| 5 | Método | "Que regra existia por causa da limitação?" | As seis perguntas de Goldratt | — |
| 6 | Caso | "A fila do gargalo decide o mês" | Sequenciar o tambor | N2 → N3 |
| 7 | Método | "Prove antes de deixar agir" | Modo sombra, medindo resultado e não concordância | — |
| 8 | Caso | "A ordem entrou cedo demais" | Liberação pela corda e prioridade pela cor do pulmão: regra em N4, IA que explica | N4 por regra |
| 9 | Método | "O aprovador que carimba" | Os alertas do N3 e do N4 | — |
| 10 | Caso | "Ruptura na loja com o CD cheio" | Pulmão de estoque e ajuste dinâmico: regra + IA nas exceções | N3, N4 em item estável |
| 11 | Método | "Até onde a máquina pode ir sozinha" | O envelope e o caminho de descer | — |
| 12 | Caso | "Qual prazo prometer para o pedido 4521?" | Prometer prazo pela carga do gargalo | N2 |
| 13 | Método | "Quanto a IA aumentou o throughput?" | Medir em T, I e OE | — |
| 14 | Método | "Quando a regra codificada vira o gargalo" | Inércia, governança e a próxima restrição | — |

**Ficam para uma segunda temporada de casos:**
- previsão (o ajuste do planejador vale? medido pelo valor agregado à previsão, o FVA);
- compras de indiretos e manutenção (N3), separada de negociação (N1/N2);
- monitoramento de risco de fornecedor (N1);
- documento de fornecedor virando dado, como fundação de dados.

## 8. Como as séries se encaixam (recomendação dos revisores, para decisão)

São ~15 posts por mês na cadência de um a cada 2 dias. Com quatro séries ao mesmo tempo, cada uma sairia a cada 8 dias ou mais, e ninguém acompanha. A recomendação:
- **"IA na operação"** (esta) vira a série principal, porque é a que conversa com quem decide e com a marca GHDARU.
- **"IA do básico ao avançado"** continua, com ritmo menor, até fechar os 10 episódios.
- **"Por dentro do agente"** fica em pausa: fala com quem constrói, não com quem compra. Volta depois.

A grade fica com o orquestrador e o Darú.

**Produto que a série prepara (sem venda nos posts):** um *diagnóstico de autonomia* de 3 a 4 semanas. Entrega o inventário de decisões com nível atual e nível-alvo, aponta a restrição e deixa um piloto rodando em modo sombra. O critério de sucesso é throughput ou caixa, não acurácia. A oferta aparece no máximo no episódio 14 ou num post-âncora com o checklist dos portões.

## 9. O que os revisores apontaram (e foi incorporado)

| Revisor | Principais correções |
|---|---|
| Operações e TOC | "Subordinar" não é "mudar a regra": a política entra no explorar. O 5º passo é a inércia. A IA já entra em N1 no passo 1. Restrição é recurso, mercado ou política, não decisão. Setup só importa no gargalo. Regra não é IA. Entraram mix, corda, pulmão dinâmico e promessa de prazo. Portões com resultado (T/I/OE), estabilidade, aderência do chão e gravação no ERP |
| Automação e governança | A escala ficou com um eixo só ("quem autoriza, e quando"). Paralelos refeitos. O SAE saiu da tabela. O alerta do N3 passou a se basear em complacência e viés de automação, e o problema do "nível 3 do carro" foi para o N4. Veto com prazo virou variante explícita. Responsável desde o N1, caminho de descer e teto por reversibilidade. Citações corrigidas |
| Adoção e conteúdo | Tese em uma frase no topo. As escalas foram para um anexo, sem abrir o texto. Inventário de decisões, portões numéricos e o diagnóstico como produto. Incentivo do planejador no portão do N3. Série única alternando método e caso; pausa na série de agentes. Evitar venda nos posts e exemplos de N5 |

**Para o Darú decidir:**
1. A série única "IA na operação" e a pausa em "Por dentro do agente".
2. O nome da escada.
3. **Conflito de interesse:** reposição, pulmão e DBM estão no centro do mercado do seu empregador, e a série serve à marca GHDARU. Antes de publicar, confira as cláusulas que se aplicam ao seu contrato e use só exemplos genéricos ou públicos, sem casos nem dados de clientes da empresa.

## Fontes

- SAE INTERNATIONAL. *SAE J3016: Taxonomy and Definitions for Terms Related to Driving Automation Systems for On-Road Motor Vehicles*. Revisão J3016_202104, com a ISO/SAE PAS 22736:2021. Resumo em: https://blog.ansi.org/sae-levels-driving-automation-j-3016-2021/
- SHERIDAN, T. B.; VERPLANK, W. L. *Human and Computer Control of Undersea Teleoperators*. Cambridge, MA: MIT Man-Machine Systems Laboratory, 1978.
- PARASURAMAN, R.; SHERIDAN, T. B.; WICKENS, C. D. A model for types and levels of human interaction with automation. *IEEE Transactions on Systems, Man, and Cybernetics – Part A: Systems and Humans*, v. 30, n. 3, p. 286–297, 2000.
- FENG, K. J. K.; McDONALD, D. W.; ZHANG, A. X. *Levels of Autonomy for AI Agents*. arXiv:2506.12469, 2025. https://arxiv.org/abs/2506.12469v1
- BAINBRIDGE, L. Ironies of automation. *Automatica*, v. 19, n. 6, p. 775–779, 1983.
- PARASURAMAN, R.; MANZEY, D. H. Complacency and bias in human use of automation. *Human Factors*, v. 52, n. 3, p. 381–410, 2010.
- GOLDRATT, E. M.; SCHRAGENHEIM, E.; PTAK, C. A. *Necessary but Not Sufficient*. Great Barrington: North River Press, 2000.
- UNIÃO EUROPEIA. Regulamento (UE) 2024/1689 (AI Act), art. 14.
- BODENSTAB, J. Gartner's Six Levels of Supply Chain Planning Autonomy. ToolsGroup, 22 jun. 2017. Resumo da palestra de Andrew Downard (Gartner). https://www.toolsgroup.com/blog/gartners-six-levels-of-supply-chain-planning-autonomy/
- LOGISTICS MANAGEMENT. Gartner analysis points to fewer supply chains letting AI make planning calls by 2030. 25 set. 2026. https://www.logisticsmgmt.com/article/gartner_analysis_points_to_fewer_supply_chains_letting_ai_make_planning_calls_by_2030
- ACATECH. *Industrie 4.0 Maturity Index*, atualização 2020. https://en.acatech.de/publication/industrie-4-0-maturity-index-update-2020/
