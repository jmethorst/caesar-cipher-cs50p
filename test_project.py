from project import validate, clean_input, caesar
import pytest


def test_validate():
    assert validate("test", "e", "0") == True
    assert validate("!Numbers and special chars123...",
                    "DECRYPT", "50") == True
    assert validate("CaPiTal SIgns", "Encrypt", "12") == True
    with pytest.raises(SystemExit):
        assert validate("", "", "") == "No text given, provide some text"
        assert validate(
            "asd", "f", "20") == "value given is invalid, use encrypt/e or decrypt/d"
        assert validate(
            "asd", "6", "20") == "value given is invalid, use encrypt/e or decrypt/d"
        assert validate(
            "asd", "!", "20") == "value given is invalid, use encrypt/e or decrypt/d"
        assert validate(
            "asd", "D", "-1") == "invalid number given, use 0 or a positif number"
        assert validate(
            "asd", "D", "!a") == "invalid number given, use 0 or a positif number"
        assert validate(
            "asd", "D", -1) == "invalid number given, use 0 or a positif number"


def test_clean_input():
    assert clean_input(("test", "encrypt", "5")) == (("test", True, 5))
    assert clean_input((" 34test!  ", "D", "27")) == (("34test!", False, 27))
    with pytest.raises(ValueError):
        clean_input(("too", "many", "values", "here"))
        clean_input(("value", "missing"))
        clean_input(())
    with pytest.raises(TypeError):
        clean_input("forgot", "the", "tupple")


def test_caesar():
    assert caesar("lowercase", True, 1) == 'mpxfsdbtf'
    assert caesar("UPPERCASE", False, 100) == 'YTTIVGEWI'
    assert caesar("1248 numbers 1234", True, 12) == "1248 zgynqde 1234"
    assert caesar("! ''[] whitespace special 123", False,
                  9) == "! ''[] nyzkvjgrtv jgvtzrc 123"
    assert caesar("! [/[/.]]", False, 9) == "! [/[/.]]"
    assert caesar("", True, 10) == ""
    assert caesar("Er Was Eens Een Kikker Genaamd Mik", True,
                  641322) == "Kx Cgy Kkty Kkt Qoqqkx Mktggsj Soq"

    with pytest.raises(TypeError):
        caesar()
        caesar("dva")
        caesar("ad", False, 12, "nani")
        caesar("text", "True", 4)
        caesar(44, True, 1)
        caesar("txt", False, "one")
