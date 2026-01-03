import turtle
p=turtle.Turtle()
p.shape("turtle")
p.penup()
p.goto(300,100)
p1=p.clone()
p1.goto(-700,-300)
p1.pendown()
p1.fd(1500)
p2=p.clone()
p2.goto(200,100)
p3=p2.clone()
p3.goto(100,100)
p4=p3.clone()
p4.goto(0,100)
p5=p4.clone()
p5.goto(-100,100)
p6=p5.clone()
p6.goto(-200,100)
p.color("red")
p.rt(90)
p2.color("yellow")
p2.rt(90)
p3.color("black")
p3.rt(90)
p4.color("orange")
p4.rt(90)
p5.color("blue")
p5.rt(90)
p6.color("pink")
p6.rt(90)
import random
for i in range(150):
    p.fd(random.randint(1,5))
    p2.fd(random.randint(1,5))
    p3.fd(random.randint(1,5))
    p4.fd(random.randint(1,5))
    p5.fd(random.randint(1,5))
    p6.fd(random.randint(1,5))
    
    
    





