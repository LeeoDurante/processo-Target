#Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
# escreva um programa na linguagem que desejar onde, informado um número, 
# ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def fibonacci_sequence(n):
    # Inicializando a sequência de Fibonacci
    fibonacci = [0, 1]
    
    # Gerando a sequência de Fibonacci até o número informado
    while fibonacci[-1] < n:
        next_value = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_value)
    
    return fibonacci

def is_fibonacci_number(number):
    
    fibonacci = fibonacci_sequence(number)
    

    if number in fibonacci:
        return f"O número {number} pertence à sequência de Fibonacci."
    else:
        return f"O número {number} não pertence à sequência de Fibonacci."


while True:
    user_input = input("Digite um número para verificar (ou 'q' para sair): ")
    
    if user_input.lower() == 'q':
        print("Saindo do programa...")
        break
    
    try:
        num = int(user_input)
        print(is_fibonacci_number(num))
    except ValueError:
        print("Por favor, digite um número válido ou 'q' para sair.")
