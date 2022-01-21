import tkinter as t
import webbrowser
prog_version = "0.1.1"
def_font = "Helvetica"
#Chrck Button Vars
#Functions go here
def temp_command():
    global close_browser
    print("THIS IS A TEMP COMMAND!")
    print("PLEASE FIND THE BUTTON USING IT AS IT IS NOT USING IT'S OWN FUNCTION!")
    print(close_browser.get())
print("Info: Hello! Welcome to MrHatman26's URL Saver!\nCurrent Version is: " + prog_version + "\n\nUpdate: Starting GUI")
resolution = "675x620"
print("Info: GUI resolution is: " + resolution)
title = "MrHatman26's URL Saver " + prog_version
print("Info: Title is: " + title + "\nUpdate: Creating main window...", end="")
window = t.Tk()
close_browser = t.BooleanVar()
append_urls = t.BooleanVar()
delete_urls = t.BooleanVar()
open_sep_win = t.BooleanVar()
print("Done!\nUpdate: Setting resolution and title", end="")
window.geometry(resolution)
window.title(title)
print("Done!\nUpdate: Creating GUI widgets...", end="")
#Save URLs Frame
save_frame = t.Frame(window)
save_frame_save_label = t.Label(save_frame, text="Save URLs", font=(def_font, 25)).pack(side=t.TOP)
save_frame_urls = t.Text(save_frame, height=10, width=80)
save_frame_urls.pack()
#Save Button Sub Frame
save_frame_button_frame = t.Frame(save_frame)
save_frame_button_frame_button = t.Button(save_frame_button_frame, text="Save URLs", command=temp_command, width=10).pack(side=t.LEFT)
#Save Check Box Sub Sub Frame
save_frame_check_frame = t.Frame(save_frame_button_frame)
save_frame_close_b_check = t.Checkbutton(save_frame_check_frame, text="Close all browser windows/tabs on save.", variable=close_browser, onvalue=True, offvalue=False)
save_frame_close_b_check.pack(padx=(9, 0))
save_frame_append_check = t.Checkbutton(save_frame_check_frame, text="Append new URLs. (Prevent Overwrite)", variable=append_urls, onvalue=True, offvalue=False)
save_frame_check_frame.pack(side=t.RIGHT)
save_frame_append_check.pack()
save_frame_button_frame.pack(side=t.BOTTOM, pady=10)
save_frame.pack()
#Load URLs Frame
load_frame = t.Frame(window)
load_frame_load_label = t.Label(load_frame, text="Load URLs", font=(def_font, 25)).pack(side=t.TOP)
load_frame_urls = t.Text(load_frame, height=10, width=80)
load_frame_urls.pack()
#Load Button Sub Frame
load_frame_button_frame = t.Frame(load_frame)
load_frame_button_frame_button = t.Button(load_frame_button_frame, text="Save URLs", command=temp_command, width=10).pack(side=t.LEFT)
#Load Check Box Sub Sub Frame
load_frame_check_frame = t.Frame(load_frame_button_frame)
load_frame_delete_urls_check = t.Checkbutton(load_frame_check_frame, text="Delete all URLs after opening.", variable=delete_urls, onvalue=True, offvalue=False)
load_frame_delete_urls_check.pack()
load_frame_sep_windows_check = t.Checkbutton(load_frame_check_frame, text="Open all URLs in separate windows.", variable=open_sep_win, onvalue=True, offvalue=False)
load_frame_sep_windows_check.pack(padx=(30, 0))
load_frame_check_frame.pack(side=t.RIGHT)
load_frame_button_frame.pack(side=t.BOTTOM, pady=10)
load_frame.pack()
exit_button_line = t.Label(window, text="-----------------------------------------------------------------------------------------------------------------------------").pack()
exit_button = t.Button(window, text="Exit", command=temp_command, width=10).pack(pady=(5, 0))

save_frame_urls.configure(state="disabled")
window.resizable(False, False)
print("Done!\n\nWaiting for input...")
window.mainloop()
