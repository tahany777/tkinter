from tkinter import *
from tkinter import messagebox

age_app = Tk()

# change App Text

age_app.title('Tahani age app')

# set Dimensions

age_app.geometry("400x200")

# Write Age Label
the_text = Label(age_app, text="write your age", height=2, font=("Arial", 20))

the_text.pack() #Place The Text Into the main window
#Age variables

age = StringVar()

#set default value for age
age.set("00")
# create input age
age_input = Entry(age_app, width=2, font=("Arial", 30), textvariable=age)
age_input.pack() #Place the Input Into the main window



def calc():
    # Get Age In years
    the_age_value = age.get()

    # Get Time Units
    months = int(the_age_value) * 12
    weeks = months * 4
    days = int(the_age_value) * 365

    line_one = f"Your Age In Months Is: {months}"
    line_two = f"Your Age In Weeks Is: {weeks}"
    line_three = f"your Age In Days Is: {days}"

    all_lines = [line_one, line_two, line_three]
    messagebox.showinfo('Your Age', "\n".join(all_lines))


# create the calculate button
btn = Button(age_app, text="Calculate Age", width=20, height=2, bg="#e91e63", fg='white', borderwidth=0, command=calc)
btn.pack()
age_app.mainloop()
