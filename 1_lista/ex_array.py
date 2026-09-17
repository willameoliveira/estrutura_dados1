def inserir_no_array_estatico(arr, tamanho_atual, capacidade, indice, valor):
    # 1. Checa se o array estático está cheio
    if tamanho_atual >= capacidade:
        raise IndexError("Erro: Array Cheio!")
    
    # 2. Desloca os elementos para a direita (Custo O(n))
    for i in range(tamanho_atual, indice, -1):
        arr[i] = arr[i - 1]
        
    # 3. Insere o valor no índice desejado (Custo O(1))
    arr[indice] = valor

# --- Execução em Aula ---
capacidade = 6
# Cria array de inteiros ('i') pré-alocado com zeros
meu_array = [10, 20, 30, 40, None, None] 
tamanho_atual = 4

# Insere o valor 99 na posição 1
inserir_no_array_estatico(meu_array, tamanho_atual, capacidade, indice=1, valor=99)

print(meu_array)  # Output: array('i', [10, 99, 20, 30, 40, None])