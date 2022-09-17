from email.mime import image
import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()
window.title('ASignL')

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_width = 960
window_height = 700

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

greeting = tk.Label(text="AsignL", fg="#f58853",bg = "#e3cdcd", width=100, height=1, font=("Times 40"))
greeting.pack()

frame1 = tk.Frame(master=window, height=370, bg="#d3c7cd")
frame1.pack(fill=tk.X)

#video goes here
frame2 = tk.Frame(master=window, height=400, bg="#FFFFFF")
frame2.pack(fill=tk.X)

output = tk.Label(text= "Translation: ", height=0, bg="#e3cdcd", anchor='w', font=("Times 30"))
output.pack(fill=tk.X)

#translation text goes here
frame3 = tk.Frame(master=window, height=999, bg="#d3c7cd")
frame3.pack(fill=tk.X)

image1 = Image.open("delphianyearbooktemplate (1).png")
image1 = image1.resize((60, 60), Image.ANTIALIAS)

test = ImageTk.PhotoImage(image1)
label1 = tk.Label(frame1, image=test)
label1.pack()

window.mainloop()

#orange color: #f58853
#dark blue color: #34398f
#pastel pinkish: #e3cdcd
#pastel purplish: #d3c7cd