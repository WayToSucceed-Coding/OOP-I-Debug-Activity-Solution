import turtle

# Define a class to create a dynamic flower
class Flower:
    def __init__(self, num_petals, petal_length, color):
        self.t = turtle.Turtle()
        self.t.speed(10)

    def draw_petal(self):
        for _ in range(2):
            self.t.forward(self.petal_length)
            self.t.left(60)
            self.t.forward(self.petal_length)
            self.t.left(120)

    def draw_flower(self):
        self.t.color(self.color)
        for _ in range(self.num_petals):
            self.draw_petal()
            self.t.left(360 / self.num_petals)

    def change_color(self, new_color):
        self.color = new_color
        self.t.color(self.color)  # Set the new color
        self.draw_flower()

    def set_number_of_petals(self, new_num_petals):
        self.num_petals = new_num_petals
        self.draw_flower()  # Redraw the flower with the new number of petals

# Create a Flower object
flower = Flower(6, 80, "red")
flower.draw_flower()


change_color("yellow")  
set_number_of_petals(8) 

# End the turtle program
turtle.done()
