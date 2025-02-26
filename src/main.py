from fasthtml.common import *
from datetime import *
from classes.hotel import *

app, rt = fast_app(debug=True)

def room_card(room: Room):
    return Card(
        Img(src=room.image, cls="card-img-top", alt=f"Room {room.room_id}",
        style="width: auto; max-height: 300px; object-fit: cover;"),
        Div(
            H4(f"Room {room.room_id}"),
            P(f"Type: {room.type}"),
            P(f"Size: {room.size}"),
            P(f"Price: {room.price}"),
            P(f"Status: {"Available" if room.status == 1 else "Unavailable"}"),
            P(f"Things: {', '.join(room.things)}"),
            Button("Book", cls="btn btn-primary", hx_post="/book"),
            cls="card-text",
            style="text-align: left; margin-left: 20px;"
        ),
        style="width: 100%; margin: 10px; display: flex;"
    )


#temporary create an instance of room
room1 = Room(101, "Single", 20, 100, 1, ["TV", "AC", "Wifi"], "./images/room1.jpg")
room2 = Room(102, "Double", 30, 150, 1, ["TV", "AC", "Wifi"], "./images/room2.jpg")

room_list = [room1, room2]

def get_room(start_date, end_date, room_type):
    returned_room = []
    print("Pressed")
    for room in room_list:
        print(f"Room Type: {room.type}")
        if room.status == 1 and room.type == room_type or room_type == "All":
            print("Should be here")
            returned_room.append(room_card(room))
    return returned_room

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
async def get(request):
    return Titled("Booking",
        Container(
            H1("Book a Room"),
            Form(
                Div(
                    Label("Check-in Date",
                          Input(type="date", name="check-in", required=True)
                        ),
                    Label("Check-out Date",
                          Input(type="date", name="check-out", required=True)
                        ),
                    style="display: flex; justify-content: space-evenly;"
                ),
                Label("Room Type"),
                Select(
                    Option("Single", value="Single"),
                    Option("Double", value="Double"),
                    Option("Family", value="Family"),
                    Option("Suite", value="Suite"),
                    Option("All", value="All", selected=True),
                    name="room-type"
                ),
                Button("Search", type="submit", cls="btn btn-primary", hx_post=f"/get-rooms/", hx_target="#room-list"),
                id="room-filter",
                style=""
            ),
            Hr(),
            Div(
                H2("Available Rooms"),
                Div(id="room-list"),
                style="text-align: center;"
            ),
        )
    )


@rt("/get-rooms/")
async def post(request):
    form_data = await request.form()
    start_date = form_data.get("check-in")
    end_date = form_data.get("check-out")
    room_type = form_data.get("room-type")

    print(start_date, end_date, room_type)

    return Div(*get_room(start_date, end_date, room_type))

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