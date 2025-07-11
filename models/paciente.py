from datetime import datetime
import re

from models.exception import DNIInvalidoError, NombreInvalidoError, FechaNacimientoInvalidaError

class Paciente:
    def __init__(self, nombre, dni, fecha_nacimiento):
       
        if nombre.strip() == "":
            raise NombreInvalidoError("El nombre no puede estar vacío")

    
        if not re.match(r"^\d{8}$", dni): 
            raise DNIInvalidoError("DNI inválido. Debe tener al menos 7 números")

     
        try:
            fecha_obj = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
            if fecha_obj > datetime.now():
                raise FechaNacimientoInvalidaError("La fecha no puede ser futura")
        except ValueError:
            raise FechaNacimientoInvalidaError("Formato incorrecto. Usar dd/mm/aaaa")

    
        self.__nombre = nombre
        self.__dni = dni
        self.__fecha_nacimiento = fecha_nacimiento

    def obtener_dni(self):
        return self.__dni
    
    def obtener_nombre(self):
        return self.__nombre

    def __str__(self):
       
        return f"{self.__nombre}, {self.__dni}, {self.__fecha_nacimiento}"