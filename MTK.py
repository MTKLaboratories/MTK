#Imports required modules.
from math import *
import turtle
import sys
import os
import tkinter
 
#Defines mathematical constants.
phi=(1+sqrt(5))/2
 
#Defines variables used in the program.
loop = 1
r = 1
 
#Version.
version = "0.03"
 
#Defines list of commands.
commands = ["whileloop","ifloop","display","sqrt","cbrt","absolutevalue","sine","cosine","tangent","arcsine","arccosine","arctangent",
"mean","psdeviation","ssdeviation","plot","barplot","scatterplot"]
 
#Defines aliases.
aliases = {'whileloop':['whileloop','while'],
           'ifloop':['ifloop','if'],
           'display':['display','di'],
           'sqrt':['sqrt','sq'],
           'cbrt':['cbrt','cb'],
           'absolutevalue':['absolutevalue','abs'],
           'sine':['sine','sin'],
           'cosine':['cosine','cos'],
           'tangent':['tangent','tan'],
           'arcsine':['arcsine','asin'],
           'arccosine':['arccosine','acos'],
           'arctangent':['arctangent','atan'],
           'mean':['mean','mn'],
           'psdeviation':['psdeviation','psd'],
           'ssdeviation':['ssdeviation','ssd'],
           'plot':['plot','plt'],
           'iplot':['plot','iplt'],
           'barplot':['barplot','bplt'],
           'scatterplot':['scatterplot','splt'],
           }
 
#Loops
def whileloop(arg):
  commands = ""
  count = 0
  while 1:
    inpt = input("\033[91m|\033[0m ").replace('print("','print("\033[91m\\\033[0m ",')
    if inpt != "end":
      if count == 0:
        commands = commands + inpt
      else:
        commands = commands + inpt + ";"
    else:
      break
  while arg.split("=")[0]==arg.split("=")[1]:
    eval(commands)
     
def ifloop(arg):
  commands = ""
  count = 0
  while 1:
    inpt = input("\033[91m|\033[0m ").replace('print("','print("\033[91m\\\033[0m ",')
    if inpt != "end":
      if count == 0:
        commands = commands + inpt
      else:
        commands = commands + inpt + ";"
    else:
      break
  if arg.split("=")[0]==arg.split("=")[1]:
    eval(commands)
 
#Loads add-ons in /Addons.
if len(os.listdir("Addons"))>2:
  import importlib
  sys.path.append('/Addons')
  for item in os.listdir("Addons"):
    if item!="__init__.py":
      if item!=".DS_Store":
        name=item.replace(".py","")
        commands.append(name)
        aliases[name]=[name,name[:2]]
        exec("from Addons."+name+" import *",globals(),globals())
 
#Used in plot.
def drange(x, y, jump):
  while x < y:
    yield x
    x += jump
 
#Used for sets.
def intset(arg):
  returnset=[]
  for item in arg:
    returnset.append(float(item))
  return returnset
 
#Display
 
def display(arg):
  if "+-" in arg:
    print(eval(arg.replace("+-","+"),globals()))
    print(eval(arg.replace("+-","-"),globals()))
  else:
    return eval(arg,globals())
 
#Roots
 
def sqrt(arg):
  return float(arg)**(1/2)
 
def cbrt(arg):
  return float(arg)**(1/3)
 
#Trigonometric Functions
def sine(arg):
  a=eval(str(arg),globals())
  global r
  if r==0:
    a=radians(a)
  else:
    0
 
  return sin(a)
 
def cosine(arg):
  return sine(arg+"+pi/2")
 
def tangent(arg):
    a=eval(str(arg),globals())
    global r
    if r==0:
        a=radians(a)
    else:
        0
    return tan(a)
 
def arcsine(arg):
    a=eval(str(arg),globals())
    global r
    if r==0:
        a=radians(a)
    else:
        0
    return asin(a)
 
def arccosine(arg):
    a=eval(str(arg),globals())
    global r
    if r==0:
        a=radians(a)
    else:
        0
    return acos(a)
 
def arctangent(arg):
    a=eval(str(arg),globals())
    global r
    if r==0:
        a=radians(a)
    else:
        0
    return atan(a)
 
#Definitions
def define(arg):
    arg2=arg
    arg.replace(";","")
    define = arg.split()
    if len(define[1]) == 1:
        try:
            if "{" in arg:
              exec(define[1]+"="+define[2].replace("{","(").replace("}",")"),globals(),globals())
            else:
              exec(define[1]+"="+define[2],globals(),globals())
        except:
            0
    else:
        if "(" in arg:
            try:
                var = define[1][2]
                exec("""def """+define[1][0]+"""("""+var+"""):
                    return """+define[2]+"""""",globals(),globals())
                 
            except:
                0
 
#Statistics
def listcompute(arg):
    values = arg.split(",")
    new_list = []
    for item in values:
        new_list.append(eval(item,globals()))
    return new_list
     
def mean(arg):
    values = listcompute(arg)
    return sum(values)/len(values)
     
def psdeviation(arg):
    values = listcompute(arg)
    mean = sum(values)/len(values)
    new_list = []
    for item in values:
        new_list.append((item-mean)**2)
    mean2 = sum(new_list)/len(new_list)
    return mean2**(1/2)
     
def ssdeviation(arg):
    values = listcompute(arg)
    mean = sum(values)/len(values)
    new_list = []
    for item in values:
        new_list.append((item-mean)**2)
    mean2 = sum(new_list)/(len(new_list)-1)
    return mean2**(1/2)
#Number Theory
def absolutevalue(arg):
    return abs(arg)
 
#Plotting
def cnotch(mx):
    size = 0
    while size < mx:
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(10)
        turtle.right(180)
        turtle.forward(20)
        turtle.left(180)
        turtle.forward(10)
        turtle.right(90)
        size = size+50
 
def ccoords(s1,s2):
    turtle.right(90)
    cnotch(s2)
    turtle.left(180)
    turtle.goto(0,0)
    cnotch(s2)
    turtle.right(90)
    turtle.goto(0,0)
    cnotch(s1)
    turtle.left(180)
    turtle.goto(0,0)
    cnotch(s1)
     
 
def point(x,y):
    turtle.penup()
    turtle.goto(x+1,y-1)
    turtle.pendown()
    turtle.goto(x+1,y+1)
    turtle.goto(x-1,y+1)
    turtle.goto(x-1,y-1)
    turtle.goto(x+1,y-1)
    turtle.penup()
     
def plot(arg):
  wn = turtle.Screen()
  wn.bgcolor('white')
  turtle.title("MTK")
  turtle.tracer(0)
  ccoords(turtle.window_width()/2,turtle.window_height()/2)
  turtle.goto(turtle.window_width()/-2,0)
  for x in drange(turtle.window_width()/-2,turtle.window_width()/2,0.1):
    turtle.goto(x*50,eval(arg.replace("x",str(x))+"*50"))
  turtle.update()
  wn.exitonclick()
 
def iplot(arg):
  wn = turtle.Screen()
  wn.bgcolor('white')
  turtle.title("MTK")
  turtle.tracer(0)
  ccoords(turtle.window_width(),turtle.window_height())
  for x in range(-500,500):
    for y in range(-500,500):
      sides = arg.split("=")
      if eval(sides[0],globals()) == eval(sides[1],globals()):
        turtle.goto(x,y)
  turtle.update()
  wn.exitonclick()
 
     
def barplot(arg):
    sarg = intset(arg.split(","))
    absarg = []
    for item in sarg:
        absarg.append(abs(item))
    c = 50
    wn = turtle.Screen()
    wn.bgcolor('white')
    turtle.title("MTK")
    turtle.hideturtle()
    turtle.tracer(0)
    windowwidth = turtle.window_width()-5
    turtle.forward((windowwidth/2)-5)
    turtle.left(180)
    turtle.forward(windowwidth)
    turtle.right(90)
    num = len(sarg)
    barsize = windowwidth/num
    if max(absarg)*50 >= (turtle.window_height()/2)-5:
        c = ((turtle.window_height()/2)-5)/(max(absarg))
    for item in sarg:
        turtle.forward(item*c)
        turtle.right(90)
        turtle.forward(barsize)
        turtle.right(90)
        turtle.forward(item*c)
        turtle.left(180)
    turtle.update()
    wn.exitonclick()
 
def scatterplot(arg):
    c = 50
    x = 0
    turtle.hideturtle()
    turtle.tracer(0)
    sarg = arg.split(",")
    xvallist = []
    yvallist = []
    for item in sarg:
        xvallist.append(float(item.split(":")[0]))
        yvallist.append(float(item.split(":")[1]))
    wn = turtle.Screen()
    wn = turtle.Screen()
    wn.bgcolor('white')
    turtle.title("MTK")
    turtle.speed(1000000)
    ccoords(turtle.window_width(),turtle.window_height())
    turtle.goto(0,0)
    if max(xvallist)*c > turtle.window_height()/2:
        c = ((turtle.window_height()/2)-5)/max(xvallist)
    if max(yvallist)*c > turtle.window_height()/2:
        c = ((turtle.window_width()/2)-5)/max(yvallist)
    turtle.goto(0,0)
    for x in range(0,len(xvallist)):
        point(xvallist[x]*50,yvallist[x]*50)
    turtle.update()
    wn.exitonclick()
     
     
         
def checkfor(parsed_input, cmd):
  if parsed_input[0] in aliases[cmd]:
    try:
      if "loop" or "plot" in cmd:
        eval(cmd+"(parsed_input[1])")
        print("\033[91m\\\033[0m "+cmd+" "+parsed_input[1].replace("("," ").replace(")"," ")+" ")
         
      else:
        print("\033[91m\\\033[0m "+str(eval(cmd+"(' '.join(parsed_input[1:]))")))
    except ZeroDivisionError:
      print("\033[91m\\ Error: Division by 0.\033[0m")
    except NameError:
      print("\033[91m\\ Error: 1 or more variables/functions not defined.\033[0m")
    except IndexError:
      print("\033[91m\\ Error: Incorrect syntax.\033[0m")
 
def evalu(input):
    global loop
    parsed_input = input.replace("^","**").replace("√","sqrt").replace("π","pi").replace("Φ","phi")
    count = 0
    count2 = 1
    for char in parsed_input:
        if char == "|":
            if count%2 == 0:
                parsed_input = parsed_input.replace("|","abs(",1)
                count +=1
            else:
                parsed_input = parsed_input.replace("|",")",1)
                count +=1
        if char == " ":
            if count2%2 == 0:
                parsed_input = parsed_input.replace(" ","(",1)
                count2 +=1
            else:
                parsed_input = parsed_input.replace(" ",")",1)
                count2 +=1
    parsed_input = parsed_input.replace(")"," ",1)
    countopen = 0
    countclosed = 0
    for char in parsed_input:
      if char == "(":
        countopen += 1
      if char == ")":
        countclosed += 1
    parsed_input=parsed_input+")"*(countopen-countclosed)
    parsed_input = parsed_input.split()
    for str in commands:
        checkfor(parsed_input,str)
    if parsed_input[0] == "quit":
      loop = 0
 
def launch():
  global ent
  global inpt
  global window
  inpt = ent.get()
  window.destroy()
#Sets up launch window.
window = tkinter.Tk()
tkinter.Label(window, text="MTK").pack()
tkinter.Label(window, text="Directory:").pack()
ent = tkinter.Entry(window)
btn = tkinter.Button(window, text="Launch", command=launch)
ent.pack()
btn.pack()
window.title("MTK")
window.mainloop()
 
#Checks if input is empty, and if it is, runs terminal.
if inpt == "":
    while loop==1:
      try:
        evalu(input("\033[91m/\033[0m "))
      except:
        print("\033[91m\\ Error: Incorrect Syntax.\033[0m")
else:
    file = open(inpt,"r")
    for line in file:
        evalu(line)
    file.close()
    
