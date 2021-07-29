﻿import tkinter as tk

x_left = -16
canvas_h = 650
canvas_w = 800
x_left = -16
x_right = 16
y_top = 16
y_bottom = -16
dx = canvas_w / (x_right-x_left)    #цена пикселя по х
dy = canvas_h / (y_top-y_bottom)    #цена пикселя по y

def main(a=1, b=0, c=0):
    global canvas, list_x_old, list_y_old
    window2 = tk.Tk()
    canvas = tk.Canvas(window2, width=canvas_w, height=canvas_h, bg='#012')
    canvas.pack()
    window2.title('холст')
    window2.geometry(f'{canvas_w}x{canvas_h}+200+10')

    oxes(x_left, x_right, y_top, y_bottom)
    list_x_old = list_x()               #список координат х в обычной системе координат (не canvas)
    list_y_old = list_y(a, b, c)
    draw_graf()
    window2.mainloop()

def oxes(x_left, x_right, y_top, y_bottom):
    cx = -x_left*dx
    cy = y_top*dy
    canvas.create_line(0, cy, canvas_w, cy, fill="white")
    canvas.create_line(cx, 0, cx, canvas_h, fill="white")
    print(cy, canvas_w, cy)
    x_step = (x_right - x_left) / 8
    x = x_left + x_step
    while x < x_right:
        x_canvas = (x-x_left)*dx
        canvas.create_line(x_canvas, cy-5, x_canvas, cy+5, fill="white")
        canvas.create_text(x_canvas, cy+15, text=str(round(x, 1)), fill='white')
        x += x_step
    y_step = (y_top - y_bottom) / 8
    y = y_top - y_step
    while y > y_bottom:
        y_canvas = (y-y_top)*dy
        canvas.create_line(cx-5, -y_canvas, cx+5, -y_canvas, fill="white")
        canvas.create_text(cx+15, -y_canvas, text=str(round(y, 1)), fill='white')
        y -= y_step
def list_x():
    list1=[]
    x=x_left
    step=(x_right-x_left) / canvas_w
    while x<=x_right:
        list1.append(x)
        x+=step
    return list1
def list_y(a,b,c):
    list2=[]
    for x in list_x():
        y=a*x**2+b*x+c
        list2.append(y)
    return list2
def draw_graf():
    i=0
    for x in list_x_old:
        x=(x-x_left)*dx
        y=(list_y_old[i]-y_top)*dy
        canvas.create_line(x,-y,x+1,-y, fill='yellow')
        i+=1
