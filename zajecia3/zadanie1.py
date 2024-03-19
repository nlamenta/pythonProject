lista1 = []
moje_niu = '83751'

# tworzenie listy

for i in range(1, 101):
if i % 3 == 0 and i % 5 == 0:
           lista1.append("LoveUEP")
elif i % 3 == 0:
           lista1.append("Love")
elif i % 5 == 0:
if i == 50:
               lista1.append(moje_niu)
else:
               lista1.append("UEP")
else:
           lista1.append(i)

print(lista1)
print(lista1[49])