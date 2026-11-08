# pluvio

> **Attention : les données fournies avec ce projet sont entièrement fictives.**
> Elles ne proviennent d'aucune station de mesure.

## Description

`pluvio` est un petit outil Python en ligne de commande.
Il lit un fichier CSV de relevés de pluie de communes de Martinique
et calcule des statistiques : total, moyenne, maximum, total par commune.
Il s'adresse aux étudiants qui découvrent la documentation de projet.

![Schéma du flux de données, du CSV aux statistiques](docs/schema_flux.svg)
*Figure 1 : flux de données de pluvio*

## Prérequis

- Python 3.10 ou une version plus récente
- Git
- `pytest` (installé avec `requirements.txt`)

## Installation

Sous Linux et macOS (bash) :

```bash
git clone https://github.com/jenniferkeleen-hue/Tp-pluvio.git Tp-pluvio
cd Tp-pluvio
cd TP01/fichiers_depart
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Sous Windows (PowerShell) :

```powershell
git clone https://github.com/jenniferkeleen-hue/Tp-pluvio.git Tp-pluvio
cd Tp-pluvio
cd TP01/fichiers_depart
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Utilisation

Lancez les commandes depuis la racine du dépôt.
Pour obtenir les statistiques d'une commune :

```bash
python -m pluvio.cli data/pluies_fictives.csv --commune "Le Lamentin"
```

```text
Relevés : 15
Total : 170.4 mm
Moyenne : 11.4 mm
Maximum : 33.9 mm (2025-01-08)
```

Pour obtenir le total de chaque commune :

```bash
python -m pluvio.cli data/pluies_fictives.csv --par-commune
```

```text
Commune           Total (mm)
Fort-de-France         115.6
La Trinité             171.4
Le Lamentin            170.4
Le Robert              203.3
Sainte-Anne            190.8
Schœlcher              225.0
```

Pour combiner deux filtres (une commune et un mois) :

```bash
python -m pluvio.cli data/pluies_fictives.csv --commune "Le Lamentin" --mois 2025-01
```

```text
Relevés : 10
Total : 120.4 mm
Moyenne : 12.0 mm
Maximum : 33.9 mm (2025-01-08)
```

Options de la commande :

| Option | Argument | Effet |
| :--- | :---: | :--- |
| `--commune` | texte | ne garde que cette commune |
| `--mois` | AAAA-MM | ne garde que ce mois |
| `--par-commune` | aucun | affiche le total de chaque commune |

## Tests

Lancez `pytest` depuis la racine du dépôt : tous les tests doivent réussir.

## Arborescence

```text
.
├── LICENSE
├── README.md
├── data/
│   └── pluies_fictives.csv
├── docs/
│   ├── revue_modele.md
│   └── schema_flux.svg
├── exercices/
│   ├── ex1_erreurs.md
│   ├── ex2_rendu.md
│   └── ex2_rendu_cible.png
├── grille_qualite_readme.md
├── pluvio/
│   ├── __init__.py
│   ├── cli.py
│   └── stats.py
├── pytest.ini
├── rendre_zip.py
├── requirements.txt
├── tests/
│   ├── test_cli.py
│   ├── test_readme.py
│   ├── test_stats.py
│   └── test_verifier_readme.py
└── verifier_readme.py
```

## Contribution

1. Créez une branche : `git switch -c amelioration/NOM`.
2. Faites des commits courts, au format `type: résumé`
   (par exemple `docs: ajouter la section Tests`).
3. Lancez `pytest`, puis publiez la branche :
   `git push -u origin amelioration/NOM`.
4. Ouvrez une pull request vers `main` et attendez une relecture.

## Licence

Projet sous licence MIT : voir le fichier [LICENSE](LICENSE).

## Contact

Pour toute question, ouvrez une issue sur le dépôt GitHub du projet.
