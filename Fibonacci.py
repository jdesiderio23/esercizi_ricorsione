from time import time


class Fibonacci:

    def __init__(self):
        pass

    def calcola_elemento(self, n):
        # caso terminale
        if n == 0:
            return 0
        elif n == 1:
            return 1
        # caso ricorsivo
        else:
            return self.calcola_elemento(n-1) + self.calcola_elemento(n-2)

if __name__ == "__main__":
    N = 40
    fib = Fibonacci()
    start_time = time()
    print(fib.calcola_elemento(N))
    end_time = time()
    print(f"Elapsed time - recursion: {end_time - start_time}")