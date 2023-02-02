#include "vectors.h"

extern "C"
{
    // NEW VECTOR2
    Vector2::Vector2(double inx, double iny)
    {
        x = inx;
        y = iny;
    }

    Vector2 createVector2(double inx, double iny)
    {
        Vector2 vec(inx, iny);
        return vec;
    }

    Vector2 updateVector2(Vector2 vec, double inx, double iny)
    {
        vec.x = inx;
        vec.y = iny;
        return vec;
    }


    // DISTANCE TO
    double Vector2::distanceTo(Vector2 pos)
    {
        return sqrt((pos.y - y) * (pos.y - y) + (pos.x - x) * (pos.x - x));
    }

    double distanceToVector2(Vector2 vec, Vector2 pos)
    {
        return vec.distanceTo(pos);
    }

    // VECTOR MOVEMENT
    void Vector2::vectorMovement(double plusx, double plusy)
    {
        x += plusx;
        y += plusy;
        return;
    }

    Vector2 vectorMovement(Vector2 v, double plusx, double plusy)
    {
        v.x += plusx;
        v.y += plusy;
        return v;
    }

    // MIDPOINT
    Vector2 Vector2::midpoint(Vector2 pos)
    {
        double mx = (x + pos.x) / 2;
        double my = (y + pos.y) / 2;
        Vector2 mid(mx, my);
        return mid;
    }

    Vector2 midpoint(Vector2 vector1, Vector2 vector2)
    {
        double mx = (vector1.x + vector2.x) / 2;
        double my = (vector1.y + vector2.y) / 2;
        Vector2 mid(mx, my);
        return mid;
    }

    // PERCENT DISTANCE
    double Vector2::percentDistance(Vector2 pos, double percentOfDistance)
    {
        return distanceTo(pos) / (100 / percentOfDistance);
    }

    double percentDistance(Vector2 vector1, Vector2 vector2, double percentOfDistance)
    {
        double distance = sqrt((vector2.y - vector1.y) * (vector2.y - vector1.y) + (vector2.x - vector1.x) * (vector2.x - vector1.x));
        return distance / (100 / percentOfDistance);
    }

    // NEW VECTOR3
    Vector3::Vector3(double inx, double iny, double inz)
    {
        x = inx;
        y = iny;
        z = inz;
    }

    double Vector3::distanceTo(Vector3 pos)
    {
        return sqrt((pos.y - y) * (pos.y - y) + (pos.x - x) * (pos.x - x) + (pos.z - z) * (pos.z - z));
    }

    void Vector3::vectorMovement(double plusx, double plusy, double plusz)
    {
        x += plusx;
        y += plusy;
        z += plusz;
        return;
    }

    Vector3 Vector3::midpoint(Vector3 pos)
    {
        double mx = (x + pos.x) / 2;
        double my = (y + pos.y) / 2;
        double mz = (z + pos.z) / 2;
        Vector3 mid(mx, my, mz);
        return mid;
    }
}
