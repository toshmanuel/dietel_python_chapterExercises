
my_list = [1, 2, 3, 4, 5]
print(my_list)
my_list.append(6)
print(my_list)
my_list.insert(0, 99)
print(my_list)
my_list[0] += 1
print(my_list)

my_list = my_list + [12]
print(my_list)

my_list.remove(my_list[0])
print(my_list)

my_list.pop()
print(my_list)

my_list.pop(2)
print(my_list)

name_list = ['joy', 'peace', 'good', 'bad-ass-fucking-nigga']

name_list = "*".join(name_list)
print(name_list)
my_list = tuple(my_list)
print(my_list)
print(type(my_list))

first_int = 10
second_int = 20

if first_int > second_int:
    print("The first number is greater")
else:
    print("The second number is greater")

for i, j in enumerate("hello", 1):
    print(i, j)
