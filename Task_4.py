# Answer 1)
dict = {'name': 'Alex Ryder','age':28}
dict.update(age=32)
dict['town']='calicut'
print(dict)

# Answer 2)
n = 5
dict = {}
for i in range(1, n+1):
  dict[i] = i * i
print (dict)
dict.pop(3)
print (dict)
dict.clear()
print(dict)
del dict
print(dict)
# Answer 3)
set = {"Hello",1,(0,1, 2)}
print(set)
set.add(6)
print(set)