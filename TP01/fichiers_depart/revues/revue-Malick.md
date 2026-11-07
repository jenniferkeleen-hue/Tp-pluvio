# Revue du README

Relecteur : malickms
Auteur relu : moi-même
Date : 2026-11-07

| N° | Critère | Note (0 à 2) | Preuve (numéro de ligne ou extrait) |
|---|---|---|---|
| 1 | Titre et accroche | 2 | l. 1 : un seul `# pluvio` ; l. 8-11 : description de 4 lignes ; l. 3-4 : « données entièrement fictives » |
| 2 | Prérequis explicites | 2 | l. 17-19 : « Python 3.10 ou une version plus récente », Git, `pytest` |
| 3 | Installation reproductible | 2 | l. 25-32 (bash) et l. 36-43 (PowerShell), dans l'ordre : clone, venv, activation, pip |
| 4 | Usage avec exemples exécutables | 2 | l. 50-59 et suivantes : 2 commandes `python -m pluvio.cli ...`, chacune suivie de sa sortie réelle |
| 5 | Blocs de code balisés | 2 | tous les blocs ont `bash`, `powershell` ou `text` ; aucune invite `$` |
| 6 | Structure et titres | 2 | 9 sections de niveau 2 dans l'ordre logique, aucun saut de niveau ; `verifier_readme.py` : « README conforme » |
| 7 | Éléments visuels utiles | 2 | l. 13 : image avec alt « Schéma du flux de données, du CSV aux statistiques » ; l. 79-83 : tableau des options ; l. 89 : arborescence |
| 8 | Tests | 2 | l. 87 : commande `pytest` et « tous les tests doivent réussir » |
| 9 | Maintenance et contribution | 2 | l. 122-127 : 4 étapes de contribution ; l. 131 : licence MIT + lien `LICENSE` ; l. 135 : contact par issue GitHub |
| 10 | Lisibilité du source | 2 | aucune ligne de plus de 80 caractères hors code et tableaux ; aucun espace en fin de ligne |

Total : 20 / 20

## Trois améliorations proposées

1. L. 87 : écrire le résultat attendu précis, par exemple « 40 tests réussis »,
   pour que le lecteur sache à quoi ressemble un succès.
2. L. 47 : remplacer « racine du dépôt » par « dossier `TP01/fichiers_depart` »,
   car les commandes se lancent depuis ce dossier et non depuis la racine Git.
3. L. 26-28 et 37-39 : fusionner `cd Tp-pluvio` et `cd TP01/fichiers_depart`
   en une seule commande, et ajouter le dossier `revues/` à l'arborescence
   (l. 89-118) une fois la revue fusionnée.