

def bmi_cal(height,weight):
    bmi = weight / (height**2)
    bmi=round(bmi,2)

    if bmi < 18.5:
        Category=" Underweight"
    elif bmi < 25:
        Category=" Normal"
    elif bmi < 30:
        Category=" Overweight"
    else:
        Category=" Obese"

    return bmi,Category
        
height=float(input("Enter your height in meters: "))
weight=float(input("Enter your weight in Kilograms: "))    

if height <= 0 or weight <= 0:
    print("Invalid Input")
else:
    bmi,Category = bmi_cal(height,weight)
    print(f"BMI: {bmi} Kg/m^2") 
    print(f"Category:{Category}")
