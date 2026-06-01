from address import Address


class Mailing:

    def __init__(
        self,
        to_address: Address,
        from_address: Address,
        track: str,
        cost: float
    ):

        self.track = track
        self.from_address = from_address
        self.to_address = to_address
        self.cost = cost

    def __str__(self) -> str:

        return (f"Отправление {self.track} из {self.from_address} "
                f"в {self.to_address}. Стоимость {self.cost} руб.")

    def __repr__(self) -> str:
        return (
                f"Mailing(track='{self.track}', "
                f"from_address={self.from_address!r}, "
                f"to_address={self.to_address!r}, "
                f"cost={self.cost})"
                )
