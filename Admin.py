from tkinter import*
import tkinter as tk

def test_open_new_page():
    new_page = tk.Toplevel(root)

root=tk.Tk()
root.title("Admin Page")
root.geometry("625x600+400+100")

student_heading = Label(root, text="STUDENT", font=("Microsoft YaHei UI Light", 23, "bold"))
student_add = tk.Button(root, text="• Add student", font=("Microsoft YaHei UI Light", 12, "bold"), fg="blue", cursor="hand2", width=30)
student_remove = tk.Button(root, text="• Remove student", font=("Microsoft YaHei UI Light", 12, "bold"), fg="blue", cursor="hand2", width=30)
student_update = tk.Button(root, text="• Update student", font=("Microsoft YaHei UI Light", 12, "bold"), fg="blue", cursor="hand2", width=30)

course_heading = Label(root, text="COURSES", font=("Microsoft YaHei UI Light", 23, "bold"))
course_add = tk.Button(root, text="• Add course", font=("Microsoft YaHei UI Light", 12, "bold"), fg="blue", cursor="hand2", width=30)
course_remove = tk.Button(root, text="• Remove course", font=("Microsoft YaHei UI Light", 12, "bold"), fg="blue", cursor="hand2", width=30) 
course_update = tk.Button(root, text="• Update course", font=("Microsoft YaHei UI Light", 12, "bold"), fg="blue", cursor="hand2", width=30)

student_heading.grid(row=0, column=1)
student_add.grid(row=1, column=1)
student_remove.grid(row=2, column=1)
student_update.grid(row=3, column=1)

course_heading.grid(row=0, column=5)
course_add.grid(row=1, column=5)
course_remove.grid(row=2, column=5)
course_update.grid(row=3, column=5)

student_add.bind("<Button-1>", lambda e: test_open_new_page())


root.mainloop()


