from typing import Dict
from jsonschema import validate, ValidationError

from app.domain.models.models import (
    Apellido,
    Departamento,
    DistribucionApellidoDepartamento,
    Frases
)

from app.integrations.ai_cliente import obtener_apellido_ai
from app.schemas.ai_response_schema import AI_RESPONSE_SCHEMA
from app.domain.services.apellido_no_encontrado import apellido_no_encontrado
from app.domain.services.apellido_extranjero import apellido_extranjero
from app.api.exceptions.apellido_exceptions import ApellidoInvalidoError


class ObtenerApellidoIA:
    def __init__(self, apellido_normalizado: str, apellido_original: str):
        self.apellido_normalizado = apellido_normalizado
        self.apellido_original = apellido_original

    def ejecutar(self) -> Dict:
        ai_response = obtener_apellido_ai(self.apellido_normalizado)
        
        if ai_response:
            self._validar_ai_response(ai_response)

            if not ai_response['es_apellido_real']:
                raise ApellidoInvalidoError(
                    f"Error al digitar el apellido. {self.apellido_original} no es un apellido válido."
                )
            
            if ai_response['es_apellido_extranjero']:
                return apellido_extranjero()

            apellido_obj = self._crear_apellido(ai_response)

            distribuciones = DistribucionApellidoDepartamento.objects.filter(apellido=apellido_obj)
            frases = Frases.objects.filter(apellido=apellido_obj)

            return {
                "estado": "encontrado",
                "origen": "IA",
                "apellido_original": self.apellido_original,
                "apellido_normalizado": apellido_obj.apellido,
                "departamentos": distribuciones,
                "frases": frases
            }
        else:
            return apellido_no_encontrado()
        
    def _validar_ai_response(self, ai_response: Dict):
        try:
            validate(instance=ai_response, schema=AI_RESPONSE_SCHEMA)
        except ValidationError as e:
            raise ValueError(f"Error al validar la respuesta del AI: {e}")

    def _crear_apellido(self, ai_response: Dict) -> Apellido:
        apellido_obj, _ = Apellido.objects.get_or_create(
            apellido=ai_response['apellido'],
            defaults={'origen': ai_response['origen']}
        )

        for dist in ai_response['distribuciones']:
            departamento, _ = Departamento.objects.get_or_create(
                nombre=dist['departamento']
            )
            DistribucionApellidoDepartamento.objects.get_or_create(
                apellido=apellido_obj,
                departamento=departamento,
                defaults={
                    'porcentaje': dist['porcentaje'],
                    'ranking': dist['ranking'],
                    'origen': 'IA'
                }
            )

        for frase in ai_response['frases']:
            Frases.objects.get_or_create(
                apellido=apellido_obj,
                categoria=frase['categoria'],
                frase=frase['texto'],
                defaults={'origen': 'IA'}
            )

        return apellido_obj
        