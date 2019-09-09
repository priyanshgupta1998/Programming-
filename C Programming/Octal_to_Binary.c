//Octal_to_Binary

#include <stdio.h>

int main()
{
    int oct=25,i=1,dec=0,d,p=1;
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
    
    int k=1,bin=0;
    for(int s=dec;s>0;s=s/2)
    {
        bin+=(s%2)*k;
        k=k*10;
        
    }
    printf("<______> %d <_____>",bin);
    return 0;
}
