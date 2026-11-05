"""Contrôles automatiques du README (Ex.3).

Ces tests sont rouges tant que le README n'est pas rédigé. Ils lisent le
fichier README.md et rejouent ses commandes `python -m pluvio.cli ...` ou
`python script.py ...`. Les autres commandes (venv, pip, git, pytest) ne sont
pas rejouées, notamment `pytest`, pour éviter une boucle infinie.
"""

import re
import shlex
import subprocess
import sys
import unicodedata
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parent.parent
README = RACINE / "README.md"
SECTIONS = ["Description", "Prérequis", "Installation", "Utilisation",
            "Tests", "Arborescence", "Contribution", "Licence", "Contact"]
LANGAGES_COMMANDES = {"bash", "sh", "shell", "console", "powershell", "ps1"}
BLOC = re.compile(r"^```(?P<info>[^\n`]*)\n(?P<corps>.*?)^```[ \t]*$",
                  re.DOTALL | re.MULTILINE)


def texte():
    assert README.is_file(), "README.md est absent"
    return README.read_text(encoding="utf-8")


def sans_blocs(contenu):
    return BLOC.sub("", contenu)


def titres(contenu):
    trouves = re.findall(r"^(#{1,6})[ \t]+(.+?)[ \t#]*$",
                         sans_blocs(contenu), re.MULTILINE)
    return [(len(diese), intitule) for diese, intitule in trouves]


def normaliser(chaine):
    decompose = unicodedata.normalize("NFD", chaine.casefold())
    return "".join(c for c in decompose if unicodedata.category(c) != "Mn")


def rejouable(ligne):
    """Vrai pour `python -m pluvio.cli ...` ou `python script.py ...`."""
    mots = shlex.split(ligne)
    return len(mots) > 1 and (mots[1:3] == ["-m", "pluvio.cli"]
                              or mots[1].endswith(".py"))


def commandes(contenu):
    """Renvoyer les commandes à rejouer des blocs de commandes."""
    vues = []
    for bloc in BLOC.finditer(contenu):
        if bloc["info"].strip().lower() not in LANGAGES_COMMANDES:
            continue
        for ligne in bloc["corps"].splitlines():
            ligne = ligne.strip()
            if (re.match(r"(python3?|py)\s", ligne) and rejouable(ligne)
                    and ligne not in vues):
                vues.append(ligne)
    return vues


def executer(ligne):
    mots = shlex.split(ligne)
    return subprocess.run([sys.executable] + mots[1:], cwd=RACINE, timeout=30,
                          capture_output=True, text=True, encoding="utf-8")


def test_readme_existe_et_n_est_pas_vide():
    assert len(texte().strip()) > 200


def test_un_seul_titre_de_niveau_1_en_premiere_position():
    niveaux = [n for n, _ in titres(texte())]
    assert niveaux.count(1) == 1
    assert niveaux[0] == 1


def test_hierarchie_des_titres_sans_saut():
    niveaux = [n for n, _ in titres(texte())]
    for avant, apres in zip(niveaux, niveaux[1:]):
        assert apres <= avant + 1, f"saut de niveau : h{avant} puis h{apres}"


@pytest.mark.parametrize("section", SECTIONS)
def test_section_presente(section):
    cherchee = normaliser(section)
    intitules = [normaliser(i) for _, i in titres(texte())]
    assert any(cherchee in i for i in intitules), f"section « {section} »"


def test_tous_les_blocs_de_code_ont_un_langage():
    for bloc in BLOC.finditer(texte()):
        assert bloc["info"].strip(), "bloc de code sans langage"


def test_les_blocs_de_code_sont_fermes():
    assert len(re.findall(r"^```", texte(), re.MULTILINE)) % 2 == 0


def test_signale_les_donnees_fictives():
    assert re.search(r"ficti[fv]", texte(), re.IGNORECASE)


def test_au_moins_deux_exemples_de_commande():
    assert len(commandes(texte())) >= 2


def test_les_exemples_de_commande_fonctionnent():
    lignes = commandes(texte())
    assert lignes, "aucune commande à rejouer dans le README"
    for ligne in lignes:
        resultat = executer(ligne)
        assert resultat.returncode == 0, f"{ligne} -> {resultat.stderr}"


def test_les_sorties_affichees_correspondent_aux_commandes():
    contenu = texte()
    hors_commandes = BLOC.sub(
        lambda m: "" if m["info"].strip().lower() in LANGAGES_COMMANDES
        else m.group(0), contenu)
    lignes = commandes(contenu)
    assert lignes, "aucune commande à rejouer dans le README"
    for ligne in lignes:
        premiere = next(x for x in executer(ligne).stdout.splitlines()
                        if x.strip())
        assert premiere.strip() in hors_commandes, f"sortie de : {ligne}"
