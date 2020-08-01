import time
import pyautogui as pg
import tkinter as tk

def screenshot():
    print('will screenshot in the next 5 seconds..')
    name = round(int(time.time()) * 1000)
    name = 'C:/Users/23480/Desktop/Datascience/project_folder/screenshots\\{}.png'.format(name)
    # print(name)
    
    time.sleep(5)
    img = pg.screenshot(name)
    img.show()


root = tk.Tk()

frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text="Take screenshot",
    command = screenshot
)

button.pack(side=tk.LEFT)
close = tk.Button(
    frame,
    text="QUIT",
    command = quit
)
close.pack(side=tk.LEFT)

root.mainloop()