import enum
import turtle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

class Direction(enum.Enum):
  Up = 90
  Down = 270
  Left = 180
  Right = 0

def draw_score(pen: turtle.Turtle):
  pen.penup()
  pen.goto((-(SCREEN_WIDTH/2)+10, (SCREEN_HEIGHT/2)-40))
  pen.pencolor("white")
  pen.pendown()
  pen.write("SCORE: ", font=("Arial", 24, "bold"))


def main():
  # Set up screen 
  wn = turtle.Screen()
  wn.title("Snake Game")
  wn.bgcolor("blue")
  wn.setup(width=SCREEN_WIDTH, height=SCREEN_WIDTH)
  wn.tracer(0,0) #turns off tracer updates

  # Scoring turtle
  pen = turtle.Turtle()
  draw_score(pen)

  
  # Snake Head
  head = turtle.Turtle()
  head.speed(0)
  head.shape("square")
  head.color("white")
  head.penup()
  head.goto(0,0)
  # head.setheading(Direction.Up)


  # turtle.setpos()

  # Keeps the window open
  turtle.done()
  

if __name__ == "__main__":
  main()
  # input()



