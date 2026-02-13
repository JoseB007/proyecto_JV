from rest_framework import serializers
from app.validators.apellido import validar_apellido
from app.utils.math import calcular_gramaje


class ApellidoEntradaSerializer(serializers.Serializer):
    apellido = serializers.CharField(max_length=30, required=True)

    def validate_apellido(self, value):
        resultado = validar_apellido(value)

        if not resultado["es_valido"]:
            raise serializers.ValidationError(resultado["error"])
        
        self.context["apellido_normalizado"] = resultado["normalizado"]
        self.context["lista_apellidos"] = resultado["lista_apellidos"]
        self.context["lista_originales"] = resultado["lista_originales"]
        return value


class DepartamentoSerializer(serializers.Serializer):
    nombre = serializers.CharField()
    frase = serializers.CharField()


class DistribucionSerializer(serializers.Serializer):
    departamento = DepartamentoSerializer()
    porcentaje = serializers.FloatField()
    ranking = serializers.IntegerField()
    gramaje = serializers.SerializerMethodField()

    def get_gramaje(self, obj) -> float:
        porcentaje = obj.porcentaje if hasattr(obj, 'porcentaje') else obj.get('porcentaje', 0)
        return calcular_gramaje(porcentaje)


class FraseSerializer(serializers.Serializer):
    categoria = serializers.CharField()
    frase = serializers.CharField()


class DistribucionApellidoRespuestaSerializer(serializers.Serializer):
    estado = serializers.CharField()
    fuente = serializers.CharField()
    apellido_original = serializers.CharField()
    apellido_normalizado = serializers.CharField()
    distribuciones = DistribucionSerializer(many=True)
    frases = FraseSerializer(many=True)