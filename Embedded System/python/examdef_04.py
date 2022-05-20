def cal_def(i, k, p):
    res = 0

    if p == '+':
        res= i+k
    elif p =='-':
        res = i-k
    elif p == '*':
        res = i*k
    elif p == '/':
        res = i/k
    return res

x = int(input("input 1st number : "))
y = int(input("input 2nd number : "))
z = input("input arithmetic operator : ")

result = cal_def(x, y, z)

print("The result is %f!" %result)
