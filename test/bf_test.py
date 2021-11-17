import time

def brute_force_search(pattern: str, text: str):
    M = len(pattern)
    N = len(text)
 
    # A loop to slide pattern[] one by one */
    for i in range(N - M + 1):
        j = 0
         
        # For current index i, check
        # for patterntern match */
        while(j < M):
            if (text[i + j] != pattern[j]):
                break
            j += 1
 
        if (j == M):
            print("Pattern found at index ", i)


def main():
    with open('lipsum.txt') as f:
        text = f.read()

    pattern = "bibendum"
    # pattern = "sit"

    start = time.time()
    x = brute_force_search(pattern, text)
    end = time.time()
    t = end - start
    print(f"tempo: {t:.15f}s")


if __name__ == "__main__":
    main()

