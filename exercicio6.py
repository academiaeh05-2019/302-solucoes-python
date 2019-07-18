iguais = ['a', 'a', 'a', 'a', 'a']
diferentes = ['a', 'a', 'a', 'b', 'a']

def todos_iguais(lista):
    for i in range(1, len(lista)):
        if lista[i] != lista[i-1]:
            return False
        
    return True

print(todos_iguais(iguais))
print(todos_iguais(diferentes))