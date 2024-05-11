import tkinter as tk
from tkinter import filedialog as fd

root = tk.Tk()

text=tk.Text(root)

text.grid()

def saveas():
  global text
  t = text.get("1.0", "end-1c")
  savelocation = fd.asksaveasfilename()
  file1=open(savelocation, "w+")
  file1.write(t)
  file1.close()

button = tk.Button(root,text="Save", command=saveas)

button.grid()

root.mainloop()