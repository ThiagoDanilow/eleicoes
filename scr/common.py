class Pessoa:
    __nome : str
    __RG : str
    __CPF : str

    def __init__(self, nome, RG, CPF):
        self.__nome = nome
        self.__RG = RG
        self.__CPF = CPF

    def __str__(self):
        info = (f'Nome: {self.__nome}\n'
               f'RG: {self.__RG}\n'
               f'CPF: {self.__CPF}\n')
        return info

    def __repr__(self):
        return f"Pessoa(nome='{self.__nome}', RG='{self.__RG}', CPF='{self.__CPF}')"

class Eleitor(Pessoa):
    __titulo : int
    secao : int
    zona : int

    def __init__(self, nome, RG, CPF, titulo, secao, zona):
        super().__init__(nome, RG, CPF)
        self.__titulo = titulo
        self.secao = secao
        self.zona = zona

    def __str__(self):
        info = super().__str__()
        info += (f'Titulo: {self.__titulo}\n'
                 f'Seção: {self.secao}\n'
                 f'Zona: {self.zona}\n')
        return info

    def __repr__(self):
        return f"Eleitor({super().__repr__()}, titulo='{self.__titulo}', secao='{self.secao}', zona='{self.zona}')"

    def get_titulo(self):
        return self.__titulo

class Candidato(Pessoa):
    def __init__(self, nome: str, RG: str, CPF: str, numero: int, partido: str, cargo: str):
        super().__init__(nome, RG, CPF)
        self.__numero = numero
        self.partido = partido
        self.cargo = cargo

    def __str__(self):
        return f"{super().__str__()}, Número: {self.__numero}, Partido: {self.partido}, Cargo: {self.cargo}"

    def get_numero(self):
        return self.__numero
