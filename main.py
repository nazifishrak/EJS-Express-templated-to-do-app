
from tkinter import *

from functionality.bmi_calculator import calculate_bmi, comment

# Creating the window
window = Tk()
window.title("BMI Calculator")
window.minsize(width=500, height=500)
window.config(padx=20, pady=30)


# Top Label
label = Label(text="Calculate your BMI", font= ("Century Gothic", 24, "bold"))
label.grid(row=0,column =0)

# Text Input
height_label1 = Label(text="Height in ft", font = ("Courier New", 12, "normal"))
height_label1.grid(row=1, column = 0)
text_input_x = Entry()
text_input_x.grid(row=1,column=1)

height_label2 = Label(text="Height in inches", font = ("Courier New", 12, "normal"))
height_label2.grid(row=2, column = 0)
text_input_y = Entry()
text_input_y.grid(row=2,column=1)


weight_label = Label(text="mass in kg", font = ("Courier New", 12, "normal"))
weight_label.grid(row=3, column = 0)
text_input_w = Entry()
text_input_w.grid(row=3,column=1)




# Calculate Button
def calculate_button_command():
    height_feet= (text_input_x.get())
    height_inch= (text_input_y.get())
    weight= (text_input_w.get())
    bmi = calculate_bmi(int(height_feet), int(height_inch), int(weight))
    bmi_output.config(text=f"Your BMI is {round(bmi,2)}")
    return bmi

button = Button(text="Calculate", command=calculate_button_command)
button.grid(row=4,column=1)


bmi_output = Label(text=f"", font= ("Courier New", 24, "bold"))
bmi_output.grid(row=5,column=1)

def show_comment():
    height_feet= (text_input_x.get())
    height_inch= (text_input_y.get())   
    bmi_comment.config(text=f"{comment(calculate_button_command(), x=int(height_feet), y=int(height_inch))}")


button_comment = Button(text="Show comments", command=show_comment)
button_comment.grid(row=6,column=1)
bmi_comment = Label(text=f"", font= ("Courier New", 18, "bold"))
bmi_comment.grid(row=7,column=1)
window.mainloop()