# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI=round(weight/height**2,1)
B_M_I=round(BMI)
if BMI<18.5:
    print(f"Your BMI is {B_M_I}, you are underweight.")
elif BMI<25.0:
    print(f"Your BMI is {B_M_I}, you have a normal weight.")
elif BMI<30.0:
    print(f"Your BMI is {B_M_I}, you are slightly overweight.")
elif BMI<35.0:
    print(f"Your BMI is {B_M_I}, you are obese.")
else:
    print(f"Your BMI is {B_M_I},you are clinically obese.")



