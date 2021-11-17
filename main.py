import time
import requests
import lorem
import os

def kmp_search(pattern: str, text: str):
    """[summary]
    Busca o padrão dentro do texto de entrada.
    Args:
        pattern (string): padrão a ser buscado.
        text (string): texto onde será buscado o padrão.
    """
    n = len(text)  # armazena o tamanho do texto
    m = len(pattern)  # armazena o tamanho do padrão
    lps = [0]*m  # inicializa um array de tamanho 'm' preenchido com 0's
    compute_lsp(pattern, m, lps)  # longest prefix thats is also a suffix
    i = 0
    j = 0
    while i < n:
        if text[i] == pattern[j]:
            # se elementos nos indices do texto e padrão são iguais
            # incrementa os indices
            i += 1
            j += 1
        else:
            # mismatch após j match
            # Não teve match nos caracteres lps[0, ...,j-1]
            # irão dar match de qualquer jeito
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
        if j == m:
            # encontrou o padrão
            #print("Pattern found at index :", i-j)
            j = lps[j-1]


def compute_lsp(pattern: str, m: int, lps: list):
    len = 0  # tamanho do lps anterior
    i = 1
    lps[0] = 0  # lps[0] é sempre igual a 0

    while i < m:  # calcula lps[i] de i=1 à m-1
        if pattern[i] == pattern[len]:
            lps[i] = len+1
            len += 1
            i += 1
        else:
            if len != 0:
                len = 0
            else:
                lps[i] = 0
                i += 1

def naive_search(pattern: str, text: str):
    """[summary]
    Busca padrão dentro do texto de entrada através de duas estruturas de repetição aninhadas.
    Args:
        pattern (string): padrão a ser buscado.
        text (string): texto onde será buscado o padrão.
    """
    M = len(pattern)
    N = len(text)
 
    # Primeiro loop no pattern
    for i in range(N - M + 1):
        j = 0
         
        # Para o atual index i, checar se o pattern está presente no texto
        while(j < M):
            if (text[i + j] != pattern[j]):
                break
            j += 1
        
        if (j == M):
            pass
            #print("Pattern found at index ", i)
 
def main(): 
    
    #GERADOR DE LOREM IPSUM ALEATÓRIO
    text = lorem.get_paragraph(count=10000, comma=(0, 2), word_range=(4, 10), sentence_range=(5, 10), sep=os.linesep)
    
    #GERADOR DE PADRÃO ALEATÓRIO
    pattern = lorem.get_word(count=1)
    #pattern = "consectetur"
    print("\n========= PATTERN ESCOLHIDO : ",pattern)
    
    #INICIO DO TESTE KMP
    print('\n============= KMP ================')
    start = time.time_ns()
    kmp_search(pattern, text)
    end = time.time_ns()
    t = end - start
    print(f"tempo: {t}ns")

    #INICIO DO TESTE NAIVE
    print('\n============= NAIVE ================')
    start2 = time.time_ns()
    naive_search(pattern, text)
    end2 = time.time_ns()
    t = end2 - start2
    print(f"tempo: {t}ns")

if __name__ == "__main__":
    main()
