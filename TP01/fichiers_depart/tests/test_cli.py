"""Tests de l'interface en ligne de commande."""

from pathlib import Path

from pluvio import cli

DONNEES = str(Path(__file__).resolve().parent.parent / "data"
              / "pluies_fictives.csv")


def test_resume_pour_une_commune(capsys):
    assert cli.main([DONNEES, "--commune", "Le Lamentin"]) == 0
    sortie = capsys.readouterr().out
    assert "Relevés : 15" in sortie
    assert "Maximum : 33.9 mm (2025-01-08)" in sortie


def test_total_par_commune(capsys):
    assert cli.main([DONNEES, "--par-commune", "--mois", "2025-02"]) == 0
    assert "Sainte-Anne" in capsys.readouterr().out


def test_commune_inconnue_renvoie_1(capsys):
    assert cli.main([DONNEES, "--commune", "Inconnue"]) == 1
    assert "Aucun relevé" in capsys.readouterr().out


def test_fichier_absent_renvoie_2(capsys):
    assert cli.main(["absent.csv"]) == 2
    assert "Erreur" in capsys.readouterr().err
