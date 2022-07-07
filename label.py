from turtle import Turtle

class Label:
    def __init__(self):
        pass


    def create_label(self, position, state_label):
        new_label = Turtle()
        new_label.hideturtle()
        new_label.penup()
        new_label.goto(position)
        new_label.write(f'{state_label}')

    
