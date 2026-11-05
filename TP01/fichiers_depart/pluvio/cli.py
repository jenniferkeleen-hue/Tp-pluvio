"""Interface en ligne de commande de pluvio."""

import argparse
import sys

from pluvio import stats


def construire_parseur():
    """Construire l'analyseur des arguments de la ligne de commande."""
    p = argparse.ArgumentParser(
        prog="pluvio",
        description="Statistiques sur des relevés de pluie fictifs.",
    )
    p.add_argument("fichier", help="chemin du fichier CSV")
    p.add_argument("--commune", help="ne garder que cette commune")
    p.add_argument("--mois", help="ne garder que ce mois (AAAA-MM)")
    p.add_argument("--par-commune", action="store_true",
                   help="afficher le total de chaque commune")
    return p


def main(argv=None):
    """Exécuter la commande ; renvoyer 0 (succès), 1 (vide) ou 2 (erreur)."""
    args = construire_parseur().parse_args(argv)
    try:
        releves = stats.lire_releves(args.fichier)
    except (OSError, ValueError, KeyError) as erreur:
        print(f"Erreur : {erreur}", file=sys.stderr)
        return 2
    releves = stats.filtrer(releves, args.commune, args.mois)
    if not releves:
        print("Aucun relevé pour ces critères.")
        return 1
    if args.par_commune:
        print(f"{'Commune':<18}{'Total (mm)':>10}")
        for nom, total in stats.total_par_commune(releves).items():
            print(f"{nom:<18}{total:>10.1f}")
        return 0
    r = stats.resume(releves)
    print(f"Relevés : {r['nombre']}")
    print(f"Total : {r['total_mm']} mm")
    print(f"Moyenne : {r['moyenne_mm']} mm")
    print(f"Maximum : {r['maximum_mm']} mm ({r['jour_maximum']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
