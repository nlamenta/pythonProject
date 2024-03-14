lista = []

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        lista.append("LoveUEP")
    elif i % 3 == 0:
        lista.append("Love")
    elif i % 5 == 0:
        if i == 50:
            lista.append("83751")
        else:
            lista.append("UEP")
    else:
        lista.append(i)
print(lista)