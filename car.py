class Car:
    def __init__(self, brand, model, year, horsepower, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.horsepower = horsepower
        self.price = price

    def show_info(self):
        print(f"Marka: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Rok Produkcji: {self.year}")
        print(f"Moc: {self.horsepower} KM")
        print(f"Cena: {self.price} PLN")

    def to_dict(self):
        return {
            "brand": self.brand,
            "model": self.model,
            "year": self.year,
            "horsepower": self.horsepower,
            "price": self.price
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["brand"], data["model"], data["year"], data["horsepower"], data["price"])
        