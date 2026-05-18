class Address:

    def __init__(self, index=None, city=None, street=None,
                 house=None, apartment=None):

        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

        def __str__(self):

            parts = []

            if self.index:
                parts.append(f"Индекс: {self.index}")

            if self.city:
                parts.append(f"г. {self.city}")

            if self.street:
                parts.append(f"ул. {self.street}")

            if self.house:
                parts.append(f"д. {self.house}")

            if self.apartment:
                parts.append(f"кв. {self.apartment}")

            return ", ".join(parts) if parts else "Адрес не указан"

    def to_dict(self):

        return {
            'index': self.index,
            'city': self.city,
            'street': self.street,
            'house': self.house,
            'apartment': self.apartment
        }

    @classmethod
    def from_dict(cls, data):

        return cls(
            index=data.get('index'),
            city=data.get('city'),
            street=data.get('street'),
            house=data.get('house'),
            apartment=data.get('apartment')
        )
