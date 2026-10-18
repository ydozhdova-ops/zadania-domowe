from math import pow

n = int(input("n="))
factorial = 0

while n>=0:
    factorial += pow(2,n)
    n -= 1

print(f"Result={factorial}")