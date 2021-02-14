# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 22:12:42 2021

@author: Zhong
"""

import time
import turtle as t

def drawLine(draw):
    t.penup()
    t.fd(10)
    t.pendown() if draw else t.penup() 
    t.fd(40)
    t.penup()
    t.fd(10)
    t.right(90)

def drawDigit(digit):
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [1,3,4,5,6,7,8,9,0] else drawLine(False)
    drawLine(True) if digit in [2,3,5,6,8,9,0] else drawLine(False)
    drawLine(True) if digit in [2,6,8,0] else drawLine(False)
    t.left(90)
    drawLine(True) if digit in [4,5,6,8,9,0] else drawLine(False)
    drawLine(True) if digit in [2,3,5,6,7,8,9,0] else drawLine(False)
    drawLine(True) if digit in [1,2,3,5,7,8,9,0] else drawLine(False)
    t.left(180)
    t.penup()
    t.fd(60)
    
def drawDate(date):
    for i in date:
        if i == '-':
            t.write("年",font=("Arial",54,"normal"))
            t.fd(120)
            t.pencolor("green")
        elif i == '=':
            t.write("月",font=("Arial",54,"normal"))
            t.fd(120)
        elif i == '+':
            t.write("日",font=("Arial",54,"normal"))
            t.fd(120)
        else:
            drawDigit(eval(i))


def main():
    t.pencolor("red")
    t.setup(800,400,200,200)
    t.speed(1000)
    t.hideturtle()
    t.penup()
    t.fd(-600)
    t.pensize(10)
    drawDate(time.strftime("%Y-%m=%d+",time.gmtime()))
    t.done()
    
main()



    
    