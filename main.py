
from tkinter import *

from functionality.bmi_calculator import calculate_bmi, comment

# Creating the window
window = Tk()
window.title("BMI Calculator")
window.minsize(width=500, height=500)


# Top Label
label = Label(text="Calculate your BMI", font= ("Arial", 24, "bold"))
label.pack()

# Text Input
text_input_x = Entry(width=20)
text_input_x.pack()

text_input_y = Entry(width=20)
text_input_y.pack()

text_input_w = Entry(width=20)
text_input_w.pack()




# Calculate Button
def calculate_button_command():
    height_feet= (text_input_x.get())
    height_inch= (text_input_y.get())
    weight= (text_input_w.get())
    bmi = calculate_bmi(int(height_feet), int(height_inch), int(weight))
    bmi_output.config(text=f"Your BMI is {round(bmi,2)}")
    return bmi

button = Button(text="Calculate", command=calculate_button_command)
button.pack()


bmi_output = Label(text=f"", font= ("Arial", 24, "bold"))
bmi_output.pack()

def show_comment():
    height_feet= (text_input_x.get())
    height_inch= (text_input_y.get())   
    bmi_comment.config(text=f"{comment(calculate_button_command(), x=int(height_feet), y=int(height_inch))}")
    bmi_output.pack()


button_comment = Button(text="Show comments", command=show_comment)
button_comment.pack()
bmi_comment = Label(text=f"", font= ("Arial", 24, "bold"))
bmi_comment.pack()
window.mainloop()