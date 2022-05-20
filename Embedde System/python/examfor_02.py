list = [1, 2, 3]
tuple = ('a', 'b', 'c')
dict = {'a':1, 'b':2, 'c':3}
set = {'A', 'B', 'C'}

for i in list:
    print(i)

for j in tuple:
    print(j)

for key in dict:
    print("key : " + key + " value : " + str(dict[key]))

for k in set:
    print(k)
