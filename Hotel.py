from Room import Room


class Hotel:
    """
    Клас що представляє готель та містить його назву,
    рейтинг, місто в якому знаходиться, кімнати та чорний список.
    """

    def __init__(self, name, stars_rating, city):
        self.__name = name
        self.__stars_rating = stars_rating
        self.__city = city
        self.__rooms = []
        self.__blacklist = []

    def add_room(self, room):
        """
        Метод для додавання кімнати у готель.
        """

        if type(room) == Room:
            if room in self.__rooms:
                print("Цей номер вже є в готелі.")
            else:
                room.set_hotel(self)
                self.__rooms.append(room)
                print(f"Номер {room.get_num()} додано до готелю {self.__name}.")
        else:
            print("Об'єкт не є кімнатою.")

    def add_customer_to_blacklist(self, customer):
        """
        Метод для додавання клієнта у чорний список.
        """

        if customer not in self.__blacklist:
            self.__blacklist.append(customer)
            print("Користувач доданий у чорний список.")

    def get_available_rooms(self, entry_date, exit_date):
        """
        Повертає список доступних кімнат на вказаний період.
        """

        available_rooms = []
        for room in self.__rooms:
            if room.is_available(entry_date, exit_date):
                available_rooms.append(room)
        return available_rooms

    def get_name(self):
        return self.__name

    def get_stars_rating(self):
        return self.__stars_rating

    def get_city(self):
        return self.__city

    def get_rooms(self):
        return self.__rooms

    def get_blacklist(self):
        return self.__blacklist