from pessoa_fisica import PessoaFisica
from pessoa_juridica import PessoaJuridica

pessoaf = PessoaFisica("123.105.184-17", "Matheus", 27)
pessoaj = PessoaJuridica("44.639.277/0001-34", "Mikaela", 25)

print(
    f"Nome: {pessoaf.getNome()}\n"
    f"CPF: {pessoaf.getCPF()}\n"
    f"Idade: {pessoaf.getIdade()} anos\n"
)
