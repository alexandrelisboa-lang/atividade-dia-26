import os

os.system("cls" or "clear")
peso = float(input("digite seu peso em KG(ex: 70.5):"))
altura = float(input("gite sua altura wm metros(ex: 1.78):"))
imc = peso / (altura ** 2)
print(f"seu e imc e: {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso ideal")
elif imc <= 24.9:
    print("peso ideal")
elif imc <= 29.9:
    print("levimente acima do peso")
elif imc <= 34.9:
    print("obesidade grau 1")
elif imc <=39.9:
    print("obesidade grau 2")
elif imc <=40.00:
    print("obesidade grau 3")
    