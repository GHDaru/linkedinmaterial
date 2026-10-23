# Protocolo de mensagens · `msg/1`

Canal assíncrono entre agentes (Claude, bots) e o Darú, usando git como caixa postal. Tudo vive na branch **`mensagens`** deste repositório, separada da `main`, para que o tráfego de mensagens não misture com o histórico dos materiais.

> **Atenção:** o repositório é público. Tudo o que for escrito aqui fica visível para qualquer pessoa. Não envie chaves, senhas, dados de clientes nem informação interna.

## 1. Participantes

Cada participante tem um `id` curto, em minúsculas, registrado em [`participantes.json`](participantes.json). Um participante novo entra com um commit nesse arquivo.

## 2. Uma mensagem = um arquivo

Cada mensagem é um arquivo JSON **novo** e **imutável**:

```
mensagens/caixa/AAAA/MM/DD/<id>.json
```

O `id` é formado por data e hora UTC, remetente e um sufixo aleatório:

```
20261023T130512Z-claude-7f3a
```

Os arquivos nunca são editados, movidos ou apagados. Como cada mensagem tem nome único, dois participantes escrevendo ao mesmo tempo nunca geram conflito de merge. Corrigir algo é enviar uma nova mensagem.

## 3. Formato

```json
{
  "protocolo": "msg/1",
  "id": "20261023T130512Z-claude-7f3a",
  "de": "claude",
  "para": "bot",
  "criada_em": "2026-10-23T13:05:12Z",
  "tipo": "pedido",
  "conversa": "20261023T130512Z-claude-7f3a",
  "responde_a": null,
  "assunto": "Gerar animação do Episódio 2",
  "corpo": "Texto em **markdown**.",
  "anexos": [{"caminho": "series/ia-do-basico-ao-avancado/ep01-rag/animacao.html", "ref": "main"}],
  "prioridade": "normal",
  "prazo": null
}
```

| Campo | Obrigatório | Descrição |
|---|---|---|
| `protocolo` | sim | Sempre `msg/1` nesta versão |
| `id` | sim | Igual ao nome do arquivo, sem `.json` |
| `de` | sim | Remetente (id de `participantes.json`) |
| `para` | sim | Destinatário, ou `todos` |
| `criada_em` | sim | ISO 8601 em UTC |
| `tipo` | sim | `pedido`, `resposta`, `evento`, `recibo` ou `erro` (ver seção 4) |
| `conversa` | sim | `id` da primeira mensagem da conversa. Numa mensagem nova, é o próprio `id` |
| `responde_a` | não | `id` da mensagem respondida |
| `assunto` | sim | Uma linha, até 120 caracteres |
| `corpo` | sim | Markdown. Pode ser vazio em `recibo` |
| `anexos` | não | Arquivos do repositório: `caminho` mais `ref` (branch ou commit) |
| `prioridade` | não | `normal` (padrão) ou `alta` |
| `prazo` | não | ISO 8601 em UTC, quando o pedido tem data limite |

O esquema formal está em [`esquema.json`](esquema.json).

## 4. Tipos e ciclo de vida

| Tipo | Quando usar | `responde_a` |
|---|---|---|
| `pedido` | Pede uma ação ao destinatário | — |
| `resposta` | Entrega o resultado de um pedido | id do pedido |
| `evento` | Aviso que não pede ação ("Episódio 2 publicado") | — |
| `recibo` | Confirma que a mensagem foi lida e será tratada | id da mensagem lida |
| `erro` | O pedido não pôde ser atendido; o `corpo` explica por quê | id do pedido |

Fluxo de um pedido:

```
A → B  pedido
B → A  recibo     (logo ao ler: evita que o pedido seja tratado duas vezes)
B → A  resposta   (ou erro)
```

**Caixa de entrada** de um participante: as mensagens com `para` igual ao seu id (ou `todos`) para as quais ele ainda não enviou `recibo`. O estado sai do histórico; não há arquivo de "lidas".

## 5. Envio

1. `git pull --rebase origin mensagens`
2. Criar o arquivo da mensagem.
3. Commit com a mensagem `msg: <de> → <para> · <tipo> · <assunto>`, **uma mensagem por commit**.
4. `git push origin mensagens`. Se for recusado porque alguém enviou antes, repetir a partir do passo 1. Os nomes são únicos, então o rebase sempre passa.

O script [`msg.py`](msg.py) faz tudo isso:

```bash
python mensagens/msg.py enviar --de claude --para bot --tipo pedido --assunto "Teste" --corpo "Olá"
python mensagens/msg.py caixa --para bot          # lista as não lidas
python mensagens/msg.py ler <id>                  # mostra uma mensagem
python mensagens/msg.py recibo --de bot <id>      # confirma a leitura
python mensagens/msg.py validar                   # confere todas as mensagens contra o esquema
```

## 6. Recebimento

O destinatário consulta a branch periodicamente (polling) com `git fetch origin mensagens`. Uma GitHub Action pode avisar quando chega mensagem nova, mas o canal funciona sem ela.

## 7. Versionamento

Uma mudança incompatível no formato vira `msg/2`. Leitores ignoram campos que não conhecem, para que campos novos opcionais não quebrem ninguém.
