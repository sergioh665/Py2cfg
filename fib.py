def fibonacci(n):
    # Inicializando a sequência com os dois primeiros números de Fibonacci
    sequencia = [0, 1]
    
    # Gerando a sequência até o n-ésimo termo
    for i in range(2, n):
        # Cada novo termo é a soma dos dois anteriores
        proximo = sequencia[i-1] + sequencia[i-2]
        sequencia.append(proximo)
    
    return sequencia

# Definindo o número de termos da sequência
n = 10
sequencia_fibonacci = fibonacci(n)

# Exibindo a sequência
print(f"Sequência de Fibonacci com {n} termos:")
print(sequencia_fibonacci)
