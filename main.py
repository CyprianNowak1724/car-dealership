from car import Car

garage = []
is_running = True

while is_running:
    print("=== KOMIS SAMOCHODOWY ===")
    print("1 - Dodaj samochod")
    print("2 - Wyswietl samochody")
    print("3 - Usun samochod")
    print("4 - Szukaj samochodu")
    print("5 - Wyjdz")

    action = int(input("Wybierz akcje: "))

    match action:
        case 1:
            brand = input("Podaj marke: ")
            model = input("Podaj model: ")
            year = int(input("Podaj rok produkcji: "))
            horsepower = int(input("Podaj moc: "))
            price = float(input("Podaj cene: "))

            new_car = Car(brand, model, year, horsepower, price)
            garage.append(new_car)

            print("Samochod zostal dodany do garazu.")
        case 2:
            if len(garage) == 0:
                print("Brak samochodow w garazu.")
            else:
                for car in garage:
                    car.show_info()
        case 3:
            if len(garage) == 0:
                print("Brak samochodow w garazu.")
            else:
                for index, car in enumerate(garage):
                    print(f"{index} - {car.brand} {car.model}")
                car_index = int(input("Podaj numer samochodu do usuniecia: "))
                if car_index < 0 or car_index >= len(garage):
                    print("Nieprawidlowy numer samochodu.")
                else:
                    removed_car = garage.pop(car_index)
                    print(f"Samochod {removed_car.brand} {removed_car.model} zostal usuniety z garazu.")
        case 4:
            found = False
            
            if len(garage) == 0:
                print("Brak samochodow w garazu.")
            else:
                search_brand = input("Podaj marke samochodu do wyszukania: ")
                for car in garage:
                    if car.brand.lower() == search_brand.lower():
                        car.show_info()
                        found = True
                if not found:
                    print(f"Nie znaleziono samochodow marki {search_brand}.")
                
        case 5:
            is_running = False
            print("Dziekujemy za skorzystanie z naszego komisu samochodowego.")