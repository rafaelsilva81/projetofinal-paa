import csv
import time
import lorem
import utils
from algorithms import kmp_search, naive_search

header = ['tamanho_texto', 'tamanho_padrao', 'tempo (ms)']

#Esse teste aumenta o tamanho do texto, e utiliza o padrao de tamanho medio (6 Caracteres)
def teste_texto():
    data_kmp = []
    data_naive = []
    pattern = "aliqua"
    word_number = 10000

    while (word_number < 200000):
        
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

    file_name = 'tests/teste_texto' + time.strftime("%d%m%Y-%H%M%S") + '.csv'
    with open(file_name, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['KMP'])
        writer.writerow(header)
        writer.writerows(data_kmp)
        writer.writerow([])
        writer.writerow(['NAIVE'])
        writer.writerow(header)
        writer.writerows(data_naive)




