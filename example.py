import turtle

sc = turtle.Screen()
sc.setup(500, 500)
sc.bgpic("background.gif")
sc.register_shape("ducky.gif")
sc.register_shape("bread.gif")

player = turtle.Turtle()
player.shape("ducky.gif")
player.up()

bread = turtle.Turtle()
bread.shape("bread.gif")
bread.up()
