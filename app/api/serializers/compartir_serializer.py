from rest_framework import serializers
from app.validators.apellido import validar_apellido


class SolicitudCompartirSerializer(serializers.Serializer):
    apellido = serializers.CharField()
    canal = serializers.ChoiceField(choices=["email", "whatsapp"])
    destinatario = serializers.CharField()

    def validate(self, data):
        canal = data.get("canal")
        destinatario = data.get("destinatario")

        if canal == "email":
            from django.core.validators import validate_email
            from django.core.exceptions import ValidationError
            try:
                validate_email(destinatario)
            except ValidationError:
                raise serializers.ValidationError({"destinatario": "Debe ser un correo electrónico válido."})
        
        return data

    def validate_apellido(self, value):
        resultado = validar_apellido(value.upper())

        if not resultado["es_valido"]:
            raise serializers.ValidationError(resultado["error"])
        
        self.context["apellido_normalizado"] = resultado["normalizado"]
        return value
    

class RespuestaCompartirSerializer(serializers.Serializer):
    estado = serializers.CharField()
    canal = serializers.CharField()
    mensaje = serializers.CharField()