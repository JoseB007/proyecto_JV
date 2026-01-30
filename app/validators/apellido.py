import re
import unicodedata
from typing import Optional, Dict


# APELLIDO_REGEX = re.compile(r'^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]{2,30}$')
# APELLIDO_REGEX = re.compile(r'^(?!.*(.)\1{2})[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]{3,30}$')
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


def validar_apellido(apellido: Optional[str]) -> Dict[str, Optional[str]]:
    # Campo obligatorio
    if not apellido:
        return {
            "es_valido": False,
            "error": "El apellido es obligatorio",
            "normalizado": None
        }

    # Espacios al inicio o fin
    if apellido != apellido.strip():
        return {
            "es_valido": False,
            "error": "El apellido no debe contener espacios al inicio o al final",
            "normalizado": None
        }

    # Regex principal
    if not APELLIDO_REGEX.match(apellido):
        return {
            "es_valido": False,
            "error": (
                "El apellido debe tener entre 3 y 30 letras, no contener espacios ni caracteres especiales o más de dos caracteres consecutivos repetidos"
            ),
            "normalizado": None
        }

    # Normalización
    apellido_upper = apellido.upper()
    apellido_normalizado = remover_acentos(apellido_upper)

    return {
        "es_valido": True,
        "error": None,
        "normalizado": apellido_normalizado
    }
