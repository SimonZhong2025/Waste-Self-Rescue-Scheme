# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 12:34:15 2021

@author: Zhong
"""

import turtle, time

def drawLine(draw):
    turtle.penup()
    turtle.fd(10)
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    turtle.penup()
    turtle.fd(10)
    turtle.right(90)
    
def drawDigit(digit):
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
    
def drawDate(date):
    turtle.pencolor("red")
    for i in date:
        if  i == '-':
            turtle.pencolor("green")
            turtle.write("年",font=("Arial", 18, "normal"))
            turtle.fd(40)
        elif i == '=':
            turtle.write("月",font=("Arial", 18, "normal"))
            turtle.fd(40)
        elif i == '+':            
            turtle.write("日",font=("Arial", 18, "normal"))
            turtle.fd(40)
        else:
            drawDigit(eval(i))
        
def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate(time.strftime("%Y-%m=%d+",time.gmtime()))
    turtle.hihdeturtle()
    turtle.done()
    
main()


    