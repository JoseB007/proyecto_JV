import re
import unicodedata
from typing import Optional, Dict


APELLIDO_REGEX = re.compile(
    r'^(?=[^aeiouáéíóúü]*[aeiouáéíóúü])'  # Al menos una vocal
    r'(?!.*[^aeiouáéíóúü]{4})'            # Máximo 4 consonantes seguidas
    r'(?!.*(.)\1{2})'                     # Máximo 2 letras iguales seguidas
    r'[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]{3,30}$',     # Caracteres permitidos y longitud
    re.IGNORECASE
)


def remover_acentos(apellido: str) -> str:
    normalizado = unicodedata.normalize("NFD", apellido)
    return "".join(
        char for char in normalizado
        if unicodedata.category(char) != "Mn"
    )


def validar_apellido(apellido_input: Optional[str]) -> Dict[str, Optional[str]]:
    # Campo obligatorio
    if not apellido_input:
        return {
            "es_valido": False,
            "error": "El apellido es obligatorio",
            "normalizado": None,
            "lista_apellidos": [],
            "lista_originales": []
        }

    # Espacios al inicio o fin
    if apellido_input != apellido_input.strip():
        return {
            "es_valido": False,
            "error": "El apellido no debe contener espacios al inicio o al final",
            "normalizado": None,
            "lista_apellidos": [],
            "lista_originales": []
        }

    # Separar los apellidos por espacio y devuelve una lista de apellidos
    partes = apellido_input.split()

    if len(partes) > 2:
        return {
            "es_valido": False,
            "error": "Se permite un máximo de dos apellidos",
            "normalizado": None,
            "lista_apellidos": [],
            "lista_originales": []
        }

    apellidos_normalizados = []
    apellidos_originales = []

    for idx, parte in enumerate(partes):
        # Regex principal para cada parte
        if not APELLIDO_REGEX.match(parte):
            return {
                "es_valido": False,
                "error": (
                    f"El {'primer' if idx == 0 else 'segundo'} apellido debe tener entre 3 y 30 letras, "
                    "no contener caracteres especiales o más de dos caracteres consecutivos repetidos"
                ),
                "normalizado": None,
                "lista_apellidos": [],
                "lista_originales": []
            }
        
        # Normalización individual
        apellido_upper = parte.upper()
        apellidos_normalizados.append(remover_acentos(apellido_upper))
        apellidos_originales.append(parte)

    return {
        "es_valido": True,
        "error": None,
        "normalizado": " ".join(apellidos_normalizados),
        "lista_apellidos": apellidos_normalizados,
        "lista_originales": apellidos_originales
    }
