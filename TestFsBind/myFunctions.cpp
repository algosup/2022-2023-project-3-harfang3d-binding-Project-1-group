#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <math.h>

extern "C"
{
    int add(int a, int b)
    {
        return a + b;
    }
    int factorial(int n)
    {
        int result = 1;
        for (int i = 1; i <= n; i++)
        {
            result *= i;
        }
        return result;
    }
}