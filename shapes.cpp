#include <GL/glut.h>
#include "OpenGlFunctions.cpp"


void drawHourglass() {
    glClear(GL_COLOR_BUFFER_BIT);


    // Draw the first triangle
    glColor3f(1.0f, 1.0f, 1.0f);


    //Draw upper triangle
    OpenGlFunctions::drawTriangle(0.0f, 0.5f, 0.25f);


    //Draw lower triangle
    glColor3f(1.0f, 1.0f, 1.0f);
    OpenGlFunctions::drawTriangle(0.0f, -0.5f, 0.25f);


    glFlush();
}


void drawLetter()
{
    glClear(GL_COLOR_BUFFER_BIT);


    glColor3f(0.0f, 0.0f, 1.0f);


    // Draw main vertical bar of 'F'
    OpenGlFunctions::drawRectangle(0.0f, 0.0f, 0.07f, 0.9f);


    // Draw top horizontal bar of 'F'
    OpenGlFunctions::drawRectangle(0.07f, 0.9f, 0.5f, 0.8f);


    // Draw bottom horizontal bar of 'F'
    OpenGlFunctions::drawRectangle(0.07f, 0.6f, 0.5f, 0.5f);


    glFlush();
}


void drawHexagon()
{
    glClear(GL_COLOR_BUFFER_BIT);


    glColor3f(0.0f, 1.0f, 0.0f);


    OpenGlFunctions::drawPolygon(0.0f, 0.0f, 0.5f, 6);


    glFlush();
}


void drawArrow()
{
    glClear(GL_COLOR_BUFFER_BIT);


    glColor3f(0.0f, 1.0f, 0.0f);


    OpenGlFunctions::drawTriangle(0.0f, 0.3f, 0.3f, 0.3f, 0.4f, 0.5f);
    OpenGlFunctions::drawTriangle(0.0f, 0.3f, 0.3f, 0.3f, 0.4f, 0.1f);


    glFlush();
}

void drawUnevenTriangle()
{
    glClear(GL_COLOR_BUFFER_BIT);


    glColor3f(0.0f, 1.0f, 0.0f);


    OpenGlFunctions::drawTriangle(0.0f, 0.0f, 0.7f, 0.5f, 0.5f, 0.7f);


    glFlush();
}


void drawCircleShape()
{
    glClear(GL_COLOR_BUFFER_BIT);


    glColor3f(0.0f, 1.0f, 0.0f);


    OpenGlFunctions::drawCircle(0.0f, 0.0f, 0.5f);


    glFlush();
}


void reshape(int width, int height) {
    glViewport(0, 0, width, height);
}


int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(800, 800);
    glutCreateWindow("OpenGL Shapes");


    glutDisplayFunc(drawHourglass);
    glutReshapeFunc(reshape);


    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);


    glutMainLoop();
    return 0;
}
