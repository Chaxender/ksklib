def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

weight = float(input("Kilonuzu girin (kg): "))
height = float(input("Boyunuzu girin (metre): "))
bmi = calculate_bmi(weight, height)
print(f"BMI Değeriniz: {bmi}")

if bmi < 18.5:
    print("Zayıf")
elif 18.5 <= bmi < 24.9:
    print("Normal")
elif 25 <= bmi < 29.9:
    print("Fazla kilolu")
else:
    print("Obez")
