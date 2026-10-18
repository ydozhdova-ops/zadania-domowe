isStop = False
source = []

while not isStop:
    inpt = input()
    if inpt == "stop":
        isStop = True
    else:
        source.append(int(inpt))

print(f"średnią arytmetyczną={sum(source)/len(source)}")
