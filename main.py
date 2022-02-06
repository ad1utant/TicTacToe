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
    elif buttons[0][0]['state'] == "disabled" and buttons[0][1]['state'] == "disabled" and buttons[0][2]['state'] == "disabled" and buttons[1][0]['state'] == "disabled" and buttons[1][1]['state'] == "disabled" and buttons[1][2]['state'] == "disabled" and buttons[2][0]['state'] == "disabled" and buttons[2][1]['state'] == "disabled" and buttons[2][2]['state'] == "disabled":
        info = tk.messagebox.showinfo(title=None, message="Remis")
        exit()
def Nacisk():
    i=0
    for j in range(3):
        for k in range(3):
            if buttons[j][k]['state'] == 'disabled':
                i+=1
    return i
def HandleButtonClick(x, y):
    i = Nacisk()
    letters = ['a', 'b', 'c']
    if i % 2 == 0:
        buttons[x][y]['image'] = cross
        buttons[x][y]["state"] = "disabled"
        krzyze.append(letters[x] + str(y + 1))
    else:
        buttons[x][y]['image'] = circle
        buttons[x][y]["state"] = "disabled"
        kolka.append(letters[x] + str(y + 1))
    Sprawdzacz()
##
buttons = []
for j in range(3):
    buttonRow = []
    for k in range(3):
        buttonRow.append(tk.Button(root, height=40, width=40, bg="#F7F7F7", image=blank, command=lambda j=j, k=k: HandleButtonClick(j, k)))
    buttons.append(buttonRow)
##
def Gridy(buttons):
    for j in range(3):
        for k in range(3):
            buttons[j][k].grid(ipady=30, ipadx=30, padx=5, pady=5, column=j+1, row=k+1)
    return buttons
##
gridy = Gridy(buttons)
root.mainloop()
