#First Tkinter progrsm to didplay hello world in a window.
import tkinter as tk
window = tk.Tk()
label = tk.Label(window,text="Hello World").pack()
window.mainloop()
