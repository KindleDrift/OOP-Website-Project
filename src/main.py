from fasthtml.common import *
from datetime import datetime, timedelta
from classes.hotel import *

app, rt = fast_app(debug=True, secret_key="secret")

login_redir = RedirectResponse('/login', status_code=303)

# def before(req, sess):
#     auth = req.scope['auth'] = sess.get('auth', None)
#     if not auth: return login_redir


def room_card_booking(room: Room, start_date, end_date):
    return Card(
        Img(src=f"/images/{room.image}", cls="card-img-top", alt=f"Room {room.room_id}",
        style="width: auto; max-height: 300px; object-fit: cover;"),
        Div(
            H2(f"Room {room.room_id}"),
            P(f"Room Type: {room.type}"),
            P(f"Maximum People: {"👤" * room.size}"),
            P(f"Price: ฿{room.price} / Day"),
            P(f"Status: {"Available" if room.status == 1 else "Unavailable"}"),
            P(f"Commodity: {', '.join(room.things)}"),
            Button(f"Book now for ฿{(end_date - start_date).days * room.price}", cls="btn btn-primary", onclick=f"document.location='/booking/{room.room_id}/{start_date.strftime("%Y-%m-%d")}/{end_date.strftime("%Y-%m-%d")}'",
                   style="font-weight: bold;"),
            cls="card-text",
            style="text-align: left; margin-left: 20px;"
        ),
        style="width: 100%; margin: 10px; display: flex;"
    )


def room_card(room: Room, start_date, end_date):
    return Card(
        Img(src=f"/images/{room.image}", cls="card-img-top", alt=f"Room {room.room_id}",
        style="width: auto; max-height: 300px; object-fit: cover;"),
        Div(
            H2(f"Room {room.room_id}"),
            P(f"Room Type: {room.type}"),
            P(f"Maximum People: {"👤" * room.size}"),
            P(f"Price: ฿{room.price} / Day"),
            P(f"Status: {"Available" if room.status == 1 else "Unavailable"}"),
            P(f"Commodity: {', '.join(room.things)}"),
            P(f"Check-in Date: {start_date.strftime('%Y-%m-%d')}"),
            P(f"Check-out Date: {end_date.strftime('%Y-%m-%d')}"),
            P(f"Total Price: ฿{(end_date - start_date).days * room.price}"),
            cls="card-text",
            style="text-align: left; margin-left: 20px;"
        ),
        style="width: 100%; margin: 10px; display: flex;"
    )

#temporary create an instance of room
hotel = Hotel()
hotel.add_room(Room(101, "Single", 1, 100, 1, ["AC", "Wifi"], "room1.jpg"))
hotel.add_room(Room(102, "Double", 2, 150, 1, ["TV", "AC", "Wifi"], "room2.jpg"))
hotel.add_room(Room(103, "Family", 4, 200, 1, ["TV", "AC", "Wifi"], "room3.jpg"))
hotel.add_room(Room(104, "Suite", 6, 300, 1, ["TV", "AC", "Wifi"], "room4.jpg"))
hotel.add_room(Room(105, "Single", 1, 100, 1, ["TV", "AC", "Wifi"], "room5.jpg"))
hotel.add_room(Room(106, "Double", 2, 150, 1, ["AC", "Wifi"], "room6.jpg"))
hotel.add_room(Room(107, "Family", 4, 200, 1, ["TV", "AC", "Wifi"], "room7.jpg"))
hotel.add_room(Room(108, "Suite", 6, 300, 1, ["TV", "AC", "Wifi"], "room8.jpg"))


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
async def get():
    return Titled("Booking",
        Container(H1("Book a Room"),
            Form(Label("Check-in Date and Check-out Date",
                    Group(
                        Input(type="date", name="check-in", value=f"{(datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")}", required=True),
                        Input(type="date", name="check-out", value=f"{(datetime.today() + timedelta(days=2)).strftime("%Y-%m-%d")}", required=True)
                    )
                ),
                Label("Room Details",
                    Group(
                        Select(
                            Option("Single", value="Single"),
                            Option("Double", value="Double"),
                            Option("Family", value="Family"),
                            Option("Suite", value="Suite"),
                            Option("All", value="All", selected=True),
                            name="room-type"
                        ),
                        Input(type="number", name="guests", placeholder="Guest Count", required=True, max=10, min=1),
                        Input(type="number", name="max-price", placeholder="Max Budget", required=True, min=1, max=10000),
                        Button("Search", type="submit", cls="btn btn-primary", required=True, hx_post=f"/get-rooms/", hx_target="#room-list")
                    )
                ),
                Label("Commodities: ",
                    Input(type="checkbox", name="things-TV", value="TV"),"Television",
                    Input(type="checkbox", name="things-AC", value="AC"),"Air-Conditioning",
                    Input(type="checkbox", name="things-Wifi", value="Wifi"),"Wi-Fi"
                )
            ),
            Hr(),
            Div(
                H2("Available Rooms"),
                Div(id="room-list"),
                style="text-align: center;"
            )
        )
    )


@rt("/get-rooms/")
async def post(request):
    form_data = await request.form()
    start_date = datetime.strptime(form_data.get("check-in"), "%Y-%m-%d")
    end_date = datetime.strptime(form_data.get("check-out"), "%Y-%m-%d")
    room_type = form_data.get("room-type")
    guest_size = int(form_data.get("guests"))
    max_price = int(form_data.get("max-price"))
    tv = form_data.get("things-TV")
    ac = form_data.get("things-AC")
    wifi = form_data.get("things-Wifi")
    things = []
    if tv:
        things.append(tv)
    if ac:
        things.append(ac)
    if wifi:
        things.append(wifi)

    if start_date > end_date:
        return P("Invalid Date Range")
    
    if start_date < datetime.today():
        return P("Invalid Check-in Date")

    print(start_date, end_date)

    matching_hotel = hotel.get_room(room_type, guest_size, max_price, things, start_date, end_date)

    if matching_hotel == []:
        return P("No rooms available / match your criteria")   

    return Div(*(room_card_booking(room, start_date, end_date) for room in matching_hotel))

@rt("/rooms")
def get():
    return Titled(
        Container(
            H1("Our Rooms"),
            # Rooms(),
            style="text-align: center;"
        )
    )


@rt("/booking/{room_id}/{start_date}/{end_date}")
def get(room_id: int, start_date: str, end_date: str):

    formated_start = datetime.strptime(start_date, "%Y-%m-%d")
    formated_end = datetime.strptime(end_date, "%Y-%m-%d")

    if room_id not in [room.room_id for room in hotel.rooms]:
        return P("Room not found")
    # TODO check if room is available (class not implemented yet)
    if datetime.strptime(start_date, "%Y-%m-%d") < datetime.today():
        return P("Invalid Check-in Date")
    
    if datetime.strptime(start_date, "%Y-%m-%d") > datetime.strptime(end_date, "%Y-%m-%d"):
        return P("Invalid Date Range")
    
    if hotel.get_room_by_id(room_id).status == 0:
        return P("Room is not available")

    return Titled("Confirmation",
        Container(
            H1("Booking Confirmation"),
            room_card(hotel.get_room_by_id(room_id), formated_start, formated_end),
            Card(
                Form(
                    Label("Full Legal Name on Credit Card",
                        Input(type="text", name="full-name", required=True)),
                    Group(
                        Input(placeholder="Credit Card Number", type="text", name="credit-card", required=True),
                        Input(placeholder="Expiry Date (MM/YY)", type="text", name="expiration", required=True),
                        Input(placeholder="CVV", type="text", name="cvv", required=True)
                    ),
                    Label("Billing Address",
                        Input(type="text", name="address", required=True)),
                    Button("Confirm", type="submit", cls="btn btn-primary", onclick="document.location='/success'"),
                    style=""
                ),
                style="text-align: center;"
            ),
            style="text-align: left;"
        )
    )


@rt("/success")
def get():
    return Titled(
        Container(
            H1("Booking Successful"),
            P("Thank you for booking with us"),
            style="text-align: center;"
        )
    )

@rt("/profile")
def profile(session):
    if "user_id" in session:
        return f"Welcome, user {session['user_id']}!"
    else:
        return "Please login first" 
    

@rt("/signup")
def get():
    return Titled(
        Container(
            H1("Sign Up"),
            Form(
                Label("Full Name",
                    Input(type="text", name="full-name", required=True)),
                Label("Email",
                    Input(type="email", name="email", required=True)),
                Label("Password",
                    Input(type="password", name="password", required=True)),
                Button("Sign Up", type="submit", cls="btn btn-primary", onclick="document.location='/login'"),
                style=""
            ),
            style="text-align: center;"
        )
    )


@rt("/login")
def get():
    return Titled(
        Container(
            H1("Login"),
            Form(
                Label("Email",
                    Input(type="email", name="email", required=True)),
                Label("Password",
                    Input(type="password", name="password", required=True)),
                Button("Login", type="submit", cls="btn btn-primary", onclick="document.location='/'"),
                style=""
            ),
            style="text-align: center;"
        )
    )


@rt("/staff/")
def get():
    return Titled("Staff Home",
        Container(
            H1("Staff Home"),
            P("Welcome to the staff home page"),
            A("Room Management", href="/staff/room-management"),
            A("Check-in", href="/staff/check-in"),
            style="text-align: center;"
        )
    )


@rt("/staff/room-management")
async def get():
    return Titled("Room Editor",
        Container(
            H1("Room Editor"),
            H2("Add Room"),
            Form(
                Label("Room ID"),
                Input(type="number", name="room-id", required=True),
                Label("Room Type"),
                Select(
                    Option("Single", value="Single"),
                    Option("Double", value="Double"),
                    Option("Family", value="Family"),
                    Option("Suite", value="Suite"),
                    name="room-type",
                    requires=True
                ),
                Label("Size"),
                Input(type="number", name="size", required=True),
                Label("Price"),
                Input(type="number", name="price", required=True),
                Label("Status"),
                Select(
                    Option("Available", value="1"),
                    Option("Unavailable", value="0"),
                    name="status",
                    required=True
                ),
                Label("Things"),
                Input(type="text", name="things", required=True),
                Label("Image"),
                Input(type="text", name="image", required=True
                ),
                Button("Add", type="submit", cls="btn btn-primary", hx_post=f"/add-room/", hx_target="#return-message"),
                id="room-filter",
                style=""
            ),
            P(id="return-message"),
            H2("Edit Room"),
        )
    )


@rt("/staff/check-in")
def get():
    # TODO add checkin verification
    return Titled(
        Container(
            H1("Check In"),
            Form(
                Label("Room ID",
                    Input(type="number", name="room-id", required=True)),
                Label("Guest Name",
                    Input(type="text", name="guest-name", required=True)),
                Label("Check-in Date",
                    Input(type="date", name="check-in-date", required=True)),
                Label("Check-out Date",
                    Input(type="date", name="check-out-date", required=True)),
                Button("Check In", type="submit", cls="btn btn-primary", onclick="document.location='/staff/check-in'"),
                style=""
            ),
            style="text-align: center;"
        )
    )

@rt("/add-room/")
async def post(request):
    form_data = await request.form()
    room_id = form_data.get("room-id")
    room_type = form_data.get("room-type")
    size = form_data.get("size")
    price = form_data.get("price")
    status = form_data.get("status")
    things = form_data.get("things")
    image = form_data.get("image")

    if (room_id in [room.room_id for room in hotel.rooms]):
        return P("Room ID, try another ID")
    
    hotel.add_room(Room(room_id, room_type, size, price, status, things.split(","), image))

    return P("Room Added")

serve()