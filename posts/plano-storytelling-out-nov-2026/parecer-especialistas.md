# Parecer sobre o storytelling: out/nov 2026

Validação da tese, do arco em 3 atos e da sequência pedagógica da grade oficial ([`calendario/grade-orquestrador.md`](../../calendario/grade-orquestrador.md)), feita em 26/10/2026 por três revisores independentes: **narrativa**, **TOC e pedagogia** e **conteúdo para LinkedIn**. Base: o [brief](README.md) e os textos publicados de 18 a 25/10.

Nenhuma data foi alterada. O que mexe em data ou ordem está marcado como **decisão do Darú**.

## Veredito

A tese se sustenta e a virada de 26/10 funciona. Há três pontos a resolver:

1. O leitor ainda não enxerga o arco.
2. A tese omite dois passos da TOC (explorar e subordinar).
3. O Ato 3 quebra a sequência em 01/11: o post de governança de agentes sai antes dos episódios sobre agentes, evals e harness.

## Manter

- **"Minha leitura" pela TOC como bloco fixo.** Aparece em 5 dos 6 posts (18, 20, 21, 22 e 24/10). É ele que funda o arco, mais que os temas.
- **Pergunta final ligada à operação de quem lê.** A melhor síntese da tese até agora é a pergunta de 21/10: *"a IA entrou para mudar uma regra ou para acelerar a regra antiga?"*
- **26/10 como virada.** "Qual modelo vamos usar?" é um antagonista concreto e reconhecível. O Ato 1 mostra onde está a restrição; o Ato 2 tira a consequência.
- **Sequência do Ato 2.** Ep.2 (tokens) em 27/10 antes do post de custo em 28/10 é a dependência certa: o Ep.2 já diz que se paga por token de entrada e de saída.
- **Ressalvas honestas** ("segundo o fornecedor", "números ilustrativos"). Dão credibilidade técnica.

## Ajustar

1. **Tese mais fiel à TOC.** Hoje a tese pula *explorar* e *subordinar*, dois dos 5 passos de focalização (Goldratt, *A Meta*). Mudar a regra, na prática, quase sempre é subordinar. O resultado se mede em throughput. O próprio post de 22/10 já fala em "explorá-la com o que já existe".
   - Versão longa: *Restrição → explorar → mudar a regra (subordinar) → ferramenta só para elevar → medir em throughput*.
   - Versão curta para a arte: *Restrição → Regra → Ferramenta → Throughput*.
2. **Frase-assinatura literal.** A tese aparece cada vez com outras palavras ("só então usar a IA", "só então comprar ferramenta"). Sugestão: fixar *"Primeiro a restrição e a regra. Depois a ferramenta."* e repeti-la igual na "Minha leitura".
3. **Arco visível ao leitor.** Fundar, Deslocar e Governar só existem no planejamento. Três mecanismos leves resolvem:
   - **Rótulo de topo fixo por formato:** "TOC Fundamentos |", "IA do básico ao avançado · Ep.N |", "IA Aplicada |".
   - **Frase-ponte em 26/10**, por exemplo: *"Até aqui: o que é restrição. A partir de hoje: onde está a vantagem quando o modelo vira insumo."* O Ep.1 já disse que "trocar de LLM não resolve", então a ponte pode voltar ao pedido 4521.
   - **A mesma frase-ponte na virada para novembro.**
4. **Fio condutor recorrente.** Já existem quatro, pouco usados: o pedido 4521 e a cláusula 7 (Ep.1); os envolvidos de 18/10 (comprador, loja, logística, fornecedor); a sala do kickoff; e a pergunta de 21/10. Repetir pelo menos o 4521 e a pergunta nos Atos 2 e 3.
5. **25/10 (mapa de apuração) fora do arco.** Não tem TOC, nem supply chain, nem "Minha leitura". Os três revisores pediram para marcá-lo como "extra, fora do arco" e não contar como fundação. Não precisa mexer no post; a apresentação já o mostra como extra.
6. **Promessas abertas.**
   - 18/10 prometeu, para o próximo post da série, "como a reposição funciona hoje no varejo, sem IA". Nada na grade cumpre isso.
   - 27/10 (Ep.2) precisa cumprir o que o Ep.1 anunciou: "por que o assistente inventa um lead time".
7. **Âncoras dos posts pendentes.**
   - **28/10 (custo):** medir o custo por throughput ganho, não só por token, e lembrar que o RAG do Ep.1 aumenta os tokens de entrada.
   - **30/10 (ML × gen):** ancorar no baseline estatístico citado em 22/10 (FPP e StatsForecast), que é o pré-requisito real, mais que o Ep.2.
   - **03/11 (time de dados):** retomar os quadrantes de 18/10 e perguntar qual é a "sereia" do time de dados.

## Para decisão do Darú

- **01/11, governança de agentes.** Cai num domingo. Além disso, até ali o leitor só viu RAG (Ep.1) e LLM/tokens (Ep.2): ferramentas, agentes, evals e harness ainda não saíram. Opções:
  - (i) manter a data e enquadrar o post como **governança de documentos e regra de decisão** (dono, aprovação, quem tira o contrato vencido da base), que só depende do Ep.1;
  - (ii) manter o tema e mover o post para depois dos Eps. 7 e 8;
  - (iii) manter como está e explicar agentes dentro do próprio post.
- **Clímax do Ato 3.** Hoje o Ato 3 é uma lista de temas. O clímax natural é 03/11: a restrição não é a tecnologia, é o time e a regra. O revisor de narrativa sugere inverter os temas de 01/11 e 03/11, mantendo as datas, e fechar o ciclo voltando aos quadrantes de 18/10. "Fundamentos intercalados" e "Por dentro do agente" ficariam como continuação, fora do arco.
- **Promessa de 18/10.** Escolher entre cumprir (por exemplo, como ângulo de 03/11) e dizer num próximo post que o tema foi adiado.

## Arquivos dessincronizados

Os três pontos abaixo pedem alinhamento, não decisão de conteúdo:

- **Data do Ep.1.** `calendario/calendario.json` diz 23/10; o post e a grade dizem 24/10.
- **Slot de 03/11.** A grade põe "Restrição do time de dados"; o `calendario.json` põe o Ep.3 (Embeddings).
- **Post "modelo = insumo".** O `calendario.json` tem "O modelo virou commodity" em 04/11, e a grade o puxou para 26/10.

O `calendario.json` só será atualizado quando o Darú confirmar as datas.
