class Customer:
    """
    Клас, що представляє клієнта системи та містить його особисті дані.
    """

    phone_numbers = []

    def __init__(self, name, surname, phone_number):
        if not self.__validate_phone_number(phone_number):
            raise ValueError("Користувача не створено.")

        self.__name = name
        self.__surname = surname
        self.__phone_number = self.__format_phone_number(phone_number)

        Customer.phone_numbers.append(self.__phone_number)

    def __validate_phone_number(self, phone_number):
        """
        Метод, що перевіряє валідність номера телефону.
        """

        phone_number = self.__format_phone_number(phone_number)

        if phone_number in Customer.phone_numbers:
            print("Такий номер вже існує.")
            return False
        if len(phone_number) != 13:
            print("Ви ввели не 10 цифр.")
            return False
        if not phone_number[1:].isdigit():
            print("Номер має складатись з цифр.")
            return False
        if phone_number[3] != "0":
            return False

        return True

    @staticmethod
    def __format_phone_number(phone_number):
        """
        Метод, який форматує номер телефону.
        """

        if phone_number.startswith("+38"):
            return phone_number
        return f"+38{phone_number}"

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_phone_number(self):
        return self.__phone_number
