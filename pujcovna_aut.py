name_of_folder = "python-course-2022/auta.txt"

with open(name_of_folder, encoding='utf-8') as entry:
    auta = entry.readlines()

print(auta)


auta_formated = [car.strip() for car in auta]
print(auta_formated)

auta_formated= [car.replace(",", ".") for car in auta_formated]
print(auta_formated)

auto_km = [car.split() for car in auta_formated]
print(auto_km)

auto_km = [[float(car[1])] for car in auto_km]
print(auto_km)

total = sum(sum(km) for km in auto_km)
print(total)


