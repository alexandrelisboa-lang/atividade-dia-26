import os

# limpa terminal
os.system("cls || clar")

print("- solicitando dados -")
primeiro_numero = int(input("digite o primeiro numero: "))
segundo_numero = int(input("digite o segundo numero: "))

maior = max(primeiro_numero, segundo_numero)
menor = min(primeiro_numero, segundo_numero)

print("\n- exibindo resultado -")
print(f"primeiro numero:{primeiro_numero}")
print(f"segundo numero:{segundo_numero}")
print(f"maior numero:{maior}")
print(f"menor numero:{menor}")
