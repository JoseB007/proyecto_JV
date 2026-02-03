from rest_framework.exceptions import APIException
from rest_framework import status


class ApellidoInvalidoError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'El apellido proporcionado no es válido.'
    default_code = 'apellido_invalido'

    def __init__(self, mensaje, status_code=None):
        self.detail = {"mensaje": mensaje}
        if status_code:
            self.status_code = status_code