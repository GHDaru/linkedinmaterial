"""Gera calendario.html e roteiro.html a partir de calendario.json."""
import json, pathlib, datetime as dt
aqui = pathlib.Path(__file__).parent
dados = json.loads((aqui / "calendario.json").read_text(encoding="utf-8"))
for p in dados["posts"]:
    d = dt.date.fromisoformat(p["data"])
    assert d.weekday() < 5, f"{p['id']} cai em fim de semana: {d}"
for nome in ("calendario", "roteiro"):
    t = (aqui / f"{nome}.template.html").read_text(encoding="utf-8")
    (aqui / f"{nome}.html").write_text(t.replace("/*DATA*/null", json.dumps(dados, ensure_ascii=False)), encoding="utf-8")
    print("ok", nome)
