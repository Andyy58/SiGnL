import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from output import *
import cv2
from threading import Thread

window = tk.Tk()
settings_window = None
manual_window = None
window.title('ASignL')

outputs = Output()
output_devices = Output.get_output_devices()


window_width = 960
window_height = 540
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window.geometry(
    f'{window_width}x{window_height}+{screen_width // 2 - window_width // 2}+{screen_height // 2 - window_height // 2}')
window.resizable(0, 0)

frame = tk.Frame(window).pack()

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

canvas = tk.Canvas(frame, bg='black', width=window_width, height=window_height, highlightthickness=0)
canvas.pack()

camera = tk.Label(window, borderwidth=0)
cap = cv2.VideoCapture(0)

bg_img = ImageTk.PhotoImage(Image.open('static/img/background.png').resize((window_width + 10, window_height + 10)))
bg = canvas.create_image(window_width // 2, window_height // 2, image=bg_img)


def close_settings():
    global settings_window
    settings_window.destroy()
    settings_window = None


def set_device(variable):
    for od in output_devices:
        if od['name'] == variable:
            outputs.set_output_device(od['index'])
            return


def set_voice(variable):
    outputs.set_gender(variable)


def open_settings():
    global settings_window
    if settings_window is None:
        settings_window = tk.Toplevel()
        settings_window.title('ASignL Settings')
        settings_window['bg'] = '#0f4ebf'
        settings_window.geometry(f'260x180+50+50')
        settings_window.protocol('WM_DELETE_WINDOW', close_settings)

        options1 = []
        variable1 = tk.StringVar(settings_window)
        for od in output_devices:
            options1.append(od['name'])
            if od['index'] == outputs.output_device:
                variable1.set(od['name'])
        dropdown1 = tk.OptionMenu(settings_window, variable1, *options1, command=set_device)
        dropdown1.place(x=20, y=50)

        label1 = tk.Label(settings_window, text='Select Output Device:', bg='#0f4ebf', fg='#fff', font=("Calibri", 14))
        label1.place(x=20, y=20)
        label2 = tk.Label(settings_window, text='Select Gender:', bg='#0f4ebf', fg='#fff', font=("Calibri", 14))
        label2.place(x=20, y=90)
        options2 = ['Male', 'Female']
        variable2 = tk.StringVar(settings_window)
        variable2.set(outputs.gender)
        dropdown2 = tk.OptionMenu(settings_window, variable2, *options2, command=set_voice)
        dropdown2.place(x=20, y=120)

        settings_window.mainloop()


def close_manual():
    global manual_window
    manual_window.destroy()
    manual_window = None


def open_manual():
    global manual_window
    #outputs.speak('Hello World')
    if manual_window is None:
        manual_window = tk.Toplevel()
        manual_window.title('ASignL Manual')
        manual_window.geometry(f'500x500+100+100')
        manual_window.protocol('WM_DELETE_WINDOW', close_manual)

        chart_img = ImageTk.PhotoImage(Image.open('static/img/manual.png').resize((500, 500)))
        print(chart_img)
        chart_bg = tk.Label(manual_window, image=chart_img)
        chart_bg.pack()

        manual_window.mainloop()


settings_img = ImageTk.PhotoImage(Image.open('static/img/settings.png').resize((40, 40)))
settings = tk.Button(canvas, image=settings_img, highlightthickness=0, borderwidth=0, command=open_settings)
settings.pack()
canvas.create_window(window_width - 20, 20, anchor='ne', window=settings)
manual_img = ImageTk.PhotoImage(Image.open('static/img/book.png').resize((40, 40)))
manual = tk.Button(canvas, image=manual_img, highlightthickness=0, borderwidth=0, command=open_manual)
manual.pack()
canvas.create_window(window_width - 70, 20, anchor='ne', window=manual)


def show_frames():
    cv2_image = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
    frame_img = ImageTk.PhotoImage(
        Image.fromarray(cv2_image).transpose(Image.Transpose.FLIP_LEFT_RIGHT).resize((496, 372)))
    camera.frame = frame_img
    canvas.create_image(window_width // 2 - 15, window_height // 2 - 35, image=frame_img)
    canvas.tag_raise(bg)
    camera.after(10, show_frames)


show_frames()

window.mainloop()
