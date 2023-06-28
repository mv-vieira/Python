from pessoa import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self,CPF, nome,idade):
        super().__init__(nome,idade)
        self.__CPF = CPF

    def getCPF(self):
        return self.__CPF

    def setCPF(self,CPF):
        self.__CPF = CPF