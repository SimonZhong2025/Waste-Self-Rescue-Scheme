# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 12:34:15 2021

@author: Zhong
"""

import turtle as t
import time

def drawLine(draw):
    t.penup()
    t.fd(10)
    t.pendown() if draw else turtle.penup()
    t.fd(40)
    t.penup()
    t.fd(10)
    t.right(90)
    
def drawDigit(digit):
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    t.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    t.left(180)
    t.penup()
    t.fd(20)
    
def drawDate(date):
    t.pencolor("red")
    for i in date:
        if  i == '-':
            t.pencolor("green")
            t.write("年",font=("Arial", 18, "normal"))
            t.fd(40)
        elif i == '=':
            t.write("月",font=("Arial", 18, "normal"))
            t.fd(40)
        elif i == '+':            
            t.write("日",font=("Arial", 18, "normal"))
            t.fd(40)
        else:
            drawDigit(eval(i))
        
def main():
    t.setup(800,350,200,200)
    t.penup()
    t.fd(-300)
    t.pensize(5)
    drawDate(time.strftime("%Y-%m=%d+",time.gmtime()))
    t.hihdeturtle()
    t.done()
    
main()


    