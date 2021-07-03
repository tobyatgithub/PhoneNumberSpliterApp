import tkinter as tk


def popup_message(message):
    """
    Given a string message, pop up a window in GUI.
    :param message: a string
    :return: None
    """
    popup = tk.Tk()
    popup.wm_title("Message:")
    label = tk.Label(master=popup, text=message, font=("Courier", 12), bg="white")
    label.pack(side="top", fill="x", pady=10, padx=10)
    btn = tk.Button(popup, text="Ok", command=popup.destroy, width=5)
    btn.pack()
    popup.mainloop()
