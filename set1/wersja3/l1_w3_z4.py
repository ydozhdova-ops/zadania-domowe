from math import pow

boki = [int(input()), int(input()), int(input())]
boki.sort()

if pow(boki[2], 2) == (pow(boki[1], 2) + pow(boki[0], 2)):
    print("Trójkąt jest prostokątny")

if boki[0] == boki[1] or boki[1] == boki[2]:
    if boki[0] == boki[2]:
        print("Trójkąt jest różnoboczny")
    else:
        print("Trójkąt jest równoramienny")
