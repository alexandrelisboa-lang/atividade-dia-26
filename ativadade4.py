import os 

os.system ("cls" or "clear")

quantidade = int(input("digite a quantidade de macas:"))
if quantidade < 12:
    preço = 1.30
    
else:
    preço = 1.00
    
    valor = quantidade * preço
    print("A quantidade foi{}macas, o preço por unidade foi: R${:.2F}".format(quantidade, preço)) 
    print(f"o valor total da compra  e R${valor:.2f}")
    
    