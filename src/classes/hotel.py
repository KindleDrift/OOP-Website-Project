from fasthtml.common import *
from datetime import datetime, timedelta
import uuid

class Hotel:
    def __init__(self, Room=None, Booking=None, Guest=None, Staff=None, Floor=None, Things=None):
        self.__floors = []
        self.__rooms = []
        self.__bookings = []
        self.__guests = []
        self.__staffs = []
        self.__transport = Transport()
        self.__laundry = Laundry()
        self.__food_ordering = FoodOrdering()

    @property
    def rooms(self):
        return self.__rooms

    @property
    def bookings(self): 
        return self.__bookings
    
    @property
    def guests(self):
        return self.__guests
    
    @property
    def staffs(self):
        return self.__staffs
    
    @property
    def transport(self):
        return self.__transport
    
    @property
    def laundry(self):
        return self.__laundry
    
    @property
    def food_ordering(self):
        return self.__food_ordering

    def create_room(self, room):
        self.__rooms.append(room)

    def get_room_by_id(self, room_id):
        for room in self.__rooms:
            if room.room_id == room_id:
                return room
        return None
    
    def get_role_by_id(self, user_id):
        for guest in self.__guests:
            if guest.user_id == user_id:
                return "Guest"
        for staff in self.__staffs:
            if staff.user_id == user_id:
                return "Staff"
        return None

    def get_guest_by_id(self, guest_id):
        for guest in self.__guests:
            if guest.user_id == guest_id:
                return guest
        return None
    
    def get_staff_by_id(self, staff_id):
        for staff in self.__staffs:
            if staff.user_id == staff_id:
                return staff
        return None

    def get_room_by_attribute(self, room_type=None, size=None, max_price=None, things=None, start_date=None, end_date=None):
        returned_room = []
        for room in self.rooms:
            print("GetROOM",room.room_id)
            if (room.status == 1) and \
                (room.type == room_type or room_type == "All") and \
                (room.size >= size) and (room.price <= max_price) and \
                ((all(thing in room.things for thing in things) or things == [None])) and \
                (self.check_room_availability(room.room_id, start_date, end_date)):
                returned_room.append(room)
        return returned_room
    
    def check_room_availability(self, room_id, start_date, end_date):
        room = self.get_room_by_id(room_id)
        for booking in self.bookings:
            if booking.room == room and (booking.status == "Staying" or booking.status == "Pending"):
                if (booking.start_date <= start_date and booking.end_date >= start_date) or \
                    (booking.start_date <= end_date and booking.end_date >= end_date) or \
                    (booking.start_date >= start_date and booking.end_date <= end_date):
                    return False
        return True
    
    def create_booking(self, guest, room, start_date, end_date):
        self.bookings.append(Booking(guest, room, start_date, end_date, "Pending"))
        return self.bookings[-1]
    
    def get_booking_by_id(self, booking_id):
        print("BookingID",booking_id)
        for booking in self.bookings:
            if booking.booking_id == booking_id:
                return booking
        return None

    def get_booking_of_guest(self, guest):
        return [booking for booking in self.bookings if booking.guest == guest]
    
    def create_guest(self, username, real_name, email, password):
        if any(guest.username == username for guest in self.guests):
            return "Username already exists"
        if any(guest.email == email for guest in self.guests):
            return "Email already exists"
        if any(staff.username == username for staff in self.staffs):
            return "Username already exists"
        if any(staff.email == email for staff in self.staffs):
            return "Email already exists"
        self.guests.append(Guest(username, real_name, email, password))
        return "Success"
    
    def create_staff(self, username, real_name, email, password):
        self.staffs.append(Staff(username, real_name, email, password))
        return "Success"
    
    def validate_user(self, email, password):
        for guest in self.guests:
            if guest.authenticate(email, password):
                return guest
        for staff in self.staffs:
            if staff.authenticate(email, password):
                return staff
        return None
    
    

class User:
    __id_counter = 1
    def __init__(self, username, real_name, email, password):
        self.__user_id = User.__id_counter
        self.__username = username
        self.__real_name = real_name
        self.__email = email
        self.__password = password
        User.__id_counter += 1

    @property
    def user_id(self):
        return self.__user_id
    
    @property
    def username(self):
        return self.__username
    
    @property
    def real_name(self):
        return self.__real_name

    @property
    def email(self):
        return self.__email

    def authenticate(self, email, password):
        if self.__email == email and self.__password == password:
            return True
        return False


class Guest(User):
    def __init__(self, username, real_name, password, email):
        super().__init__(username, real_name, password, email)
        self.__laundry_cart = Cart()
        self.__food_cart = Cart()

    @property
    def laundry_cart(self):
        return self.__laundry_cart
    
    def clear_laundry_cart(self):
        self.__laundry_cart.clear()

    @property
    def food_cart(self):
        return self.__food_cart
    
    def clear_food_cart(self):
        self.__food_cart.clear()


class Staff(User):
    def __init__(self, username, real_name, password, email):
        super().__init__(username, real_name, password, email)


class Floor:
    def __init__(self, floor_number):
        self.__floor_id = floor_number
        self.__rooms = []

class Things:
    pass


class Room:
    def __init__(self, room_id, type, size, price, status: bool, things: Things, image):
        self.__room_id = room_id
        self.__type = type
        self.__size = size
        self.__price = price
        self.__status = status
        self.__things = things
        self.__image = image
    
    @property
    def room_id(self):
        return self.__room_id
    
    @property
    def type(self):
        return self.__type
    
    @property
    def size(self):
        return self.__size
    
    @property
    def price(self):
        return self.__price
    
    @property
    def status(self):
        return self.__status
    
    @property
    def things(self):
        return self.__things
    
    @property
    def image(self):
        return self.__image
    

class Booking():
    current_booking_id = 1
    def __init__(self, guest=None, room=None, start_date=None, end_date=None, status=None):
        self.__booking_id = self.current_booking_id
        self.__guest = guest
        self.__room = room
        self.__start_date = start_date
        self.__end_date = end_date
        self.__status = status
        Booking.current_booking_id += 1

    @property
    def booking_id(self):
        return self.__booking_id
    
    @property
    def guest(self):
        return self.__guest

    @property
    def room(self):
        return self.__room

    @property
    def start_date(self):
        return self.__start_date
    
    @property
    def end_date(self):
        return self.__end_date

    @property
    def status(self):
        return self.__status
    

# ----- Service Related Classes ----- #
class Service:
    def __init__(self, name):
        self.__name = name
        self.__reservations = []

    @property
    def reservations(self):
        return self.__reservations
    
    @reservations.setter
    def reservations(self, reservations):
        self.__reservations = reservations


class ServiceReservation:
    def __init__(self, guest):
        self.__guest = guest
        self.__status = "Pending"
        self.__timestamp = datetime.now()

    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, status):
        if status in ["Pending", "Complete", "Cancelled"]:
            self.__status = status
        else:
            raise ValueError("Invalid status")


# Transport Service #
class Transport(Service):
    def __init__(self):
        super().__init__("Transport")
        self.__routes = []

    @property
    def routes(self):
        return self.__routes

    def create_route(self, location, staff, time):
        self.__routes.append(Route(location, staff, time))

    def find_available_routes(self, search: str):
        return [p for p in self.__routes if search.lower() in p.name.lower()]
    
    def get_available_routes(self):
        return [p for p in self.__routes if not p.is_reserved]
    
    def create_reservation(self, guest, route_name):
        for route in self.__routes:
            if route.name == route_name:
                if route.is_reserved:
                    return "Already booked"
                route.is_reserved = True
                order = TransportReservation(guest, route)
                self.__reservations.append(order)
                print(order)
                return order
        return "Route not found"
    

class TransportReservation(ServiceReservation):
    def __init__(self, guest, route):
        super().__init__(guest)
        self.__route = route

class Route:
    def __init__(self, name, staff, time):
        self.__name = name
        self.__staff = staff
        self.__time = time
        self.__is_reserved = False

    @property
    def name(self):
        return self.__name
    
    @property
    def staff(self):
        return self.__staff
    
    @property
    def time(self):
        return self.__time
    
    @property
    def is_reserved(self):
        return self.__is_reserved
    
    @is_reserved.setter
    def is_reserved(self, status):
        self.__is_reserved = status

# Laundry Service #
class Laundry(Service):
    def __init__(self):
        super().__init__("Laundry")
        self.__cloths = []
        self.__orders = []  # Stores LaundryOrder objects

    @property
    def cloths(self):
        return self.__cloths

    def create_cloth(self, type, price):    
        self.__cloths.append(Cloth(type, price))

    def get_cloth_type(self, type_name):
        for cloth in self.__cloths:
            if cloth.name == type_name:
                return cloth
        return None

    def confirm_order(self, guest, cart):
        order = LaundryReservation(guest, cart.items.copy(), cart.total())
        self.__orders.append(order)
        print("Laundry order confirmed:", order)  # Debug print to console only
        return order
    

class LaundryReservation(ServiceReservation):
    def __init__(self, guest, items, total):
        super().__init__(guest)
        # Use the same generic key "product" so that for cloth items, it shows the cloth name
        self.__items = [{"name": item["product"].name, "amount": item["quantity"]} for item in items.values()]
        self.__total = total


class Cloth:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price


class FoodOrdering(Service):
    def __init__(self):
        super().__init__("Food Ordering")
        self.__dishes = []

    @property
    def dishes(self):
        return self.__dishes

    def find_dish(self, dish_name):
        for dish in self.__dishes:
            if dish.name == dish_name:
                return dish
        return None


    def restock(self, name, amount):
        dish = self.find_dish(name)
        if dish is None:
            return "Error"
        else:
            dish.amount += amount

    def add_new_menu(self, name, price, image_url):
        self.__dishes.append(Dish(name, price, image_url))

    def create_food_order(self, guest, cart):
        order = FoodReservation(guest, cart.items.copy(), cart.total())
        self.reservations.append(order)
        
        for item in cart.items.values():
            dish = item['product']
            quantity = item['quantity']
            found_dish = self.find_dish(dish.name)
            if found_dish:
                found_dish.amount -= quantity

        print("Food order confirmed:", order)
        return order

class FoodReservation(ServiceReservation):
    def __init__(self, guest, items, total):
        super().__init__(guest)
        self.__items = [{"name": item["product"].name, "amount": item["quantity"]} for item in items.values()]
        self.__total = total


class Dish:
    def __init__(self, name, price, image_url):
        self.__name = name
        self.__price = price
        self.__amount = 0
        self.__image_url = image_url

    @property
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price
    
    @property
    def amount(self):
        return self.__amount
    
    @property
    def image_url(self):
        return self.__image_url

    @amount.setter
    def amount(self, amount):
        self.__amount = amount

class Cart:
    def __init__(self):
        self.__items = {}

    @property
    def items(self):
        return self.__items

    def add(self, product):
        if product.name in self.__items:
            self.__items[product.name]['quantity'] += 1
        else:
            # Store the product under the key "product" instead of "dish"
            self.__items[product.name] = {'product': product, 'quantity': 1}

    def remove(self, product):
        if product.name in self.items:
            if self.__items[product.name]['quantity'] > 1:
                self.__items[product.name]['quantity'] -= 1
            else:
                del self.__items[product.name]

    def total(self) -> float:
        return sum(item['product'].price * item['quantity'] for item in self.items.values())
    
    def clear(self):
        self.__items = {}