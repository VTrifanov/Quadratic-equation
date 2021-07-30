import tkinter as tk


canvas_h = 650
canvas_w = 800
#x_left = -4
#x_right = 4
#y_top = 4
#y_bottom = -4
#dx = canvas_w / (x_right-x_left)    #цена пикселя по х
#dy = canvas_h / (y_top-y_bottom)    #цена пикселя по y

def main(a=1, b=0, c=0, x_left=-4, x_right=4, y_bottom=-4, y_top=4):
    global canvas, list_x_old, list_y_old
    dx = canvas_w / (x_right - x_left)  # цена пикселя по х
    dy = canvas_h / (y_top - y_bottom)  # цена пикселя по y

    window2 = tk.Tk()
    canvas = tk.Canvas(window2, width=canvas_w, height=canvas_h, bg='#012')
    canvas.pack()
    window2.title('холст')
    window2.geometry(f'{canvas_w}x{canvas_h}+200+10')

    oxes(x_left, x_right, y_top, y_bottom, dx, dy)
    list_x_old = list_x(x_left, x_right)               #список координат х в обычной системе координат (не canvas)
    list_y_old = list_y(a, b, c, x_left, x_right)
    draw_graf(x_left, y_top, dx, dy)
    window2.mainloop()

def oxes(x_left, x_right, y_top, y_bottom, dx, dy):
    cx = -x_left*dx
    cy = y_top*dy
    canvas.create_line(0, cy, canvas_w, cy, fill="white")
    canvas.create_line(cx, 0, cx, canvas_h, fill="white")
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
def list_x(x_left, x_right):
    list1=[]
    x=x_left
    step=(x_right-x_left) / canvas_w
    while x<=x_right:
        list1.append(x)
        x+=step
    return list1
def list_y(a,b,c, x_left, x_right):
    list2=[]
    for x in list_x(x_left, x_right):
        y=a*x**2+b*x+c
        list2.append(y)
    return list2
def draw_graf(x_left, y_top, dx, dy):
    i=0
    for x in list_x_old:
        x=(x-x_left)*dx
        y=(list_y_old[i]-y_top)*dy
        canvas.create_line(x,-y,x+1,-y, fill='yellow')
        i+=1
