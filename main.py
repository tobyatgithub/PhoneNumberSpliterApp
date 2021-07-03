import tkinter as tk
import tkinter.filedialog

window = tk.Tk(screenName="Phone Number Splitter")
Courier18 = ("Courier", "18")

# upper frame, where we put header, input textbox, and submit button.
upper_frame = tk.Frame(master=window, width=400, height=200,
                       bg="red", borderwidth=20)
upper_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

Header = tk.Label(master=upper_frame,
                  text="Copy Paste in the Phone Numbers Column",
                  bg="red", font=Courier18)
Header.pack(side=tk.TOP, anchor=tk.NW)

# hum, intended to limit the size of Text, but seems not working.
input_frame = tk.Frame(master=upper_frame, width=20, height=80,
                       borderwidth=10)
input_frame.pack()

multiple_input = tk.Text(master=input_frame, borderwidth=15,
                         relief=tk.FLAT)
multiple_input.pack()

# function part
file_path = ""


def get_file_path():
    global file_path
    # Open and return file path
    # file_path = tkinter.filedialog.askopenfilename(title="Select A File", filetypes=(
    # ("mov files", "*.png"), ("mp4", "*.mp4"), ("wmv", "*.wmv"), ("avi", "*.avi")))
    file_path = tkinter.filedialog.askdirectory()


submit = tk.Button(master=upper_frame, text="Submit", width=8,
                   height=2, bg="yellow", borderwidth=10,
                   font=Courier18, command=get_file_path)
submit.pack(side=tk.BOTTOM, anchor=tk.SE, pady=20)

# in lower frame, we set parameters for the process
Courier12 = ("Courier", "12")
lower_frame = tk.Frame(master=window, width=600, height=300, bg="blue")
lower_frame.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)

phone_per_file_label = tk.Label(master=lower_frame, font=Courier12,
                                text="Number of Phone per File: ",
                                bg="blue", fg="yellow")
phone_per_file_label.pack(side=tk.LEFT, padx=5, pady=5)

phone_per_file_entry = tk.Entry(master=lower_frame, width=20)
phone_per_file_entry.insert(0, "170")
phone_per_file_entry.pack(side=tk.LEFT)

print("START")
window.mainloop()
print("DONE")
print("file_path=", file_path)
