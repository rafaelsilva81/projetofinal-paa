import time

# Python program for KMP Algorithm
def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
  
    # create lps[] that will hold the longest prefix suffix 
    # values for pattern
    lps = [0]*M
    j = 0 # index for pat[]
  
    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)
  
    i = 0 # index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
  
        if j == M:
            print ("Found pattern at index " + str(i-j))
            j = lps[j-1]
  
        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
  
def computeLPSArray(pat, M, lps):
    len = 0 # length of the previous longest prefix suffix
  
    lps[0] # lps[0] is always 0
    i = 1
  
    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i]== pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar 
            # to search step.
            if len != 0:
                len = lps[len-1]
  
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1
  
def main():
    text = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent gravida faucibus turpis in fermentum. Duis viverra tortor vitae lectus suscipit commodo. Integer velit risus, aliquet at commodo sit amet, viverra sed felis. In ante nibh, gravida ac sapien ac, consectetur luctus lacus. Suspendisse varius at neque a scelerisque. Integer tempor felis a nibh auctor maximus. Pellentesque commodo orci sed volutpat placerat. Donec vitae arcu ut lectus dapibus maximus vel pellentesque magna. Donec varius nunc maximus, venenatis odio tincidunt, condimentum ipsum. Donec mauris tortor, sollicitudin eget ultrices eget, tempor sit amet arcu. Pellentesque velit ipsum, consequat in molestie eget, vehicula sed felis. Fusce ante purus, condimentum sed tempus quis, varius sed ligula. Cras ut ultrices diam, id ultricies ipsum. Sed metus lacus, posuere vitae lacus nec, rutrum ornare neque. Vivamus eget enim est. Quisque tempor dapibus justo.

    Vivamus porta erat arcu, in sodales diam tristique eu. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Praesent semper, lorem eu egestas feugiat, nisl tellus molestie purus, a interdum nibh ligula eu ipsum. In tempor lacus quis quam lobortis, quis venenatis est gravida. Donec at venenatis ligula. Cras congue commodo mi vel tempor. Etiam ac dolor lobortis nisl malesuada commodo. Aenean sed tristique massa. Curabitur nunc erat, eleifend quis consequat in, euismod aliquet ligula. Vestibulum in egestas tortor. Sed suscipit lorem vitae ex feugiat, sed rhoncus ligula lobortis. Suspendisse maximus, nisi quis condimentum pulvinar, libero leo elementum sem, eu convallis dolor augue vitae sapien. Integer id nulla ultrices, malesuada nibh nec, mollis diam.

    Nam et dolor id tellus tristique egestas. Curabitur elit velit, auctor non rhoncus eget, tempus et leo. Morbi molestie urna sed elit maximus consequat. Quisque porttitor, nisi id consectetur semper, ante est pharetra nunc, bibendum aliquam leo velit sed tortor. Sed a congue magna. Morbi facilisis dictum elit ut lobortis. Curabitur sagittis diam arcu, et dignissim est congue quis.

    Mauris tincidunt consectetura fermentum ante, quis gravida purus pretium a. Integer imperdiet pretium arcu in interdum. Quisque sit amet nisl eu purus eleifend ornare. Vestibulum consectetur malesuada erat vel bibendum. Praesent ornare est fermentum, volutpat diam eu, hendrerit sapien. Curabitur in justo id tellus feugiat viverra. Duis vestibulum ante euismod leo porttitor pharetra. Morbi facilisis eleifend scelerisque. Aliquam dignissim pretium libero ac mollis. Suspendisse ultrices, eros vel euismod vestibulum, lacus nibh posuere risus, sed blandit urna elit ac diam. Vestibulum diam lacus, lobortis sit amet massa eu, ultrices consectura interdum ex.

    Ut varius augue a viverra tempus. Vestibulum aliquam nisl sapien, eget rutrum mauris aliquam ac. consecteturax Nulla ultrices vestibulum sapien, eget lobortis lectus rutrum sit amet. Etiam tempor nisl vel tortor suscipit, sed laoreet leo tempus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut laoreet in est id lacinia. Sed bibendum dapibus varius. Ut et scelerisque neque. Sed magna ex, dictum eu aliquet et, suscipit vel neque. Donec vestibulum lacus nec consequat placerat. Praesent bibendum, dolor in egestas dapibus, turpis dolor volutpat nulla, quis faucibus lacus nunc eget urna. Vestibulum a magna enim. Maecenas arcu nibh, vestibulum ut tortor et, tempor molestie augue. Aliquam erat orci, finibus et augue ut, tempor pretium tortor. Fusce sed viverra nibh. Nulla mattis tellus neque, at porttitor leo aliquam ac. 
    """ 

    pattern = "consecteturax"
    # pattern = "sit"
    
    start = time.time()
    KMPSearch(pattern, text)
    end = time.time()
    t = end - start
    print(f"tempo: {t:.10f}s")


if __name__ == "__main__":
    main()
