class Jugada:
    """
    """
    tipo = ""
    espec = ""
    tiempo = ""
    descrip = ""
    nombre_equipo = ""

    def __init__(self, nombre_equipo, tipo, espec, tiempo, descrip):
        """
        Constructor
        """
        self.tipo = tipo
        self.espec = espec
        self.tiempo = "{}'".format(tiempo)
        self.descrip = descrip
        self.nombre_equipo = nombre_equipo

    @classmethod
    def create(cls):
        """
        Create a new instance of the class Jugada.
        """
        return cls()

    @classmethod
    def load():
        """
        Load the already created Jugada object.
        """
        pass

    def getTipo(self):
        """
        Returns the specific Jugada tipe.
        """
        pass

    def getEspec(self):
        """
        Returns the specific Jugada specialization.
        """
        pass

    def getTiempo(self):
        """
        Returns the current Jugada time.
        """
        pass

    def getDescrip(self):
        """
        Returns a wide description on the soccer play in Jugada.
        """
        pass

    def getJuagada(self):
        """
        Returns all info of Jugada in a dict the following format: '[time: '',
         tipe: '', espec: '', descrip: ''].
        """
        pass
