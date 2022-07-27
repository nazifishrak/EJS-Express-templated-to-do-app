
from tkinter import *

from bmi_calculator import calculate_bmi

# Creating the window
window = Tk()
window.title("BMI Calculator")
window.minsize(width=500, height=500)


# Top Label
label = Label(text="Calculate your BMI", font= ("Arial", 24, "bold"))
label.pack()

# Text Input
text_input = Entry(width=20)
text_input.pack()



# Calculate Button

button = Button(text="Calculate", command=calculate_bmi)





window.mainloop()