import tkinter as tk

root = tk.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('{}x{}'.format(width, height))
root.title('Ludo')

msg = ''' Welcome to Online Multi-player Ludo
- Enter your player name
!!!!!!!!!!!!!!!!!!!!!! Have Fun !!!!!!!!!!!!!!!!!!!!!!
'''
tkinter.messagebox.showinfo('Welcome', msg)

top = tk.Toplevel(root)
top.geometry('600x600')
top.title('Enter User Name')

root.mainloop()
