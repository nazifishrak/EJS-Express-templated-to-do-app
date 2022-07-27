def calculate_bmi(x: float ,y: float ,w: float ) -> float:
    """
    Calculates the BMI 
    x: height in feet
    y: remainder heigh in Inch
    w: mass in kilograms
    """
    h=x*0.3048 + y*0.0254
    return w/h**2

def comment(bmi: int, **kwargs: float) -> str:
    h=kwargs.get("x")*0.3048 + kwargs.get("y")*0.0254
    if bmi > 25:
        return f"Overweight! Your weight should be more than {round(18.5*h**2,2)} kg but less than {round(25*h**2,2)} kg"
    elif bmi <18.5:
        return f"Underweight! Your weight should be more than {round(18.5*h**2,2)} kg but less than {round(25*h**2,2)} kg"
    else:
        return f"You are doing good."



