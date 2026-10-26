# Modelos de mundo na supply chain: simule a restrição, não o mundo

**Publicado em:** 2026-10-20 · [link do post](https://www.linkedin.com/feed/update/urn:li:share:7518312859643187201/)

**Série relacionada:** prepara o Ep. 10 da série [IA do básico ao avançado](../../series/ia-do-basico-ao-avancado/).

## Texto

```
𝗠𝗢𝗗𝗘𝗟𝗢𝗦 𝗗𝗘 𝗠𝗨𝗡𝗗𝗢 𝗡𝗔 𝗦𝗨𝗣𝗣𝗟𝗬 𝗖𝗛𝗔𝗜𝗡:
𝗦𝗜𝗠𝗨𝗟𝗘 𝗔 𝗥𝗘𝗦𝗧𝗥𝗜ÇÃ𝗢, 𝗡Ã𝗢 𝗢 𝗠𝗨𝗡𝗗𝗢.

Um LLM aprende a prever a próxima palavra. Um modelo de mundo (world model) tenta prever o próximo estado de um ambiente, dada uma ação. A pergunta muda de "o que vem depois neste texto?" para "o que acontece se eu fizer isto?".

A Google DeepMind descreve assim: sistemas que simulam partes do mundo para prever como o ambiente evolui e como as ações de um agente o afetam. O Genie 3 gera mundos navegáveis em tempo real, mas a DeepMind reconhece limites: consistência por poucos minutos, e a interação entre vários agentes ainda é desafio de pesquisa.

O tema virou corrida. Em março de 2026, a AMI Labs, de Yann LeCun, captou US$ 1,03 bilhão para isso, e o CEO previu que, em seis meses, toda empresa se diria "modelo de mundo" para captar dinheiro. Em junho, a BAAI, de Pequim, lançou o Physis-v0.1 e citou simulação e gêmeos digitais como demanda futura.

E na supply chain? Quase tudo que se mostra é físico: robôs, carros, armazéns. Só que a cadeia anda por eventos, entre muitos agentes: o pedido chega, o lote libera, o caminhão atrasa, a máquina para.

Um artigo de Tsinghua e Beihang (2026) defende modelos de mundo de eventos discretos para supply chain e processos de negócio, e mostra o dilema: simuladores feitos à mão são consistentes, mas caros de construir e adaptar; modelos neurais são flexíveis, mas podem perder consistência em horizontes longos.

A previsão de demanda responde "quanto vai vender". O modelo de mundo responde "o que acontece com o fluxo se eu mudar o pedido, o lote ou a sequência". Uma estima. O outro ajuda a decidir.

Minha leitura: modelo de mundo útil em supply chain não é o que imita o mundo, é o que simula a restrição. Goldratt já dizia em A Meta: uma hora perdida no gargalo é uma hora perdida no sistema todo; uma hora ganha fora dele é miragem. Sem saber onde está o gargalo, simular tudo é custo: mais dados, mais cenários e a mesma decisão errada, com mais confiança.

O caminho é mais modesto: achar a restrição, modelar bem o que acontece nela e nos pulmões que a protegem, e só então usar a IA para testar cenários. E mudar o processo de decisão, para que a simulação vire ação, não relatório.

Se você tivesse amanhã um modelo de mundo da sua operação, qual restrição simularia primeiro?

Fontes:
Google DeepMind, Genie 3: https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/
TechCrunch, AMI Labs: https://techcrunch.com/2026/03/09/yann-lecuns-ami-labs-raises-1-03-billion-to-build-world-models/
CGTN, BAAI Physis-v0.1: https://news.cgtn.com/news/2026-06-14/China-unveils-AI-world-model-that-understands-physical-world-1NYmex0KQlG/index.html
Tsinghua e Beihang (Chen et al., 2026), modelos de mundo de eventos discretos: https://arxiv.org/abs/2603.03784

#IA #ModelosDeMundo #WorldModels #SupplyChain #TOC #TeoriaDasRestricoes #Simulacao
```

Arquivo-fonte: [`texto.txt`](texto.txt).

## Materiais

| Arquivo | O que é |
|---|---|
| [`imagem.png`](imagem.png) | Imagem final do post (1200×1200) |
| [`texto.txt`](texto.txt) | Texto publicado |

## Referências

GOOGLE DEEPMIND. Genie 3: A new frontier for world models. 2025. Disponível em: https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/. Acesso em: 20 out. 2026.

TECHCRUNCH. Yann LeCun's AMI Labs raises $1.03B to build world models. 9 mar. 2026. Disponível em: https://techcrunch.com/2026/03/09/yann-lecuns-ami-labs-raises-1-03-billion-to-build-world-models/. Acesso em: 20 out. 2026.

CGTN. China unveils AI world model that understands physical world. 14 jun. 2026. Disponível em: https://news.cgtn.com/news/2026-06-14/China-unveils-AI-world-model-that-understands-physical-world-1NYmex0KQlG/index.html. Acesso em: 20 out. 2026.

CHEN et al. Specification-Driven Generation and Evaluation of Discrete-Event World Models via the DEVS Formalism. arXiv:2603.03784, 2026. Disponível em: https://arxiv.org/abs/2603.03784. Acesso em: 20 out. 2026.

GOLDRATT, Eliyahu M.; COX, Jeff. *A Meta*. São Paulo: Nobel, [s.d.].
