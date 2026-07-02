import tkinter as tk

# create window
root = tk.Tk()
root.title("calculator")
root.geometry("380x450")
root.resizable(False, False)

# display
display = tk.Entry(
    root,
    font=("Arial", 24),
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
    "7",
    "8",
    "9",
    "/",
    "4",
    "5",
    "6",
    "*",
    "1",
    "2",
    "3",
    "-",
    "0",
    ".",
    "=",
    "+",
]

for i, button in enumerate(buttons):
    row = i // 4
    column = i % 4
    tk.Button(
        root,
        text=button,
        font=("Arial", 18),
        width=5,
        height=2,
    ).grid(
        row=row + 1,
        column=column,
        padx=5,
        pady=5,
        sticky="nsew",
    )

# start the event loop
root.mainloop()
