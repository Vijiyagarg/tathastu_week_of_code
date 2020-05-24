N= int(input("Enter the value of N: "))
a = 0
b = 1
print("The Fibanacci series upto", N, "th number is following:")
for i in range(N):
    print(a,end = " ")
    c = a + b
    a = b
    b = c
