from math import pi, pow, sqrt

print("Bryly - a | Plaskie - b")
inp = input("inp: ").lower().strip()
if inp == "a":
    print("ppBryl - a | vBryl - b")
    inp = input("inp: ").lower().strip()
    if inp == "a":
        print(
            "ppSzecianu - a | ppProstopadloscianu - b | ppGraniastoslupa - c | ppOstroslupa - d | ppWalca - e | ppStozka - f | ppKuli - g"
        )
        inp = input("inp: ").lower().strip()
        if inp == "a":
            a = float(input("a = "))
            print(f"ppSzecianu o boku {a} = {6*a**2}")
        elif inp == "b":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(f"ppProstopadloscianu o bokach {a} {b} {c} = {2*a*b+2*b*c+2*c*a}")
        elif inp == "c":
            pp = float(input("pp = "))
            pb = float(input("pb = "))
            print(f"ppGraniastoslupa o Pp {pp} i Pb {pb} = {2*pp+pb}")
        elif inp == "d":
            pp = float(input("pp = "))
            pb = float(input("pb = "))
            print(f"ppOstroslupa o Pp {pp} i Pb {pb} = {pp+pb}")
        elif inp == "e":
            r = float(input("r = "))
            h = float(input("h = "))
            print(f"ppWalca o R {r} i H {h} = {2*pi*pow(r,2)+2*pi*r*h}")
        elif inp == "f":
            r = float(input("r = "))
            l = float(input("l = "))
            print(f"ppStozka o R {r} i L {l} = {pi*pow(r,2)+pi*r*l}")
        elif inp == "g":
            r = float(input("r = "))
            print(f"ppKuli o R {r} = {4*pi*pow(r,2)}")
        else:
            print("Nie ma takiej komendy: ")
    elif inp == "b":
        print(
            "vSzecianu - a | vProstopadloscianu - b | vGraniastoslupa - c | vOstroslupa - d | vWalca - e | vStozka - f | vKuli - g"
        )
        inp = input("inp: ").lower().strip()
        if inp == "a":
            a = float(input("a = "))
            print(f"vSzecianu o boku {a} = {pow(a,3)}")
        elif inp == "b":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(f"vProstopadloscianu o bokach {a} {b} {c} = {a*b*c}")
        elif inp == "c":
            pp = float(input("pp = "))
            h = float(input("h = "))
            print(f"vGraniastoslupa o Pp {pp} i H {h} = {pp*h}")
        elif inp == "d":
            pp = float(input("pp = "))
            h = float(input("h = "))
            print(f"vOstroslupa o Pp {pp} i H {h} = {(1/3)*pp*h}")
        elif inp == "e":
            r = float(input("r = "))
            h = float(input("h = "))
            print(f"vWalca o R {r} i H {h} = {pi*pow(r,2)*h}")
        elif inp == "f":
            r = float(input("r = "))
            h = float(input("h = "))
            print(f"vStozka o R {r} i H {h} = {(1/3)*pi*pow(r,2)*h}")
        elif inp == "g":
            r = float(input("r = "))
            print(f"vKuli o R {r} = {(4/3)*pi*pow(r,3)}")
    else:
        print("nie ma takiej komendy")
elif inp == "b":
    print("obwody fig plaskie - a | pp fig plaskich - b")
    inp = input("inp: ").lower().strip()
    if inp == "a":
        print(
            "oKwadratu - a | oProstokata - b | oPownolegloboku - c | oTrapezu - d | oTrojkata - e | oTrojkataRownobocznego - f | oKola - g | oRombu - h"
        )
        inp = input("inp: ").lower().strip()
        if inp == "a":
            a = float(input("a = "))
            print(f"oKwadratu o boku {a} = {4*a}")
        elif inp == "b":
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"oProstokata o bokach {a} {b} = {2*a+2*b}")
        elif inp == "c":
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"oPownolegloboku o bokach {a} {b} = {2*a+2*b}")
        elif inp == "d":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            d = float(input("d = "))
            print(f"oTrapezu o bokach {a} {b} {c} {d} = {a+b+c+d}")
        elif inp == "e":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(f"oTrojkata o bokach {a} {b} {c} = {a+b+c}")
        elif inp == "f":
            a = float(input("a = "))
            print(f"oTrojkataRownobocznego o boku {a} = {3*a}")
        elif inp == "g":
            r = float(input("r = "))
            print(f"oKola o R {r} = {2*pi*r}")
        elif inp == "h":
            a = float(input("a = "))
            print(f"oRombu o boku {a} = {4*a}")
        else:
            print("Nie ma takiej komendy: ")
    elif inp == "b":
        print(
            "ppKwadratu - a | ppProstokata - b | ppPownolegloboku - c | ppTrapezu - d | ppTrojkata - e | ppTrojkataRownobocznego - f | ppKola - g | ppRombu(a,h) - h | ppRombu(e,f) - i"
        )
        inp = input("inp: ").lower().strip()
        if inp == "a":
            a = float(input("a = "))
            print(f"ppKwadratu o boku {a} = {pow(a,2)}")
        elif inp == "b":
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"ppProstokata o bokach {a} {b} = {a*b}")
        elif inp == "c":
            a = float(input("a = "))
            h = float(input("h = "))
            print(f"ppPownolegloboku o boku {a} i wysokosci {h} = {a*h}")
        elif inp == "d":
            a = float(input("a = "))
            b = float(input("b = "))
            h = float(input("h = "))
            print(f"ppTrapezu o bokach {a} {b} i wysokosci {h} = {(a+b)*h/2}")
        elif inp == "e":
            a = float(input("a = "))
            h = float(input("h = "))
            print(f"ppTrojkata o boku {a} i wysokosci {h} = {(1/2)*a*h}")
        elif inp == "f":
            a = float(input("a = "))
            print(f"ppTrojkataRownobocznego o boku {a} = {pow(a,2)*sqrt(3)/4}")
        elif inp == "g":
            r = float(input("r = "))
            print(f"ppKola o R {r} = {pi*pow(r,2)}")
        elif inp == "h":
            a = float(input("a = "))
            h = float(input("h = "))
            print(f"ppRombu(a,h) o boku {a} i wysokosci {h} = {a*h}")
        elif inp == "i":
            e = float(input("e = "))
            f = float(input("f = "))
            print(f"ppRombu(e,f) o diagonali {e} {f} = {e*f/2}")
        else:
            print("Nie ma takiej komendy: ")
    else:
        print("nie ma takiej komendy")
else:
    print("Nie ma takiej komendy")
