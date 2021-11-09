import tkinter as tk

#
#ass Application(tk.Frame):
#  def __init__(self, master=None):
#      super().__init__(master)
#      self.master = master
#      self.pack()
#      self.create_widgets()
#  def create_widgets(self):
#      self.hi_there = tk.Button(self)
#      self.hi_there["text"] = "Citar"
#      self.hi_there["command"] = self.say_hi
#      self.hi_there.place(x=60, y=40, width=100, height=30)
#      self.hi_there = tk.Button(self)
#      self.hi_there["text"] = "Actualizar"
#      self.hi_there["command"] = self.say_bye
#      self.hi_there.pack(side="top")
#      self.quit = tk.Button(self, text="QUIT", fg="red",
#                            command=self.master.destroy)
#      self.quit.pack(side="bottom")
#
#  def say_hi(self):
#      print("hi there, everyone!")
#  def say_bye(self):
#      print("hi there, everyone!")
#ot = tk.Tk()
#p = Application(master=root)
#p.mainloop()




import tkinter as tk
from tkinter import ttk
from tkinter.constants import ANCHOR, CENTER
class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.iconbitmap(r"Imagenes\unnamed.ico")
        main_window.title("Ocasa Citaciones")
        main_window.configure(width=485, height=120)
        main_window.resizable(width=0, height=0)
        self.place(relwidth=1, relheight=1)
        self.button = ttk.Button(self, text="Citar",)
        self.button.place(x=5, y=20, relheight=0.44, relwidth=0.16)
        self.button = ttk.Button(self, text="Actualizar\n    Tabla")
        self.button.place(x=100, y=20, relheight=0.44, relwidth=0.16 )
        self.button = ttk.Button(self, text="   Modificar\nTransportista")
        self.button.place(x=200, y=20, relheight=0.44, relwidth=0.16)
        self.button = ttk.Button(self, text="    Eliminar\nTransportista")
        self.button.place(x=300, y=20, relheight=0.44, relwidth=0.16)
        self.button = ttk.Button(self, text="    Agregar\nTransportista")
        self.button.place(x=400, y=20, relheight=0.44, relwidth=0.16)
        self.quit = ttk.Button(self, text="Salir",
        command=self.master.destroy)
        self.quit.place(x=200, y=90)
main_window = tk.Tk()
app = Application(main_window)
app.mainloop()