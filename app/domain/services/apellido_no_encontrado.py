from typing import Dict


def apellido_no_encontrado() -> Dict:
    return {
    "estado": "no_encontrado",
    "origen": "REAL",
    "apellido_original": "Genérico",
    "apellido_normalizado": "GENERICO",
    "departamentos": [
        {"departamento": "Caldas", "porcentaje": 40.0, "ranking": 1, "origen": "IA"},
        {"departamento": "Cundinamarca", "porcentaje": 36.0, "ranking": 2, "origen": "IA"},
        {"departamento": "Magdalena", "porcentaje": 24.0, "ranking": 3, "origen": "IA"},
    ],
    "frases": [
        {"categoria": "PERSONALIDAD", "frase": "Cada historia comienza con un nombre.", "origen": "IA"},
        {"categoria": "SABOR", "frase": "Descubre tu sabor único.", "origen": "IA"}
    ]
}