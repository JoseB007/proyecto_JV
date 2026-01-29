from typing import Dict
from django.db import transaction
from jsonschema import validate, ValidationError

from app.domain.models.models import (
    Apellido,
    Departamento,
    DistribucionApellidoDepartamento,
    Frases
)

from app.api.integrations.ai_cliente import obtener_apellido_ai
from app.api.schemas.ai_response_schema import AI_RESPONSE_SCHEMA


class ObtenerApellidoIA:
    def __init__(self, apellido_normalizado: str, apellido_original: str):
        self.apellido_normalizado = apellido_normalizado
        self.apellido_original = apellido_original

    def ejecutar(self) -> Apellido:
        # ai_response = obtener_apellido_ai(self.apellido)

        # self._validar_ai_response(ai_response)
        # apellido = self._crear_apellido(ai_response)

        # return apellido

        return {
            "estado": "no_encontrado",
            "origen": "IA",
            "apellido_original": self.apellido_original,
            "apellido_normalizado": self.apellido_normalizado,
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
        
    # def _validar_ai_response(self, ai_response: Dict):
    #     try:
    #         validate(instance=ai_response, schema=AI_RESPONSE_SCHEMA)
    #     except ValidationError as e:
    #         raise ValueError(f"Error al validar la respuesta del AI: {e}")

    # def _crear_apellido(self, ai_response: Dict) -> Apellido:
    #     apellido_obj, _ = Apellido.objects.get_or_create(
    #         apellido=ai_response['apellido'],
    #         origen=ai_response['origen'],
    #     )

    #     for dist in ai_response['distribuciones']:
    #         departamento, _ = Departamento.objects.get_or_create(
    #             nombre=dist['departamento']
    #         )
    #         DistribucionApellidoDepartamento.objects.get_or_create(
    #             apellido=apellido_obj,
    #             departamento=departamento,
    #             porcentaje=dist['porcentaje'],
    #             ranking=dist['ranking'],
    #         )

    #     for frase in ai_response['frases']:
    #         Frases.objects.create(
    #             categoria=frase['categoria'],
    #             frase=frase('texto'),
    #             origen='IA',
    #         )

    #     return apellido_obj
        