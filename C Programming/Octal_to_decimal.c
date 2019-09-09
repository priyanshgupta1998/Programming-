//octal to decimal

#include <stdio.h>

int main()
{
    int oct,i=1,dec=0,d,p=1;
    printf("Give any Octal Number Input between 0-7 : ");
    scanf("%d",&oct);
    for(int j=oct;j>0;j=j/10)
    {
       d = j%10;
        if(i==1)
        {
            p=p*1;
        }
        else{
            p=p*8;
        }
        dec =dec + (d*p);
        i++;
    }
    printf("<______> %d <_____>",dec);
    return 0;
}
