def piramida_angka(angka):
    for i in range(1, angka + 1):
        print("  " * (angka - i), end=" ")

        for j in range(1, i + 1):
            print(j, end=" ")

        for j in range (i - 1, 0, -1):
            print(j, end=" ")

        print()
piramida_angka(5)
        