from tkinter import *
from tkinter.font import Font
from tkinter import messagebox

def open_course_selection():
    course_selection_window = Toplevel(root)
    course_selection_window.title("Course Selection")
    course_selection_window.geometry("300x100")
  
    course_label = Label(course_selection_window, text="Select a Course to enroll:")
    course_label.pack(anchor="center")
    
    course_var = StringVar()
    course_var.set("Select a Course", )
    
    course_options = ["Foundation", "Diploma", "Degree"]
    course_menu = OptionMenu(course_selection_window, course_var, *course_options)
    course_menu.pack()
    
    submit_button = Button(course_selection_window, text="Submit", command=lambda: submit_course(course_var.get(), course_selection_window))
    submit_button.pack()

def submit_course(selected_course, course_selection_window):
    if selected_course == "Select a Course":
        messagebox.showwarning("Invalid Action", "Please select a course.")
    else:
        course_status.set(selected_course)
        course_selection_window.destroy()
        timetable_view()

def open_timetable():
    timetable_window = Toplevel(root)
    timetable_window.title("Timetable")
    timetable_window.geometry("500x300")

    timetable_label = Label(timetable_window, text="Timetable")
    timetable_label.pack(anchor="w")
    
def timetable_view():
    global timetableb
    timetableb = Button(root, text="View Timetable", command=open_timetable)
    timetableb.grid(row=4, column=1, pady=10)

root = Tk()
root.geometry("400x200")
font_bold = Font(family="Calibri", size=16, weight="bold", )

# Defining
head = Label(root, text="USER PROFILE", font=(font_bold))
name = Label(root, text="NAME: ")
email = Label(root, text="EMAIL: ")
course = Label(root, text="COURSE: ")
course_status = StringVar()
course_status.set("Not Enrolled")
course_label = Label(root, textvariable=course_status)

# Display
head.grid(row=0, column=1)
name.grid(row=1, column=0, sticky="e")
email.grid(row=2, column=0, sticky="e")
course.grid(row=3, column=0, sticky="e")
course_label.grid(row=3, column=1, sticky="w")

enrollb = Button(root, text="Enroll", command=open_course_selection)
enrollb.grid(row=4, column=1, pady=10)

root.mainloop()
