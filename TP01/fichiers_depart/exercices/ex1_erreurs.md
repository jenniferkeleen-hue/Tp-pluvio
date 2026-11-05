# Fiche d'utilisation de pluvio

Cette fiche résume l'emploi de l'outil. Les données sont fictives.

### Préparer l'environnement

Étapes à suivre :

- Installer Python
 - Vérifier la version avec `python --version`
 - Prévoir la version 3.10 ou une plus récente
- Cloner le dépôt

##Options de la commande

| Option | Effet |
| `--commune` | filtre par commune |
| `--mois` | filtre par mois |

## Exemple

Commande :

```bash
python -m pluvio.cli data/pluies_fictives.csv --commune "Le Lamentin"
```

Résultat :

```
Relevés : 15
Total : 170.4 mm
```

## Ressources

Le jeu de données : [pluies_fictives.csv] (../data/pluies_fictives.csv).

![](../docs/schema_flux.svg)

## Contact

Service fictif des relevés
12 rue de l'Exemple
Fort-de-France

## Remarques

Remplacer <commune> par le nom de la commune voulue.

** À vérifier ** : les totaux sont arrondis à une décimale.

## À faire

- [] Relire la fiche
- [x] Écrire la fiche

## Contenu de requirements.txt

```text
pytest>=7
