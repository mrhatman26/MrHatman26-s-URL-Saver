import tkinter as t
from tkinter import messagebox
import webbrowser
prog_version = "0.2.1"
def_font = "Helvetica"
urls = []
#Chrck Button Vars
#Regular Functions
def get_urls():
    print("Update: Getting URLs from file...", end="")
    opened = False
    try:
        file = open("URLs.txt", "r")
        opened = True
    except:
        print("Failed!\nError: File not found.")
        t.messagebox.showerror("Error", "Error: Unable to find URLs.txt.")
    if opened is True:
        load_frame_urls.delete("1.0", "end")
        urls = []
        for lines in file:
            load_frame_urls.configure(state="normal")
            load_frame_urls.insert("end", "\n" + lines)
            urls.append(lines)
            load_frame_urls.configure(state="disabled")
#Functions for buttons
def temp_command():
    global close_browser
    print("THIS IS A TEMP COMMAND!")
    print("PLEASE FIND THE BUTTON USING IT AS IT IS NOT USING IT'S OWN FUNCTION!")
    print(close_browser.get())
def exit_button():
    print("\nUpdate: User clicked exit button.\nUpdate: Exiting...", end="")
    window.destroy()
    print("Update: Done!")
print("Info: Hello! Welcome to MrHatman26's URL Saver!\nCurrent Version is: " + prog_version + "\n\nUpdate: Starting GUI")
resolution = "675x375"
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
#Load URLs Frame
load_frame = t.Frame(window)
load_frame_load_label = t.Label(load_frame, text="Load URLs", font=(def_font, 25)).pack(side=t.TOP)
load_frame_urls = t.Text(load_frame, height=10, width=80)
load_frame_urls.pack()
#Load Button Sub Frame
load_frame_button_frame = t.Frame(load_frame)
load_frame_button_frame_button = t.Button(load_frame_button_frame, text="Open URLs", command=temp_command, width=10).pack(side=t.LEFT)
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
info_button = t.Button(window, text="Info", command=temp_command, width=10).pack(pady=(5, 0))
exit_button = t.Button(window, text="Exit", command=exit_button, width=10).pack(pady=(4, 0))

load_frame_urls.configure(state="disabled")
get_urls()
window.resizable(False, False)
print("Done!\n\nWaiting for input...")
window.mainloop()
