#include<stdio.h>
int main()
{

int n;
scanf("%d", &n);

int a[n][n];

int i=0;
int j=0;

for(i=0; i<n; i++)
{
	for(j=0; j<n; j++)
	{
		scanf("%d", &a[i][j]);

	}
	
}


// functioning 

int d1=0;
int d2=0;

for(i=0 ;i<n; i++)
{
	d1 = d1 + a[i][i];
	d2 = d2 + a[i][n-1-i];	
}

//printf("d1 is %d\n", d1);
//printf("d2 is %d\n", d2);

if (d1>d2)
{
	printf("%d\n", d1-d2);
}
else
{
	printf("%d\n", d2-d1);

}

return 0;








} 