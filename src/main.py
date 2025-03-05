from fasthtml.common import *
from datetime import datetime, timedelta
from dataclasses import dataclass
from classes.hotel import *

app, rt = fast_app(debug=False)

def create_instance():
    #temporary create an instance of room
    global hotel
    hotel = Hotel()
    hotel.add_room(Room(101, "Single", 1, 100, 1, ["AC", "Wifi"], "room1.jpg"))
    hotel.add_room(Room(102, "Double", 2, 150, 1, ["TV", "AC", "Wifi"], "room2.jpg"))
    hotel.add_room(Room(103, "Family", 4, 200, 1, ["TV", "AC", "Wifi"], "room3.jpg"))
    hotel.add_room(Room(104, "Suite", 6, 300, 1, ["TV", "AC", "Wifi"], "room4.jpg"))
    hotel.add_room(Room(105, "Single", 1, 100, 1, ["TV", "AC", "Wifi"], "room5.jpg"))
    hotel.add_room(Room(106, "Double", 2, 150, 1, ["AC", "Wifi"], "room6.jpg"))
    hotel.add_room(Room(107, "Family", 4, 200, 1, ["TV", "AC", "Wifi"], "room7.jpg"))
    hotel.add_room(Room(108, "Suite", 6, 300, 1, ["TV", "AC", "Wifi"], "room8.jpg"))

    # user account
    hotel.create_guest("JohnDoe", "John Doe", "john.d@domain.xyz", "password")
    hotel.create_guest("JaneDoe", "Jane Doe", "jane.d@domain.xyz", "password")
    hotel.create_staff("admin", "Joe Hill", "joe.h@cozyhotel.com", "password")

    hotel.create_booking(hotel.get_guest_by_id(1), hotel.get_room_by_id(101), datetime.today(), datetime.today() + timedelta(days=1))
    hotel.create_booking(hotel.get_guest_by_id(2), hotel.get_room_by_id(102), datetime.today(), datetime.today() + timedelta(days=1))
    hotel.create_booking(hotel.get_guest_by_id(1), hotel.get_room_by_id(103), datetime.today(), datetime.today() + timedelta(days=1))
    hotel.create_booking(hotel.get_guest_by_id(2), hotel.get_room_by_id(104), datetime.today(), datetime.today() + timedelta(days=1))

    print("---")
    for user in hotel.guests:
        print(user.username, user.user_id)
    for user in hotel.staffs:
        print(user.username, user.user_id)
    print("---")


######################
#    UI Functions    #
######################
def menu(session):
    extra = "Sign Up"
    login = "Login"
    if "user_id" in session:
        extra = "Profile"
        login = "Logout"
    if get_user_role(session) == "staff":
        extra = "Staff"

    return Nav(
                Div(
                    A("Home", href="/", cls="secondary"),
                    A("Room", href="/rooms", cls="secondary"),
                    cls="navbar-links",
                    style="display: flex; gap: 15px; text-align: center; font-weight: 800;"
                    
                ),
                Div(
                    A(f"{extra}", href=f"/{extra.lower().replace(' ', '')}", cls="secondary"),
                    A(f"{login}", href=f"/{login.lower()}", cls="secondary"),
                    cls="navbar-auth",
                    style="display: flex; gap: 10px; text-align: center; font-weight: 800;);",
                ),
            cls="navbar secondary",
            style="box-shadow: 0 5px 10px black; \
            padding: 10px 20px; \
            display: flex; \
            justify-content: space-between; \
            align-items: center;"
            )


def display_room(room: Room, start_date, end_date):
    return Card(
        Img(src=f"/images/{room.image}", cls="card-img-top", alt=f"Room {room.room_id}",
        style="max-height: 300px; object-fit: cover;"),
        Div(
            H2(f"Room {room.room_id}"),
            P(f"Room Type: {room.type}"),
            P(f"Maximum People: {"👤" * room.size}"),
            P(f"Price: ฿{room.price} / Day"),
            P(f"Status: {'Available' if room.status == 1 else 'Unavailable'}"),
            P(f"Commodity: {', '.join(room.things)}"),
            Button(f"Book now for ฿{(end_date - start_date).days * room.price}", cls="btn btn-primary", onclick=f"document.location='/booking/{room.room_id}/{start_date.strftime("%Y-%m-%d")}/{end_date.strftime("%Y-%m-%d")}'",
                   style="font-weight: bold;"),
            cls="card-text",
            style="text-align: left; margin-left: 20px;"
        ),
        style="width: 100%; margin: 10px 0; display: flex;"
    )


def reciept_card(room: Room, start_date, end_date):
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
        style="width: 100%; margin: 10px 0; display: flex;"
    )


def checkin_table(booking):
    return Tr(
                Td(booking.booking_id),
                Td(booking.room.room_id),
                Td(booking.guest.name),
                Td(booking.start_date),
                Td(booking.end_date),
                Td(Button("Check In", cls="btn btn-primary", onclick="document.location='/staff/check-in/{booking.room.room_id}/{booking.guest.name}/{booking.start_date}/{booking.end_date}'"))
            )


######################
#   API  Functions   #
######################
def check_login(session, page=None):
    if "user_id" not in session:
        return RedirectResponse(f"/login?redirect={page}" if page else "/login", status_code=303)
    

def get_user_role(session):
    if "user_id" not in session:
        return None
    for staff in hotel.staffs:
        if staff.user_id == session["user_id"]:
            return "staff"
    return "guest"



@app.on_event("startup")
async def startup():
    create_instance()
    print("Hotel instance created")
    print(hotel.rooms)


@rt("/")
def get(session):
    return (Title("Cozy Hotel"),
        menu(session),
        Div(Container(
            Div(
                H1("Welcome to Cozy Hotel", style="font-size: 5em; color: white; text-shadow: 2px 2px 5px black; font-weight: 800;"),
                P("We have the coziest rooms in the world", style="font-size: 2em; color: white; text-shadow: 2px 2px 5px black; font-weight: 800;"),
                style="text-align: center; padding: 100px 0;"            
            ),
            Button("Book Now", cls="btn btn-primary", onclick="document.location='/booking'")
        ),
            cls="hero",
            style="text-align: center; \
            background-image: url('./images/hotel.jpg'); \
            background-size: cover; \
            background-repeat: no-repeat; \
            background-attachment: fixed; \
            background-position: center; \
            padding: 250px 0;"),
    )


@rt("/booking")
async def get(session):
    return (Title("Booking"),
        menu(session), Br(),
        Container(H1("Book a Room"),
            Form(Label("Check-in Date and Check-out Date",
                    Group(
                        Input(type="date", name="check-in", value=f"{(datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")}", required=True),
                        Input(type="date", name="check-out", value=f"{(datetime.today() + timedelta(days=2)).strftime("%Y-%m-%d")}", required=True)
                    ), P("Select the date range for your stay, you will need to book a room a day in advance", style="font-size: 0.8em;")
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
                        Input(type="number", name="guests", placeholder="Guest Count", required="True", min=1, max=10),
                        Input(type="number", name="max-price", placeholder="Max Budget Per Day", required="True", min=1, max=10000),
                        Button("Search", type="submit", cls="btn btn-primary")
                    )
                ),
                Label("Commodities: ",
                    Input(type="checkbox", name="things-TV", value="TV",),"Television",
                    Input(type="checkbox", name="things-AC", value="AC"),"Air-Conditioning",
                    Input(type="checkbox", name="things-Wifi", value="Wifi"),"Wi-Fi"
                ),
                hx_post="/get-rooms", hx_target="#room-list"
            ),
            Hr(),
            Div(
                H2("Available Rooms"),
                Div(id="room-list"),
                style="text-align: center;"
            )
        )
    )


@rt("/get-rooms")
async def post(request):
    try:
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

        print("Received form data:", form_data)
    except:
        return P("Invalid form data", style="color: red")

    if start_date > end_date:
        return P("Invalid Date Range", style="color: red;")
    
    if start_date < datetime.today():
        return P("Invalid Check-in Date", style="color: red;")

    if room_type not in ["Single", "Double", "Family", "Suite", "All"]:
        return P("Invalid Room Type", style="color: red;")

    matching_hotel = hotel.get_room(room_type, guest_size, max_price, things, start_date, end_date)

    if matching_hotel == []:
        return P("No rooms available / match your criteria 😔")   

    return Div(*(display_room(room, start_date, end_date) for room in matching_hotel))

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
def get(session, room_id: int, start_date: str, end_date: str):


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
            reciept_card(hotel.get_room_by_id(room_id), formated_start, formated_end),
            Card(
                Form(
                    Label("Full Legal Name on Credit Card",
                        Input(type="text", name="full-name", required=True)),
                    Group(
                        Input(placeholder="Credit Card Number", type="text", name="credit-card", required=True, aria_invalid="true"),
                        Input(placeholder="Expiry Date (MM/YY)", type="text", name="expiration", required=True),
                        Input(placeholder="CVV", type="text", name="cvv", required=True)
                    ),
                    Label("Billing Address",
                        Input(type="text", name="address", required=True)),
                    Button("Confirm", type="submit", cls="btn btn-primary"),
                    hx_post=f"/booking/{room_id}/{start_date}/{end_date}", hx_target="#booking-form"
                ),
                style="text-align: center;"
            ),
            style="text-align: left;",
            id="booking-form"
        )
    )


@rt("/booking/{room_id}/{start_date}/{end_date}")
async def post(request):
    form_data = await request.form()
    card_number = form_data.get("credit-card")

    # if len(card_number) != 16:
    #     return P("Invalid Credit Card Number")
    # if not card_number.isdigit():
    #     return P("Invalid Credit Card Number")
    
    start_date = datetime.strptime(request.path_params["start_date"], "%Y-%m-%d")
    end_date = datetime.strptime(request.path_params["end_date"], "%Y-%m-%d")

    hotel.create_booking(hotel.get_guest_by_id(1), hotel.get_room_by_id(101), start_date, end_date)

    #Create booking instance
    return Container(
        H1("Booking Successful"),
        P("Thank you for booking with us"),
        style="text-align: center;"
    )

@rt("/success")
def get():
    return Container(
        H1("Booking Successful"),
        P("Thank you for booking with us"),
        style="text-align: center;"
    )

@rt("/profile")
def get(session):
    check_login(session, "profile")

    if get_user_role(session) == "staff":
        return P("You're staff")
    
    user = hotel.get_guest_by_id(session["user_id"])
    return (Title("Profile"),
            (menu(session), Br(),
            Container(Card(
                H1("Profile"),
                P(f"Username: {user.username}"),
                P(f"Full Name: {user.real_name}"),
                P(f"Email: {user.email}"),
                # Check Booking history
                H2("Booking History"),
                Table(
                    Thead(
                        Tr(
                            Th("Booking ID"),
                            Th("Room ID"),
                            Th("Check-in Date"),
                            Th("Check-out Date"),
                            Th("Status"),
                            Th("View Reciept")
                        )
                    ),
                    Tbody(
                        *(Tr(
                            Td(booking.booking_id),
                            Td(booking.room.room_id),
                            Td(booking.start_date),
                            Td(booking.end_date),
                            Td(booking.status),
                            Td(Button("View", cls="btn btn-primary", onclick=f"document.location='/booking/{booking.room.room_id}/{booking.start_date}/{booking.end_date}'"))
                        ) for booking in hotel.bookings if booking.guest.user_id == user.user_id)
                    ),
                    cls="striped"
                ),
                style="text-align: center;"
            )
                
        )
    ))
    

@rt("/signup")
def get(session, request):
    if "user_id" in session:
        return RedirectResponse("/", status_code=303)
    
    redirect = "/"

    if "redirect" in request.query_params:
        redirect = request.query_params["redirect"]
        
    return (Title("Sign Up"),
        menu(session), Br(),
        Container(
            H1("Sign Up", style="text-align: center;"),
            Card(
                Form(
                    Input(type="hidden", name="redirect", value=redirect),
                    Label("Username",
                        Input(type="text", name="username", placeholder="Username", required=True)),
                    Label("Full Name",
                        Group(Input(type="text", name="first-name", placeholder="First Name", required=True),
                              Input(type="text", name="last-name", placeholder="Last Name", required=True))),
                    Label("Email",
                        Input(type="email", name="email", required=True)),
                    Label("Password",
                        Input(type="password", name="password", required=True)),
                    Label("Confirm Password",
                        Input(type="password", name="confirm-password", required=True)),
                    P(id="return-message", style="color: red;"),
                    Button("Sign Up", type="submit", cls="btn btn-primary", required=True, style="width: 150px;"),
                    hx_post="/signup", hx_target="#return-message"
                ),
                Hr(),
                A("Login", href="/login", style="text-align: center;"),
                style="text-align: center; max-width: 400px; margin: 0 auto"
            )
        )
    )


@rt("/signup")
async def post(request):
    form_data = await request.form()
    username = form_data.get("username")
    first_name = form_data.get("first-name")
    last_name = form_data.get("last-name")
    email = form_data.get("email")
    password = form_data.get("password")
    confirm_password = form_data.get("confirm-password")

    if password != confirm_password:
        return P("Password does not match")

    real_name = first_name.capitalize() + " " + last_name.capitalize()

    if hotel.create_guest(username, real_name, email, password) == "Success":
        return Redirect("/login")
    else:
        return P("Username already exists")


@rt("/login", methods=["GET"])
def get(session, request):
    if "user_id" in session:
        return RedirectResponse("/", status_code=303)

    redirect = "/"

    if "redirect" in request.query_params:
        redirect = request.query_params["redirect"]

    return (Title("Login"),
        menu(session), Br(),
        Container(
            H1("Login", style="text-align: center;"),
            Card(
                Form(
                    Input(type="hidden", name="redirect", value=redirect),
                    Label("Email",
                        Input(type="email", name="email", required=True)),
                    Label("Password",
                        Input(type="password", name="password", required=True)),
                    P(id="return-message", style="color: red;"),
                    Button("Login", type="submit", cls="btn btn-primary", style="width: 150px;"),
                    hx_post="/login", hx_target="#return-message"
                ),
                Hr(),
                A("Sign Up", href="/signup", style="text-align: center;"),
                style="text-align: center; max-width: 400px; margin: 0 auto"
            )
        )
    )


@rt("/login")
async def post(request, session):
    form_data = await request.form()
    email = form_data.get("email")
    password = form_data.get("password")

    hidden_redirect = form_data.get("redirect", "/")

    account = hotel.validate_user(email, password)
    print(email)
    if account is not None: 
        session["user_id"] = account.user_id
        return Redirect(hidden_redirect)
    else:
        return P("Invalid credentials", style="color: red;")


@rt("/logout")
def get(session):
    session.pop("user_id", None)
    return Redirect("/")


@rt("")


@rt("/staff/")
def get(session):
    if "user_id" not in session:
        return login_redir("staff")
    for staff in hotel.staffs:
        if staff.user_id == session["user_id"]:
            return Titled("Staff Home",
                Container(
                    H1("Staff Home"),
                    P("Welcome to the staff home page"),
                    A("Room Management", href="/staff/room-management"),
                    A("Check-in", href="/staff/check-in"),
                    style="text-align: center;"
                )
            )
    return RedirectResponse("/", status_code=303)


# @rt("/staff/room-management")
# async def get():
#     return Titled("Room Editor",
#         Container(
#             H1("Room Editor"),
#             H2("Add Room"),
#             Form(
#                 Label("Room ID"),
#                 Input(type="number", name="room-id", required=True),
#                 Label("Room Type"),
#                 Select(
#                     Option("Single", value="Single"),
#                     Option("Double", value="Double"),
#                     Option("Family", value="Family"),
#                     Option("Suite", value="Suite"),
#                     name="room-type",
#                     requires=True
#                 ),
#                 Label("Size"),
#                 Input(type="number", name="size", required=True),
#                 Label("Price"),
#                 Input(type="number", name="price", required=True),
#                 Label("Status"),
#                 Select(
#                     Option("Available", value="1"),
#                     Option("Unavailable", value="0"),
#                     name="status",
#                     required=True
#                 ),
#                 Label("Things"),
#                 Input(type="text", name="things", required=True),
#                 Label("Image"),
#                 Input(type="text", name="image", required=True
#                 ),
#                 Button("Add", type="submit", cls="btn btn-primary", hx_post=f"/add-room/", hx_target="#return-message"),
#                 id="room-filter",
#                 style=""
#             ),
#             P(id="return-message"),
#             H2("Edit Room"),
#         )
#     )


@rt("/staff/check-in")
def get(session):
    if "user_id" not in session:
        return login_redir("staff/check-in")
    for staff in hotel.staffs:
        if staff.user_id == session["user_id"]:
            return (Title("Check In"),
                menu(session),
                Br(),
                Container(
                    H1("Check In"),
                    Form(
                        Group(Input(type="number", name="room-id", required=True),
                            Input(type="text", name="guest-name", required=True),
                            Input(type="date", name="check-in-date", required=True),
                            Input(type="date", name="check-out-date", required=True),
                            Button("Search", type="submit", cls="btn btn-primary", hx_post="/staff/check-in", hx_target="#return-message"),
                            id="return-message")
                    ), Hr(),
                    Table(
                        Thead(
                            Tr(
                            Th("Booking ID"),
                            Th("Room ID"),
                            Th("Guest Name"),
                            Th("Check-in Date"),
                            Th("Check-out Date"),
                            Th("Action")
                        )
                    ),
                    Tbody(*(checkin_table(booking) for booking in hotel.bookings)), cls="striped"),
                    style="text-align: center;"
                
            ))
    return RedirectResponse("/", status_code=303)


# @rt("/add-room/")
# async def post(request):
#     form_data = await request.form()
#     room_id = form_data.get("room-id")
#     room_type = form_data.get("room-type")
#     size = form_data.get("size")
#     price = form_data.get("price")
#     status = form_data.get("status")
#     things = form_data.get("things")
#     image = form_data.get("image")

#     if (room_id in [room.room_id for room in hotel.rooms]):
#         return P("Room ID, try another ID")
    
#     hotel.add_room(Room(room_id, room_type, size, price, status, things.split(","), image))

#     return P("Room Added")


serve()