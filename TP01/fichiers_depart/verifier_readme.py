"""Contrôles simples sur un fichier README Markdown.

Usage : python verifier_readme.py README.md
"""

import re
import sys
import unicodedata
from pathlib import Path

SECTIONS_ATTENDUES = ("Description", "Prérequis", "Installation",
                      "Utilisation", "Tests", "Arborescence",
                      "Contribution", "Licence", "Contact")


def normaliser(texte):
    """Mettre en minuscules et retirer les accents (« Prérequis » -> « prerequis »)."""
    decompose = unicodedata.normalize("NFD", texte.casefold())
    return "".join(c for c in decompose if unicodedata.category(c) != "Mn")


def titres(texte):
    """Lister les titres « # » du texte, hors blocs de code.

    Chaque titre est un couple (niveau, intitulé).
    """
    resultat = []
    dans_un_bloc = False
    for ligne in texte.splitlines():
        if ligne.strip().startswith("```"):
            dans_un_bloc = not dans_un_bloc
        elif not dans_un_bloc:
            m = re.match(r"(#{1,6})[ \t]+(.+?)[ \t#]*$", ligne)
            if m:
                resultat.append((len(m.group(1)), m.group(2)))
    return resultat


def sections_manquantes(texte, attendues=SECTIONS_ATTENDUES):
    # TODO (Ex.4, question 1) : écrire la docstring, puis le corps.
    raise NotImplementedError


def blocs_sans_langage(texte):
    # TODO (Ex.4, question 2) : écrire la docstring, puis le corps.
    raise NotImplementedError


def main(argv=None):
    """Afficher le rapport ; renvoyer 0 si le README est conforme, sinon 1."""
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 1:
        print("Usage : python verifier_readme.py README.md", file=sys.stderr)
        return 2
    texte = Path(argv[0]).read_text(encoding="utf-8")
    manquantes = sections_manquantes(texte)
    sans_langage = blocs_sans_langage(texte)
    for section in manquantes:
        print(f"Section manquante : {section}")
    for numero in sans_langage:
        print(f"Ligne {numero} : bloc de code sans langage")
    if not manquantes and not sans_langage:
        print("README conforme.")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
