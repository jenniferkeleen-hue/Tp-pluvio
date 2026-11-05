"""Tests du module pluvio.stats."""

from pathlib import Path

import pytest

from pluvio import stats

RACINE = Path(__file__).resolve().parent.parent
DONNEES = RACINE / "data" / "pluies_fictives.csv"


@pytest.fixture
def petit_csv(tmp_path):
    chemin = tmp_path / "mini.csv"
    chemin.write_text(
        "# commentaire\n"
        "date,commune,pluie_mm\n"
        "\n"
        "2025-01-01,Schœlcher,10.0\n"
        "2025-01-02,Schœlcher,0.0\n"
        "2025-02-01,Le Marin,5.5\n",
        encoding="utf-8",
    )
    return chemin


def test_lire_releves_ignore_commentaires_et_lignes_vides(petit_csv):
    releves = stats.lire_releves(petit_csv)
    assert len(releves) == 3
    assert releves[0] == {"date": "2025-01-01", "commune": "Schœlcher",
                          "pluie_mm": 10.0}


def test_lire_releves_fichier_reel():
    assert len(stats.lire_releves(DONNEES)) == 90


def test_filtrer_par_commune_sans_tenir_compte_de_la_casse(petit_csv):
    releves = stats.lire_releves(petit_csv)
    assert len(stats.filtrer(releves, commune="le marin")) == 1


def test_filtrer_par_mois(petit_csv):
    releves = stats.lire_releves(petit_csv)
    assert len(stats.filtrer(releves, mois="2025-01")) == 2


def test_resume_liste_vide():
    assert stats.resume([]) is None


def test_resume_valeurs(petit_csv):
    r = stats.resume(stats.lire_releves(petit_csv))
    assert r == {"nombre": 3, "total_mm": 15.5, "moyenne_mm": 5.2,
                 "maximum_mm": 10.0, "jour_maximum": "2025-01-01"}


def test_total_par_commune_est_trie(petit_csv):
    totaux = stats.total_par_commune(stats.lire_releves(petit_csv))
    assert list(totaux) == ["Le Marin", "Schœlcher"]
    assert totaux["Schœlcher"] == 10.0
