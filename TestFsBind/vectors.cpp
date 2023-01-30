#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <math.h>

struct Vector2
{
    double x;
    double y;
    Vector2(double x, double y);
    double distanceTo(Vector2 pos);
    void vectorMovement(double plusx, double plusy);
    Vector2 midpoint(Vector2 pos);
    double percentDistance(Vector2 pos, double percentOfDistance);
};

struct Vector3
{
    double x;
    double y;
    double z;
    Vector3(double inx = 0, double iny = 0, double inz = 0);
    double distanceTo(Vector3 pos);
    void vectorMovement(double plusx, double plusy, double plusz);
    Vector3 midpoint(Vector3 pos);
    double percentDistance(Vector3 pos, double percentOfDistance = 100);
};

extern "C"
{

    Vector2::Vector2(double x, double y) : x(x), y(y) {} 
    double Vector2::distanceTo(Vector2 pos)
    {
        return sqrt(pow(x - pos.x, 2) + pow(y - pos.y, 2));
    }
    void Vector2::vectorMovement(double plusx, double plusy)
    {
        x += plusx;
        y += plusy;
    }
    Vector2 Vector2::midpoint(Vector2 pos)
    {
        return Vector2((x + pos.x) / 2, (y + pos.y) / 2);
    }
    double Vector2::percentDistance(Vector2 pos, double percentOfDistance)
    {
        return distanceTo(pos) * percentOfDistance;
    }

    double v2distanceTo(double x1, double y1, double x2, double y2)
    {
        return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
    }

    double v2percentDistance(double x, double y, double percentOfDistance)
    {
        return v2distanceTo(x, y, 0, 0) * percentOfDistance;
    }

}

extern "C"
{

    Vector3::Vector3(double x, double y, double z) : x(x), y(y), z(z) {}
    double Vector3::distanceTo(Vector3 pos) {
        return sqrt((pos.y - y) * (pos.y - y) + (pos.x - x) * (pos.x - x) + (pos.z - z) * (pos.z - z));
    }
    void Vector3::vectorMovement(double plusx, double plusy, double plusz) {
        x += plusx;
        y += plusy;
        z += plusz;
    }

    Vector3 Vector3::midpoint(Vector3 pos) {
        return Vector3((x + pos.x) / 2, (y + pos.y) / 2, (z + pos.z) / 2);
    }

    double Vector3::percentDistance(Vector3 pos, double percentOfDistance) {
        return distanceTo(pos) * percentOfDistance;
    }

    double v3distanceTo(double x1, double y1, double z1) {
        return sqrt(pow(x1, 2) + pow(y1, 2) + pow(z1, 2));
    }

    double v3percentDistance(double x, double y, double z, double percentOfDistance) {
        return v3distanceTo(x, y, z) * percentOfDistance;
    }

}