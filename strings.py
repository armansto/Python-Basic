#1st class#
print('Hello I\'m Sayed')
print("Hello I'm Sayed")

#2nd Class#
Var1 = "I love Bangladesh"
Var2 = "2 + 2"
Var3 = 2 + 2

print(Var1)
print(Var2)
print(Var3)

#Concatenation#
Var4 = "Hello I am "
Var5 = input("Name?")
print(Var4 + Var5)

#Concatenation# Using Sting and Arithmatic#
Text = "Two and Tow Makes "
Math = 2 + 2

#print(Text + Math) //We cannot print string and integer at same print function//
#TO solve this we made another Variable Named Result which converts int to string


Result = str(Math)
print(Text + Result)

#Different syle Variable
X,Y = (3,7)
print(X)
print(Y)
print(X + Y)

#Class_4# If-Else

age = 19
if(age <= 13):
    print("You are a Kid")
elif (age >= 20):
    print("You are a Adult")
else:
    print("You are Teenager")

#Class 5 (Whine loop)

Text = ("I live Python")
i = 1
while (i<=10):
    print(Text)
    i = i + 1
#instead of above formula we can write: i+=1
Text = ("I live Python")
i = 1
while (i<=50):
    if(i%2!=0):
        print(i)
    i += 1

#List with while and for loop
data = [1, 9, 6, 5, 4, 3, 2, 29, 50, 20, 45]
i = 0
while (i<=10):
    print(data[i])
    i += 1

for x in data:
    print(x)


#Nested List

list = [23, 45, 2, 56, 6, 89, 88, 56, 2, 2, "Hello"]
list1 = [[2, 5, [3, 4, 6, 9, 90], 7, 9], 23, 45, 2, 56, 6, 89, 88, 56, 2, 2, "Hello"]

print(list[-1])
print(list)
print(list[0])
print(list[0][0])
print(list[0][2][3])

#Updating List
list = [23, 45, 2, 56, 6, 89, 88, 56, 2, 2, "Hello"]

list.insert(1, 33)
list.append(33)
list.extend([0, 2, 3])
list.remove(2)
list.pop()
list.remove(list[1])
print(list)
print(list.index(6))
print(list.count(2))

#Dictionary

dictionaryExample = {"name" : "Adam",
                     "id" : "171-15-8829",
                     "year" : "3rd"}
print(dictionaryExample)
print(dictionaryExample["name"])


#Function_1
def function4first():
    print("This is the first time i am using function is python")
    a,b,c = [4,5,3]
    sum = a + b + c
    print(sum)

function4first()

#Function_2
def sum(num1,numb2):
    total = num1 + numb2
    print(total)

sum(5,6)
sum(11,15)