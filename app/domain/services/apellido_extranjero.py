from typing import Dict


def apellido_extranjero() -> Dict:
    return {
    "estado": "no_encontrado",
    "origen": "REAL",
    "apellido_original": "Genérico",
    "apellido_normalizado": "GENERICO",
    "departamentos": [
        {"departamento": "Caldas", "porcentaje": 40.0, "ranking": 1, "origen": "REAL"},
        {"departamento": "Cundinamarca", "porcentaje": 36.0, "ranking": 2, "origen": "REAL"},
        {"departamento": "Magdalena", "porcentaje": 24.0, "ranking": 3, "origen": "REAL"},
    ],
    "frases": [
        {"categoria": "PERSONALIDAD", "frase": "Cada historia comienza con un nombre.", "origen": "REAL"},
        {"categoria": "SABOR", "frase": "Descubre tu sabor único.", "origen": "REAL"}
    ]
}