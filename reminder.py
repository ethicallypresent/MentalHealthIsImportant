from tkinter import *
import time


def new_label(master, text):
    new_label = Label(master=master, text=text)
    new_label.pack()


while True:
    time.sleep(5)
    root = Tk()
    root.title('REMINDER')
    root.geometry('300x100')
    new_label(root, "You're great don't forget that")

    exit_button = Button(root, text='Exit', command=root.quit)
    exit_button.pack()
    root.mainloop()
    root.destroy()
    break

while True:
    time.sleep(5)
    root = Tk()
    root.title("SERIOUSLY")
    root.geometry('300x100')
    new_label(root, "You're worth it")

    exit_button = Button(root, text="exit", command=root.quit)
    exit_button.pack()
    root.mainloop()
    root.destroy()
    break

while True:
    time.sleep(3)
    root = Tk()
    root.title("BELIEVE ME")
    root.geometry('300x100')
    new_label(root, 'take a break')

    exit_button = Button(root, text='exit', command=root.quit)
    exit_button.pack()
    root.mainloop()
    root.destroy()
    break

while True:
    time.sleep(3)
    root = Tk()
    root.title("WHY...")
    root.geometry('300x100')
    new_label(root, 'are you still here...?')

    exit_button = Button(root, text='exit', command=root.quit)
    exit_button.pack()
    root.mainloop()
    root.destroy()
    break

while True:
    time.sleep(5)
    root = Tk()
    root.title("GO")
    root.geometry('300x100')
    new_label(root, 'drink water, take a walk, something other than sit here.')

    exit_button = Button(root, text='exit', command=root.quit)
    exit_button.pack()
    root.mainloop()
    root.destroy()
    break

final_root = Tk()
final_root.geometry('400x100')
final_root.title('Your mental health')
new_label(final_root, 'is more important, please just do something positive.')
final_root.mainloop()
