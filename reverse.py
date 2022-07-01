from cProfile import label
import tkinter as tk

def reverse():
    txt = box1.get()
    box2.delete(0, tk.END)
    box2.insert(0, txt[::-1])

def clear():
    box1.delete(0, tk.END)
    box2.delete(0, tk.END)

app = tk.Tk()
app.title("String Reverser app")
app.geometry("800x220")
app.iconbitmap("jonty_dp_G1h_icon.ico")
button1 = tk.Button(app , font=("Arial",15),bg ="Orange",text ="Reverse",command=reverse)
button1.place(x=180 , y= 150 , width = 80)

button2 = tk.Button(app , font=("Arial",15),bg ="red",text ="Clear!!",command=clear)
button2.place(x=280 , y= 150 , width = 70)

label1 =tk.Label(app, text = "Number:",font = ("Arial", 25))
label1.place(x=40, y=0)

label2 =tk.Label(app, text = "Reversed:",font = ("Arial", 25))
label2.place(x=20, y=100)

box1 = tk.Entry(app, font = ("Arial", 25), bg="#D3D3D3")
box1.place(x=180, y=10)

box2 = tk.Entry(app, font = ("Arial", 25), bg="#D3D3D3")
box2.place(x=180, y=100)

image = tk.PhotoImage(file="images.png")
label = tk.Label(image = image)
label.place(x=580, y=00)
app.mainloop()