class Smartphone:
    def __init__(self, brand, model, phone_number):
        self.brand = brand
        self.model = model
        self.phone_number = phone_number


catalog = []

catalog.append(Smartphone("Honor X8", "TFY-LX", "+7-921-358-54-17"))
catalog.append(Smartphone("Honor 7A", "AUM-L29", "+7-921-865-85-08"))
catalog.append(Smartphone("Apple", "IPhone 17 Pro Max", "+7-821-345-67-89"))
catalog.append(Smartphone("Lenovo A536", "Cortex-A7", "+7-812-456-78-90"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 15 Pro", "+7-950-027-16-01"))

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. \
          {smartphone.phone_number}")
