a = int(input("자연수를 입력하세요(input numbers) : "))

if a%3 == 0:
    print("3의 배수입니다(Multiple of 3)")

elif a%2==1:
    print("홀수입니다.(Odd number)")
else:
    print("짝수입니다.(Even number)")
