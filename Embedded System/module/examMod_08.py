import sys
sys.path.append('/home/pi/practice30417/python')

import examClass03 as Cal

x = int(input("1st number : "))
y = int(input("2nd number : "))

a = Cal.MoreCalcul(x, y)

print(a.add())
print(a.sub())
print(a.mul())
print(a.div())
print(a.pow())
