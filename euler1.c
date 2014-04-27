#include <stdio.h>

int main (void)
{	
int x = 0;
int i = 0;
while (i < 1000)
{ 
	if (i%3 == 0 || i%5 ==0)
		{
		x += i;
		}
i++;
}
printf("Solution to Euler Problem Number 1 is: %d\n", x);
return 0;
}
