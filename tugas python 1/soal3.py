print("Selamat datang di kalkulator BMI")
berat_badan = float(input("silakan masukan berat badan (dalam Kilogram) : "))
tinggi_badan = float(input("silakan masukan tinggi badan (dalam meter) :"))     
bmi = berat_badan / (tinggi_badan/100) **2
print(bmi)

if bmi <= 18.5 :
    print("kamu kurus")
elif bmi <= 24.9:
    print("berat badan anda normal")
elif bmi <= 29.2:
    print("berat badan anda berlebih")
else:
    print("badan kamu obesitas")