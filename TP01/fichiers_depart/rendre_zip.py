"""Créer rendu.zip, l'archive de secours du dépôt (dossier .git compris).

Usage : python rendre_zip.py
Les environnements virtuels et les caches Python sont exclus.
"""

import zipfile
from pathlib import Path

RACINE = Path(__file__).resolve().parent
EXCLUS = {".venv", "__pycache__", ".pytest_cache", "rendu.zip"}


def fichiers_a_archiver(racine=RACINE):
    """Lister les fichiers du dépôt, sauf les dossiers exclus."""
    for chemin in sorted(racine.rglob("*")):
        relatif = chemin.relative_to(racine)
        if chemin.is_file() and not EXCLUS.intersection(relatif.parts):
            yield chemin, relatif


def main():
    """Écrire rendu.zip à la racine et afficher le nombre de fichiers."""
    sortie = RACINE / "rendu.zip"
    with zipfile.ZipFile(sortie, "w", zipfile.ZIP_DEFLATED) as archive:
        for chemin, relatif in fichiers_a_archiver():
            archive.write(chemin, relatif.as_posix())
    with zipfile.ZipFile(sortie) as archive:
        print(f"{sortie.name} créé : {len(archive.namelist())} fichiers")


if __name__ == "__main__":
    main()
