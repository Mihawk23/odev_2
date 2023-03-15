ogrenci=["Ahmet A","Mehmet A","Veli A"]
print(ogrenci)

ogrenci.append("Zeynep A")
print(ogrenci)

ogrenci.remove("Mehmet A")
print(ogrenci)

ogrenci.extend(["Mehmet A", "Ali A"])
print(ogrenci)

print(len(ogrenci))

print(ogrenci[0])
print(ogrenci[1])
print(ogrenci[2])
print(ogrenci[3])
print(ogrenci[4])

print("*************")
# veya

for list in ogrenci:
    print(list)
  
print("*************")

ogrenci_no=ogrenci[2]
print(ogrenci_no)

print("*************")

i=0
while i< len(ogrenci):
    if ogrenci[i] == "Zeynep A":
        break
    print(ogrenci[i])
    i+=1