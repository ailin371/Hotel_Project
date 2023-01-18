from datetime import datetime
from models.booking import Booking
from models.costumer import Customer
from models.room import Room, RoomType
from table import Table
rooms_table = Table("tables/rooms.json",
                    ["id", "size", "capacity", "number_of_beds", "type", "price"], "id")
booking_table = Table("tables/bookings.json",
                      ["cutomer_id", "room_id", "arrival_date", "departure_date", "total_price", "id"], "id")
customers_table = Table("tables/customers.json",
                        ["id", "name", "address", "city", "email", "age"], "id")


def main_menu():
    print("Hello and welcome to our California hotel! What would you like to do?")
    print("1. Add a new room")
    print("2. Display all rooms")
    print("3. Display available rooms for a specific date")
    print("4. Find a room by type")
    print("5. Find room by number")
    print("6. Remove room")
    print("7. Book a room")
    print("8. Cancel booking")
    print("9. Display all bookings")
    print("10. Display booked rooms for a specefic date")
    print("11. Add a new customer")
    print("12. Display all customers")
    print("13. Find customer by name")
    print("14. Remove customer")

    selection = input()
    if selection == "1":
        add_room()
    elif selection == "2":
        print("Here are all the rooms in California hotel: ")
        display_rooms()
    elif selection == "3":
        print("Here are all the rooms for the specific date you asked: ")
    elif selection == "4":
        find_room_by_type()
    elif selection == "5":
        find_room_by_num()
    elif selection == "6":
        remove_room()
    elif selection == "7":
        print("The room was booked.")
    elif selection == "8":
        print("The booking was canceled.")
    elif selection == "9":
        print("Here are all the bookings: ")
    elif selection == "10":
        print("Here are the rooms you asked to see by date: ")
    elif selection == "11":
        add_customer()
    elif selection == "12":
        display_customers()
    elif selection == "13":
        find_customer_by_name()
    elif selection == "14":
        remove_customer()
    else:
        print("Invalid option, please choose what would you like to do from the menu")


def ask_room_number():
    return input("Please enter the room number: ")


def ask_room_type():
    print("Select room type: ")
    print(f"\t1. {RoomType.BASIC}")
    print(f"\t2. {RoomType.DELUXE}")
    print(f"\t3. {RoomType.SUITE}")
    selected_type = input()
    if selected_type == "1":
        roomtype = RoomType.BASIC
    elif selected_type == "2":
        roomtype = RoomType.DELUXE
    elif selected_type == "3":
        roomtype = RoomType.SUITE
    else:
        raise Exception("Invalid option")
    return roomtype


def add_room():
    id = input("Please enter the room number: ")
    size = float(input("Enter the room size: "))
    capacity = int(input("Enter the room capacity: "))
    number_of_beds = int(input("Enter the room number_of_beds: "))
    roomtype = ask_room_type()

    price = float(input("Enter the room price: "))
    room = Room(id, size, capacity, number_of_beds, roomtype, price)
    added_room = rooms_table.add(room)
    print(added_room)


def display_rooms():
    rooms_table.print()


def find_available_rooms(date: datetime):
    return


def display_available_rooms():
    date = input("Please enter the date: ")
    available_rooms = find_available_rooms(date)
    return


def find_room_by_type():
    room_type = ask_room_type()
    room = rooms_table.find("type", room_type)
    print(room)


def find_room_by_num():
    room_num = ask_room_number()
    room = rooms_table.find("id", room_num)
    print(room)


def remove_room():
    room_num = ask_room_number()
    room = rooms_table.find("id", room_num)
    if room != None:
        rooms_table.delete(room_num)
        print(f'{room}\nhas been deleted')

# "cutomer_id", "room_id", "arrival_date", "departure_date", "total_price", "id"


def book_room():
    cutomer_id = input("Please enetr the customer's id: ")
    room_id = input("Please enetr the room's id: ")
    arrival_date = input("Please enetr the arrival date: ")
    departure_date = input("Please enetr the departure date: ")
    total_price = input("Please enetr the total price: ")
    booking = Booking()


def add_customer():
    id = int(input("Please enter the id: "))
    name = input("Please enter the name: ")
    address = input("Please enter the address: ")
    city = input("Please enter the city: ")
    email = input("Please enter the email: ")
    age = int(input("Please enter the age: "))

    customer = Customer(id, name, address, city, email, age)
    customer = customers_table.add(customer)
    print(customer)


def display_customers():
    customers_table.print()


def find_customer_by_name():
    customer_name = input("Please enter the customer name: ")
    customer = customers_table.find("name", customer_name)
    print(customer)


def remove_customer():
    customer_id = input("Please enter the customer's id: ")
    customer = customers_table.find("id", customer_id)
    if customer != None:
        customers_table.delete(customer_id)
        print(f'{customer}\nhas been deleted')
