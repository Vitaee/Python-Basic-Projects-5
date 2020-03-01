print("\nWelcome to the Basketball Roster Program")
#Programı açtığımızda bizi bu yazı ile karşılıyor.


#Listeyi oluşturmamız için input almamız gerekiyor.
a = input("Who is your point guard: ").title()
b = input("Who is your shooting guard: ").title()
c = input("Who is your small forward: ").title()
d = input("Who is your power forward: ").title()
e = input("Who is your center: ").title()

#Alınan inputları print ediyoruz.
print("\n\tYour starting 5 for the upcoming basketball season")
print("\t\tPoint Guard: ",     a)
print("\t\tShooting Guard:",b)
print("\t\tSmall Forward: ", c)
print("\t\tPower Forward: ", d)
print("\t\tCenter: ",           e)

#Boş bir liste tanımlayıp alınan inputları içine atıyoruz.
g = []
g.append(a)
g.append(b)
g.append(c)
g.append(d)
g.append(e)

#Sakat olan oyuncu print ediliyor
print("\nOh no,", c, "is injured")
#Sakatlanan oyuncuyu listeden kaldırıyoruz.
g.remove(c)
#Listenin uzunluğunu yazıyoruz
print("Your roster only has",len(g), "players")

g.insert(2,"Lebron James")
print("Who will take ",c,"spot?")
f = input("Name of player: ").title()
#Listedeki 3.elemanı siliyoruz
del g[2]

print("\n\tYour starting 5 for the upcoming basketball season")
print("\t\tPoint Guard: ",a)
print("\t\tShooting Guard: ",b)
print("\t\tSmall Forward: ",f)
print("\t\tPower Forward: ",d)
print("\t\tCenter: ",e)
#Yeni oyuncu adını append ettik listeye.
g.append(f)

print("\nGood luck",f,"you will do great!")
print("Your roster now has",len(g),"players.")
