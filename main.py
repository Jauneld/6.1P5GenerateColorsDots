from browser import document, html, window, alert
import random 

def sketch(pop): 
  #this parameter is needed because it will be the processing sketch itself. This will do things like background color, size, etc. 
  # background(0) instead of pop.background(0)
  def setup():
    pop.createCanvas(1250,500)
    pop.background(0)
    pop.rectMode(pop.CENTER)
    
  def draw():
    colorList = ["#22577a", "#38a3a5", "#57cc99", "#80ed99", "#c7f9cc"]
    pop.noStroke()
    pop.fill(random.choice(colorList))
    pop.ellipse(pop.mouseX,pop.mouseY,50,50)
    
  def mousePressed(user):
    pop.background(0)
  def keyPressed(user):
    if pop.key == " ":
      print("LOL :)")
  pop.setup = setup
  pop.draw = draw
  pop.mousePressed = mousePressed
  pop.keyPressed = keyPressed
  
myp5 = window.p5.new(sketch)
