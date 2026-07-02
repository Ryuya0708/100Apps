import tkinter as tk

# create window
root = tk.Tk()
root.title("calculator")
root.geometry("280x380")
root.resizable(False, False)

# display
display = tk.Entry(
    root,
    font=("Arial", 20),
    width=16,
    justify="right",
)

display.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=10,
    pady=10,
    sticky="nsew",
)

# buttons
buttons = [
    "←",
    "C",
    "%",
    "÷",
    "7",
    "8",
    "9",
    "x",
    "4",
    "5",
    "6",
    "-",
    "1",
    "2",
    "3",
    "+",
    "☺",
    "0",
    ".",
    "=",
]

for i, button in enumerate(buttons):
    row = i // 4
    column = i % 4
    tk.Button(
        root,
        text=button,
        font=("Arial", 12),
        width=5,
        height=2,
        command=lambda b=button: click_event(b),
    ).grid(
        row=row + 1,
        column=column,
        padx=5,
        pady=5,
        sticky="nsew",
    )


def click(value):
    num = display.get()
    new_text = num + value
    display.delete(0, tk.END)
    display.insert(0, new_text)

    # display.insert(tk.END, value)でも書ける。練習で流れにそって書いた


# 各項目の動作
def clear():
    display.delete(0, tk.END)


def calculate():
    num = display.get()
    result = eval(num)
    display.delete(0, tk.END)
    display.insert(0, result)


def operator(value):
    if value == "÷":
        value = "/"
    elif value == "x":
        value = "*"
    num = display.get()
    new_text = num + value
    display.delete(0, tk.END)
    display.insert(0, new_text)


def nikochan():
    return None


def backspace():
    num = display.get()
    new_text = num[:-1]
    display.delete(0, tk.END)
    display.insert(0, new_text)


def click_event(button):
    if button == "=":
        calculate()
    elif button == "C":
        clear()
    elif button in ["÷", "x", "-", "+"]:
        operator(button)
    elif button == "☺":
        nikochan()
    elif button == "←":
        backspace()
    else:
        click(button)


# start the event loop
root.mainloop()
