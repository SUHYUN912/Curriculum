#include <stdio.h>

void main()
{
	int a, b;
	int sum=0;
	
	printf("숫자 두 개를 입력하시오.\n");
	scanf("%d %d", &a, &b);
	sum = a+b;

	printf("결과 값 : %d\n", sum);
}
