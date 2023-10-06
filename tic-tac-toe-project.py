from tkinter import *

root = Tk()
root.geometry("500x500")
root.title('Tic Tac Toe')

frame1 = Frame(root)
frame1.pack()

titlelabel1 = Label(frame1, text='Tic Tac Toe' , font=("Arial",30))
titlelabel1.pack()

frame2 = Frame(root)
frame2.pack()

# Tic tac toe board

# first row 

Button1 = Button(frame2,text=" ",width=10,height=6)
Button1.grid(row=0,column=0)

Button1 = Button(frame2,text=" ",width=10,height=6)
Button1.grid(row=0,column=1)

Button1 = Button(frame2,text=" ",width=10,height=6)
Button1.grid(row=0,column=2)

# second row 

Button1 = Button(frame2,text=" ",width=10,height=6)
Button1.grid(row=1,column=0)

Button1 = Button(frame2,text=" ",width=10,height=6)
Button1.grid(row=1,column=1)

Button1 = Button(frame2,text=" ",width=10,height=6)
Button1.grid(row=1,column=2)

# third row 

Button1 = Button(frame2,text=" ",width=10,height=6)
Button1.grid(row=2,column=0)

Button1 = Button(frame2,text=" ",width=10,height=6)
Button1.grid(row=2,column=1)

Button1 = Button(frame2,text=" ",width=10,height=6)
Button1.grid(row=2,column=2)




root.mainloop()