#Importar as bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter  import ttk

#criar nossa janela
jan = Tk()
jan.title("DP Systems - Acess Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)


# ====== Carregar imagens
logo = PhotoImage(file="icons/logo.png")

#=== Widgets ==========
LeftFrame = Frame(jan, width= 200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

Rightframe = Frame(jan, width= 395, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=100)

UserLabel = Label(Rightframe, text="Username:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(Rightframe, widht=30)
UserEntry.place(x=150, y=110)





jan.mainloop()
