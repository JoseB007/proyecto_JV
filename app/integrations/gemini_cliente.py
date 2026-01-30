import json

from typing import Dict
from google import genai

from app.schemas.ai_response_schema import AI_RESPONSE_SCHEMA


class GeminiIACliente:
    def __init__(self):
        self.cliente = genai.Client()
        self.config_generacion = {
            "response_mime_type": "application/json",
            "response_schema": AI_RESPONSE_SCHEMA,
            "temperature": 0.1,
        }

    def obtener_apellido(self, apellido: str) -> Dict:
        prompt = self._ai_prompt(apellido)

        try:
            response = self.cliente.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
                config=self.config_generacion
            )

            resultado = json.loads(response.text)

            if not resultado.get('es_apellido_real'):
                return None
            
            return resultado
        except Exception as e:
            print(f"Error al consultar GeminiAI: {e}")
            return None
        
    def _ai_prompt(self, apellido: str):
        return f"""
        Analiza el término '{apellido}'. 

        TAREA DE VALIDACIÓN:
        - Si el término es texto aleatorio (ej. 'asdfg'), una combinación sin sentido de letras, o un insulto, establece 'es_apellido_real' en false y deja los arrays de 'distribuciones' y 'frases' vacíos.
        
        
        TAREA DE GENERACIÓN (Solo si 'es_apellido_real' es true):
        1. Genera estadísticas demográficas para el apellido '{apellido}' en Colombia.
        2. Genera 4 frases obligatorias:
            - La primera: Categoría 'PERSONALIDAD' (relacionada con el ímpetu o historia del apellido).
            - Las otras tres: Categoría 'SABORES' (metáforas gastronómicas sobre el café, derivados y relacionados propios de la región de origen).
        3. 'confianza' debe ser bajo si el apellido es extranjero o muy raro en Colombia.
        """

# class GeminiIACliente:
#     def __init__(self):
#         self.cliente = genai.Client()

#     def obtener_apellido(self, apellido: str) -> Dict:
#         prompt = self._ai_prompt(apellido)

#         try:
#             response = self.cliente.models.generate_content(
#                 model="gemini-3-flash-preview",
#                 contents=prompt
#             )

#             contenido = response.text

#             return json.loads(contenido)
#         except Exception as e:
#             print(f"Error al consultar GeminiAI: {e}")
#             return None
        
#     def _ai_prompt(self, apellido: str):
#         return f"""
#         Inferir estadísticas de apellidos para Colombia.

#         Apellido: {apellido}
#         Lenguaje: Español

#         Reglas:
#         - Devolver SOLO JSON
#         - Reducir la confianza si no hay certeza

#         JSON estructura: {AI_RESPONSE_SCHEMA}
#         """