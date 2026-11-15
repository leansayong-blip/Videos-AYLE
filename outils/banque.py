"""Banque de photos Unsplash deja telechargees (economie de tokens et d'appels Unsplash).

Usage :
  python3 outils/banque.py chercher "nuit,voiture" [--theme Storytime] [--jours 14]
      -> photos dont les tags/description contiennent un des mots, non utilisees depuis N jours (defaut 14)
  python3 outils/banque.py ajouter <fichier.jpg> <id> "<photographe>" <username> <Theme> "<description>" "tag1,tag2"
      -> copie la photo (1620 px de large max) dans banque/photos/<id>.jpg et l'ajoute a l'index
  python3 outils/banque.py preparer <dossier_src> <nom_scene>=<id> [...]
      -> copie banque/photos/<id>.jpg vers <dossier_src>/<nom_scene>.jpg (pour generic_build)
  python3 outils/banque.py utiliser <video> <date_publication> <id> [...]
      -> note l'utilisation (evite de reprendre la meme photo trop tot)
  python3 outils/banque.py credits <id> [...]
      -> liste des photographes a citer
"""
import json, os, sys, shutil, datetime
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IDX = os.path.join(R, "banque", "index.json")

def load(): return json.load(open(IDX)) if os.path.exists(IDX) else []
def save(d): json.dump(d, open(IDX, "w"), ensure_ascii=False, indent=1)

def chercher(mots, theme=None, jours=14):
    ref = datetime.date.today() + datetime.timedelta(days=1)
    mots = [m.strip().lower() for m in mots.split(",") if m.strip()]
    for p in load():
        txt = (" ".join(p["tags"]) + " " + p["description"]).lower()
        if mots and not any(m in txt for m in mots): continue
        last = max([u["publication"] for u in p["utilisations"]], default="2000-01-01")
        recent = (ref - datetime.date.fromisoformat(last)).days < jours
        flag = "RECENT" if recent else "ok"
        print(f'{p["id"]:14} {flag:6} {p["theme"]:10} {last}  {p["description"]}  [{",".join(p["tags"])}]')

def ajouter(f, pid, phot, user, theme, desc, tags):
    from PIL import Image
    d = load()
    if any(p["id"] == pid for p in d): print("deja dans la banque"); return
    out = f"banque/photos/{pid}.jpg"
    im = Image.open(f).convert("RGB")
    if im.width > 1620: im = im.resize((1620, round(im.height * 1620 / im.width)), Image.LANCZOS)
    im.save(os.path.join(R, out), quality=86, optimize=True)
    d.append(dict(id=pid, fichier=out, photographe=phot, username=user, theme=theme, description=desc,
                  tags=[t.strip() for t in tags.split(",")], largeur=im.width, hauteur=im.height, utilisations=[]))
    save(d); print("ajoutee", pid)

def preparer(src, pairs):
    os.makedirs(src, exist_ok=True)
    for pr in pairs:
        nom, pid = pr.split("="); shutil.copy(os.path.join(R, "banque", "photos", pid + ".jpg"), os.path.join(src, nom + ".jpg"))
    print("ok", len(pairs))

def utiliser(video, date, ids):
    d = load()
    for p in d:
        if p["id"] in ids: p["utilisations"].append(dict(video=video, publication=date))
    save(d); print("ok")

def credits(ids):
    d = {p["id"]: p["photographe"] for p in load()}
    print(", ".join(dict.fromkeys(d[i] for i in ids if i in d)))

if __name__ == "__main__":
    a = sys.argv[1:]
    if not a: print(__doc__); sys.exit()
    c = a[0]
    if c == "chercher":
        th = a[a.index("--theme") + 1] if "--theme" in a else None
        j = int(a[a.index("--jours") + 1]) if "--jours" in a else 14
        chercher(a[1] if len(a) > 1 and not a[1].startswith("--") else "", th, j)
    elif c == "ajouter": ajouter(*a[1:8])
    elif c == "preparer": preparer(a[1], a[2:])
    elif c == "utiliser": utiliser(a[1], a[2], a[3:])
    elif c == "credits": credits(a[1:])
