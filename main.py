import time
import lorem
NANO_MULTIPLIER = 1000000000

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

    
    N = len(text) #obtem o tamanho do texto
    M = len(pattern) #obtem o tamanho do padrão

    """
        Tamanho máximo que o padrão pode estar no texto
        Exemplo :
        Tamanho do Texto N = 100 
        Tamanho do Padrão M = 10
        Se o Padrão não for encontrado até a posição [90] não será possível encontrar ele a partir da posição 91, pois
        não há mais tamanho sobrando no texto.
    """
    max_range = (N - M + 1)

    # Primeiro loop no pattern
    for i in range(max_range):
        j = 0

        # Para o atual index i, checar se o pattern está presente no texto
        while(j < M):
            if (text[i + j] != pattern[j]): #Caso encontre um erro na checagem do pattern, finalize e itere a buca
                break
            j += 1

        if (j == M):
            pass #Encontrado com sucesso
            #print("Pattern found at index ", i)

def main():

    word_number = 500000
    print("Processando...")
    # GERADOR DE LOREM IPSUM ALEATÓRIO
    text = lorem.get_sentence(count=1, comma=(
       0, 2), word_range=(word_number, word_number))

    #text = "The quick brown fox jumps over the lazy dog"

    # GERADOR DE PADRÃO ALEATÓRIO
    #pattern = lorem.get_word(count=1)
    pattern = "eoifoaslwllclsadlwlecjwwoepapwewpelacegtlclaspspeqlelcvlfkedlasckaqwleledlwcaseçeçcpqereqlceqwpcasrlrqwoaclrçqwojcaçlvmqwpievpçkajspojqwepozxcpborwkepçasçdlvkbwprjvaçvçbmhw"

    start = time.time()
    kmp_search(pattern, text)
    end = time.time()
    t = end - start

    start2 = time.time()
    naive_search(pattern, text)
    end2 = time.time()
    t2 = end2 - start2

    print(
        "-----------------------------------------\n"+
        " BUSCANDO PELA PALAVRA :", pattern, "\n"+
        " TEXTO DE", word_number, "PALAVRAS\n"+
        "-----------------------------------------\n"+
        "| KMP   : ", f"{t:.20f} sec |", int((t * NANO_MULTIPLIER)), "ns |\n"+
        "| NAIVE : ", f"{t2:.20f} sec |", int((t2 * NANO_MULTIPLIER)), "ns |\n"+
        "-----------------------------------------"
    )

if __name__ == "__main__":
    main()
