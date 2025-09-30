print("* ME INFORME O DESMATAMENTO EM METROS QUADRADOS E EU RETORNAREI A QUANTIDADE EM CAMPOS DE FUTEBOL PADRÃO ELE REPRESENTA *")

desmatamento = int(input(
    "Digite quantos metros quadrados de desmatamentos foram registrados(Ex: 100m² = 100)... "))

desmatamento = desmatamento * desmatamento
campofutebol = 100 * 60

print("Processando...")

resposta = (desmatamento / campofutebol)

print(int(resposta))
