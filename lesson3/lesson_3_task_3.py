from address import Address
from mailing import Mailing

from_address = Address("198035", "Санкт-Петербург",
                       "ул.Невельская", "1", "212")

to_address = Address("196628", "Санкт-Петербург", "ул.Изборская", "3", "351")

mailing = Mailing(to_address, from_address, "track92135854", 100)

print(f"Отправление {mailing.track} из {mailing.from_address.index}, "
      f"{mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house} - "
      f"{mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. "
      f"Стоимость {mailing.cost} рублей.")
