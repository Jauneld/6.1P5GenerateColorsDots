from browser import document, window, alert
import random 

# VARIABLES */
eyeWidth = 50
eyeHeight = 40
pupilWidth = 22
pupilHeight = 25

#/* SETUP RUNS ONCE */
def setup():
    #sets the screen size
    createCanvas(400, 400) 

  #sets the background color
    background(244,204,204)


# DRAW LOOP REPEATS */
def draw():
    angleMode(DEGREES)
    rectMode(CENTER)

  #Face
    fill(253, 242, 230)
    ellipse(width/2, height/2, 175, 200)
    if (mouseIsPressed):
    #Eyes closed
    fill(0)
    ellipse(170, 170, eyeWidth, eyeHeight/8) 
    ellipse(230, 170, eyeWidth, eyeHeight/8)

    #Mild - Smile
    fill('white')
    arc(200,230,50,50,0,180) 

else:
    #Eyes open
    fill('#7f6000ff')
    ellipse(170, 170, eyeWidth, eyeHeight)
    ellipse(230, 170, eyeWidth, eyeHeight)
    fill(0)
    ellipse(170, 170, pupilWidth, pupilHeight)
    ellipse(230, 170, pupilWidth, pupilHeight)

    #//Mild - Mouth
    fill('#ea9999ff')
    arc(200,230,50,50,0,180)
  

  #Nose
  fill(253, 242, 230)
  triangle(190, 220, 200, 200, 210, 220)

  #//Hair
  fill(0)
  rect(120,240,30,180)
  rect(280,240,30,180)
  arc(245,110,85,85,30,210)
  arc(155,110,85,85,330,150)

  #//Text
  fill(0)
  textSize(15)
  text('“If you only do what you can do, \nyou will never be more than you are now.”', 15,25)
  textSize(12)
  text('- Master Oogway from Kung fu Panda', 15,70)
  #Directions for mouse press
  fill(0)
  textSize(15)
  text('Click to see \nme blink \nand smile.', 300,350)


myp5 = window.p5.new(sketch)
