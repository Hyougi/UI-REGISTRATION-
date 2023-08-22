from tkinter import*
import tkinter as tk

root=tk.Tk()
root.title("Admin Page")
root.geometry("625x600+400+100")
root.configure(bg="white")
root.resizable(False,False)


def test_open_new_page():
    new_page = tk.Toplevel(root)
    
frame1 = Frame(root, width=430, height=100, bg="#fff")
frame1.place(x=100, y=30)

frame2 = Frame(root, width=430, height=400, bg="white")
frame2.place(x=100, y=140)

student_heading = Label(frame1, text="STUDENT",bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
student_add = tk.Button(frame2, text="• Add student", bg="white", font=("Microsoft YaHei UI Light", 12, "bold"), fg="blue", cursor="hand2", width=15)
student_remove = tk.Button(frame2, text="• Remove student", bg="white", font=("Microsoft YaHei UI Light", 12, "bold"), fg="blue", cursor="hand2", width=15)
student_update = tk.Button(frame2, text="• Update student", bg="white", font=("Microsoft YaHei UI Light", 12, "bold"), fg="blue", cursor="hand2", width=15)

course_heading = Label(frame1, text="COURSES",bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
course_add = tk.Button(frame2, text="• Add course", bg="white", font=("Microsoft YaHei UI Light", 12, "bold"), fg="blue", cursor="hand2", width=15)
course_remove = tk.Button(frame2, text="• Remove course", bg="white", font=("Microsoft YaHei UI Light", 12, "bold"), fg="blue", cursor="hand2", width=15) 
course_update = tk.Button(frame2, text="• Update course", bg="white", font=("Microsoft YaHei UI Light", 12, "bold"), fg="blue", cursor="hand2", width=15)


student_heading.place(x=10, y=30)
student_add.place(x=10, y=30)
student_remove.place(x=10, y=80)
student_update.place(x=10, y=130)

course_heading.place(x=270, y=30)
course_add.place(x=270, y=30)
course_remove.place(x=270, y=80)
course_update.place(x=270, y=130)


student_add.bind("<Button-1>", lambda e: test_open_new_page())


root.mainloop()


