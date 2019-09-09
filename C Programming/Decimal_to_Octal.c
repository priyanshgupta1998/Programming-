
#include <stdio.h>

int main()
{
    int dec=21,i=1,oct=0;
    for(int j=dec;j>0;j=j/8)
    {
        oct+=(j%8)*i;
        i=i*10;
        
    }
    printf("<______> %d <_____>",oct);
    return 0;
}
