import tkinter

window = tkinter.Tk()
window.geometry("300x200")

def change_text():
    label.config(text="hi.......")

label = tkinter.Label(
    window, text="متن نمونه", font=("tahoma", 16), fg="white", bg="darkblue", width=20, height=2, padx=10, pady=5
)
label.pack()

button = tkinter.Button(window, text="change", command=change_text)
button.pack()
tkinter.mainloop()
