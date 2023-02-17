#ifndef VECTOR_H
#define VECTOR_H

#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <math.h>

#ifdef __cplusplus
extern "C"
{
#endif

    class Vector2
    {
    public:
        Vector2(double inx = 0, double iny = 0);
        mutable double x;
        mutable double y;
        double distanceTo(Vector2 pos);
        void vectorMovement(double plusx, double plusy);
        Vector2 midpoint(Vector2 pos);
        double percentDistance(Vector2 pos, double percentOfDistance = 100);
    };

    class Vector3
    {
    public:
        Vector3(double inx = 0, double iny = 0, double inz = 0);
        double x;
        double y;
        double z;
        double distanceTo(Vector3 pos);
        void vectorMovement(double plusx, double plusy, double plusz);
        Vector3 midpoint(Vector3 pos);
        double percentDistance(Vector3 pos, double percentOfDistance = 100);
    };

#ifdef __cplusplus
}
#endif

#endif