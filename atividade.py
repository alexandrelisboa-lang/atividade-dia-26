import os

os.system("cls")

#entrada
idade = int(input("digite a idade da pessoa"))

#processamento

if idade <=16:
    print("nao pode voltar")
elif idade<=17:
    print("voto opicional")
elif idade<=18:
    print("obrigatorio a voltar")
elif idade<=65:
    print("voto opicional")
else:
    print("nao podem votar")
    
    

    
    

