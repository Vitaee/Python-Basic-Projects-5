print("\n\t Summary Table")

a = ["15", "100", "55", "42"]
print("\nThe variable a is a ", type(a))
print("It contains the elements: ",a)
print("The element ", a[0], "is a", type(a[0]))

b = [15, 100, 55, 42]
print("\nThe variable a is a ", type(b))
print("It contains the elements: ",b)
print("The element ", b[0], "is a", type(b[0]))

c = [[1,2,3], [4,5,6], [7,8,9]]
print("\nThe variable a is a ", type(c))
print("It contains the elements: ",c)
print("The element ", c[0], "is a", type(c[0]))

d = [2.2, 5.0, 1.245, 0.14235]
print("\nThe variable a is a ", type(d))
print("It contains the elements: ",d)
print("The element ", d[0], "is a", type(d[0]))

print("\nNow sorting a and b..")
b.sort()
print("Sorted a: ",sorted(a))
print("Sorted b: ",b)
print("\nStrings are sorted alphabetically while integers are sorted numerically!")
