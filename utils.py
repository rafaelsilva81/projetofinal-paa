import lorem

# The original lorem ipsum text pool.
pool = ('ad', 'adipiscing', 'aliqua', 'aliquip', 'amet', 'anim', 'aute', 'cillum', 'commodo',
         'consectetur', 'consequat', 'culpa', 'cupidatat', 'deserunt', 'do', 'dolor', 'dolore',
         'duis', 'ea', 'eiusmodo', 'elit', 'enim', 'esse', 'est', 'et', 'eu', 'ex', 'excepteur',
         'exercitation', 'fugiat', 'id', 'in', 'incididunt', 'ipsum', 'irure', 'labore', 'laboris',
         'laborum', 'lorem', 'magna', 'minim', 'mollit', 'nisi', 'non', 'nostrud', 'nulla',
         'occaecat', 'officia', 'pariatur', 'proident', 'qui', 'quis', 'reprehenderit', 'sed',
         'sint', 'sit', 'sunt', 'tempor', 'ullamco', 'ut', 'velit', 'veniam', 'voluptate', 'intellectualized'
         , 'quinquagintaquadringentillionths')

def get_pool():
    return pool

def get_custom_word(tam):
    for var in pool:
        if(len(var) == tam):
            return var
    return 'lorem'

def ms(tempo, casas_decimais): 
    return round((tempo * 1000), casas_decimais)

def set_custom_pool():
    # 2 : ad
    # 4 : amet
    # 8 : eiusmodo
    # 16 : intellectualized
    # 32 : quinquagintaquadringentillionths
    lorem.set_pool(pool)
    