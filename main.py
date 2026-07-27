from car import Car

garage = []
is_running = True

while is_running:
    print("=== KOMIS SAMOCHODOWY ===")
    print("1 - Dodaj samochod")
    print("2 - Wyswietl samochody")
    print("3 - Usun samochod")
    print("4 - Wyjdz")

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
                pass
        case 4:
            is_running = False
            print("Dziekujemy za skorzystanie z naszego komisu samochodowego.")