import turtle as t # turtle이 기니까 이제 t로 부르겠다

class MagicBrush:
    t.color('blue')
    def draw_square(self):
        for i in range(4):
            t.forward(100)
            t.right(90)

    def draw_triangle(self):
        for i in range(3):
            t.forward(100)
            t.right(120)
    
    def go(self):
        t.forward(200)

    def turn(self):
        t.right(90)


# m1 = MagicBrush() # MagicBrush를 만든다
# m2 = MagicBrush()

brad = t.Turtle()
brad.shape('turtle')
brad.speed(2)
brad.forward(100)

# m1.go()
# m2.turn()
# m1.turn()
# m1.go()
# m2.go()

# m2.draw_triangle()
# m1.draw_square()

# m2.draw_square
# m1.draw_triangle





t.mainloop()