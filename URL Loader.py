import tkinter as t
from tkinter import messagebox
import webbrowser
prog_version = "0.3.4"
def_font = "Helvetica"
urls = []
#Chrck Button Vars
#Regular Functions
def get_urls():
    global urls
    print("Update: Getting URLs from file...", end="")
    opened = False
    try:
        file = open("URLs.txt", "r")
        opened = True
    except:
        print("Failed!\nError: File not found.")
        load_frame_button_frame_button['state'] = t.DISABLED
        load_frame_urls.configure(state="normal")
        load_frame_urls.delete("1.0", "end")
        load_frame_urls.insert("end", "No File Loaded!")
        load_frame_urls.configure(state="disabled")
    if opened is True:
        load_frame_button_frame_button['state'] = t.NORMAL
        load_frame_urls.delete("1.0", "end")
        urls = []
        for lines in file:
            load_frame_urls.configure(state="normal")
            load_frame_urls.insert("end", "\n" + lines)
            urls.append(lines)
            load_frame_urls.configure(state="disabled")
        if len(urls) < 1:
            load_frame_button_frame_button['state'] = t.DISABLED
            load_frame_urls.configure(state="normal")
            load_frame_urls.delete("1.0", "end")
            load_frame_urls.insert("end", "File is empty!")
            load_frame_urls.configure(state="disabled")
    print("Done!\nUpdate: Closing file...", end="")
    try:
        file.close()
        print("Done!")
    except:
        print("Failed!\nError: File already closed.")
#Functions for buttons
def open_urls():
    print("\nUpdate: User clicked open urls button.\nUpdate: Opening URLs.")
    global urls
    if len(urls) != 0:
        for single_url in urls:
            try:
                webbrowser.open(single_url)
                print("Update: Opened " + single_url)
            except:
                print("Update: Failed to open " + single_url)
        if delete_urls.get() is True:
            print("Update: Deleting URLs...", end="")
            urls = []
            load_frame_urls.configure(state="normal")
            load_frame_urls.delete("1.0", "end")
            load_frame_urls.configure(state="disabled")
            try:
                file = open("URLs.txt", "w").close()
                get_urls()
                print("Done!")
            except:
                print("Failed!")
    else:
        print("Error! No URLs loaded!")
    print("Done!\n\nWaiting for input...")
    if open_sep_win.get() is True:
        print("Update: Program set to close...")
        window.destroy()
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
print("Done!\nUpdate: Setting resolution and title...", end="")
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
load_frame_button_frame_button = t.Button(load_frame_button_frame, text="Open URLs", command=open_urls, width=10)
load_frame_button_frame_button.pack(side=t.LEFT)
#Load Check Box Sub Sub Frame
load_frame_check_frame = t.Frame(load_frame_button_frame)
load_frame_delete_urls_check = t.Checkbutton(load_frame_check_frame, text="Delete all URLs after opening.", variable=delete_urls, onvalue=True, offvalue=False)
load_frame_delete_urls_check.pack()
load_frame_sep_windows_check = t.Checkbutton(load_frame_check_frame, text="Close program after opening URLs.", variable=open_sep_win, onvalue=True, offvalue=False)
load_frame_sep_windows_check.pack(padx=(30, 0))
load_frame_check_frame.pack(side=t.RIGHT)
load_frame_button_frame.pack(side=t.BOTTOM, pady=10)
load_frame.pack()
exit_button_line = t.Label(window, text="-----------------------------------------------------------------------------------------------------------------------------").pack()
info_button = t.Button(window, text="Info", command=temp_command, width=10).pack(pady=(5, 0))
exit_button = t.Button(window, text="Exit", command=exit_button, width=10).pack(pady=(4, 0))

load_frame_urls.configure(state="disabled")
load_frame_button_frame_button['state'] = t.DISABLED
print("Done!")
get_urls()
window.resizable(False, False)
print("Done!\n\nWaiting for input...")
window.mainloop()
