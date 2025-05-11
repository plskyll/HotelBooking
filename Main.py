from datetime import datetime
from Hotel import Hotel
from Room import Room
from Customer import Customer
from Booking import Booking


def main():
    hotels = []
    customers = []
    bookings = []

    while True:
        print("\n===== СИСТЕМА БРОНЮВАННЯ ГОТЕЛІВ =====")
        print("1. Створити готель")
        print("2. Додати номер до готелю")
        print("3. Зареєструвати клієнта")
        print("4. Забронювати номер")
        print("5. Скасувати бронювання")
        print("6. Вийти")
        print("=====================================")

        choice = int(input("Виберіть номер операції: "))

        if choice == 1:
            name = input("Введіть назву готелю: ")
            stars = input("Введіть рейтинг готелю в зірках : ")
            city = input("Введіть місто: ")

            hotel = Hotel(name, stars, city)
            hotels.append(hotel)
            print(f"Готель '{name}' успішно створено!")

        elif choice == 2:
            if not hotels:
                print("Спочатку створіть хоча б один готель!")
                continue

            print("Доступні готелі:")

            index = 1
            for hotel in hotels:
                print(f"{index}. {hotel.get_name()}, {hotel.get_city()}")
                index += 1

            hotel_idx = int(input("Виберіть номер готелю: ")) - 1
            room_num = input("Введіть номер кімнати: ")
            room_type = input("Введіть тип кімнати: ")
            beds = int(input("Введіть кількість ліжок: "))
            comforts = input("Введіть зручності (через кому): ").split(",")
            price = int(input("Введіть ціну за ніч: "))

            room = Room(room_num, room_type, beds, comforts, price)
            hotels[hotel_idx].add_room(room)


        elif choice == 3:
            name = input("Введіть ім'я клієнта: ")
            surname = input("Введіть прізвище клієнта: ")
            phone = input("Введіть номер телефону: +38")

            customer = Customer(name, surname, phone)
            customers.append(customer)

            print(f"Клієнт {name} {surname} успішно зареєстрований!")

        elif choice == 4:
            if not hotels or not customers:
                print("Необхідно спочатку створити готель і зареєструвати клієнта!")
                continue

            print("Виберіть клієнта:")

            index = 1
            for customer in customers:
                print(f"{index}. {customer.get_name()} {customer.get_surname()}")
                index += 1

            customer_idx = int(input("Номер клієнта: ")) - 1

            print("Виберіть готель:")
            index = 1
            for hotel in hotels:
                print(f"{index}. {hotel.get_name()}, {hotel.get_city()}")
                index += 1

            hotel_idx = int(input("Номер готелю: ")) - 1

            entry_date = datetime.strptime(input("Дата заїзду (ДД.ММ.РРРР): "), "%d.%m.%Y").date()
            exit_date = datetime.strptime(input("Дата виїзду (ДД.ММ.РРРР): "), "%d.%m.%Y").date()

            available_rooms = hotels[hotel_idx].get_available_rooms(entry_date, exit_date)

            if not available_rooms:
                print("На вказані дати немає доступних номерів!")
                continue

            print("Доступні номери:")

            index = 1
            for room in available_rooms:
                print(f"{index}. Номер {room.get_num()}, тип: {room.get_type_room()}, ціна: {room.get_price()} грн/ніч")
                index += 1

            room_idx = int(input("Виберіть номер кімнати: ")) - 1
            guests = int(input(f"Введіть кількість гостей: "))

            booking = Booking(customers[customer_idx], available_rooms[room_idx], entry_date, exit_date, guests)
            bookings.append(booking)
            print("Бронювання успішно створено!")

        elif choice == 5:
            if not bookings:
                print("Немає жодного активного бронювання!")
                continue

            print("Список активних бронювань:")
            for i in range(len(bookings)):
                for booking in bookings:
                    customer = booking.get_customer()
                    room = booking.get_room()
                    print(f"{i + 1}. {customer.get_name()} {customer.get_surname()}, Кімната {room.get_num()}")

            booking_idx = int(input("Виберіть номер бронювання для скасування: ")) - 1
            booking = bookings[booking_idx]
            booking.cancel()
            bookings.remove(booking)

        elif choice == 6:
            print("Дякуємо за використання системи бронювання готелів!")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")


main()