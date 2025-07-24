

def Day2_learning ():
 print(123456789)

 print(type(123.235))
 print(type(123))
 print(type("456"))
 print(type(False))

 val = int("456")
 data = str(val)
 print(val)  #int() converts to int
 print(data)


def BMI_calculator():
 print("BMI calculator")
 weight  = 84
 height  = 1.65
 BMI = weight / (height*height)
 print(f"BMI: {BMI} | Rounded: {round(BMI)}")  # f is stands for formatted string literal, also known as an f-string. converts into string like snprintf


def TIP_calculator():
 print("TIP calculator")
 Bill = 50
 Tip  = 10.25
 Total  = Bill + ((Tip/100)* Bill)
 print(f"Total bill : {Total}")



