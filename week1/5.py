""" Write a Python program to calculate body mass index.
formula : BMI = weight(kg)/height*height(m) """

weight = float(input("Input your weight in Kilogram: "))
height = float(input("Input your height in meters: "))
print("Your body mass index is: ", round(weight / (height * height), 2))

""" Input your weight in Kilogram: 65
Input your height in meters: 1.68
Your body mass index is:  23.03 """