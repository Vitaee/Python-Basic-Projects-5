print("Welcome to the Binary/Hexadecimal Converter App\n")
a = int(input("Compute binary and hexadecimal values up to the following decimal number: "))

decimal = list(range(1, a+1)) #a+1 dedik çünkü range fonksiyonu son sayıyı almıyor.
binary = []
hexadecimal = []
for i in decimal: #for döngüsü oluşturarak decimal binary ve hexadecimal değerleri listelere atadık.
    binary.append(bin(i))
    hexadecimal.append(hex(i))

print("Generating lists.. complete!\n")

print("Using slices, we will now show a portion of each list")
b = int(input("What decimal number would you like to start at: "))
c = int(input("What decimal number would you like to stop at: "))


print("\nDecimal values from", b, "to", c,":")
for i in decimal[b-1:c]:      #list slice kullanarak değerlei girilen aralıklarda yazdırmış olduk
    print(i)

print("\nBinary values from",b, "to", c,":")
for i in binary[b-1:c]:
    print(i)

print("\nHexadecimal values from", b, "to", c,":")

for i in hexadecimal[b-1:c]:
    print(i)

input("\nPress Enter to see al values from 1 to " + str(a))
print("Decimal----Binary----Hexadecimal")
print("-------------------------------------")

for e,f,g in zip(decimal, binary, hexadecimal): #ve ilk başta girdiğimiz değeri mesela 40, 40 a kadar olan decimal , binary, hexadecimal değerleri yazdırdık.
    print(str(e) + "----" + str(f) + "-----" + str(g))
