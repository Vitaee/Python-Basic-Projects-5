print("\nWelcome to the Favorite Teachers Program")

a = input("Who is your first favorite teacher: ").title()
b = input("Who is your second favorite teacher: ").title()
c = input("Who is your third favorite teacher: ").title()
d = input("Who is your forth favorite teacher: ").title()

e = []
e.append(a)
e.append(b)
e.append(c)
e.append(d)

print("Your favorite teachers ranked are: ", e)
f = sorted(e)
print("\nYour favorite teachers alphabetically are: ", f)
g = sorted(e, reverse = True)
print("Your favorite teachers in reverse alphabetically: ", g)

print("Your top two teachers are: ", e[0],"and",e[1])
print("Your next two favorite teachers are: ", e[2],"and",e[3])
print("Your last favorite teacher is:", e[-1])
print("You have a total of",len(e),"favorite teachers")

print("Opps", e[0],"is no longer your first favorite teacher")
x = input("Who is your new FAVORITE teacher: ").title()

e.insert(0,x)

print("Your favorite teachers ranked are: ", e)
f = sorted(e)
print("\nYour favorite teachers alphabetically are: ", f)
g = sorted(e, reverse = True)
print("Your favorite teachers in reverse alphabetically: ", g)

print("Your top two teachers are: ", e[0],"and",e[1])
print("Your next two favorite teachers are: ", e[2],"and",e[3])
print("Your last favorite teacher is:", e[-1])
print("You have a total of",len(e),"favorite teachers")

print("You've decided you no longer lika a teacher.")
y = input("Which teacher would you like to remove from your list: ").title()
e.remove(y)

print("Your favorite teachers ranked are: ", e)
f = sorted(e)
print("\nYour favorite teachers alphabetically are: ", f)
g = sorted(e, reverse = True)
print("Your favorite teachers in reverse alphabetically: ", g)

print("Your top two teachers are: ", e[0],"and",e[1])
print("Your next two favorite teachers are: ", e[2],"and",e[3])
print("Your last favorite teacher is:", e[-1])
print("You have a total of",len(e),"favorite teachers")
