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


def signup():
    username = user.get()
    password = code.get()
    confirm_password = con_code.get()

    if password == confirm_password:
        try:
            with open("datasheet.json", "r+") as file:
                data = json.load(file)
                data[username] = password
                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()

            messagebox.showinfo("Signup", "Successfully Sign Up")
            root.destroy()
            subprocess.run(["python", "Login.py"])

        except:
            with open("datasheet.json", "w") as file:
                data = {username: password}
                json.dump(data, file, indent=4)

    else:
        messagebox.showerror("Invalid", "Both Passwords Should Match")


        

#Redirect to Login Page
def sign():
    root.destroy()
    subprocess.run(["python", "Login.py"])
    

#Images
image = Image.open("images/login.png")
resize_image = image.resize((130,130))
img = ImageTk.PhotoImage(resize_image)
Label(root, image=img, bg="#fff").place(x=250, y=90)

#Heading
heading = Label(root, text="Sign Up", fg="#57a1f8", bg="#fff", font=("Microsoft YaHei UI Light", 23, "bold"))
heading.place(x=255, y=30)

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

#########----------------------------------------

def toggle_conpas():
    if con_code.cget("show") == '':
        con_code.config(show='*')
        toggle_btn2.config(image=resize_show1)
    else:
        con_code.config(show='')
        toggle_btn2.config(image=resize_hide1)
        
        
show_image = PhotoImage(file =r"images/show.png")
resize_show1 = show_image.subsample(45,45)

hide_image = PhotoImage(file =r"images/hide.png")
resize_hide1 = hide_image.subsample(45,45)
        
toggle_btn2 = Button(root, image=resize_show1, bg="#fff", border=0, compound=LEFT, command=toggle_conpas)
toggle_btn2.place(x=410, y=380)


def on_enter(e):
    name=con_code.get()
    if name=="Confirm Password":
        con_code.delete(0, "end")
        con_code.config(show="*")
        
    
def on_leave(e):
    name=con_code.get()
    if name=="":
        con_code.insert(0,"Confirm Password")
        con_code.config(show="")
        

con_code = Entry(frame, width=25, fg="black", border=0, bg="#fff", font=("Microsoft YaHei UI Light", 11))
con_code.place(x=25, y=140)
con_code.insert(0, "Confirm Password")
con_code.bind("<FocusIn>", on_enter)
con_code.bind("<FocusOut>", on_leave)

Frame(frame,width=295, height=2, bg="black").place(x=15, y=165)

#################################################

Button(frame, width=30, pady=7, text="Sign Up", bg="#57a1f8", fg="#fff", border=0, command=signup).place(x=23, y=190)
label = Label(frame, text="Have an Account?", fg="black", bg="#fff", font=("Microsoft YaHei UI Light", 9))
label.place(x=50, y=230)

log_in = Button(frame, width=6, text="Login", border=0, bg="#fff", cursor="hand2", fg="#57a1f8", command=sign)
log_in.place(x=155, y=230)



root.mainloop()