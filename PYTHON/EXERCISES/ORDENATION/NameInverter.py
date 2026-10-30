name = "Sacul"
list_name = list(name)
tamanho = len(list_name)

if __name__ == "__main__":
    for n in range(tamanho // 2):
        j = tamanho - 1 - n
        aux = list_name[n]
        list_name[n] = list_name[j]
        list_name[j] = aux
        print("N:", n, "| J:", j, "->", list_name)

    resultado = "".join(list_name)   # sacuL
    print("Hard:",resultado.capitalize())

def easyinversor(a):
    return a[::-1]

print("Easy:", easyinversor("sacuL"))
