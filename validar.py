numero = None

while numero is None:
    try:
        numero = int(input("Digite um número inteiro: "))
    except ValueError:
        print("Erro: era pra ter digitado um número inteiro. tenta de novo pa nois ae")

print(f"O numero digitado foi {numero}")