

print("dtb or btd?")
answer = input()
if answer == "dtb":
    decimalNumber = int(input("please input your decimal number"))
    bina = []
    binareverse = []
    contador = 0
    while (decimalNumber/2) != 0: 
        decimalNumber = decimalNumber//2
        bina.append(decimalNumber%2)
        binareverse.append(bina[contador-1])
        contador = contador + 1
    print(binareverse)
elif answer == "btd":
    binary = input("Enter a binary number: ")
    decimal = 0
    for i in range(len(binary)):
        decimal += int(binary[len(binary) - 1 - i]) * (2 ** i)
    print(decimal)

else:
    print("Invalid input.")
    