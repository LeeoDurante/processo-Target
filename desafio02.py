# Escreva um programa que verifique, em uma string, a existência da letra ‘a’, 
# seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

def verificar_letra_a(string):
   
    string_lower = string.lower()
    
    
    quantidade_a = string_lower.count('a')
    

    if quantidade_a > 0:
        print(f"A letra 'a' aparece {quantidade_a} vezes na string.")
    else:
        print("A letra 'a' não está presente na string.")


while True:
    texto = input("Digite uma palavra para verificar (ou 'q' para sair): ")
    
    if texto.lower() == 'q':
        print("Saindo do programa...")
        break
    
    verificar_letra_a(texto)
