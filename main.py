from car import Car

list = []
bmw = Car("BMW", "M3", 2021, 480, 300000)
mercedes = Car("Mercedes", "C63 AMG", 2020, 510, 350000)
audi = Car("Audi", "RS5", 2022, 450, 320000)
list.append(bmw)
list.append(mercedes)
list.append(audi)

for car in list:
    car.show_info()
    print("--------------------")

print(f"Liczba samochodow w garazu: {len(list)}")