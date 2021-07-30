import tkinter as tk
import random
import grafic
from fractions import Fraction

intx = (lambda x: int(x) if x == int(x) else x)  # если возможно делаем тип int
floatx = (lambda x: float(x) if float(x) == round(float(x), 12) else x)  # если возможно делаем тип float
revers_sign = (lambda x: '-' if x == '+' else '')


def check_input():  # пытаемся преобразовать коэффициенты из строки в число
    res = []
    a = input_a.get()
    if a == '': a = '0'
    b = input_b.get()
    if b == '': b = '0'
    c = input_c.get()
    if c == '': c = '0'
    for x in (a, b, c):
        try:
            x = Fraction(x)
            x = floatx(x)
            x = intx(x)
            res.append(x)
        except:
            res.append(x)
    return res


def signs_koef(a, b, c):  # определяем знаки коэффициентов, для красивой печати
    if a < 0:
        a_sign = '-'
    else:
        a_sign = ''
    if b < 0:
        b_sign = '-'
    else:
        b_sign = '+'
    if c < 0:
        c_sign = '-'
    else:
        c_sign = '+'
    return (a_sign, b_sign, c_sign)


def calculate():
    global a, b, c, answer
    a, b, c = check_input()
    answer = []
    if type(a) != str and type(b) != str and type(
            c) != str:  # если вместо a,b или c введены не числа, то просим исправить
        a_sign, b_sign, c_sign = signs_koef(a, b, c)
        button2.config(state=tk.NORMAL)
        result.delete('1.0', tk.END)
        result.config(fg='black', font="Arial 20")
        result.insert('1.0', f'получили уравнение:\n{a}x\u00B2{b_sign}{abs(b)}x{c_sign}{abs(c)}=0')
        if a == 0 and b != 0 and c != 0:  # получаем линейное уравнение
            result.insert('3.0', f', а точнее\n{b}x{c_sign}{abs(c)}=0\nэто не квадратное уравнение\nвсё равно решим\n')
            c1 = Fraction(str(c))
            b1 = Fraction(str(b))
            x = -c1 / b1
            x = floatx(x)
            x = intx(x)
            result.insert('6.0', f'{b}x={revers_sign(c_sign)}{abs(c)}\nx={x}')
            answer = [x]
        elif a == 0 and b != 0 and c == 0:
            result.insert('3.0', f', а точнее\n{b}x=0\nэто не квадратное уравнение\nвсё равно решим\nx=0')
            answer = [0]
        elif a == 0 and b == 0 and c != 0:
            result.insert('3.0', f', а точнее\n{c}=0\nэто не квадратное уравнение\nтут нет решения')
            button2.config(state=tk.DISABLED)
        elif a == 0 and b == 0 and c == 0:
            result.insert('3.0', f', а точнее\n0=0\nэто верно при любом x\nввдите ненулевые коэффициенты')
            button2.config(state=tk.DISABLED)
        else:
            a1 = Fraction(str(a))  # для подсчёта используем обыкновенные дроби
            b1 = Fraction(str(b))
            c1 = Fraction(str(c))
            D = b1 ** 2 - 4 * a1 * c1
            D = floatx(D)
            D = intx(D)
            result.insert('3.0', f'\nдискриминант D=b\u00B2-4ac\nD=({b})\u00B2-4*({a})*({c})={D}')
            if D < 0:
                result.insert('6.0', f'\nдискриминант меньше нуля\nнет решения')
            elif D == 0:
                x = -b / 2 * a
                x = floatx(x)
                x = intx(x)
                result.insert('6.0', f'\nодин корень\nx=-b/2a => x=({b}) / (2*{a})\nx={x}')
                answer = [x]
            elif D ** (1 / 2) != round(D ** (1 / 2), 9):
                result.insert('6.0', '\nиррациональные корни\n')
                result.insert('7.0', f'два корня:\nx1=(-b+u\u221aD)/2a  и  x2=(-b-u\u221aD)/2a')
                result.insert('8.0',
                              f'\n\nx1=({revers_sign(b_sign)}{abs(b)}+\u221a{D}) / ({2 * a}),\nx2=({revers_sign(b_sign)}{abs(b)}-\u221a{D}) / ({2 * a})')
                answer = [(-b + D ** 0.5) / (2 * a), (-b - D ** 0.5) / (2 * a)]
            else:
                x1 = (-b1 + Fraction(str(D ** 0.5))) / (2 * a1)
                x1 = floatx(x1)
                x1 = intx(x1)
                x2 = (-b1 - Fraction(str(D ** 0.5))) / (2 * a1)
                x2 = floatx(x2)
                x2 = intx(x2)
                result.insert('5.0', f'\nдва корня:\nx1=(-b+u\u221aD)/2a  и  x2=(-b-u\u221aD)/2a')
                result.insert('8.0',
                              f'\n\nx1=({revers_sign(b_sign)}{abs(b)}+{intx(D ** 0.5)}) / ({2 * a}) = {x1},\nx2=({revers_sign(b_sign)}{abs(b)}-{intx(D ** 0.5)}) / ({2 * a}) = {x2}')
                answer = [(-b + D ** 0.5) / (2 * a), (-b - D ** 0.5) / (2 * a)]
    else:
        result.delete('1.0', tk.END)
        result.config(fg='red')
        result.insert('1.0', 'все коэффициенты должны быть числовыми')
        button2.config(state=tk.DISABLED)


def draw_grafic():
    # a=0
    # b=0
    # c=0
    button2.config(state=tk.DISABLED)
    answer.append(0)
    answer.append(-3)
    answer.append(3)
    if a!=0:
        answer.append(-b/(2*a))
    answer_y=[]
    for i in answer:
        answer_y.append(a*i**2+b*i+c)
    answer_y.append(0)
    print(answer, answer_y)
    x_min_canvas = round(min(answer))
    x_max_canvas = round(max(answer))
    y_min_canvas = round(min(answer_y))
    y_max_canvas = round(max(answer_y))
    print(x_min_canvas, x_max_canvas)
    x_max_canvas += 6-(x_max_canvas - x_min_canvas) % 6
    y_max_canvas += 6-(y_max_canvas - y_min_canvas) % 6
    print('x=>', x_min_canvas, x_max_canvas)
    print('y=>', y_min_canvas, y_max_canvas)
    dx=(x_max_canvas - x_min_canvas)
    dy=(y_max_canvas - y_min_canvas)
    x_min_canvas -= (dx // 6)
    x_max_canvas += (dx // 6)
    y_min_canvas -= (dy // 6)
    y_max_canvas += (dy // 6)
    print(x_min_canvas, x_max_canvas, y_min_canvas, y_max_canvas)
    grafic.main(a, b, c, x_min_canvas, x_max_canvas, y_min_canvas, y_max_canvas)


# случайный выбор цвета фона главного окна (светлые тона)
r = lambda: random.randint(155, 255)
colors = ('#%02X%02X%02X' % (r(), r(), r()))

window = tk.Tk()
window.title('квадратное уравнение')
window.geometry('800x650+200+10')
window.config(bg=colors)
greeting = tk.Label(text='Квадратное уровнение имеет вид: ax\u00B2+bx+c=0', bg=colors, font="Arial 22")
greeting.pack()

# область ввода коэффициентов a, b, c
input_area = tk.Frame(window, bg=colors)
tk.Label(input_area, text='введите коэффициенты a, b, c', bg=colors, font="Arial 22").pack()
input_a = tk.Entry(input_area, width=7, font="Arial 17")
input_a.pack(side=tk.LEFT)
tk.Label(input_area, text='x\u00B2+', bg=colors, font="Arial 22").pack(side=tk.LEFT)
input_b = tk.Entry(input_area, width=7, font="Arial 17")
input_b.pack(side=tk.LEFT)
tk.Label(input_area, text='x+', bg=colors, font="Arial 22").pack(side=tk.LEFT)
input_c = tk.Entry(input_area, width=7, font="Arial 17")
input_c.pack(side=tk.LEFT)
tk.Label(input_area, text='=0', bg=colors, font="Arial 22").pack(side=tk.LEFT)
input_area.pack()

# кнопки и вывод результата
frame2 = tk.Frame(window, bg=colors)
frame2.pack()
button1 = tk.Button(frame2, text='решить уравнение', font="Arial 17", command=calculate)
button1.pack(side=tk.LEFT, padx=20, pady=20)
button2 = tk.Button(frame2, text='бонус', font="Arial 17", state=tk.DISABLED, command=draw_grafic)
button2.pack(side=tk.RIGHT, padx=20, pady=20)
result = tk.Text(window, width=50, height=13, font="Arial 20")
result.pack()

window.mainloop()
