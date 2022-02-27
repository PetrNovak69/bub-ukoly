#include <stdio.h>
#include <math.h>
#include <stdlib.h>

float uhel = 1;

float degToRad(float x){
    x = x * 0.0174532925;
    return x;
}

float radToDeg(float x){
    x = x / 0.0174532925;
    return x;
}

int main(){
    for(float i = 0; i <= 360; i += 30){
        printf("%f; %f; %f; %f \n", i, degToRad(i), sin(degToRad(i)), cos(degToRad(i)));
    }
    return 0;
}
