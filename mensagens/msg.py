"""Cliente do protocolo msg/1 (só biblioteca padrão do Python).

Rode a partir da raiz do repositório, na branch `mensagens`:
  python mensagens/msg.py enviar --de claude --para bot --tipo pedido --assunto "..." --corpo "..."
  python mensagens/msg.py caixa --para bot
  python mensagens/msg.py ler <id>
  python mensagens/msg.py recibo --de bot <id>
  python mensagens/msg.py validar
Use --sem-git em enviar/recibo para só gravar o arquivo, sem pull/commit/push.
"""
import argparse, datetime as dt, json, pathlib, re, secrets, subprocess, sys

BASE = pathlib.Path(__file__).resolve().parent
CAIXA = BASE / "caixa"
BRANCH = "mensagens"
TIPOS = {"pedido", "resposta", "evento", "recibo", "erro"}
RE_ID = re.compile(r"^\d{8}T\d{6}Z-[a-z0-9_]+-[0-9a-f]{4}$")
RE_DATA = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
OBRIG = ["protocolo", "id", "de", "para", "criada_em", "tipo", "conversa", "assunto", "corpo"]


def participantes():
    dados = json.loads((BASE / "participantes.json").read_text(encoding="utf-8"))
    return {p["id"] for p in dados["participantes"]}


def todas():
    for f in sorted(CAIXA.rglob("*.json")):
        yield f, json.loads(f.read_text(encoding="utf-8"))


def achar(id_):
    for f, m in todas():
        if m.get("id") == id_:
            return m
    sys.exit(f"Mensagem não encontrada: {id_}")


def problemas(m, arquivo=None, ids=None):
    p = [f"falta o campo '{c}'" for c in OBRIG if c not in m]
    if p:
        return p
    validos = participantes() | {"todos"}
    if m["protocolo"] != "msg/1": p.append("protocolo deve ser 'msg/1'")
    if not RE_ID.match(m["id"]): p.append("id fora do padrão AAAAMMDDTHHMMSSZ-de-xxxx")
    if arquivo and arquivo.stem != m["id"]: p.append("nome do arquivo diferente do id")
    if m["de"] not in validos - {"todos"}: p.append(f"remetente desconhecido: {m['de']}")
    if m["para"] not in validos: p.append(f"destinatário desconhecido: {m['para']}")
    if not RE_DATA.match(m["criada_em"]): p.append("criada_em deve ser ISO 8601 UTC (…Z)")
    if m["tipo"] not in TIPOS: p.append(f"tipo inválido: {m['tipo']}")
    if not 1 <= len(m["assunto"]) <= 120: p.append("assunto deve ter de 1 a 120 caracteres")
    if m["tipo"] in {"resposta", "recibo", "erro"} and not m.get("responde_a"):
        p.append(f"'{m['tipo']}' exige responde_a")
    if ids is not None and m.get("responde_a") and m["responde_a"] not in ids:
        p.append(f"responde_a aponta para mensagem inexistente: {m['responde_a']}")
    if m.get("prioridade", "normal") not in {"normal", "alta"}: p.append("prioridade inválida")
    return p


def git(*args):
    return subprocess.run(["git", *args], cwd=BASE.parent, check=True, text=True, capture_output=True).stdout


def publicar(arquivo, m):
    git("add", str(arquivo))
    git("commit", "-q", "-m", f"msg: {m['de']} → {m['para']} · {m['tipo']} · {m['assunto']}")
    for tentativa in range(3):
        try:
            git("push", "-q", "origin", BRANCH)
            return
        except subprocess.CalledProcessError:
            git("pull", "-q", "--rebase", "origin", BRANCH)
    sys.exit("Não consegui enviar depois de 3 tentativas. O commit ficou local.")


def criar(de, para, tipo, assunto, corpo, responde_a=None, anexos=None, prioridade="normal",
          prazo=None, sem_git=False):
    if not sem_git:
        git("pull", "-q", "--rebase", "origin", BRANCH)
    agora = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    id_ = f"{agora:%Y%m%dT%H%M%SZ}-{de}-{secrets.token_hex(2)}"
    conversa = achar(responde_a)["conversa"] if responde_a else id_
    m = {"protocolo": "msg/1", "id": id_, "de": de, "para": para,
         "criada_em": agora.strftime("%Y-%m-%dT%H:%M:%SZ"), "tipo": tipo, "conversa": conversa,
         "responde_a": responde_a, "assunto": assunto, "corpo": corpo, "anexos": anexos or [],
         "prioridade": prioridade, "prazo": prazo}
    erros = problemas(m, ids={x["id"] for _, x in todas()})
    if erros:
        sys.exit("Mensagem inválida:\n  " + "\n  ".join(erros))
    arquivo = CAIXA / f"{agora:%Y/%m/%d}" / f"{id_}.json"
    arquivo.parent.mkdir(parents=True, exist_ok=True)
    arquivo.write_text(json.dumps(m, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if not sem_git:
        publicar(arquivo, m)
    print(id_)
    return m


def caixa(para):
    msgs = [m for _, m in todas()]
    lidas = {m["responde_a"] for m in msgs if m["tipo"] == "recibo" and m["de"] == para}
    pend = [m for m in msgs if m["para"] in {para, "todos"} and m["de"] != para
            and m["tipo"] != "recibo" and m["id"] not in lidas]
    for m in pend:
        marca = "!" if m.get("prioridade") == "alta" else " "
        print(f"{marca} {m['id']}  {m['de']:>8} · {m['tipo']:<8} {m['assunto']}")
    if not pend:
        print(f"Nenhuma mensagem pendente para {para}.")


def main():
    ap = argparse.ArgumentParser(description="Cliente do protocolo msg/1")
    sub = ap.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("enviar")
    e.add_argument("--de", required=True); e.add_argument("--para", required=True)
    e.add_argument("--tipo", required=True, choices=sorted(TIPOS))
    e.add_argument("--assunto", required=True); e.add_argument("--corpo", default="")
    e.add_argument("--responde-a"); e.add_argument("--anexo", action="append", default=[])
    e.add_argument("--prioridade", default="normal", choices=["normal", "alta"])
    e.add_argument("--prazo"); e.add_argument("--sem-git", action="store_true")
    c = sub.add_parser("caixa"); c.add_argument("--para", required=True)
    l = sub.add_parser("ler"); l.add_argument("id")
    r = sub.add_parser("recibo"); r.add_argument("--de", required=True); r.add_argument("id")
    r.add_argument("--sem-git", action="store_true")
    sub.add_parser("validar")
    a = ap.parse_args()

    if a.cmd == "enviar":
        anexos = [{"caminho": x.split("@")[0], "ref": x.split("@")[1] if "@" in x else "main"} for x in a.anexo]
        criar(a.de, a.para, a.tipo, a.assunto, a.corpo, a.responde_a, anexos, a.prioridade, a.prazo, a.sem_git)
    elif a.cmd == "caixa":
        caixa(a.para)
    elif a.cmd == "ler":
        print(json.dumps(achar(a.id), ensure_ascii=False, indent=2))
    elif a.cmd == "recibo":
        orig = achar(a.id)
        criar(a.de, orig["de"], "recibo", f"Recebido: {orig['assunto']}"[:120], "", a.id, sem_git=a.sem_git)
    elif a.cmd == "validar":
        lista = list(todas()); ids = {m.get("id") for _, m in lista}; ruins = 0
        for f, m in lista:
            for p in problemas(m, f, ids):
                ruins += 1; print(f"{f.relative_to(BASE)}: {p}")
        print(f"{len(lista)} mensagens, {ruins} problemas")
        sys.exit(1 if ruins else 0)


if __name__ == "__main__":
    main()
