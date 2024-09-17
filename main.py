import turtle, random, time

sc = turtle.Screen()
sc.title("Duck Bread Collector Game")
sc.bgpic("background.gif")
sc.setup(500, 500) 
sc.register_shape("ducky.gif")
sc.register_shape("ducky2.gif")
sc.register_shape("bread.gif")
sc.tracer(0)

tim = turtle.Turtle()
tim.shape("ducky.gif")
tim.penup()

tom = turtle.Turtle()
tom.shape("bread.gif")
tom.penup()
tom.speed(0)
tom.ht()

#functions
score = 0
sk = turtle.Turtle()
sk.ht()
sk.penup()
sk.goto(-220, 220)

def s1():
  #show score
  global score
  f = ("Courier", 15, "bold")
  sk.clear()
  sk.write(f"Score: {score}", align="left", font = f)

def detect_tom():
  global score
  for t in all_tom:
    if tim.distance(t) < 50:
      score += 1
      s1()
      all_tom.remove(t)
      t.ht()
      random_tom()

def go_right():
  tim.shape("ducky2.gif")
  tim.setx(tim.xcor()+10)
  if tim.xcor() > 250:
    tim.setx(-250)
def go_left():
  tim.shape("ducky.gif")
  tim.setx(tim.xcor()-10)
  if tim.xcor() < -250:
    tim.setx(250)
def go_up():
  tim.sety(tim.ycor()+10)
  if tim.ycor() > 250:
    tim.sety(-250)
def go_down():
  tim.sety(tim.ycor()-10)
  if tim.ycor() < -250:
    tim.sety(250)

sc.onkey(go_right, 'Right')
sc.onkey(go_left, 'Left')
sc.onkey(go_up, 'Up')
sc.onkey(go_down, 'Down')
sc.listen()

all_tom = []
def random_tom():
  newtom = tom.clone()
  newtom.st()
  randx = random.randint(-250, 250)
  randy = random.randint(-250, 250)
  newtom.goto(randx, randy)
  all_tom.append(newtom)

for i in range(20):
  random_tom()

#game loop
limit = 31
tTime = turtle.Turtle()
tTime.ht()
tTime.up()
tTime.goto(0, 220)
start_time = time.time()

while (time.time() - start_time) < limit:
  time_elapsed = int(time.time() - start_time)
  tTime.clear()
  tTime.write(f"{time_elapsed}", align = "center", font = ('Courier', 15, "normal"))
  time.sleep(0.05)
  sc.update()
  detect_tom()

#gameover code
sc.onkey(None, "Up")
sc.onkey(None, "Down")
sc.onkey(None, "Left")
sc.onkey(None, "Right")
for t in all_tom:
  t.ht()
tim.ht()
#sc.bgpic("win.gif")
sc.update()