#include <GL/glut.h>
#include <cmath>


class OpenGlFunctions
{
    public:
        static void drawRectangle(float x1, float y1, float x2, float y2)
        {
            glBegin(GL_POLYGON);
            glVertex2f(x1, y1);
            glVertex2f(x2, y1);
            glVertex2f(x2, y2);
            glVertex2f(x1, y2);
            glEnd();
        }


        static void drawTriangle(float b, float h, float w)
        {
            glBegin(GL_TRIANGLES);
            glVertex2f(b, b);
            glVertex2f(-w, h);
            glVertex2f(w, h);
            glEnd();
        }


        static void drawTriangle(float px1, float py1, float px2, float py2, float px3, float py3)
        {
            glBegin(GL_TRIANGLES);
            glVertex2f(px1, py1);
            glVertex2f(px2, py2);
            glVertex2f(px3, py3);
            glEnd();
        }


        static void drawPolygon(float centerX, float centerY, float size, int numSides) 
        {
            glBegin(GL_POLYGON);
            for (int i = 0; i < numSides; ++i) {
                float angle = 2.0 * M_PI * static_cast<float>(i) / numSides;
                float x = centerX + size * cos(angle);
                float y = centerY + size * sin(angle);
                glVertex2f(x, y);
            }
            glEnd();
        }


        static void drawCircle(float centerX, float centerY, float radius) 
        {
            int sides = 200;
            glBegin(GL_POLYGON);
            for (int i = 0; i < sides; ++i) {
                float angle = 2.0 * M_PI * static_cast<float>(i) / sides;
                float x = centerX + radius * cos(angle);
                float y = centerY + radius * sin(angle);
                glVertex2f(x, y);
            }
            glEnd();
}
};
