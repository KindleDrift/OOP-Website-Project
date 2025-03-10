from fasthtml.common import *
from datetime import datetime, timedelta, date

class Hotel:
    def __init__(self):
        self.__floors = []
        self.__rooms = []
        self.__bookings = []
        self.__guests = []
        self.__staffs = []
        self.__items = []
        self.__transport = Transport()
        self.__laundry = Laundry()
        self.__food_ordering = FoodOrdering()
        self.__cleaning = CleaningService()
        self.__repair_service = RepairService()

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
    def items(self):
        return self.__items
    
    @property
    def transport(self):
        return self.__transport
    
    @property
    def laundry(self):
        return self.__laundry
    
    @property
    def food_ordering(self):
        return self.__food_ordering

    @property
    def cleaning(self):
        return self.__cleaning
    
    @property
    def repair_service(self):
        return self.__repair_service

    def check_in_guest(self, booking_id):
        booking = self.get_booking_by_id(booking_id)
        if booking is None:
            return "Booking not found"
        if booking.status == "Staying":
            return "Guest already checked in"
        if booking.status == "Cancelled":
            return "Booking cancelled"
        booking.status = "Staying"
        return "Success"


    def filter_check_in(self, room_id=None, guest_name=None, check_in_date=None, check_out_date=None):
        valid_booking = []
        
        for booking in self.bookings:
            if booking.status == "Staying" or booking.status == "Cancelled" or booking.status == "Checked Out":
                continue

            # Room ID filter
            room_match = (room_id is None or booking.room.room_id == room_id)
            
            # Guest Name filter
            guest_match = (guest_name is None or booking.guest.real_name == guest_name)
            
            # Date Range filter (allows None values separately)
            date_match = (
                (check_in_date is None or check_out_date is None) or  # If either is None, allow any date
                (booking.start_date <= check_out_date and booking.end_date >= check_in_date)  # Correct overlap check
            )

            # If all filters match, add to results
            if room_match and guest_match and date_match:
                valid_booking.append(booking)

        return valid_booking
    

    def check_out_guest(self, booking_id):
        booking = self.get_booking_by_id(booking_id)
        if booking is None:
            return "Booking not found"
        if booking.status == "Checked Out":
            return "Guest already checked out"
        if booking.status == "Cancelled":
            return "Booking cancelled"
        booking.status = "Checked Out"
        return "Success"
    
    def filter_check_out(self, room_id=None, guest_name=None, check_in_date=None, check_out_date=None):
        valid_booking = []
        
        for booking in self.bookings:
            if booking.status == "Checked Out" or booking.status == "Cancelled" or booking.status == "Pending":
                continue

            # Room ID filter
            room_match = (room_id is None or booking.room.room_id == room_id)

            # Guest Name filter
            guest_match = (guest_name is None or booking.guest.real_name == guest_name)

            # Date Range filter (allows None values separately)
            date_match = (
                (check_in_date is None or check_out_date is None) or  # If either is None, allow any date
                (booking.start_date <= check_out_date and booking.end_date >= check_in_date)  # Correct overlap check
            )

            # If all filters match, add to results
            if room_match and guest_match and date_match:
                valid_booking.append(booking)

        return valid_booking


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

    def get_room_by_attribute(self, room_type=None, guest_count=None, max_budget_per_day=None, items=None, start_date=None, end_date=None):
        returned_room = []
        for room in self.rooms:
            if (room.status == 1) and \
                (room.type == room_type or room_type == "All") and \
                (room.size >= guest_count) and (room.price <= max_budget_per_day) and \
                ((all(item in room.items for item in items) or items == [None])) and \
                (self.check_room_availability(room.room_id, start_date, end_date)):
                returned_room.append(room)
        return returned_room
    
    def check_room_availability(self, room_id, start_date, end_date):
        room = self.get_room_by_id(room_id)
        for booking in self.bookings:
            if booking.room == room and (booking.status == "Staying" or booking.status == "Pending"):
                if (booking.start_date <= start_date.date() and booking.end_date >= start_date.date()) or \
                    (booking.start_date <= end_date.date() and booking.end_date >= end_date.date()) or \
                    (booking.start_date >= start_date.date() and booking.end_date <= end_date.date()):
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
    
    def get_service_fee(self, booking):
        total_fee = 0
        for service in booking.service_reservations:
            total_fee += service.total
        return total_fee
    
    def get_services_of_booking(self, booking, service_name):
        return [service for service in booking.service_reservations if service.name == service_name]
    
    def create_item(self, name, category, price, has_repair_fee):
        self.__items.append(Item(name, category, price, has_repair_fee))
        return "Success"
    
    def get_item_by_name(self, name):
        for item in self.__items:
            if item.name == name:
                return item
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
        self.__status = "Available"
        self.__working_log = []
        self.__current_service = None

    @property
    def status(self):
        return self.__status
    
    @property
    def working_log(self):
        return self.__working_log
    
    @property
    def current_service(self):
        return self.__current_service

    def assign_service(self, service):
        self.__working_log.append(service)
        self.__current_service = service
        self.__status = "Busy"

    def complete_service(self):
        self.__status = "Available"
        self.__current_service = None


class Floor:
    def __init__(self, floor_number):
        self.__floor_id = floor_number
        self.__rooms = []

class Room:
    def __init__(self, room_id, type, size, price, status: bool, items, image):
        self.__room_id = room_id
        self.__type = type
        self.__size = size
        self.__price = price
        self.__status = status
        self.__items = items
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
    def items(self):
        return self.__items
    
    @property
    def image(self):
        return self.__image
    

class Item:
    def __init__(self, name, category, price, has_repair_fee):
        self.__name = name
        self.__category = category
        self.__price = price
        self.__status = "Fine"

    @property
    def name(self):
        return self.__name
    
    @property
    def category(self):
        return self.__category
    
    @property
    def price(self):
        return self.__price
    
    @property
    def status(self):
        return self.__status
    

class Booking():
    current_booking_id = 1
    def __init__(self, guest=None, room=None, start_date=None, end_date=None, status=None):
        self.__booking_id = self.current_booking_id
        self.__guest = guest
        self.__room = room
        self.__start_date = start_date
        self.__end_date = end_date
        self.__status = status
        self.__service_reservations = []
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
    
    @status.setter
    def status(self, status):
        self.__status = status

    @property
    def service_reservations(self):
        return self.__service_reservations
    

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

    def get_reserved_reservation(self):
        return [reservation for reservation in self.reservations if (reservation.status == "Pending" or reservation.status == "Ongoing")]
    
    def assign_reservation(self, reservation_id, staff):
        for reservation in self.reservations:
            if reservation.id == reservation_id and staff.status == "Available":
                reservation.status = "Ongoing"
                reservation.staff = staff
                staff.assign_service(reservation)
                return "Success"
        return "Reservation not found"
    
    def unassign_reservation(self, reservation_id, staff):
        for reservation in self.reservations:
            if reservation.id == reservation_id and reservation.staff == staff:
                reservation.status = "Pending"
                staff.complete_service()
                return "Success"
        return "Reservation not found"

    def complete_reservation(self, reservation_id, staff):
        for reservation in self.reservations:
            if reservation.id == reservation_id and reservation.staff == staff:
                reservation.status = "Complete"
                staff.complete_service()
                return "Success"
        return "Reservation not found"
    
    def cancel_reservation(self, reservation_id, staff):
        for reservation in self.reservations:
            if reservation.id == reservation_id and reservation.staff == staff:
                reservation.status = "Cancelled"
                staff.complete_service()
                return "Success"
        return "Reservation not found"


class ServiceReservation:
    __id_counter = 1
    def __init__(self, name, guest):
        self.__name = name
        self.__id = ServiceReservation.__id_counter
        self.__guest = guest
        self.__staff = None
        self.__status = "Pending"
        self.__timestamp = datetime.now()
        self.__total = 0
        ServiceReservation.__id_counter += 1

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @property
    def guest(self):
        return self.__guest

    @property
    def staff(self):
        return self.__staff
    
    @staff.setter
    def staff(self, staff):
        self.__staff = staff

    @property
    def status(self):
        return self.__status
    
    @property
    def total(self):
        return self.__total
    
    @status.setter
    def status(self, status):
        if status in ["Pending", "Ongoing", "Complete", "Cancelled"]:
            self.__status = status
        else:
            raise ValueError("Invalid status")
        
    @property
    def timestamp(self):
        return self.__timestamp


# Transport Service #
class Transport(Service):
    def __init__(self):
        super().__init__("Transport")
        self.__routes = []

    @property
    def routes(self):
        return self.__routes

    def create_route(self, location, price):
        self.__routes.append(Route(location, price))

    def create_reservation(self, guest, route_name, date, booking):
        for route in self.__routes:
            if route.name == route_name:
                order = TransportReservation(guest, route, date)
                self.reservations.append(order)
                booking.service_reservations.append(order)
                print(order)
                return order
        return "Route not found"
    

class TransportReservation(ServiceReservation):
    def __init__(self, guest, route, assigned_time):
        super().__init__("Transport", guest)
        self.__route = route
        self.__total = route.price
        self.__assigned_time = assigned_time

    @property
    def route(self):
        return self.__route
    
    @property
    def total(self):
        return self.__total
    
    @property
    def assigned_time(self):
        return self.__assigned_time

class Route:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price
    
# Laundry Service #
class Laundry(Service):
    def __init__(self):
        super().__init__("Laundry")
        self.__clothes = []

    @property
    def clothes(self):
        return self.__clothes

    def create_cloth(self, type, price):    
        self.__clothes.append(Cloth(type, price))

    def get_cloth_type(self, type_name):
        for cloth in self.__clothes:
            if cloth.name == type_name:
                return cloth
        return None

    def create_reservation(self, guest, cart, booking):
        order = LaundryReservation(guest, cart.items.copy(), cart.total())
        self.reservations.append(order)
        booking.service_reservations.append(order)
        guest.laundry_cart.clear()
        print("Laundry order confirmed:", order)  # Debug print to console only
        return order
    

class LaundryReservation(ServiceReservation):
    def __init__(self, guest, items, total):
        super().__init__("Laundry", guest)
        # Use the same generic key "product" so that for cloth items, it shows the cloth name
        self.__items = [{"name": item["product"].name, "amount": item["quantity"]} for item in items.values()]
        self.__total = total

    @property
    def items(self):
        return self.__items
    
    @property
    def total(self):
        return self.__total


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


# Cleaning Service #
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

    def create_food_order(self, guest, cart, booking):
        order = FoodReservation(guest, cart.items.copy(), cart.total())
        self.reservations.append(order)
        booking.service_reservations.append(order)
        
        for item in cart.items.values():
            dish = item['product']
            quantity = item['quantity']
            found_dish = self.find_dish(dish.name)
            if found_dish:
                found_dish.amount -= quantity

        guest.food_cart.clear()

        print("Food order confirmed:", order)
        return order

class FoodReservation(ServiceReservation):
    def __init__(self, guest, items, total):
        super().__init__("Food Ordering", guest)
        self.__items = [{"name": item["product"].name, "amount": item["quantity"]} for item in items.values()]
        self.__total = total

    @property
    def items(self):
        return self.__items
    
    @property
    def total(self):
        return self.__total


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


# Cleaning Service #
class CleaningService(Service):
    def __init__(self):
        super().__init__("Cleaning Service")

    def create_reservation(self, guest, appointment_date, appointment_time, booking):
        order = CleaningReservation(guest, appointment_date, appointment_time, booking.room.room_id)
        self.reservations.append(order)
        booking.service_reservations.append(order)
        print("Cleaning appointment confirmed:", order)  # Debug print to console only
        return order
    

class CleaningReservation(ServiceReservation):
    def __init__(self, guest, appointment_date, appointment_time, room_id):
        super().__init__("Cleaning Service", guest)
        self.__appointment_date = appointment_date
        self.__appointment_time = appointment_time
        self.__room_id = room_id

    @property
    def appointment_date(self):
        return self.__appointment_date
    
    @property
    def appointment_time(self):
        return self.__appointment_time
    
    @property
    def room_id(self):
        return self.__room_id

# Repair Service #
class RepairService(Service):
    def __init__(self):
        super().__init__("Repair Service")

    def create_reservation(self, guest, appointment_date, appointment_time, item, repair_issue, booking):
        order = RepairReservation(guest, appointment_date, appointment_time, item, repair_issue, booking.room.room_id)
        booking.service_reservations.append(order)
        self.reservations.append(order)
        return order
    

class RepairReservation(ServiceReservation):
    def __init__(self, guest, appointment_date, appointment_time, item, repair_issue, room_id):
        super().__init__("Repair Service", guest)
        self.__appointment_date = appointment_date
        self.__appointment_time = appointment_time
        self.__item = item
        self.__repair_issue = repair_issue
        self.__room_id = room_id
        self.__total = item.price

    @property
    def appointment_date(self):
        return self.__appointment_date
    
    @property
    def appointment_time(self):
        return self.__appointment_time
    
    @property
    def item(self):
        return self.__item

    @property
    def repair_issue(self):
        return self.__repair_issue
    
    @property
    def room_id(self):
        return self.__room_id
    
    @property
    def total(self):
        return self.__total