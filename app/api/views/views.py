from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app.api.serializers.apellido_serializer import ApellidoEntradaSerializer, DistribucionApellidoRespuestaSerializer
from app.domain.services.obtener_apellido import obtener_informacion_apellido


class ApellidoView(APIView):
    def post(self, request):
        serializer = ApellidoEntradaSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            apellido_normalizado = serializer.context["apellido_normalizado"]
            apellido_original = serializer.validated_data['apellido']
            info_apellido = obtener_informacion_apellido(apellido_normalizado, apellido_original)
            
            response = DistribucionApellidoRespuestaSerializer(info_apellido)
            
            return Response(
                response.data,
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"mensaje": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

        