from fasthtml.common import *
from datetime import datetime, timedelta
import uuid

class Hotel:
    def __init__(self, Room=None, Booking=None, Guest=None, Staff=None, Floor=None, Things=None):
        self.__rooms = []
        self.__bookings = []
        self.__guests = []
        self.__staffs = []

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

    def add_room(self, room):
        self.__rooms.append(room)

    def get_room_by_id(self, room_id):
        for room in self.__rooms:
            if room.room_id == room_id:
                return room
        return None
    
    def get_guest_by_id(self, guest_id):
        for guest in self.__guests:
            if guest.user_id == guest_id:
                return guest
        return None
    
    def get_room(self, room_type=None, size=None, max_price=None, things=None, start_date=None, end_date=None):
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
    def __init__(self, name, real_name, email, password):
        self.__user_id = User.__id_counter
        self.__username = name
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
    def __init__(self, name, real_name, password, email):
        super().__init__(name, real_name, password, email)
        self.__bookings = []


class Staff(User):
    def __init__(self, name, real_name, password, email):
        super().__init__(name, real_name, password, email)


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
    

