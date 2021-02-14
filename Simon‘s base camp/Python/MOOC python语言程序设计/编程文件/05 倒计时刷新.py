# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 23:25:49 2021

@author: Zhong
"""

import time
import turtle as t

start = time.perf_counter()

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

def drawPaint(paint):
    a = eval (paint)
    for i in range(a):
        drawDigit(a-i)
        global start
        dur = time.perf_counter() - start #如何确保证倒计时就是一秒钟呢？用turtle.write？
        print("{:.2f}",format(dur))
        time.sleep(0.7)
        t.clear()
        t.goto(0,0)
    drawDigit(0)
    t.clear()
    t.goto(0,0)
    
def main():
    t.hideturtle()
    t.pencolor("red")
    t.speed(1000)
    t.pensize(10)
    t.penup()
    t.goto(0,0)
    drawPaint(input("请输入一个数字"))
    t.setup(800,400,200,200)
    t.done()
    
main()