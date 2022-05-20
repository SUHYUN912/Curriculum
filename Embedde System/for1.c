#include <stdio.h>

void main()
{
	int a, i;
	int sum=0;
	printf("숫자 하나를 입력하시오.\n");
	scanf("%d", &a);

	for(i=0 ; i<a ; i++)
	{
		sum=sum+i;
	}
	printf("결과 : %d\n", sum);
}
