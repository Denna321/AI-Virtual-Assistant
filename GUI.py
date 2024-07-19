from tkinter import *
from PIL import Image,ImageTk
import action
import spt
import textto


root=Tk()
root.title("AI ASSISTANT")
root.geometry("550x675")
root.resizable(True,True)
root.config(bg="#6ecc87")
def ask():
    userval=spt.speech_to_text()
    botval=action.Action(userval)
    text.insert(END, "Me --> "+userval+"\n") 
    if botval != None:
       text.insert(END, "Bot <-- "+ str(botval)+"\n")
    if botval == "ok sir":
        root.destroy()
def User_send():
    send=entry1.get()
    bot=action.Action(send)
    text.insert(END, "User --> "+send+"\n")
    if bot != None:
       text.insert(END, "Bot <-- "+ str(bot)+"\n")
    if bot == "ok sir":
        root.destroy() 
def delete_text():
     text.delete('1.0',"end")

frame=LabelFrame(root,padx=10,pady=7,borderwidth=3,relief="raised")
frame.config(bg="#fcca03")
frame.grid(row=0,column=1,padx=55,pady=15)


image_get=ImageTk.PhotoImage(Image.open("ass1.png"))
image_label=Label(frame,image=image_get)
image_label.grid(row=1,column=0,pady=20)

text_label=Label(frame,text="YOUR AI FRIEND IN NEED!",font=(("comic Sans ms"),14,"bold"),bg="#c37fdb")
text_label.grid(row=0,column=0,padx=20,pady=10)


text=Text(root , font= ('Courier 10 bold') , bg = "#356696")
text.grid(row = 2,  column= 0)
text.place(x= 50, y= 450, width= 375, height= 100) 



entry1 = Entry(root, justify = CENTER)
entry1.place(x=50 , y = 580 , width= 350, height= 30)

button1 =  Button(root,  text="ASK" , bg="#356696" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,  command=ask)
button1.place(x= 70, y= 615)

# Add a text button2
button2 =  Button(root,  text="Send" , bg="#356696" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,  command=User_send)
button2.place(x= 170, y= 615)

# Add a text button3
button3 = Button(root, text="Delete", bg="#356696" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,command=delete_text)
button3.place(x= 250, y= 615)

root.mainloop()