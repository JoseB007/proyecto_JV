AI_RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "apellido": {"type": "string"},
        "es_apellido_real": {
            "type": "boolean",
            "description": "Indica si el término es un apellido legítimo con trasfondo histórico. False para texto aleatorio o insultos."
        },
        "es_apellido_extranjero": {
            "type": "boolean",
            "description": "Indica si el término es un apellido extranjero. True para este apellido"
        },
        "origen": {
            "type": "string",
            "enum": ["IA"] 
        },
        "confianza": {
            "type": "number",
            "minimum": 0,
            "maximum": 1,
            "description": "Nivel de certeza de la IA sobre la veracidad de los datos demográficos."
        },
        "distribuciones": {
            "type": "array",
            "minItems": 0,
            "maxItems": 3,
            "items": {
                "type": "object",
                "properties": {
                    "departamento": {"type": "string"},
                    "porcentaje": {"type": "number"},
                    "ranking": {"type": "number"},
                },
                "required": ["departamento", "porcentaje", "ranking"],
            },
        },
        "frases": {
            "type": "array",
            "minItems": 0,
            "maxItems": 4,
            "items": {
                "type": "object",
                "properties": {
                    "categoria": {
                        "type": "string",
                        "enum": ["PERSONALIDAD", "SABORES"]
                    },
                    "texto": {"type": "string", "minLength": 15},
                },
                "required": ["categoria", "texto"]
            },
        },
    },
    "required": ["apellido", "es_apellido_real", "es_apellido_extranjero", "origen", "confianza", "distribuciones", "frases"],
}


# AI_RESPONSE_SCHEMA = {
#     "type": "object",
#     "properties": {
#         "apellido": {"type": "string"},
#         "origen": {
#             "type": "string",
#             "enum": ["IA"] 
#         },
#         "confianza": {
#             "type": "number",
#             "minimum": 0,
#             "maximum": 1
#         },
#         "distribuciones": {
#             "type": "array",
#             "minItems": 3,
#             "maxItems": 3,
#             "items": {
#                 "type": "object",
#                 "properties": {
#                     "departamento": {"type": "string"},
#                     "porcentaje": {"type": "number"},
#                     "ranking": {"type": "number"},
#                 },
#                 "required": ["departamento", "porcentaje", "ranking"],
#             },
#         },
#         "frases": {
#             "type": "array",
#             "minItems": 4,
#             "maxItems": 4,
#             "items": {
#                 "type": "object",
#                 "properties": {
#                     "categoria": {
#                         "type": "string",
#                         "description": "Categoría de la frase (PERSONALIDAD o SABORES)"
#                     },
#                     "texto": {"type": "string", "minLength": 15},
#                 },
#                 "required": ["categoria", "texto"]
#             },
#         },
#     },
#     "required": ["apellido", "origen", "confianza", "distribuciones", "frases"],
# }


# AI_RESPONSE_SCHEMA = {
#     "type": "object",
#     "properties": {
#         "apellido": {"type": "string"},
#         "origen": { "enum": ["IA"] },
#         "confianza": {
#             "type": "number",
#             "minimum": 0,
#             "maximum": 1
#         },
#     },
#     "required": ["apellido", "origen", "confianza"],
#     "distribuciones": {
#         "type": "array",
#         "minItems": 3,
#         "maxItems": 3,
#         "items": {
#             "type": "object",
#             "properties": {
#                 "departamento": {"type": "string"},
#                 "porcentaje": {"type": "number"},
#                 "ranking": {"type": "number"},
#             },
#             "required": ["departamento", "porcentaje", "ranking"],
#         },
#     },
#     "frases": {
#         "type": "array",
#         "minItems": 4,
#         "maxItems": 4,
#         "prefixItems": [
#             { "properties": { "categoria": { "const": "PERSONALIDAD" } } }, 
#             { "properties": { "categoria": { "const": "SABORES" } } },     
#             { "properties": { "categoria": { "const": "SABORES" } } },     
#             { "properties": { "categoria": { "const": "SABORES" } } },     
#         ],
#         "items": {
#             "type": "object",
#             "properties": {
#                 "texto": {"type": "string", "minLength": 15},
#             },
#             "required": ["categoria", "texto"]
#         },
#     },
# }