def printRomano(numero):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    romano = ["I", "IV", "V", "IX", "X", "XL",
              "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12

    while numero:
        div = numero // num[i]
        numero %= num[i]

        while div:
            print(romano[i], end="")
            div -= 1
        i -= 1


# Driver code
if __name__ == "__main__":
    numero = int(input("digite o seu número "))
    print("o valor em Romano é:", end=" ")
    printRomano(numero)
