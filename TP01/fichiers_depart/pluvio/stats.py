"""Lecture et calculs sur des relevés de pluie (données fictives)."""

import csv
from pathlib import Path


def lire_releves(chemin):
    """Lire un CSV (date, commune, pluie_mm) et renvoyer une liste de dicts.

    Les lignes vides et celles qui commencent par « # » sont ignorées.
    """
    releves = []
    with Path(chemin).open(encoding="utf-8", newline="") as fichier:
        lignes = (x for x in fichier if x.strip() and not x.startswith("#"))
        for ligne in csv.DictReader(lignes):
            releves.append({
                "date": ligne["date"],
                "commune": ligne["commune"],
                "pluie_mm": float(ligne["pluie_mm"]),
            })
    return releves


def filtrer(releves, commune=None, mois=None):
    """Garder les relevés d'une commune et/ou d'un mois (format AAAA-MM)."""
    if commune is not None:
        voulue = commune.casefold()
        releves = [r for r in releves if r["commune"].casefold() == voulue]
    if mois is not None:
        releves = [r for r in releves if r["date"].startswith(mois)]
    return releves


def resume(releves):
    """Calculer nombre, total, moyenne et maximum ; None si liste vide."""
    if not releves:
        return None
    total = sum(r["pluie_mm"] for r in releves)
    plus_forte = max(releves, key=lambda r: r["pluie_mm"])
    return {
        "nombre": len(releves),
        "total_mm": round(total, 1),
        "moyenne_mm": round(total / len(releves), 1),
        "maximum_mm": plus_forte["pluie_mm"],
        "jour_maximum": plus_forte["date"],
    }


def total_par_commune(releves):
    """Additionner la pluie de chaque commune, classée par nom."""
    totaux = {}
    for r in releves:
        totaux[r["commune"]] = totaux.get(r["commune"], 0.0) + r["pluie_mm"]
    return {nom: round(totaux[nom], 1) for nom in sorted(totaux)}
