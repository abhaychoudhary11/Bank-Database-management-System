from tkinter import *
from PIL import ImageTk,Image 
from tkinter import messagebox

home = Tk() 
home.title('BANK DATABASE MANAGEMENT')
home.geometry('1566x790')
home.resizable(True,True)


#backgroundimage
img=Image.open("bglogin.jpg")
img=img.resize((1566,790))
bg= ImageTk.PhotoImage(img)
Label(home,image=bg,bg='white').place(x=0,y=0)

#banklogo
logo1=Image.open("banklogo.png")
logo1=logo1.resize((500,500))
banklogo= ImageTk.PhotoImage(logo1)
Label(home,image=banklogo).place(x=950,y=130)   

#frame
frame=Frame(home,width=600,height=600,bg="white")
frame.place(x=100,y=80)
heading=Label(frame,text='Login',fg='#57a1f8',bg='white',font=('Poppins',19,'bold'))
heading.place(x=250,y=5)

#id password
#ID
Label(frame,text='User Id',fg='black',bg='white',font=('Poppins',17,'bold')).place(x=80,y=80)
user= Entry(frame,width=65,fg='black',border=2,bg="white",font=('Poppins',11))
user.place(x=30,y=120)
#uidlogo= ImageTk.PhotoImage("usernid.png")
#Label(frame,image=uidlogo).place()

    
#PASSWORD   
Label(frame,text='Password',fg='black',bg='white',font=('Poppins',17,'bold')).place(x=80,y=150)
password= Entry(frame,width=65,fg='black',border=2,bg="white",font=('Poppins',11))
password.place(x=30,y=190)

#button
Button(frame,width=39,pady=7,text='Login',bg='#57a1f8',fg='white',border=0).place(x=160,y=240)



home.mainloop()