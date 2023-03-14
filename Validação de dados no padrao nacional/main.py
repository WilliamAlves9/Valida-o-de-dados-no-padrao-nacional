from cpf_cnpj import Documento
from Numero_de_telefone import TelefonesBr
from datas import Datas
from acesso_cep import BuscaEndereco

#Busca os bairro, cidade e uf de um cep, podendo ser adicionado novos elementos para busca
cep = "01001000"
objeto_cep = BuscaEndereco(cep)
bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(bairro, cidade, uf)

#Verifica quando o usuario se cadastrou, porém, por não ter acesso a um banco de dados está incompleto
cadastro = Datas()
print(cadastro)


cpf_teste = "52841687040"
cpf_falso = "12341025700"
cnpj_teste = "80477995000115"
cnpj_falso = "12377456000115"

documento_cpf = Documento.verifica_documento(cpf_teste)
documento_cnpj = Documento.verifica_documento(cnpj_teste)
print(documento_cnpj)

#Busca um número de telefone dentro de uma string, não sendo obrigatório o codigo telefónico
telefone = "552126481234"
telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto)

