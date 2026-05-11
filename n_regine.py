

class NRegine():
    def __init__(self):
        pass

    #===========================================APPROCCIO 2=====================================
    # Rappresentiamo soluzione come un vettore di N regine,
    # ognuno rappresentante una regina come riga e colonna
    def solve2(self, N):
        self._ricorsione2([], N)

    # parziale è un vettore di coppie (riga, colonna)
    def _ricorsione2(self, parziale, N):
        # caso terminale: ho messo N regine
        if len(parziale) == N:
            print(parziale)
        # caso ricorsivo: ho messo < N regine
        else:


if __name__ == "__main__":
    nreg = NRegine()
    nreg.solve(4)
