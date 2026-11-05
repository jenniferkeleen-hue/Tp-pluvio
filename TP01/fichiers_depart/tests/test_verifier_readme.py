"""Tests de verifier_readme.py (Ex.4)."""

import pytest

import verifier_readme as v

COMPLET = "\n".join(f"## {s}" for s in v.SECTIONS_ATTENDUES) + "\n"


def test_aucune_section_manquante():
    assert v.sections_manquantes(COMPLET) == []


def test_section_manquante_detectee():
    texte = COMPLET.replace("## Licence\n", "")
    assert v.sections_manquantes(texte) == ["Licence"]


def test_casse_et_accents_ignores():
    texte = "# prerequis et INSTALLATION\n"
    manquantes = v.sections_manquantes(texte, ("Prérequis", "Installation"))
    assert manquantes == []


def test_titre_dans_un_bloc_de_code_ignore():
    texte = "```text\n## Licence\n```\n"
    assert v.sections_manquantes(texte, ("Licence",)) == ["Licence"]


def test_blocs_sans_langage_donne_les_numeros_de_ligne():
    texte = "Texte\n```\nx = 1\n```\n"
    assert v.blocs_sans_langage(texte) == [2]


def test_blocs_avec_langage_acceptes():
    assert v.blocs_sans_langage("```python\nx = 1\n```\n") == []


def test_la_fermeture_d_un_bloc_n_est_pas_comptee():
    texte = "```bash\nls\n```\n\n```\nsortie\n```\n"
    assert v.blocs_sans_langage(texte) == [5]


def test_main_readme_conforme(tmp_path, capsys):
    fichier = tmp_path / "README.md"
    fichier.write_text(COMPLET, encoding="utf-8")
    assert v.main([str(fichier)]) == 0
    assert "README conforme." in capsys.readouterr().out


def test_main_readme_non_conforme(tmp_path, capsys):
    fichier = tmp_path / "README.md"
    fichier.write_text("# Titre\n```\nx\n```\n", encoding="utf-8")
    assert v.main([str(fichier)]) == 1
    sortie = capsys.readouterr().out
    assert "Section manquante : Licence" in sortie
    assert "Ligne 2 : bloc de code sans langage" in sortie


@pytest.mark.parametrize("fonction", [v.sections_manquantes,
                                      v.blocs_sans_langage])
def test_docstring_conforme_pep_257(fonction):
    doc = fonction.__doc__
    assert doc, "docstring absente"
    assert not doc.startswith((" ", "\n")), "résumé après les guillemets"
    lignes = doc.splitlines()
    assert lignes[0].endswith("."), "le résumé doit finir par un point"
    assert len(lignes[0]) <= 79, "résumé trop long"
    if len(lignes) > 1:
        assert lignes[1].strip() == "", "ligne vide après le résumé"
