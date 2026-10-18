from math import pow

boki = [int(input()), int(input()), int(input())]
boki.sort()

if pow(boki[2], 2) == (pow(boki[0], 2) + pow(boki[1], 2)):
    print(f"Z odcinków {boki} można utworzyć trójkąt prostokątny")
else:
    print(f"Nie można utworzyć trójkąta prostokątnego z odcinków {boki}")
