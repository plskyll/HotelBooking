from datetime import datetime

class Booking:
    """
    Клас який представляє бронювання та містить основну інформацію про нього.
    """

    def __init__(self, customer, room, entry_date, exit_date, num_guests, entry_time="14:00", exit_time="12:00",
                 options=None):
        if not self.__validation(customer, room, entry_date, exit_date, num_guests, entry_time, exit_time):
            raise ValueError("Бронювання не створено.")

        self.__customer = customer
        self.__room = room
        self.__entry_date = entry_date
        self.__exit_date = exit_date
        self.__entry_time = entry_time
        self.__exit_time = exit_time
        self.__num_guests = num_guests
        self.__options = []

        room.add_booking(self)

    @staticmethod
    def __validation(customer, room, entry_date, exit_date, num_guests, entry_time, exit_time):
        """
        Метод валідує дані бронювання та перевіряє:
        - чи клієнт не у чорному списку
        - чи правильна дата заїзду та виїзду
        - чи правилльна кількість гостей для цього номеру
        - чи номер не зайнятий на вказані дати
        """

        if customer.get_phone_number() in room.get_hotel().get_blacklist():
            print("Клієнт у чорному списку")
            return False
        if entry_date > exit_date:
            print("Дата заїзду має бути раніше дати виїзду")
            return False
        if num_guests > (room.get_num_beds() * 2):
            print("Занадто багато гостей для цього номера")
            return False
        if not room.is_available(entry_date, exit_date):
            print("Номер зайнятий на ці дати")
            return False

        return True

    def cancel(self):
        if self in self.__room.get_bookings():
            self.__room.remove_booking(self)
            print("Бронювання скасовано.")

            choice = input("Додати користувача у чорний список(так/ні)?: ")
            if choice.lower() == "так":
                self.__room.get_hotel().add_customer_to_blacklist(self.__customer)

    def get_customer(self):
        return self.__customer

    def get_room(self):
        return self.__room

    def get_entry_date(self):
        return self.__entry_date

    def get_exit_date(self):
        return self.__exit_date

    def get_entry_time(self):
        return self.__entry_time

    def get_exit_time(self):
        return self.__exit_time

    def get_num_guests(self):
        return self.__num_guests

    def get_options(self):
        return self.__options