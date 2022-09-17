import tkinter as tk

window = tk.Tk()
window.title('ASignL')

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_width = screen_width * 3 // 4
window_height = screen_height * 3 // 4

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

window.mainloop()