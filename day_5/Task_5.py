# 1) answer
list=[23, 45, 25 ,78, 90, 45, 22, 56, 99, 12, 9, 75, 32]
print("The list is :",list)
print("The elements in even positions are : ")
for i in range(1, len(list),2): 
    print(list[i]); 
del list[5:8]
print("Updated list is :", list)


# 2)Answer 
input = ['a', 'e', 'i', 'o', 'u'] 
list = [x.upper() for x in input]
print(list)
# 3) Answer
fruits = ("banana","cherry","apple","grapes")

(yellow,*red,green) = fruits
print(yellow)
print(red)
print(green)