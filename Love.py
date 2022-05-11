from email.mime import image
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import tkinter.messagebox

love = 'D:\\tech\\python\\love\\love.png'

def closeWindow():
    messagebox.showinfo(title="我爱你", message="爱我别走！")
    return


def tongyi():
    win = tk.Toplevel(window)
    win.geometry("800x500+{}+{}".format(int((screenwidth - width) / 2),
                 int((screenheight - height) / 2)))
    win.title("秋宇")
    label = tk.Label(
        win, text="宝宝我超级喜欢你，我会好好对你\n坚定的选择我，我会好好爱你。\n mua～(｡･ω･｡)ﾉ♡\n\n (ɔˆ ³(ˆ⌣ˆc)\n\n(づ￣ ³￣)づ\n\n(ღ♡‿♡ღ)\n\n", font=("宋体", 30))
    label.pack()

    btn = tk.Button(win, text="亲亲", width=10,
                    height=2, command=window.destroy)
    btn.pack()


def butongyi():
    B2.place_forget()
    B2.place(x=random.randint(100,500), y=random.randint(100, 500))


if __name__ == '__main__':
    window = tk.Tk()
    window.title('爱爱秋宇')
    width = 600
    height = 600

    # 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth -
                                                width) / 2, (screenheight - height) / 2)
    window.geometry(alignstr)
    # 设置窗口是否可变长、宽，True：可变，False：不可变
    window.resizable(width=False, height=True)
    window.geometry('800x500')

    window.protocol("WM_DELETE_WINDOW", closeWindow)

    L1 = tk.Label(window, text='亲爱的宝宝：愿意和我一直到老吗？', font=("宋体", 28))
    L1.place(x=50, y=50)

    load=Image.open(love)
    render=ImageTk.PhotoImage(load)
    L2=tk.Label(window, image = render)
    L2.place(x = 180, y = 100) 

    B1 = tk.Button(window, text='好呀', font=("华文行楷", 28), command=tongyi)
    B1.place(x=200, y=300)

    B2 = tk.Button(window, text='考虑一下', font=("华文行楷", 28), command=butongyi)
    B2.place(x=450, y=300)

    window.mainloop()
