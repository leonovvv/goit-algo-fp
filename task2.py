import turtle
import math

# Function to draw the Pythagoras Tree
def draw_pythagoras_tree(t, branch_length, level):
    if level == 0:
        return

    # Draw the main branch
    t.forward(branch_length)
    
    # Draw the left branch
    t.left(45)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1)

    # Return to the main branch
    t.right(45)
    t.forward(branch_length * math.sqrt(2) / 2)
    
    # Draw the right branch
    t.right(45)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1)

    # Return to the main branch
    t.left(45)
    t.backward(branch_length * math.sqrt(2) / 2)
    t.backward(branch_length)

# Function to set up the Turtle graphics
def pythagoras_tree(level):
    screen = turtle.Screen()
    screen.title("Pythagoras Tree Fractal")
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)  # Point the turtle upwards
    t.penup()
    t.setpos(0, -200)  # Move the turtle to the starting position
    t.pendown()
    
    draw_pythagoras_tree(t, 100, level)
    
    screen.mainloop()

# Get the recursion level from the user
if __name__ == "__main__":
    level = int(input("Enter the recursion level for the Pythagoras Tree: "))
    pythagoras_tree(level)