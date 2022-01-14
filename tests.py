from asyncore import write
import csv
import time
import lorem
import utils
from algorithms import kmp_search, naive_search


header = ['tamanho_texto', 'tamanho_padrao', 'tempo (ms)']

#Função para escrever os testes em um .csv
def write_test(data_kmp, data_naive, tipo) :
    metadata = ['Tipo do teste : ' + tipo, 'Horário : ' + time.strftime("%d-%m-%Y %H:%M:%S") ]
    file_name = 'tests/' + tipo + time.strftime("%d-%m-%Y-%H_%M_%S")  + '.csv'
    with open(file_name, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['KMP'])
        writer.writerow(header)
        writer.writerows(data_kmp)
        writer.writerow(['NAIVE'])
        writer.writerow(header)
        writer.writerows(data_naive)
        writer.writerow(metadata)
        
#Esse teste dobra o tamanho do texto, e utiliza o padrao de tamanho medio (6 Caracteres)
def padrao_fixo(word_min, word_max, pattern):
    data_kmp = []
    data_naive = []
    word_number = word_min

    while (word_number < word_max):
        
        text = lorem.get_word(count=word_number, sep=' ', func=None, args=[], kwargs={})

        #Teste KMP
        start = time.time()
        kmp_search(pattern, text)
        end = time.time()
        t = utils.ms(end - start, 3)
        
        #Teste Naive
        start2 = time.time()
        naive_search(pattern, text)
        end2 = time.time()
        t2 = utils.ms(end2 - start2, 3)

        data_kmp.append([word_number, len(pattern), t])
        data_naive.append([word_number, len(pattern), t2])

        word_number = word_number * 2

    write_test(data_kmp, data_naive, 'padrao_fixo')


#Irá automaticamente fazer os testes com os padrões de tamanho 2 até 32
def texto_fixo(text_size):
    data_kmp = []
    data_naive = []
    word_number = text_size
    pattern_size = 2

    while (pattern_size <= 32):
        pattern = utils.get_custom_word(pattern_size)
        text = lorem.get_word(count=word_number, sep=' ', func=None, args=[], kwargs={})

        #Teste KMP
        start = time.time()
        kmp_search(pattern, text)
        end = time.time()
        t = utils.ms(end - start, 3)
        
        #Teste Naive
        start2 = time.time()
        naive_search(pattern, text)
        end2 = time.time()
        t2 = utils.ms(end2 - start2, 3)

        data_kmp.append([word_number, len(pattern), t])
        data_naive.append([word_number, len(pattern), t2])

        pattern_size = pattern_size * 2

    write_test(data_kmp, data_naive, 'texto_fixo')

def dobrar_ambos(min_text):
    data_kmp = []
    data_naive = []
    word_number = min_text
    pattern_size = 2

    while (pattern_size <= 32):
        pattern = utils.get_custom_word(pattern_size)
        text = lorem.get_word(count=word_number, sep=' ', func=None, args=[], kwargs={})

        #Teste KMP
        start = time.time()
        kmp_search(pattern, text)
        end = time.time()
        t = utils.ms(end - start, 3)
        
        #Teste Naive
        start2 = time.time()
        naive_search(pattern, text)
        end2 = time.time()
        t2 = utils.ms(end2 - start2, 3)

        data_kmp.append([word_number, len(pattern), t])
        data_naive.append([word_number, len(pattern), t2])

        word_number = word_number * 2
        pattern_size = pattern_size * 2

    write_test(data_kmp, data_naive, 'dobrar_ambos')

