import tkinter as tk
import tkinter.filedialog
from phoneSplitter.transfer_function import transfer
from phoneSplitter.helper import popup_message


def main():
    window = tk.Tk(screenName="Phone Number Splitter")
    courier18 = ("Courier", "18")
    courier12 = ("Courier", "12")
    save_file_path = ""

    # upper frame, where we put header, input textbox, and submit button.
    upper_frame = tk.Frame(master=window, width=400, height=200,
                           bg="red", borderwidth=20)
    header = tk.Label(master=upper_frame,
                      text="Instructions:\n"
                           + "- Copy Paste Phone Numbers Column into the TextBox below.\n"
                           + "- Specify the saving path using the button of left.\n"
                           + "- Specify number of phone# per file at the bottom box.\n"
                           + "- Then hit Submit!",
                      bg="red", font=courier12, anchor="w", justify=tk.LEFT)
    header.pack(fill="both", side=tk.TOP)

    input_frame = tk.Frame(master=upper_frame, width=20, height=80,
                           borderwidth=10)
    multiple_input = tk.Text(master=input_frame, borderwidth=15,
                             relief=tk.FLAT)
    multiple_input.pack()
    to_display = tk.StringVar()
    to_display.set("Current save path: " + save_file_path)
    save_path_display = tk.Label(master=input_frame, textvariable=to_display, font=courier12)
    save_path_display.pack(side=tk.LEFT)

    # function part
    btn_frame = tk.Frame(master=window, borderwidth=1, bg="red")

    def get_file_path():
        nonlocal save_file_path
        # Open and return file path
        # file_path = tkinter.filedialog.askopenfilename(title="Select A File", filetypes=(
        # ("mov files", "*.png"), ("mp4", "*.mp4"), ("wmv", "*.wmv"), ("avi", "*.avi")))
        save_file_path = tkinter.filedialog.askdirectory()
        print("file_path=", save_file_path)
        to_display.set("Current save path: " + save_file_path)
        if save_file_path:
            popup_message("Save path updated successfully to:\n" + save_file_path)
        else:
            popup_message("Please specify a saving path.")

    set_save_path_btn = tk.Button(master=btn_frame, text="Set Path", width=8,
                                  height=2, bg="yellow", borderwidth=10,
                                  font=courier18, command=get_file_path)
    set_save_path_btn.pack(side=tk.LEFT, padx=15, pady=20)

    def text_to_txtfile():
        transfer(multiple_input.get("1.0", tk.END), save_file_path, phone_per_file_entry.get(), filename_entry.get())

    transfer_btn = tk.Button(master=btn_frame, text="Submit", width=8,
                             height=2, bg="yellow", borderwidth=10,
                             font=courier18, command=text_to_txtfile)
    # submit.bind("<Button-1>", get_file_path)
    transfer_btn.pack(side=tk.RIGHT, padx=15, pady=20)

    # in lower frame, we set parameters for the process
    lower_frame = tk.Frame(master=window, width=600, height=300, bg="blue")

    phone_per_file_label = tk.Label(master=lower_frame, font=courier12,
                                    text="Number of Phone per File: ",
                                    bg="blue", fg="yellow")
    phone_per_file_label.pack(side=tk.LEFT, padx=5, pady=5)
    phone_per_file_entry = tk.Entry(master=lower_frame, width=20)
    phone_per_file_entry.insert(0, "170")
    phone_per_file_entry.pack(side=tk.LEFT)

    filename_entry = tk.Entry(master=lower_frame, width=10)
    filename_entry.insert(0, "NANA")
    filename_entry.pack(side=tk.RIGHT, padx=15)
    tk.Label(master=lower_frame, font=courier12,
             text="Filename prefix: ", bg="blue", fg="yellow").pack(side=tk.RIGHT, padx=5, pady=5)

    # layouts
    upper_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
    input_frame.pack()
    lower_frame.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)
    btn_frame.pack(fill=tk.BOTH)
    print("START")
    window.mainloop()
    print("DONE")
