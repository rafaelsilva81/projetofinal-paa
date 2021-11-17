import time

def brute_force_search(pattern: str, text: str):
    """
    Função Brute Force usando estrutura de for aninhado
    Encontra o primeiro index de 'pattern' em 'text'
    Se nada é encontrado, não retorna nenhum valor. 
    ENTRADA : 
        pattern - String : padrão a ser buscado
        text - String : texto no qual o padrão será buscado
    SAÍDA : 
        inteiro 'i' representando o index no qual o padrão pattern é encontrado em text
        ou 'None' 
    """
    n = len(text)
    m = len(pattern)
    for i in range(1 + (n - m)):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            return i


def main():
    text = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent gravida faucibus turpis in fermentum. Duis viverra tortor vitae lectus suscipit commodo. Integer velit risus, aliquet at commodo sit amet, viverra sed felis. In ante nibh, gravida ac sapien ac, consectetur luctus lacus. Suspendisse varius at neque a scelerisque. Integer tempor felis a nibh auctor maximus. Pellentesque commodo orci sed volutpat placerat. Donec vitae arcu ut lectus dapibus maximus vel pellentesque magna. Donec varius nunc maximus, venenatis odio tincidunt, condimentum ipsum. Donec mauris tortor, sollicitudin eget ultrices eget, tempor sit amet arcu. Pellentesque velit ipsum, consequat in molestie eget, vehicula sed felis. Fusce ante purus, condimentum sed tempus quis, varius sed ligula. Cras ut ultrices diam, id ultricies ipsum. Sed metus lacus, posuere vitae lacus nec, rutrum ornare neque. Vivamus eget enim est. Quisque tempor dapibus justo.

    Vivamus porta erat arcu, in sodales diam tristique eu. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Praesent semper, lorem eu egestas feugiat, nisl tellus molestie purus, a interdum nibh ligula eu ipsum. In tempor lacus quis quam lobortis, quis venenatis est gravida. Donec at venenatis ligula. Cras congue commodo mi vel tempor. Etiam ac dolor lobortis nisl malesuada commodo. Aenean sed tristique massa. Curabitur nunc erat, eleifend quis consequat in, euismod aliquet ligula. Vestibulum in egestas tortor. Sed suscipit lorem vitae ex feugiat, sed rhoncus ligula lobortis. Suspendisse maximus, nisi quis condimentum pulvinar, libero leo elementum sem, eu convallis dolor augue vitae sapien. Integer id nulla ultrices, malesuada nibh nec, mollis diam.

    Nam et dolor id tellus tristique egestas. Curabitur elit velit, auctor non rhoncus eget, tempus et leo. Morbi molestie urna sed elit maximus consequat. Quisque porttitor, nisi id consectetur semper, ante est pharetra nunc, bibendum aliquam leo velit sed tortor. Sed a congue magna. Morbi facilisis dictum elit ut lobortis. Curabitur sagittis diam arcu, et dignissim est congue quis.

    Mauris tincidunt consectetura fermentum ante, quis gravida purus pretium a. Integer imperdiet pretium arcu in interdum. Quisque sit amet nisl eu purus eleifend ornare. Vestibulum consectetur malesuada erat vel bibendum. Praesent ornare est fermentum, volutpat diam eu, hendrerit sapien. Curabitur in justo id tellus feugiat viverra. Duis vestibulum ante euismod leo porttitor pharetra. Morbi facilisis eleifend scelerisque. Aliquam dignissim pretium libero ac mollis. Suspendisse ultrices, eros vel euismod vestibulum, lacus nibh posuere risus, sed blandit urna elit ac diam. Vestibulum diam lacus, lobortis sit amet massa eu, ultrices consectura interdum ex.

    Ut varius augue a viverra tempus. Vestibulum aliquam nisl sapien, eget rutrum mauris aliquam ac. consecteturax Nulla ultrices vestibulum sapien, eget lobortis lectus rutrum sit amet. Etiam tempor nisl vel tortor suscipit, sed laoreet leo tempus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut laoreet in est id lacinia. Sed bibendum dapibus varius. Ut et scelerisque neque. Sed magna ex, dictum eu aliquet et, suscipit vel neque. Donec vestibulum lacus nec consequat placerat. Praesent bibendum, dolor in egestas dapibus, turpis dolor volutpat nulla, quis faucibus lacus nunc eget urna. Vestibulum a magna enim. Maecenas arcu nibh, vestibulum ut tortor et, tempor molestie augue. Aliquam erat orci, finibus et augue ut, tempor pretium tortor. Fusce sed viverra nibh. Nulla mattis tellus neque, at porttitor leo aliquam ac. 
    """ 

    pattern = "consecteturax"

    start = time.time()
    x = brute_force_search(pattern, text)
    end = time.time()
    t = end - start
    print(x)
    print(f"tempo: {t:.10f}s")


if __name__ == "__main__":
    main()

