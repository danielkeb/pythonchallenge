import turtle

def display_coordinates(x, y):
    print(f"Clicked at coordinates - X: {x}, Y: {y}")

screen = turtle.Screen()
screen.title("Click Event Example")

# Set up the screen size
screen.setup(width=500, height=500)

# Register the display_coordinates function to be called on screen click
turtle.onscreenclick(display_coordinates)

# Keep the window open
turtle.mainloop()
