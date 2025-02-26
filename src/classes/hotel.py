from fasthtml.common import *

class Hotel:
    pass


class User:
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