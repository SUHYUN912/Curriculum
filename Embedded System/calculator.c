#include <stdio.h>

void main()
{
	int a, b;
	char s;

	printf("계산식을 입력하시오.\n");

	scanf("%d %c %d", &a, &s, &b);

	switch(s)
	{
		case '+':
			printf("결과는 %d\n", a+b);
			break;
		case '-':
			printf("결과는 %d\n", a-b);
			break;
		case '*':
			printf("결과는 %d\n", a*b);
			break;
		case '/':
			printf("결과는 %d\n", a/b);
			break;
	}
}
