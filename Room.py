class Room:
    """
    Клас, що представляє готельний номер та містить
    інформацію про його тип, кількість ліжок, зручності тощо.
    """

    num_rooms = []

    def __init__(self, num, type_room, num_beds, comforts, price, hotel=None):
        self.__num = num
        self.__type_room = type_room
        self.__num_beds = num_beds
        self.__comforts = comforts
        self.__price = price
        self.__bookings = []
        self.__hotel = hotel

        Room.num_rooms.append(num)

    def is_available(self, customer_entry, customer_exit):
        """
        Метод перевіряє, чи обраний номер(апартамент) доступний на вказаний період.
        """

        for booking in self.__bookings:
            if not (booking.get_exit_date() <= customer_entry or booking.get_entry_date() >= customer_exit):
                return False
        return True

    @staticmethod
    def num_is_available(num):
        """
        Перевіряє, чи доступний номер(ідентифікатор) кімнати для створення.
        """

        if num in Room.num_rooms:
            print("Апартамент під таким номером вже існує.")
            return False
        else:
            return True

    def add_booking(self, booking):
        """
        Метод для додавання бронювань номеру.
        """

        self.__bookings.append(booking)

    def remove_booking(self, booking):
        """
        Метод для видалення бронювання зі списку бронювань.
        """

        self.__bookings.remove(booking)

    def get_num(self):
        return self.__num

    def get_type_room(self):
        return self.__type_room

    def get_comforts(self):
        return self.__comforts

    def get_price(self):
        return self.__price

    def get_hotel(self):
        return self.__hotel

    def get_bookings(self):
        return self.__bookings

    def get_num_beds(self):
        return self.__num_beds

    def set_hotel(self, hotel):
        self.__hotel = hotel