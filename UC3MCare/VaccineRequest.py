"""
    Nombre: VaccineRequest
    Descripcion: Solicitud de vacunas
"""
import json
#from datetime import datetime
#import pandas

class VaccineRequest:
    """Clase encargada de la solicitud de vacunas"""
    def __init__( self, idcode, phoneNumber ):
        self.__phoneNumber = phoneNumber
        self.__idcode = idcode
        #justnow = datetime.utcnow()
        #self.__timeStamp = datetime.timestamp(justnow)

    def __str__(self):
        return "VaccineRequest:" + json.dumps(self.__dict__)

    @property
    def phone(self):
        """Telefono del usuario"""
        return self.__phoneNumber
    @phone.setter
    def phone( self, value ):
        self.__phoneNumber = value

    @property
    def idDocument(self):
        """Id del documento"""
        return self.__idcode
    @idDocument.setter
    def idDocument(self,value):
        self.__idcode = value
