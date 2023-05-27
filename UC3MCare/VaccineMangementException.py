"""
    Nombre: VaccioneManagementException
    Descripcion: Gestiona las excepciones """
class VaccineManagementException(Exception):
    """Gestiona las excepciones de las vacunas"""
    def __init__(self, message):
        self.__message = message
        super().__init__(self.message)

    @property
    def message(self):
        """Mensaje"""
        return self.__message

    @message.setter
    def message(self,value):
        self.__message = value
