def quicksort(sequenza):
    # caso terminale
    if len(sequenza) <= 1:
        return sequenza
    # caso ricorsivo
    else:
        # 1. scelta pivot
        pivot = sequenza[0]
        # 2. dividere sequenza secondo il pivot
        # sequenza_smaller = []
        # sequenza_pivot = []
        # sequenza_larger = []
        # for s in sequenza:
        #     # il numero è < pivot
        #     if s < pivot:
        #         sequenza_smaller.append(s)
        #     # il numero è uguale al pivot
        #     elif s == pivot:
        #         sequenza_pivot.append(s)
        #     # il numero è > pivot
        #     else:
        #         sequenza_larger.append(s)

        sequenza_smaller = [s for s in sequenza if s < pivot]
        sequenza_pivot = [s for s in sequenza if s == pivot]
        sequenza_larger = [s for s in sequenza if s > pivot]
        # 3. la soluzione è data da: ordinare il vettore smaller + il vettore = pivot + il vettore larger
        return (quicksort(sequenza_smaller)
                + sequenza_pivot
                + quicksort(sequenza_larger))




if __name__ == "__main__":
    sequenza = [9, 3, 2, 6, 8, 5, 199]
    print(quicksort(sequenza))