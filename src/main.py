from fasthtml.common import *
from datetime import *
from classes.hotel import *

app, rt = fast_app(debug=True)

def room_card(room: Room):
    return Card(
        Div(
            H4(f"Room {room.room_id}"),
            cls="card-header",
            style="text-align: center;"
        ),
        Div(
            P(f"Type: {room.type}"),
            P(f"Size: {room.size}"),
            P(f"Price: {room.price}"),
            P(f"Status: {room.status}"),
            P(f"Things: {', '.join(room.things)}"),
            Img(src=room.image, cls="card-img-top", alt="Room Image"),
            cls="card-body",
            style="text-align: center;"
        ),
        style="width: 18rem; margin: 10px;"
    )


#temporary create an instance of room
room = Room(101, "Single", 20, 100, "Available", ["TV", "AC", "Wifi"], "./images/room1.jpg")

def get_room():
    return room_card(room)

@rt("/")
def get():
    return Titled("Hotel",
        Container(
            Div(
                H1("Welcome to the Hotel", style="color: white;"),
                P("We have the best rooms in the world", style="color: white;"),
                style="text-shadow: 0px 0px 4px black;"               
            ),
            Button("Book Now", cls="btn btn-primary", onclick="document.location='/booking'"),
            style="text-align: center; \
                    background-image: url('./images/hotel.jpg'); \
                    background-size: cover; \
                    background-repeat: no-repeat; \
                    background-attachment: fixed; \
                    background-position: center; \
                    padding: 100px 0;"
        )
    )


@rt("/booking")
def get():
    return Titled("Booking",
        Container(
            H1("Book a Room"),
            # Search Rooms
            P(get_room()),
            Form(
                Input(placeholder="Name", cls="form-control"),
                Input(placeholder="Email", cls="form-control"),
                Input(placeholder="Check-in", cls="form-control"),
                Input(placeholder="Check-out", cls="form-control"),
                Button("Book", cls="btn btn-primary", hx_post="/book"),
                style="text-align: center;"
            )
        )
    )

@rt("/rooms")
def get():
    return Titled(
        Container(
            H1("Our Rooms"),
            # Rooms(),
            style="text-align: center;"
        )
    )


@rt("/book")
def post():
    return Titled(
        Container(
            H1("Booking Confirmation"),
            # BookingConfirmation(),
            style="text-align: center;"
        )
    )


@rt("/staff/room-management")
def get():
    return Titled(
        Container(
            H1("Room Management"),
            # RoomManagement(),
            style="text-align: center;"
        )
    )

serve()