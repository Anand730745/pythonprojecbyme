from tkinter import *
root=Tk()

main_menu=Menu(root)
root.config(menu=main_menu)
#to creat file in filemenu bar
file_menu=Menu(main_menu,tearoff=False)
main_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",accelerator="ctrl+N")
file_menu.add_command(label="New Window",accelerator="ctrl+Shift+N")
file_menu.add_command(label="Open",accelerator="ctrl+o")
file_menu.add_command(label="save",accelerator="ctrl+s")
file_menu.add_command(label="save as",accelerator="ctrl+Shift+o")
file_menu.add_command(label="Page setup")
file_menu.add_command(label="Print",accelerator="ctrl+p")
file_menu.add_command(label="Exit",command=quit)

#to creat file in editmenu bar
edit_menu=Menu(main_menu,tearoff=False)
main_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Undo",accelerator="ctrl+z")
edit_menu.add_command(label="Cut",accelerator="ctrl+x")
edit_menu.add_command(label="Copy",accelerator="ctrl+c")
edit_menu.add_command(label="paste",accelerator="ctrl+v")
edit_menu.add_command(label="Delete",accelerator="Del")
edit_menu.add_command(label="Find",accelerator="ctrl+f")
edit_menu.add_command(label="find next",accelerator="F3")
edit_menu.add_command(label="find previous",accelerator="shift+F3")
edit_menu.add_command(label="Replace",accelerator="ctrl+H")
edit_menu.add_command(label="Go to",accelerator="ctrl+G")
edit_menu.add_command(label="Select all",accelerator="ctrl+A")
edit_menu.add_command(label="Time/Date",accelerator="F5")
edit_menu.add_command(label="Font")

#to creat file in Viewmenu bar

view_menu=Menu(main_menu,tearoff=False)
main_menu.add_cascade(label="View",menu=view_menu)

# add a submenu in zoom_menu
sub_menu=Menu(view_menu,tearoff=False)
view_menu.add_cascade(label="Zoom",menu=sub_menu)
sub_menu.add_command(label="Zoom in",accelerator=("ctrl+plus"))
sub_menu.add_command(label="Zoom out",accelerator=("ctrl+minus"))
sub_menu.add_command(label="Restore default zoom",accelerator=("ctrl+0"))

view_menu.add_command(label="Status bar")
view_menu.add_command(label="Word wrap")




root.wm_iconbitmap("nota.ico")
#root.wm_resizable(0,0)
root.geometry("500x400+120+140")
root.title("My Notepad")
root.mainloop()