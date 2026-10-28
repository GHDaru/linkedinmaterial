# Parecer de três críticos · Tipos de modelos de linguagem

Avaliação em 28/10/2026 do vídeo (versão sem crítica, fechando nos eixos) e do texto do post.

| Crítico | Veredito |
|---|---|
| Pesquisador de IA | Sólido e publicável; quatro ajustes de precisão, nenhum erro grosseiro. |
| Estrategista de LinkedIn | 7/10. Conteúdo próprio e sólido, mas o gancho cita "esta imagem", que não aparece no post, e a virada pela TOC só vem no fim. |
| Diretor de supply chain | Salvaria pelos eixos, passaria reto pelo resto: até o MoE parece aula de IA, e o problema dele só aparece no fim. |

## Em que os três concordam

1. **O gancho "Esta imagem resume bem" não funciona**: o post mostra o vídeo, não a imagem. Crédito sugerido: "Inspirado no infográfico 'Top 5 Types of Language Models', de Jean Lee".
2. **O vídeo não tem a virada TOC**, que é o diferencial. Sugestão: cena final "Coletor → pequeno · Foto de avaria → visão · Reposição → raciocínio + ferramenta · Volume alto → o mais barato que acerta. Escolha pela restrição."
3. **MoE ocupa duas trocas de token para um detalhe de arquitetura.** Encurtar.
4. **O exemplo do palete "48 caixas" é arriscado**: contagem é ponto fraco conhecido dos VLMs, e inventário inferido não se aceita. Trocar por leitura de etiqueta e DANFE, ou avaria no recebimento.
5. **Texto fala em cinco tipos, vídeo numera seis.** Alinhar.

## Correções técnicas (pesquisador)

- LLM: "modelo grande treinado em texto; a maioria gera prevendo o próximo token" (o dLLM também é LLM).
- MoE: economiza cálculo, não memória; "especialista" não é especialista em assunto.
- SLM: faixa de "centenas de milhões a ~10 bi"; os menores, quantizados, rodam no celular.
- Difusão: "3 passadas" exagera; usar "vários tokens por passo · menos passos que tokens".
- LRM: "treinado com aprendizado por reforço para raciocinar"; "pense passo a passo" no prompt não basta.
- Híbridos: "Nemotron-H (Mamba), Qwen3-Next (Gated DeltaNet)".
- Embeddings: "base da busca semântica no RAG".
- Cena do LLM: "pós-treino (ajuste fino e RLHF)".

## Leitura no celular (estrategista)

Nota cinza do VLM, rótulos "Especialista N" e etiquetas dos eixos ficam pequenos demais: mínimo 28 px ou cortar. A cena do LRM precisa de 4 s ou perde a linha de checagem.

## Para o público de operação (diretor)

- Explicar token ("pedaço de palavra") e parâmetro ("tamanho do modelo; quanto maior, mais caro de rodar").
- Destilação, poda e quantização são jargão de fabricante: cortar do vídeo.
- Difusão, Mamba e VLA: reduzir a uma linha ("quase nunca são a primeira escolha para a operação hoje").
- O caminhão das 7h50 é conta de TMS: vira exemplo de quando **não** usar LRM.
- Chamada melhor: "Qual processo seu travaria primeiro se a IA errasse?" (alternativa do estrategista: "Qual é a restrição do seu processo hoje: latência, custo, imagem ou cálculo?").
- Exemplo que ele comentaria: doca de recebimento, com VLM lendo DANFE e etiqueta e cruzando com o pedido, SLM no coletor offline e modelo barato classificando ocorrências em texto livre.

## Divergência

O estrategista quer abrir com "não são 5 caixas, são eixos" (a crítica). O Darú decidiu que a crítica fica fora da animação; o vídeo segue com "Eixos dos modelos".
