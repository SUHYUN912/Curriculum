for i in range(0, 7):
    print(i)
print("********************")

sum = 0

for j in range(0, 100, 2):
    sum += j
print("sum : %d" %sum)
print("********************")

sum=0
for k in range(0, 11, 1):
    if k<10:
        print("%d +" %k, end = " ")
    elif k==10:
        print("%d" %k, end = " ")
    sum+=k

print("=%d" %sum)
