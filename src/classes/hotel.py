from fasthtml.common import *

class Hotel:
    def __init__(self, Room=None, Booking=None, Guest=None, Staff=None, Floor=None, Things=None):
        self.__rooms = []
        self.__bookings = []
        self.__guests = []

    @property
    def rooms(self):
        return self.__rooms

    @property
    def bookings(self): 
        return self.__bookings
    
    @property
    def guests(self):
        return self.__guests

    def add_room(self, room):
        self.__rooms.append(room)

    def get_room_by_id(self, room_id):
        for room in self.__rooms:
            if room.room_id == room_id:
                return room
        return None
    
    def get_room(self, room_type=None, size=None, max_price=None, things=None, start_date=None, end_date=None):
        returned_room = []
        for room in self.rooms:
            if (room.status == 1) and (room.type == room_type or room_type == "All") and (room.size >= size) and (room.price <= max_price) and ((all(thing in room.things for thing in things) or things == [None])):
                returned_room.append(room)
        return returned_room
    
    def create_booking(self):
        self.bookings.append(Booking())
        return self.bookings[-1]
    
    def create_guest(self, user_id, name, password, email, phone, address):
        self.guests.append(Guest(user_id, name, password, email, phone, address))
        return "Success"


class User:
    def __init__(self, user_id, name, password, email, phone, address):
        self.__user_id = user_id
        self.__name = name
        self.__password = password
        self.__email = email
        self.__phone = phone
        self.__address = address

    @property
    def user_id(self):
        return self.__user_id
    
    @property
    def name(self):
        return self.__name

    def authenticate(self, name, password):
        if self.__name == name and self.__password == password:
            return True
        return False


class Guest(User):
    def __init__(self, user_id, name, password, email, phone, address):
        super().__init__(user_id, name, password, email, phone, address)
        self.__bookings = []


class Staff:
    pass


class Floor:
    pass


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
    pass