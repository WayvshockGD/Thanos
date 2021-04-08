import tkinter
import json
import os
import gd

hacks = []
hack_sep = '\n'

with open('configs.json') as f:
    config = json.load(f)

root_window = tkinter.Tk()
root_window.title(config['title'])
root_window.geometry('550x600')

background = config["background_color"]
text = config["text_color"]


for file in os.listdir('/mods'):
    if file.endswith('.py'):
        print(file)
        newFile = file()
        hacks.append(f'{newFile.name} - {newFile.description}')


gd_version = tkinter.Label(root_window, text=f'Game version: {config["game_version"]}', bg=background, fg=text)
gd_version.pack(fill='x')

gs_mods = tkinter.Label(root_window, text=hack_sep.join(hacks))

root_window.configure(bg=background)

root_window.mainloop()
