var = input("Enter your String: ")

print("Your original string is-", var.upper())
print("Printing only even index characters ")

for i in range(0, len(var), 2):
        print("index[", i, "]", var[i].upper())

