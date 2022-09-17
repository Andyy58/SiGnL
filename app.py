import tkinter as tk
import pyglet

window = tk.Tk()
window.title('ASignL')

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_width = 960
window_height = 540

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

greeting = tk.Label(text="AsignL", fg="#f58853", bg = "#e3cdcd", width=100, height=1, font=("Times 40"))
greeting.pack()

frame1 = tk.Frame(master=window, height=370, bg="#d3c7cd")
frame1.pack(fill=tk.X)

output = tk.Label(text= "Translation: ", height=170, bg="#e3cdcd", anchor='w')
output.pack(fill=tk.X)

frame4 = tk.Frame(master=window, height=999, bg="#d3c7cd")
frame4.pack(fill=tk.X)

window.mainloop()

#orange color: #f58853
#dark blue color: #34398f
#pastel pinkish: #e3cdcd
#pastel purplish: #d3c7cd