"""Solução do exercicio numero 3 da aula anterior."""

import random


def embaralhar(lista):
    """Embaralha uma lista recebida como argumento."""
    try:
        for i in range(len(lista) - 1, 0, -1):
            indice_aleatorio = random.randint(0, i)

            valor_temporario = lista[i]
            lista[i] = lista[indice_aleatorio]
            lista[indice_aleatorio] = valor_temporario
        return lista
    except TypeError:
        print("A função embaralhar deve ser chamada com uma <LISTA>."
              + "Houve um erro de tipagem.")
    except KeyError:  
        print("A função embaralhar deve ser chamada com uma <LISTA>. Houve um erro de indexação (chave).")


VALORES = [1, 2, 3, 4, 5, 6, 7, 8]

EMBARALHADO = embaralhar(VALORES)
print(EMBARALHADO)
