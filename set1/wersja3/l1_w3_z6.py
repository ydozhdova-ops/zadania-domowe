k, m = int(input()), int(input())

temp_k = k
count = 0

while temp_k >= m:
    if temp_k % m == 0:
        count += 1
        temp_k = temp_k // m
    else:
        temp_k = 0

print(f"Liczba {k} jest podzielna przez liczbę {m} {count} razy.")
