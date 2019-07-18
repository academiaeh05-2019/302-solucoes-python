meninos = ["Luiz", "João", "Alex", "Guilherme"]
meninas = ["Laís", "Larissa", "Ana"]

todos = meninos + meninas

i = 1
j = 0

for pessoa1 in todos:
  for k in range(j, len(todos)):
    if pessoa1 != todos[k]:
      print(f"Parzinho {i}: {pessoa1} e {todos[k]}")
      i += 1

  j += 1