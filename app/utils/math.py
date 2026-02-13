from typing import Dict, List, Any
from app.utils.constantes import GRAMAJE_TOTAL_CAFE


def ajustar_porcentaje(distribuciones: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    total_porcentaje = sum(d['porcentaje'] for d in distribuciones)
    if total_porcentaje != 100:
        diferencia = 100 - total_porcentaje
        for d in distribuciones:
            min_porcentaje = min(d['porcentaje'] for d in distribuciones)
            if d['porcentaje'] == min_porcentaje:
                d['porcentaje'] += diferencia
                break
    return distribuciones


def calcular_gramaje(porcentaje: float) -> float:
    """
    Calcula los gramos de café basados en el porcentaje y el total base (250g).
    """
    return round((porcentaje * GRAMAJE_TOTAL_CAFE) / 100, 2)