# Ex.2

# Aide-mémoire : lancer pluvio

## 1. Préparer l'environnement

* Créer l'environnement virtuel :
  * Linux et macOS : `python3 -m venv .venv`
  * Windows : `py -m venv .venv`
* Installer pytest

## 2. Lancer un calcul

* Choisir le fichier CSV
* Ajouter des options si besoin

| Option | Argument |
| :--- | :--- |
| `--commune` | texte |
| `--mois` | AAAA-MM |
| `--par-commune` | aucun |

Appel depuis Python :

```python
from pluvio import stats

releves = stats.lire_releves("data/pluies_fictives.csv")
print(len(releves))