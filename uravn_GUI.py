import tkinter as tk
import random
from fractions import Fraction

intx = (lambda x: int(x) if x == int(x) else x)  # если возможно делаем тип int
floatx = (lambda x: float(x) if float(x) == round(float(x), 12) else x)  # если возможно делаем тип float
revers_sign = (lambda x: '-' if x == '+' else '')


def create_canvas():  # TODO
    window2 = tk.Tk()
    canvas = tk.Canvas(window2)
    canvas.pack()
    window2.title('холст')
    window2.geometry('800x650+200+10')


def check_vvod(x):  # пытаемся преобразовать коэффициенты из строки в число
    while True:
        if '/' in x:
            try:
                x = Fraction(x)
                x = floatx(x)
                x = intx(x)
                return x
            except:
                return x
        try:
            x = float(x)
            x = intx(x)
            return x
        except:
            return x


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
    a = vvod_a.get()
    if a == '': a = '0'
    b = vvod_b.get()
    if b == '': b = '0'
    c = vvod_c.get()
    if c == '': c = '0'
    a = check_vvod(a)
    b = check_vvod(b)
    c = check_vvod(c)

    if type(a) != str and type(b) != str and type(
            c) != str:  # если вместо a,b или c введены не числа, то просим исправить
        a_sign, b_sign, c_sign = signs_koef(a, b, c)

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
        elif a == 0 and b != 0 and c == 0:
            result.insert('3.0', f', а точнее\n{b}x=0\nэто не квадратное уравнение\nвсё равно решим\nx=0')
        elif a == 0 and b == 0 and c != 0:
            result.insert('3.0', f', а точнее\n{c}=0\nэто не квадратное уравнение\nтут нет решения')
        elif a == 0 and b == 0 and c == 0:
            result.insert('3.0', f', а точнее\n0=0\nэто верно при любом x\nввдите ненулевые коэффициенты')
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
            elif D ** (1 / 2) != round(D ** (1 / 2), 9):
                result.insert('6.0', '\nиррациональные корни\n')
                result.insert('7.0', f'два корня:\nx1=(-b+u\u221aD)/2a  и  x2=(-b-u\u221aD)/2a')
                result.insert('8.0',
                              f'\n\nx1=({revers_sign(b_sign)}{abs(b)}+\u221a{D}) / ({2 * a}),\nx2=({revers_sign(b_sign)}{abs(b)}-\u221a{D}) / ({2 * a})')
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


    else:
        result.delete('1.0', tk.END)
        result.config(fg='red')
        result.insert('1.0', 'все коэффициенты должны быть числовыми')


r = lambda: random.randint(155, 255)
colors = ('#%02X%02X%02X' % (r(), r(), r()))

window = tk.Tk()
window.title('квадратное уравнение')
window.geometry('800x650+200+10')
window.config(bg=colors)
greeting = tk.Label(text='Квадратное уровнение имеет вид: ax\u00B2+bx+c=0', bg=colors, font="Arial 22")
greeting.pack()

oblast_vvoda = tk.Frame(window, bg=colors)
tk.Label(oblast_vvoda, text='введите коэффициенты a, b, c', bg=colors, font="Arial 22").pack()
vvod_a = tk.Entry(oblast_vvoda, width=7, font="Arial 17")
vvod_a.pack(side=tk.LEFT)
tk.Label(oblast_vvoda, text='x\u00B2+', bg=colors, font="Arial 22").pack(side=tk.LEFT)
vvod_b = tk.Entry(oblast_vvoda, width=7, font="Arial 17")
vvod_b.pack(side=tk.LEFT)
tk.Label(oblast_vvoda, text='x+', bg=colors, font="Arial 22").pack(side=tk.LEFT)
vvod_c = tk.Entry(oblast_vvoda, width=7, font="Arial 17")
vvod_c.pack(side=tk.LEFT)
tk.Label(oblast_vvoda, text='=0', bg=colors, font="Arial 22").pack(side=tk.LEFT)
oblast_vvoda.pack()
frame2 = tk.Frame(window, bg=colors)
frame2.pack()
button = tk.Button(frame2, text='решить уравнение', font="Arial 17", command=calculate)
button.pack(side=tk.LEFT, padx=20, pady=20)
button = tk.Button(frame2, text='бонус', font="Arial 17", state=tk.DISABLED, command=create_canvas)
button.pack(side=tk.RIGHT, padx=20, pady=20)
result = tk.Text(window, width=50, height=13, font="Arial 20")
result.pack()

window.mainloop()
