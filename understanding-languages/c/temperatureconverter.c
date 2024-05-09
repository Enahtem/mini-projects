#include <stdio.h>

int main(){
    float f, c;
    f=0;
    while (f<=300){
        c = 5.0*(f-32.0)/9.0;
        printf("%10.2f %10.2f\n", f, c);
        f+=20;
    }
    return 0;
}