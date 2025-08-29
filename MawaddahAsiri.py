import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Initial window size
width, height = 800, 600

# Ship position along the x-axis
ship_pos_x = 0.0

# Default sky color
sky_color = [0.8, 0.85, 0.85]

# Function to draw buildings in the background
def draw_buildings():
    # Building 1 - Leftmost greenish building
    glColor3f(0.5, 0.8, 0.7)
    glBegin(GL_QUADS)
    glVertex2f(-1.0, -0.1)
    glVertex2f(-0.75, -0.1)
    glVertex2f(-0.75, 0.14)
    glVertex2f(-1.0, 0.14)
    glEnd()

    # Building 2 - Pink building
    glColor3f(1.0, 0.8, 0.86)
    glBegin(GL_QUADS)
    glVertex2f(-0.75, -0.1)
    glVertex2f(-0.2, -0.1)
    glVertex2f(-0.2, 0.29)
    glVertex2f(-0.75, 0.29)
    glEnd()

    # Building 3 - Orange tall building
    glColor3f(1.0, 0.0, 0.5)
    glBegin(GL_QUADS)
    glVertex2f(-0.2, -0.1)
    glVertex2f(0.1, -0.1)
    glVertex2f(0.1, 0.5)
    glVertex2f(-0.2, 0.5)
    glEnd()

    # Building 4 - Light blue building
    glColor3f(0.68, 0.85, 0.9)
    glBegin(GL_QUADS)
    glVertex2f(0.1, -0.1)
    glVertex2f(0.7, -0.1)
    glVertex2f(0.7, 0.20)
    glVertex2f(0.1, 0.20)
    glEnd()

    # Building 5 - Rightmost greenish building
    glColor3f(0.5, 0.8, 0.7)
    glBegin(GL_QUADS)
    glVertex2f(0.7, -0.1)
    glVertex2f(1.0, -0.1)
    glVertex2f(1.0, 0.11)
    glVertex2f(0.7, 0.11)
    glEnd()

    # Navy line at the bottom of all buildings
    glColor3f(0.2, 0.3, 0.5)
    glBegin(GL_QUADS)
    glVertex2f(-1.0, -0.1)
    glVertex2f(1.0, -0.1)
    glVertex2f(1.0, -0.12)
    glVertex2f(-1.0, -0.12)
    glEnd()

# Function to draw the sea
def draw_sea():
    # Main sea area
    glColor3f(0.4, 0.6, 0.65)
    glBegin(GL_QUADS)
    glVertex2f(-1.0, -0.12)
    glVertex2f(1.0, -0.12)
    glVertex2f(1.0, -1.0)
    glVertex2f(-1.0, -1.0)
    glEnd()

    # Waves on the sea
    glColor3f(1.0, 1.0, 1.0)
    # Wave 1 - Left side
    glBegin(GL_LINES)
    glVertex2f(-0.9, -0.5)
    glVertex2f(-0.7, -0.5)
    glEnd()
    # Wave 2 - Right side
    glBegin(GL_LINES)
    glVertex2f(0.7, -0.5)
    glVertex2f(0.9, -0.5)
    glEnd()
    # Wave 3 - Middle
    glBegin(GL_LINES)
    glVertex2f(0.0, -0.3)
    glVertex2f(0.2, -0.3)
    glEnd()
    # Wave 4 - Lower middle
    glBegin(GL_LINES)
    glVertex2f(0.0, -0.65)
    glVertex2f(0.2, -0.65)
    glEnd()

# Function to draw the sun in the top-right corner
def draw_sun():
    glColor3f(1.0, 0.9, 0.2)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0.90, 0.90)  # Center of the sun
    radius = 0.1
    # Draw sun using a circle approximation
    for angle in range(0, 361, 10):
        rad = math.radians(angle)
        x = 0.85 + math.cos(rad) * radius
        y = 0.85 + math.sin(rad) * radius
        glVertex2f(x, y)
    glEnd()

# Function to draw a cloud at a given position and scale
def draw_cloud(x, y, scale):
    glColor3f(1.0, 1.0, 1.0)
    radius = 0.05 * scale
    # Draw overlapping circles to form the cloud
    for dx in [-0.05, -0.025, 0, 0.025, 0.05]:
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(x + dx, y)
        for angle in range(0, 361, 10):
            rad = math.radians(angle)
            cx = x + dx + math.cos(rad) * radius
            cy = y + math.sin(rad) * radius
            glVertex2f(cx, cy)
        glEnd()

# Function to draw the ship
def draw_ship():
    global ship_pos_x

    # Apply ship's movement translation
    glPushMatrix()
    glTranslatef(ship_pos_x, 0.0, 0.0)

    # Ship base
    glColor3f(0.2, 0.3, 0.5)
    glBegin(GL_QUADS)
    glVertex2f(0.32, -0.4)
    glVertex2f(0.68, -0.4)
    glVertex2f(0.65, -0.46)
    glVertex2f(0.35, -0.46)
    glEnd()

    # Left sail
    glColor3f(0.2, 0.3, 0.5)
    glBegin(GL_TRIANGLES)
    glVertex2f(0.495, -0.13)
    glVertex2f(0.35, -0.4 + 0.02)
    glVertex2f(0.495, -0.4 + 0.02)
    glEnd()

    # Right sail
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(0.505, -0.13)
    glVertex2f(0.65, -0.4 + 0.02)
    glVertex2f(0.505, -0.4 + 0.02)
    glEnd()

    glPopMatrix()

# Main display function
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    # Set the sky color
    glClearColor(*sky_color, 1.0)

    # Draw all elements
    draw_buildings()
    draw_sea()
    draw_sun()
    draw_ship()
    draw_cloud(-0.7, 0.8, 1.0)  # Cloud 1
    draw_cloud(0.0, 0.85, 0.8)  # Cloud 2
    draw_cloud(0.5, 0.75, 0.9)  # Cloud 3
    glFlush()

# Handle keyboard inputs for ship movement
def keyboard(key, x, y):
    global ship_pos_x
    key = key.decode('utf-8')
    if key == 'l' or key == 'L':  # Move left
        ship_pos_x -= 0.05
    elif key == 'r' or key == 'R':  # Move right
        ship_pos_x += 0.05
    glutPostRedisplay()

# Handle sky color changes through the menu
def sky_menu(option):
    global sky_color
    if option == 1:
        sky_color = [1.0, 0.6, 0.7]  # Pink
    elif option == 2:
        sky_color = [1.0, 0.7, 0.4]  # Orange
    elif option == 3:
        sky_color = [0.75, 0.85, 0.95]  # Original
    glutPostRedisplay()

# Handle main menu actions
def main_menu(option):
    if option == 0:  # Exit
        sys.exit(0)

# Create the menu system
def create_menu():
    submenu = glutCreateMenu(sky_menu)
    glutAddMenuEntry("Sunset Pink", 1)
    glutAddMenuEntry("Orange", 2)
    glutAddMenuEntry("Original Color", 3)

    menu = glutCreateMenu(main_menu)
    glutAddSubMenu("Sky Color", submenu)
    glutAddMenuEntry("Exit", 0)
    glutAttachMenu(GLUT_RIGHT_BUTTON)

# Initialize OpenGL settings
def init():
    glClearColor(*sky_color, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

# Main function to set up the program
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"Mawaddah Asiri_2306042_IAR")
    init()
    create_menu()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()


