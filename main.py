import tkinter as tk
import tkinter.messagebox
##
i = 1
kolka =[]
krzyze =[]
##
def Okienko():
    root = tk.Tk()
    root.geometry("350x350")
    root.title("TicTacToe Mikołaj Marasek")
    return root
##
root = Okienko()
##
circle = tk.PhotoImage(file="circle.png")
cross = tk.PhotoImage(file="cross.png")
blank = tk.PhotoImage(file="blank.png")
##
def Sprawdzacz():
    if ("a1" in krzyze and "a2" in krzyze and "a3" in krzyze) or (
            "b1" in krzyze and "b2" in krzyze and "b3" in krzyze) or (
            "c1" in krzyze and "c2" in krzyze and "c3" in krzyze) or (
            "a1" in krzyze and "b1" in krzyze and "c1" in krzyze) or (
            "a2" in krzyze and "b2" in krzyze and "c2" in krzyze) or (
            "a3" in krzyze and "b3" in krzyze and "c3" in krzyze) or (
            "a1" in krzyze and "b2" in krzyze and "c3" in krzyze) or (
            "c1" in krzyze and "b2" in krzyze and "a3" in krzyze):
        info = tk.messagebox.showinfo(title=None, message="Krzyżyk wygrał")
        exit()
    elif ("a1" in kolka and "a2" in kolka and "a3" in kolka) or (
            "b1" in kolka and "b2" in kolka and "b3" in kolka) or (
            "c1" in kolka and "c2" in kolka and "c3" in kolka) or (
            "a1" in kolka and "b1" in kolka and "c1" in kolka) or (
            "a2" in kolka and "b2" in kolka and "c2" in kolka) or (
            "a3" in kolka and "b3" in kolka and "c3" in kolka) or (
            "a1" in kolka and "b2" in kolka and "c3" in kolka) or (
            "c1" in kolka and "b2" in kolka and "a3" in kolka):
        info = tk.messagebox.showinfo(title=None, message="Kółko wygrało")
        exit()
    elif a1['state'] == "disabled" and a2['state'] == "disabled" and a3['state'] == "disabled" and b1['state'] == "disabled" and b2['state'] == "disabled" and b3['state'] == "disabled" and c1['state'] == "disabled" and c2['state'] == "disabled" and c3['state'] == "disabled":
        info = tk.messagebox.showinfo(title=None, message="Remis")
        exit()
def Nacisk():
    i=0
    if a1['state'] == "disabled":
        i+=1
    if a2['state'] == "disabled":
        i+=1
    if a3['state'] == "disabled":
        i+=1
    if b1['state'] == "disabled":
        i+=1
    if b2['state'] == "disabled":
        i+=1
    if b3['state'] == "disabled":
        i+=1
    if c1['state'] == "disabled":
        i+=1
    if c2['state'] == "disabled":
        i+=1
    if c3['state'] == "disabled":
        i+=1
    return i
def a1Nacisk():
    i = Nacisk()
    if i % 2 == 0:
        a1['image'] = cross
        a1["state"] = "disabled"
        krzyze.append("a1")
    else:
        a1['image'] = circle
        a1["state"] = "disabled"
        kolka.append("a1")
    Sprawdzacz()
def a2Nacisk():
    i = Nacisk()
    if i % 2 == 0:
        a2['image'] = cross
        a2["state"] = "disabled"
        krzyze.append("a2")
    else:
        a2['image'] = circle
        a2["state"] = "disabled"
        kolka.append("a2")
    Sprawdzacz()
def a3Nacisk():
    i = Nacisk()
    if i % 2 == 0:
        a3['image'] = cross
        a3["state"] = "disabled"
        krzyze.append("a3")
    else:
        a3['image'] = circle
        a3["state"] = "disabled"
        kolka.append("a3")
    Sprawdzacz()
def b1Nacisk():
    i = Nacisk()
    if i % 2 == 0:
        b1['image'] = cross
        b1["state"] = "disabled"
        krzyze.append("b1")
    else:
        b1['image'] = circle
        b1["state"] = "disabled"
        kolka.append("b1")
    Sprawdzacz()
def b2Nacisk():
    i = Nacisk()
    if i % 2 == 0:
        b2['image'] = cross
        b2["state"] = "disabled"
        krzyze.append("b2")
    else:
        b2['image'] = circle
        b2["state"] = "disabled"
        kolka.append("b2")
    Sprawdzacz()
def b3Nacisk():
    i = Nacisk()
    if i % 2 == 0:
        b3['image'] = cross
        b3["state"] = "disabled"
        krzyze.append("b3")
    else:
        b3['image'] = circle
        b3["state"] = "disabled"
        kolka.append("b3")
    Sprawdzacz()
def c1Nacisk():
    i = Nacisk()
    if i % 2 == 0:
        c1['image'] = cross
        c1["state"] = "disabled"
        krzyze.append("c1")
    else:
        c1['image'] = circle
        c1["state"] = "disabled"
        kolka.append("c1")
    Sprawdzacz()
def c2Nacisk():
    i = Nacisk()
    if i % 2 == 0:
        c2['image'] = cross
        c2["state"] = "disabled"
        krzyze.append("c2")
    else:
        c2['image'] = circle
        c2["state"] = "disabled"
        kolka.append("c2")
    Sprawdzacz()
def c3Nacisk():
    i = Nacisk()
    if i % 2 == 0:
        c3['image'] = cross
        c3["state"] = "disabled"
        krzyze.append("c3")
    else:
        c3['image'] = circle
        c3["state"] = "disabled"
        kolka.append("c3")
    Sprawdzacz()
##
a1 = tk.Button(root, height=40, width=40, bg="#F7F7F7", image=blank, command=a1Nacisk)
a2 = tk.Button(root, height=40, width=40, bg="#F7F7F7", image=blank, command=a2Nacisk)
a3 = tk.Button(root, height=40, width=40, bg="#F7F7F7", image=blank, command=a3Nacisk)
b1 = tk.Button(root, height=40, width=40, bg="#F7F7F7", image=blank, command=b1Nacisk)
b2 = tk.Button(root, height=40, width=40, bg="#F7F7F7", image=blank, command=b2Nacisk)
b3 = tk.Button(root, height=40, width=40, bg="#F7F7F7", image=blank, command=b3Nacisk)
c1 = tk.Button(root, height=40, width=40, bg="#F7F7F7", image=blank, command=c1Nacisk)
c2 = tk.Button(root, height=40, width=40, bg="#F7F7F7", image=blank, command=c2Nacisk)
c3 = tk.Button(root, height=40, width=40, bg="#F7F7F7", image=blank, command=c3Nacisk)
##
def Gridy(a1, a2, a3, b1, b2, b3, c1, c2, c3):
    a1.grid(ipady=30, ipadx=30, padx=5, pady=5, column=1, row=1)
    a2.grid(ipady=30, ipadx=30, padx=5, pady=5, column=1, row=2)
    a3.grid(ipady=30, ipadx=30, padx=5, pady=5, column=1, row=3)
    b1.grid(ipady=30, ipadx=30, padx=5, pady=5, column=2, row=1)
    b2.grid(ipady=30, ipadx=30, padx=5, pady=5, column=2, row=2)
    b3.grid(ipady=30, ipadx=30, padx=5, pady=5, column=2, row=3)
    c1.grid(ipady=30, ipadx=30, padx=5, pady=5, column=3, row=1)
    c2.grid(ipady=30, ipadx=30, padx=5, pady=5, column=3, row=2)
    c3.grid(ipady=30, ipadx=30, padx=5, pady=5, column=3, row=3)
    return a1, a2, a3, b1, b2, b3, c1, c2, c3
##
gridy = Gridy(a1, a2, a3, b1, b2, b3, c1, c2, c3)
root.mainloop()