from tkinter import*
from tkinter import messagebox


root=Tk()
root.title('contactame')
root.config(bg='#4EB9E0')
root.geometry('350x200')

frame1=Frame(root,bg='#4EB9E0')
frame1.pack()
frame2=Frame(root,bg='#4EB9E0')
frame2.pack()


logo=PhotoImage(file='logowhat.gif')

def salir():
    root.destroy()

def mensaje():
    messagebox.showinfo('contacto', "Te dejo mi contacto\nWhatsapp: +542804658107")
    

Label(frame1,font=('Courier',16,'italic'),bg='#4EB9E0',text='Hola soy Maxi!').grid(row=0,columnspan=6)
Label(frame1,font=('Courier',15,'italic'),bg='#4EB9E0',text='Contacto:').grid(row=1,column=0)
Button(frame1,bg='#4EB9E0',image=logo,command=mensaje).grid(row=2,column=0)

Button(frame2,font=('Courier',12,'italic'),bg='#4EB9E0',text='Salir',command=salir).grid(row=0,columnspan=2)


root.mainloop()