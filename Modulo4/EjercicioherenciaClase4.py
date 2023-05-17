class Persona: 
    def __init__(self,_sexo,_domicilio) -> None:
        self.sexo = _sexo
        self.domicilio = _domicilio

class Maestro(Persona):
    def __init__(self,_sexo,_domicilio,_lugar_clases, _tipo_maestria)-> None:
        super.__init__(self, _sexo , _domicilio)
        self._lugar_clases = _lugar_clases
        self._tipo_maestria = _tipo_maestria


class Estudiante(Persona):
        def __init__(self, _sexo, _domicilio) -> None:
            super.__init__(_sexo, _domicilio)