# Para que o código abaixo imprima "Éumteste", assinale abaixo a mudança necessária.
def fazAlgo(string):
    pos = 0
    string1 = ""
    while pos < len(string):
        if string[pos] != " ":
            string1 = string1 + string[pos]
        pos = pos + 1
        string1 = string1.format.capitalize()
    return string1


print(fazAlgo("É UM TESTE"))
