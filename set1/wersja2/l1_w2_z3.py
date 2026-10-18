source = []

isStop = False

while not isStop:
    a = input()
    if a == "stop":
        isStop = True
    else:
        source.append(int(a))

print(f"Max = {max(source)}")
