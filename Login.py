from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import json
import subprocess

root=Tk()
root.title("Login")
root.geometry ("625x600+450+200")
root.configure(bg="#fff")
root.resizable(False,False)

def login():
    username = user.get()
    password = code.get()
    
    with open("datasheet.json", "r") as file:
        data = json.load(file)
    
    #print(r.keys())
    #print(r.values())
    
    #Admin redirect pages
    if username=="admin" and password=="1234":
        screen=Toplevel(root)
        screen.title("Course Registration")
        screen.geometry("825x600+400+200")
        screen.config(bg="#fff")
        
        Label(screen, text="Welcome Admin", bg="#fff", font=("Calibri(body)", 50, "bold")).pack(expand=True)
        
        screen.mainloop()
        
    #Redirect to Main Page
    elif username in data and password== data[username]:
        #Redirecting to main Page
        root.destroy()
        subprocess.run(["python", "CourseSelect.py"])
        
    else:
        messagebox.showerror("Invalid","Invalid Username or Password")

        
#Redirect to register page
def register():
    root.destroy()
    subprocess.run(["python", "Registration.py"])
        

#Images
image = Image.open("images/login.png")
resize_image = image.resize((130,130))
img = ImageTk.PhotoImage(resize_image)
Label(root, image=img, bg="#fff").place(x=250, y=90)

#Heading
heading = Label(root, text="User Login", fg="#57a1f8", bg="#fff", font=("Microsoft YaHei UI Light", 23, "bold"))
heading.place(x=240, y=30)

#Frame for Entry
frame= Frame(root, width=250, height=250, bg="#fff")
frame.place(x=190, y=240)

#########----------------------------------------

def on_enter(e):
    user.delete(0, "end")
    
    
def on_leave(e):
    name=user.get()
    if name=="":
        user.insert(0,"Username")


user = Entry(frame, width=25, fg="black", border=0, bg="#fff", font=("Microsoft YaHei UI Light", 11))
user.place(x=25)
user.insert(0, "Username")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame,width=295, height=2, bg="black").place(x=15, y=25)

#########----------------------------------------

def toggle_password():
    if code.cget("show") == '':
        code.config(show='*')
        toggle_btn1.config(image=resize_show)
    else:
        code.config(show='')
        toggle_btn1.config(image=resize_hide)
        
        
show_image = PhotoImage(file =r"images/show.png")
resize_show = show_image.subsample(45,45)

hide_image = PhotoImage(file =r"images/hide.png")
resize_hide = hide_image.subsample(45,45)
        
toggle_btn1 = Button(root, image=resize_show, bg="#fff", border=0, compound=LEFT, command=toggle_password)
toggle_btn1.place(x=410, y=310)


def on_enter(e):
    name=code.get()
    if name=="Password":
        code.delete(0, "end")
        code.config(show="*")
        
    
def on_leave(e):
    name=code.get()
    if name=="":
        code.insert(0,"Password")
        code.config(show="")
        

code = Entry(frame, width=25, fg="black", border=0, bg="#fff", font=("Microsoft YaHei UI Light", 11))
code.place(x=25, y=70)
code.insert(0, "Password")
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)

Frame(frame,width=295, height=2, bg="black").place(x=15, y=95)

#################################################

Button(frame, width=30, pady=7, text="Login", bg="#57a1f8", fg="#fff", border=0, command=login).place(x=23, y=130)
label = Label(frame, text="Don't Have an Account?", fg="black", bg="#fff", font=("Microsoft YaHei UI Light", 9))
label.place(x=30, y=180)

sign_up = Button(frame, width=6, text="Sign Up", border=0, bg="#fff", cursor="hand2", fg="#57a1f8", command=register)
sign_up.place(x=185, y=180)



root.mainloop()