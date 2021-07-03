import tkinter as tk

window = tk.Tk()
frame_a = tk.Frame(master=window, width=200, height=100, bg="red")
frame_b = tk.Frame(master=window, width=100, bg="yellow")

greeting = tk.Label(master=frame_b, text="Hello, world")
greeting.pack()
label = tk.Label(
    master=frame_a,
    text="Im a label",
    foreground="#34A2FE",
    background="black",
    width=10,
    height=20,
)
label.pack()

# entry = tk.Entry(fg="yellow", bg="blue", width=50)
entry = tk.Text(master=frame_a)
entry.insert("1.0", "python")  # 1.0 = <line>.<column>
entry.insert("0.0", "hello\n")  # 1.0 = <line>.<column>
entry.pack()

submit = tk.Button(
    master=frame_a,
    text="Generate!",
    width=25,
    height=5,
    bg='blue',
    fg='yellow',
)
submit.pack()

frame_a.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frame_b.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


def handle_keypress(event):
    print(event.char)


# .bind() always takes at least two arguments:
#
# An event that’s represented by a string of the form "<event_name>", where event_name can be any of Tkinter’s events
# An event handler that’s the name of the function to be called whenever the event occurs
window.bind("<Key>", handle_keypress)

print("START")
print(entry.get("1.0", tk.END))
window.mainloop()  # tells Python to run the Tkinter event loop
print("DONE")
