"""
Nombre: VaccineManager
Descripcion: Gestiona las vacunas
Precauciones:

"""

import json
import re
import uuid

from .VaccineMangementException import VaccineManagementException
from .VaccineRequest import VaccineRequest

class VaccineManager:
    """A continuacion se exponen los metodos de la clase"""
    def __init__(self):
        pass

    @classmethod
    def validateGuid(cls, guid ):
        """Metodo que valida el GUID"""
        try:
            uuid.UUID(guid)
            r=re.compile(r'^[0-9A-F]{8}-[0-9A-F]{4}-4[0-9A-F]{3}-'
                         r'[89AB][0-9A-F]{3}-[0-9A-F]{12}$',re.IGNORECASE)
            x = r.fullmatch(guid)
            if not x:
                raise VaccineManagementException("Invalid UUID v4 format")
        except ValueError as e:
            raise VaccineManagementException ("ID received is not a UUDI") from e
        return True

    def readaccessrequestfromJson(self, fi):
        """Esta funcion lee las solicitudes de acceso"""
        try:
            with open(fi,encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError as e:
            raise VaccineManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise VaccineManagementException("JSON Decode Error - Wrong JSON Format") from e


        try:
            guid = data["id"]
            zipp = data["phoneNumber"]
            req = VaccineRequest(guid, zipp)
        except KeyError as e:
            raise VaccineManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.validateGuid(guid):
            raise VaccineManagementException("Invalid GUID")

        # Close the file
        return req
