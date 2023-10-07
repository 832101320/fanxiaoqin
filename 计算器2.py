from tkinter  import *

# 创建主窗口
root = Tk()  # 创建TK实例对象
root.title('计算器') # 为窗口命名
root.resizable(0, 0)  # 设置窗口为大小可调节，为0是表示不可调节
root.geometry('320x500')  # 设置窗口大小

# 用于显示计算结果与算式的label
equation = StringVar()  # 算式和结果都是可变文本
result= StringVar()
#result.set(0)
#equation.set('')  # 为结果和算式赋初始值

var_equation= StringVar()
var_equation= Label(root, text="25+100=", textvariable=equation, font=("微软雅黑", 16),
                          bg="white", fg="DimGray", anchor="se")
var_equation.place(x=0, y=0, width=320, height=200)

# 添加结果标签 --显示结果var_result = StringVa
var_result = Label(root, text="125", textvariable=result, font=("微软雅黑", 16), bg="gray",
                          anchor="se")
var_result.place(x=0, y=200, width=320, height=50)


# 回调函数说明
def back():  # 按下退格键时，去除最后一个字符
    temp = equation.get()
    equation.set(temp[:-1])


def getnum(num):
    content = result.get()
    if content == "0":
        result.set(num)
    else:
        result.set(content + num)


# 按下MC时，清空算式行与结果行
def clear():
    equation.set('0')
    result.set(' ')


# 按下等于号时计算结果
def go(result=result):
    # 获取detail 明细
    detail = equation.get()
    num01 = detail.replace(" ", "")[0:len(detail.replace(" ", "")) - 1]
    # 操作符取倒数第一个
    action = detail.replace(" ", "")[-1]
    num02 = result.get()
    # 根据操作符进行操作
    if action == "+":
        ans = float(num01) + float(num02)
        # 修改算式
        equation.set("{0} + {1} = ".format(num01, num02))
        # 修改result
        result.set("{:.12g}".format(ans))

    if action == "-":
        ans = float(num01) - float(num02)
        # 修改算式
        equation.set("{0} - {1} = ".format(num01, num02))
        # 修改result
        result.set("{:.12g}".format(ans))

    if action == "×":
        ans = float(num01) * float(num02)
        # 修改明细
        equation.set("{0} × {1} = ".format(num01, num02))
        # 修改result
        result.set("{:.12g}".format(ans))

    if action == "÷":
        ans = float(num01) / float(num02)
        # 修改算式
        equation.set("{0} ÷ {1} = ".format(num01, num02))
        # 修改result
        result.set("{:.12g}".format(ans))

    if action == "%":
        ans = float(num01) % float(num02)
        # 修改明细
        equation.set("{0} % {1} = ".format(num01, num02))
        # 修改result
        result.set("{:.12g}".format(ans))


def remained():
    content = result.get()
    equation.set(content + " % ")
    result.set("0")


def device():
    content = result.get()
    equation.set(content + " ÷ ")
    result.set("0")


def plus():
    content = result.get()
    equation.set(content + " + ")
    result.set("0")


def multiply():
    content = result.get()
    equation.set(content + " × ")
    result.set("0")


def minus():
    content = result.get()
    equation.set(content + " - ")
    result.set("0")


def dot():
    content = result.get()
    result.set(content + ".")


# 设置按键
# 第一行按键
button_back = Button(root, text='<—', bg='gray', command=back)  # 创建撤回按键
button_back.place(x=0, y=250, width=80, height=50)
button_remained = Button(root, text='%', bg='gray', command=remained)  # 创建'%'键,
button_remained.place(x=80, y=250, width=80, height=50)
button_device = Button(root, text='÷', bg='gray', command=device)  # 创建'÷'键
button_device.place(x=160, y=250, width=80, height=50)
button_plus = Button(root, text='+', bg='gray', command=plus)  # 创建'+'键
button_plus.place(x=240, y=250, width=80, height=50)
# 第二行按键
button_7 = Button(root, text='7', bg='gray', command=lambda: getnum('7'))  # 创建'7'键
button_7.place(x=0, y=300, width=80, height=50)
button_8 = Button(root, text='8', bg='gray', command=lambda: getnum('8'))  # 创建'8'键
button_8.place(x=80, y=300, width=80, height=50)
button_9 = Button(root, text='9', bg='gray', command=lambda: getnum('9'))  # 创建'9'键
button_9.place(x=160, y=300, width=80, height=50)
button_multiply = Button(root, text='x', bg='gray', command=multiply)  # 创建'x'键
button_multiply.place(x=240, y=300, width=80, height=50)
# 第三行按键
button_4 = Button(root, text='4', bg='gray', command=lambda: getnum('4'))  # 创建'4'键
button_4.place(x=0, y=350, width=80, height=50)
button_5 = Button(root, text='5', bg='gray', command=lambda: getnum('5'))  # 创建'5'键
button_5.place(x=80, y=350, width=80, height=50)
button_6 = Button(root, text='6', bg='gray', command=lambda: getnum('6'))  # 创建'6'键
button_6.place(x=160, y=350, width=80, height=50)
button_minus = Button(root, text='-', bg='gray', command=minus)  # 创建'-'键
button_minus.place(x=240, y=350, width=80, height=50)
# 第四行键
button_1 = Button(root, text='1', bg='gray', command=lambda: getnum('1'))  # 创建'1'键
button_1.place(x=0, y=400, width=80, height=50)
button_2 = Button(root, text='2', bg='gray', command=lambda: getnum('2'))  # 创建'2'键
button_2.place(x=80, y=400, width=80, height=50)
button_3 = Button(root, text='3', bg='gray', command=lambda: getnum('3'))  # 创建'3'键
button_3.place(x=160, y=400, width=80, height=50)
# 第五行键
button_C = Button(root, text='C', bg='gray', command=clear)  # 创建'C'键
button_C.place(x=0, y=450, width=80, height=50)
button_dot = Button(root, text=".", bg='gray', command=dot)  # 创建'.'键
button_dot.place(x=80, y=450, width=80, height=50)
button_0 = Button(root, text='0', bg='gray', command=lambda: getnum('0'))  # 创建'0'键
button_0.place(x=160, y=450, width=80, height=50)
button_equal = Button(root, text='=', bg='gray', command=go)  # 创建'='键
button_equal.place(x=240, y=400, width=80, height=100)

root.mainloop()
