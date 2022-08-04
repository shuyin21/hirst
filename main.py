# import colorgram
#
# colors = colorgram.extract('hirst.jpg', 30)
# rgb_colors = []
#
# for color in colors:
#     my_colors = (color.rgb.r, color.rgb.g, color.rgb.b)
#     rgb_colors.append(my_colors)
#
# print(rgb_colors)

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
colors = [(199, 175, 117), (124, 36, 24), (168, 106, 57), (186, 158, 53), (6, 57, 83), (109, 67, 85),
          (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53),
          (181, 96, 79),
          (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177),
          (176, 198, 203),
          (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]


def random_color():
    color = random.choice(colors)
    r = color[0]
    g = color[1]
    b = color[2]
    return r, g, b


tim.hideturtle()

tim.speed('fastest')
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):

    tim.dot(20, random_color())
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = t.Screen()


screen.exitonclick()
