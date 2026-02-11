from django.test import TestCase

import pytest
from app.validators.apellido import validar_apellido


@pytest.mark.parametrize("apellido, expected_norm, expected_list", [
    ("Gomez", "GOMEZ", ["GOMEZ"]),
    ("Gómez", "GOMEZ", ["GOMEZ"]),
    ("Muñoz", "MUNOZ", ["MUNOZ"]),
    ("Ávila", "AVILA", ["AVILA"]),
    ("Lopez", "LOPEZ", ["LOPEZ"]),
    ("Perez", "PEREZ", ["PEREZ"]),
    ("Rodriguez", "RODRIGUEZ", ["RODRIGUEZ"]),
    ("Sanchez", "SANCHEZ", ["SANCHEZ"]),
    ("Torres", "TORRES", ["TORRES"]),
    ("Vasquez", "VASQUEZ", ["VASQUEZ"]),
    ("Rosero Zambrano", "ROSERO ZAMBRANO", ["ROSERO", "ZAMBRANO"]),
    ("Perez Sosa", "PEREZ SOSA", ["PEREZ", "SOSA"]),
])
def test_validar_apellido(apellido, expected_norm, expected_list):
    resultado = validar_apellido(apellido)
    
    assert resultado["es_valido"] is True
    assert resultado["error"] is None
    assert resultado["normalizado"] == expected_norm
    assert resultado["lista_apellidos"] == expected_list
    assert len(resultado["lista_originales"]) == len(expected_list)


@pytest.mark.parametrize("apellido", [
    None,
    "",
])
def test_apellido_vacio(apellido):
    resultado = validar_apellido(apellido)
    
    assert resultado["es_valido"] is False
    assert resultado["error"] == "El apellido es obligatorio"
    assert resultado["normalizado"] is None
    assert resultado["lista_apellidos"] == []
    assert resultado["lista_originales"] == []


@pytest.mark.parametrize("apellido", [
    " Gomez",
    "Gomez ",
    " Gomez ",
])
def test_apellido_con_espacios_inicio_fin(apellido):
    resultado = validar_apellido(apellido)
    
    assert resultado["es_valido"] is False
    assert resultado["error"] == "El apellido no debe contener espacios al inicio o al final"
    assert resultado["normalizado"] is None
    assert resultado["lista_apellidos"] == []
    assert resultado["lista_originales"] == []


@pytest.mark.parametrize("apellido", [
    "G",
    "Gomez1",
    "Gómez-Álvarez",
    "Gomez!",
    "Gomez Perez Sosa",
])
def test_apellido_formato_invalido(apellido):
    resultado = validar_apellido(apellido)
    
    assert resultado["es_valido"] is False
    # El error puede variar dependiendo de si es longitud, caracteres o cantidad de apellidos
    assert "apellido debe tener entre 3 y 30 letras" in resultado["error"] or "máximo de dos apellidos" in resultado["error"]
    assert resultado["normalizado"] is None
    assert resultado["lista_apellidos"] == []
    assert resultado["lista_originales"] == []