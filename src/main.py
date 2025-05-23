from fasthtml.common import *
from datetime import datetime, timedelta, date
from classes.hotel import *

app, rt = fast_app(debug=False, secret_key="secret")

def create_instance():
    global hotel
    hotel = Hotel("Cozy Hotel")

    # Add Commodities (Services)
    hotel.create_item("TV", "Commodity", 0, False)
    hotel.create_item("AC", "Commodity", 0, False)
    hotel.create_item("Wifi", "Commodity", 0, False)
    hotel.create_item("Minibar", "Commodity", 0, False)

    # Add Furniture (Physical Items)
    hotel.create_item("Bed", "Furniture", 200, True)
    hotel.create_item("Table", "Furniture", 100, True)
    hotel.create_item("Chair", "Furniture", 50, True)
    hotel.create_item("Lamp", "Furniture", 30, True)
    hotel.create_item("Mirror", "Furniture", 80, True)
    hotel.create_item("Wardrobe", "Furniture", 150, True)
    hotel.create_item("Sofa", "Furniture", 250, True)
    hotel.create_item("Fridge", "Furniture", 300, True)

    # Items Pack
    single_room_items = [hotel.get_item_by_name(item) for item in ["Bed", "Table", "Chair", "Lamp", "Mirror", "Wardrobe", "TV", "AC", "Wifi"]]
    double_room_items = [hotel.get_item_by_name(item) for item in ["Bed", "Table", "Chair", "Lamp", "Mirror", "Wardrobe", "TV", "AC", "Wifi", "Sofa"]]
    family_room_items = [hotel.get_item_by_name(item) for item in ["Bed", "Table", "Chair", "Lamp", "Mirror", "Wardrobe", "TV", "AC", "Wifi", "Sofa", "Fridge"]]
    suite_room_items = [hotel.get_item_by_name(item) for item in ["Bed", "Table", "Chair", "Lamp", "Mirror", "Wardrobe", "TV", "AC", "Wifi", "Sofa", "Fridge", "Minibar"]]

    # Room
    hotel.create_room(101, "Single", 1, 100, 1, single_room_items, "room1.jpg")
    hotel.create_room(102, "Double", 2, 150, 1, double_room_items, "room2.jpg")
    hotel.create_room(103, "Family", 4, 200, 1, family_room_items, "room3.jpg")
    hotel.create_room(104, "Suite", 6, 300, 1, suite_room_items, "room4.jpg")
    hotel.create_room(105, "Single", 1, 100, 1, single_room_items, "room5.jpg")
    hotel.create_room(106, "Double", 2, 150, 1, double_room_items, "room6.jpg")
    hotel.create_room(107, "Family", 4, 200, 1, family_room_items, "room7.jpg")
    hotel.create_room(108, "Suite", 6, 300, 1, suite_room_items, "room8.jpg")

    hotel.create_room(201, "Single", 1, 100, 1, single_room_items, "room1.jpg")
    hotel.create_room(202, "Double", 2, 150, 1, double_room_items, "room2.jpg")
    hotel.create_room(203, "Family", 4, 200, 1, family_room_items, "room3.jpg")
    hotel.create_room(204, "Suite", 6, 300, 1, suite_room_items, "room4.jpg")
    hotel.create_room(205, "Single", 1, 100, 1, single_room_items, "room5.jpg")
    hotel.create_room(206, "Double", 2, 150, 1, double_room_items, "room6.jpg")
    hotel.create_room(207, "Family", 4, 200, 1, family_room_items, "room7.jpg")
    hotel.create_room(208, "Suite", 6, 300, 1, suite_room_items, "room8.jpg")

    # user account
    hotel.create_staff("ManagerPaul", "Paul Howard", "paul.h@cozyhotel.com", "password")
    hotel.create_staff("DriverJoe", "Joe Speed", "joe.s@cozyhotel.com", "password")
    hotel.create_staff("ChefMike", "Mike Cowave", "mike.c@cozyhotel.com", "password")
    hotel.create_guest("JohnDoe", "John Doe", "john.d@email.com", "password")
    hotel.create_guest("JaneDoe", "Jane Doe", "jane.d@email.com", "password")
    hotel.create_guest("AliceDoe", "Alice Doe", "alice.d@email.com", "password")
    hotel.create_guest("BobDoe", "Bob Doe", "bob.d@email.com", "password")
    hotel.create_guest("CharlieDoe", "Charlie Doe", "charlie.d@gmail.com", "password")

    hotel.transport.create_route("Airport", 100)
    hotel.transport.create_route("City Tour", 200)
    hotel.transport.create_route("Beach", 150)
    hotel.transport.create_route("Downtown Express", 50)
    hotel.transport.create_route("Suburban Shuttle", 50)
    hotel.transport.create_route("Nightlife Special", 100)
    hotel.transport.create_route("Train Station", 50)

    hotel.food_ordering.add_new_menu("Pasta Alfredo", 429, "https://placehold.co/200x150")
    hotel.food_ordering.add_new_menu("Margherita Pizza", 329, "https://placehold.co/200x150")
    hotel.food_ordering.add_new_menu("Caesar Salad", 269, "https://placehold.co/200x150")
    hotel.food_ordering.add_new_menu("Steak", 699, "https://placehold.co/200x150")
    hotel.food_ordering.add_new_menu("Spaghetti Carbonara", 399, "https://placehold.co/200x150")
    hotel.food_ordering.add_new_menu("Chicken Parmesan", 469, "https://placehold.co/200x150")
    hotel.food_ordering.add_new_menu("Bruschetta", 239, "https://placehold.co/200x150")
    hotel.food_ordering.add_new_menu("Tiramisu", 189, "https://placehold.co/200x150")
    hotel.food_ordering.add_new_menu("Gelato", 149, "https://placehold.co/200x150")
    hotel.food_ordering.add_new_menu("Minestrone Soup", 269, "https://placehold.co/200x150")
    hotel.food_ordering.add_new_menu("Focaccia Bread", 139, "https://placehold.co/200x150")
    hotel.food_ordering.add_new_menu("Lasagna", 429, "https://placehold.co/200x150")
    hotel.food_ordering.add_new_menu("Risotto", 479, "https://placehold.co/200x150")
    hotel.food_ordering.add_new_menu("Caprese Salad", 299, "https://placehold.co/200x150")

    for dish_name in ["Pasta Alfredo", "Margherita Pizza", "Caesar Salad", "Steak", "Spaghetti Carbonara", 
                  "Chicken Parmesan", "Bruschetta", "Tiramisu", "Gelato", "Minestrone Soup", 
                  "Focaccia Bread", "Lasagna", "Risotto", "Caprese Salad"]:
        hotel.food_ordering.restock(dish_name, 10)

    hotel.laundry.create_cloth("Shirt", 10.00)
    hotel.laundry.create_cloth("Pants", 15.50)
    hotel.laundry.create_cloth("Jacket", 20.00)
    hotel.laundry.create_cloth("Dress", 25.50)
    hotel.laundry.create_cloth("Sweater", 18.00)
    hotel.laundry.create_cloth("Coat", 30.00)
    hotel.laundry.create_cloth("Skirt", 12.50)
    hotel.laundry.create_cloth("Shorts", 9.50)
    hotel.laundry.create_cloth("Blouse", 12.50)
    hotel.laundry.create_cloth("Sweater Vest", 14.00)
    hotel.laundry.create_cloth("Scarf", 7.00)
    hotel.laundry.create_cloth("Tie", 6.50)
    hotel.laundry.create_cloth("Socks", 8.00)
    hotel.laundry.create_cloth("Bathrobe", 22.00)

    # Check-in 3 Days Ago and Check-out in three days
    hotel.create_booking(hotel.get_guest_by_id(4), hotel.get_room_by_id(105), datetime.today().date() - timedelta(days=3), datetime.today().date() + timedelta(days=3))
    hotel.check_in_booking(1)

    hotel.transport.create_reservation(hotel.get_guest_by_id(4), hotel.transport.routes[0].name, (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%dT%H:%M'), hotel.get_booking_by_id(1))
    
    hotel.get_guest_by_id(4).food_cart.add(hotel.food_ordering.dishes[0])
    hotel.get_guest_by_id(4).food_cart.add(hotel.food_ordering.dishes[0])
    hotel.get_guest_by_id(4).food_cart.add(hotel.food_ordering.dishes[1])
    hotel.get_guest_by_id(4).food_cart.add(hotel.food_ordering.dishes[2])

    hotel.food_ordering.create_food_order(hotel.get_guest_by_id(4), hotel.get_guest_by_id(4).food_cart, hotel.get_booking_by_id(1))

    hotel.get_guest_by_id(4).laundry_cart.add(hotel.laundry.clothes[0])
    hotel.get_guest_by_id(4).laundry_cart.add(hotel.laundry.clothes[1])
    hotel.get_guest_by_id(4).laundry_cart.add(hotel.laundry.clothes[1])
    hotel.get_guest_by_id(4).laundry_cart.add(hotel.laundry.clothes[2])
    hotel.laundry.create_reservation(hotel.get_guest_by_id(4), hotel.get_guest_by_id(4).laundry_cart, hotel.get_booking_by_id(1))

    hotel.cleaning.create_reservation(hotel.get_guest_by_id(4), datetime.today().date() + timedelta(days=1), datetime.now().strftime("%H:%M"), hotel.get_booking_by_id(1))

    hotel.repair_service.create_reservation(hotel.get_guest_by_id(4), datetime.today().date() + timedelta(days=1), datetime.now().strftime("%H:%M"), hotel.get_item_by_name("Lamp"), "Broken Lightbulb", hotel.get_booking_by_id(1))
    
    # create later booking
    hotel.create_booking(hotel.get_guest_by_id(5), hotel.get_room_by_id(106), datetime.today().date() + timedelta(days=3), datetime.today().date() + timedelta(days=5))
    hotel.create_booking(hotel.get_guest_by_id(6), hotel.get_room_by_id(201), datetime.today().date() + timedelta(days=2), datetime.today().date() + timedelta(days=5))
    hotel.create_booking(hotel.get_guest_by_id(7), hotel.get_room_by_id(203), datetime.today().date() + timedelta(days=1), datetime.today().date() + timedelta(days=5))
    hotel.create_booking(hotel.get_guest_by_id(8), hotel.get_room_by_id(206), datetime.today().date() + timedelta(days=9), datetime.today().date() + timedelta(days=15))





######################
#    UI Functions    #
######################
def menu(session):
    extra = "Sign Up"
    login = "Login"
    if "user_id" in session:
        extra = "Profile"
        login = "Logout"
    if get_user_role(session) == "Staff":
        extra = "Staff"

    return Nav(
                Div(
                    A("Home", href="/", cls="secondary"),
                    A("Services", href="/services", cls="secondary"),
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
            P(f"Furnitures/Commodities: {', '.join([item.name for item in room.items])}"),
            Form(
                Input(type="hidden", name="room-id", value=room.room_id),
                Button(f"Book now for ฿{(end_date - start_date).days * room.price}", cls="btn btn-primary",
                    style="font-weight: bold;"),
                action="/booking/review",
                method="GET"
            ),

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
            P(f"Furnitures/Commodities: {', '.join([item.name for item in room.items])}"),
            P(f"Check-in Date: {start_date.strftime('%Y-%m-%d')}"),
            P(f"Check-out Date: {end_date.strftime('%Y-%m-%d')}"),
            P(f"Total Price: ฿{(end_date - start_date).days * room.price}"),
            cls="card-text",
            style="text-align: left; margin-left: 20px;"
        ),
        style="width: 100%; margin: 10px 0; display: flex;"
    )


def checkin_table(booking: Booking):
    return Tr(
                Td(booking.booking_id),
                Td(booking.room.room_id),
                Td(booking.guest.real_name),
                Td(booking.start_date),
                Td(booking.end_date),
                Td(Button("Check In", cls="btn btn-primary", hx_post=f"/staff/check-in/{booking.booking_id}"))
            )


def checkout_table(booking: Booking):
    return Tr(
                Td(booking.booking_id),
                Td(booking.room.room_id),
                Td(booking.guest.real_name),
                Td(booking.start_date),
                Td(booking.end_date),
                Td(Button("Check Out", cls="btn btn-primary", hx_post=f"/staff/check-out/{booking.booking_id}"))
            )

def food_card(f, cart):
    cart_quantity = cart.items.get(f.name, {}).get('quantity', 0)
    is_available = f.amount - cart_quantity > 0
    button_text = "Add to Cart" if is_available else "Out of Stock"
    button_disabled = not is_available
    button_color = "grey" if not is_available else "#2196f3"

    return Card(
        Div(
            Div(
                H3(f.name),
                P(f"Price: ฿{f.price:.2f}"),
                P(f"Stock: {f.amount}"),
                Button(
                    button_text,
                    hx_post=f"/foods/add/{f.name}",
                    hx_target="#dish-list",
                    style=f"outline: none; margin-top: 10px; padding: 8px 12px; width:120px; background-color:{button_color}; color:white;",
                    disabled="disabled" if not cart_quantity < f.amount else ""
                ),
                style="display:flex; flex-direction:column; justify-content:center; gap:5px; padding-right:15px;"
            ),
            Img(src=f.image_url, style="width:200px; height:150px; object-fit:cover; border-radius:8px;"),
            style="display:flex; justify-content:space-between; align-items:center; width:100%;"
        ),
        style="display:flex; justify-content:space-between; align-items:center; box-shadow:0 4px 8px rgba(0,0,0,0.2); border-radius:10px; margin:10px; padding:10px;"
    )

def render_cart_items(cart, removal_url_base):
    items = []
    for item in cart.items.values():
        product = item['product']
        quantity = item['quantity']
        remove_button = Button(
            "X",
            hx_post=f"{removal_url_base}/{product.name}",
            hx_target="#cart-display",
            style="font-size:20px; padding:2px 4px; color:red; background: none; border: none; cursor: pointer;"
        )
        items.append(
            Div(
                P(f"{product.name} x {quantity} - ฿{product.price * quantity:.2f}"),
                remove_button,
                style="display: flex; align-items: center; gap: 10px;"
            )
        )
    if not items:
        items.append(P("Cart is empty."))
    return Container(*items)

def render_order_button(cart, order_endpoint):
    disabled = not bool(cart.items)
    base_style = "margin-top: 10px; padding: 8px 12px; border: none; font-size: 14px;"
    if disabled:
        style = base_style + " background-color: grey; color: white; cursor: not-allowed;"
    else:
        style = base_style + " background-color: green; color: white; cursor: pointer;"
    return Button("Place Order", hx_post=order_endpoint, disabled=disabled, style=style)

def cloth_card(cloth):
    return Card(
        H3(cloth.name),
        P(f"Price: ฿{cloth.price:.2f}"),
        Button(
            "Add",
            hx_post=f"/laundry/add/{cloth.name}", 
            hx_target="#cloth-list",
            style="outline: none;"
        ),
        style="box-shadow: 0 4px 8px rgba(0,0,0,0.2); border-radius: 10px; margin: 10px; padding: 10px;"
    )      


######################
#   Web  Functions   #
######################
def check_login(session, page=None):
    if "user_id" not in session:
        print("User not logged in")
        return RedirectResponse(f"/login?redirect={page}" if page else "/login", status_code=303)

def get_user_role(session):
    if "user_id" not in session:
        return None
    return hotel.get_role_by_id(session["user_id"])


def get_guest_staying_booking(session):
    if "user_id" not in session:
        return None
    
    for booking in hotel.get_booking_of_guest(hotel.get_guest_by_id(session["user_id"])):
        if booking.status == "Staying":
            return booking
    return None


def booking_belongs_to_user(session, booking_id):
    if "user_id" not in session:
        return False
    return hotel.get_guest_by_id(session["user_id"]) == hotel.get_booking_by_id(booking_id).guest



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
            Button("Book Now", cls="btn btn-primary", onclick="document.location='/booking'", style="width: 300px; height: 100px; font-size: 2.5em; font-weight: 800;"),
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
    redirect = check_login(session, "booking")

    if redirect:
        return redirect
    
    if get_user_role(session) == "Staff":
        return RedirectResponse("/staff", status_code=303)

    return (Title("Booking"),
        menu(session), Br(),
        Container(H1("Book a Room"),
            Form(Label("Check-in Date and Check-out Date",
                    Group(
                        Input(type="date", name="check-in", value=f"{(datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")}", required=True, min=f"{(datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d')}", max=f"{(datetime.today() + timedelta(days=365)).strftime('%Y-%m-%d')}"),
                        Input(type="date", name="check-out", value=f"{(datetime.today() + timedelta(days=2)).strftime("%Y-%m-%d")}", required=True, min=f"{(datetime.today() + timedelta(days=2)).strftime('%Y-%m-%d')}", max=f"{(datetime.today() + timedelta(days=366)).strftime('%Y-%m-%d')}"),
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
                Label("Items: ",
                    Input(type="checkbox", name="items-TV", value="TV",),"Television",
                    Input(type="checkbox", name="items-AC", value="AC"),"Air-Conditioning",
                    Input(type="checkbox", name="items-Wifi", value="Wifi"),"Wi-Fi"
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
async def post(session, request):
    try:
        form_data = await request.form()
        start_date = datetime.strptime(form_data.get("check-in"), "%Y-%m-%d")
        end_date = datetime.strptime(form_data.get("check-out"), "%Y-%m-%d")
        room_type = form_data.get("room-type")
        guest_size = int(form_data.get("guests"))
        max_price = int(form_data.get("max-price"))
        tv = form_data.get("items-TV")
        ac = form_data.get("items-AC")
        wifi = form_data.get("items-Wifi")
        items = []
        if tv:
            items.append(tv)
        if ac:
            items.append(ac)
        if wifi:
            items.append(wifi)

        print("Received form data:", form_data)
    except:
        return P("Invalid form data", style="color: red")

    if start_date > end_date:
        return P("Invalid Date Range", style="color: red;")
    
    if start_date < datetime.today():
        return P("Invalid Check-in Date", style="color: red;")

    if room_type not in ["Single", "Double", "Family", "Suite", "All"]:
        return P("Invalid Room Type", style="color: red;")

    session["booking"] = {
        "start_date": start_date.strftime("%Y-%m-%d"),
        "end_date": end_date.strftime("%Y-%m-%d"),
    }

    matching_hotel = hotel.get_room_by_attribute(room_type, guest_size, max_price, items, start_date.date(), end_date.date())

    if matching_hotel == []:
        return P("No rooms available / match your criteria 😔")   

    return Div(*(display_room(room, start_date, end_date) for room in matching_hotel))


@rt("/booking/review")
async def get(session, request):
    redirect =  check_login(session, "booking")

    if redirect:
        return redirect
    
    if get_user_role(session) == "Staff":
        return RedirectResponse("/staff", status_code=303)

    if session["booking"] is None:
        return RedirectResponse("/booking", status_code=303)

    start_date = session["booking"]["start_date"]
    end_date = session["booking"]["end_date"]

    room = request.query_params.get('room-id')

    if room is None:
        return RedirectResponse("/booking", status_code=303)

    room_id = int(room)

    formated_start = datetime.strptime(start_date, "%Y-%m-%d")
    formated_end = datetime.strptime(end_date, "%Y-%m-%d")

    if hotel.check_room_availability(room_id, formated_start, formated_end) == False:
        return P("Room is not available")

    if room_id not in [room.room_id for room in hotel.rooms]:
        return P("Invalid Room")

    if datetime.strptime(start_date, "%Y-%m-%d") < datetime.today():
        return P("Invalid Check-in Date")
    
    if datetime.strptime(start_date, "%Y-%m-%d") > datetime.strptime(end_date, "%Y-%m-%d"):
        return P("Invalid Date Range")
    
    if hotel.get_room_by_id(room_id).status == 0:
        return P("Room is not available")

    return (Title("Review"), menu(session), Br(),
        Container(
            H1("Booking Confirmation"),
            reciept_card(hotel.get_room_by_id(room_id), formated_start, formated_end),
            Card(
                Form(
                    Label("Full Legal Name on Credit Card",
                        Input(type="text", name="full-name", required=True)),
                    Group(
                        Input(placeholder="Credit Card Number", type="tel", pattern="[0-9]{16}", maxlength=19, name="credit-card", required=True),
                        Input(placeholder="Expiry Date (MM)", type="number", min=1, max=12, name="expiration-month", required=True),
                        Input(placeholder="Expiry Date (YY)", type="number", min=0, max=99, name="expiration-year", required=True),
                        Input(placeholder="CVV", type="tel", pattern="[0-9]{3,4}", name="cvv", maxlength=4, required=True),
                    ),
                    Label("Billing Address",
                        Input(type="text", name="address", required=True)),
                    P(id="return-message", style="color: red;"),
                    Input(type="hidden", name="room-id", value=room_id),
                    Button("Confirm", type="submit", cls="btn btn-primary"),
                    hx_post=f"/booking/review", hx_target="#return-message", required=True
                ),
                style="text-align: center;"
            ),
            style="text-align: left;",
            id="booking-form"
        )
    )


@rt("/booking/review")
async def post(session, request):
    form_data = await request.form()

    user = hotel.get_guest_by_id(session["user_id"])

    name = form_data.get("full-name")
    card_number = form_data.get("credit-card")
    expiration_month = int(form_data.get("expiration-month"))
    expiration_year = int(form_data.get("expiration-year"))
    cvv = form_data.get("cvv")
    address = form_data.get("address")
    room_id = int(form_data.get("room-id"))

    room = hotel.get_room_by_id(room_id)

    expiration = datetime.strptime(f"{str(expiration_month)}/{str(expiration_year)}", "%m/%y")

    if len(card_number) != 16:
        return P("Invalid Credit Card Number", id="return-message", style="color: red;")
    if not card_number.isdigit():
        return P("Invalid Credit Card Number", id="return-message", style="color: red;")
    if expiration_month not in range(1, 13):
        return P("Invalid Expiry Month", id="return-message", style="color: red;")
    if expiration_year not in range(0, 100):
        return P("Invalid Expiry Year", id="return-message", style="color: red;")
    if expiration < datetime.today():
        return P("Credit Card Expired", id="return-message", style="color: red;")
    if len(cvv) not in [3, 4]:
        return P("Invalid CVV", id="return-message", style="color: red;")
    
    start_date = (datetime.strptime(session["booking"]["start_date"], "%Y-%m-%d")).date()
    end_date = (datetime.strptime(session["booking"]["end_date"], "%Y-%m-%d")).date()

    if hotel.create_booking(user, room, start_date, end_date) != "Success":
        return P("Room is not available")

    return Redirect("/success")

@rt("/success")
def get(session):
    redirect = check_login(session, "booking")

    if redirect:
        return redirect
    
    if get_user_role(session) == "Staff":
        return RedirectResponse("/staff", status_code=303)
    
    session["booking"] = None
    return (Title("Success"), menu(session), Br(),
        Container(
        H1("Booking Successful"),
        P("Thank you for booking with us"),
        style="text-align: center;"
    ))

@rt("/profile")
def get(session):
    redirect =  check_login(session, "profile")

    if redirect:
        return redirect

    if get_user_role(session) == "Staff":
        return RedirectResponse("/staff", status_code=303)
    
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
                            Td(Button("View", cls="btn btn-primary", onclick=f"document.location='/profile/booking/{booking.booking_id}'"))
                        ) for booking in hotel.get_booking_of_guest(user))
                    ),
                    cls="striped"
                ),
                style="text-align: center;"
            )
                
        )
    ))


@rt("/profile/booking/{booking_id}")
def get(booking_id: int, session):
    redirect =  check_login(session, "profile")

    if redirect:
        return redirect
    
    if get_user_role(session) == "Staff":
        return RedirectResponse("/staff", status_code=303)

    if booking_belongs_to_user(session, booking_id) == False:
        return P("Invalid Booking ID")

    booking = hotel.get_booking_by_id(booking_id)
    print(booking)
    if booking is None:
        return P("Invalid Booking ID")

    return (Title("Booking Reciept"),
        menu(session), Br(),
        Container(
            H1("Booking Reciept", style="text-align: center;"),
            Card(
                Img(src=f"/images/{booking.room.image}", cls="card-img-top", alt=f"Room {booking.room.room_id}",
                style="width: auto; max-height: 300px; object-fit: cover;"),
                Div(
                    H2(f"Room {booking.room.room_id}"),
                    P(f"Room Type: {booking.room.type}"),
                    P(f"Maximum People: {"👤" * booking.room.size}"),
                    P(f"Price: ฿{booking.room.price} / Day"),
                    P(f"Status: {"Available" if booking.room.status == 1 else "Unavailable"}"),
                    P(f"Furniture/Commodities: {', '.join([item.name for item in booking.room.items])}"),
                    cls="card-text",
                    style="text-align: left; margin-left: 20px;"
                ),
                style="width: 100%; margin: 10px 0; display: flex;"
            ),
            Card(
                H2("Booking Details"),
                P(f"Booking ID: {booking.booking_id}"),
                P(f"Check-in Date: {booking.start_date.strftime('%Y-%m-%d')}"),
                P(f"Check-out Date: {booking.end_date.strftime('%Y-%m-%d')}"),
                P(f"Status: {booking.status}"),
                Button("Cancel Booking", cls="btn btn-primary", hx_post=f"/profile/booking/{booking.booking_id}/cancel", disabled="disabled" if booking.status != "Pending" else ""),
                style="text-align: center;"
            ),
            Card(
                H2("Payment Details"),
                P(f"Total Room Price: ฿{(booking.end_date - booking.start_date).days * booking.room.price}"),
                P(f"Total Service Fee: ฿{hotel.get_total_service_fee(booking)}"),
                P(f"Transaction only includes completed services."),
                H2("Transportation History"),
                Table(
                    Thead(
                        Tr(
                            Th("Route"),
                            Th("Price"),
                            Th("Time"),
                            Th("Status"),
                        )
                    ),
                    Tbody(
                        *(Tr(
                            Td(transport.route.name),
                            Td(f"฿{transport.route.price if transport.status != 'Cancelled' else 0}"),
                            Td(transport.assigned_time),
                            Td(transport.status),
                        ) for transport in hotel.get_services_of_booking(booking, "Transport"))
                    ),
                    Tfoot(
                        Tr(
                            Td("Total"),
                            Td(f"฿{sum(transport.route.price if transport.status != "Cancelled" else 0 for transport in hotel.get_services_of_booking(booking, "Transport"))}"),
                            Td(),
                            Td(),
                        )
                    ),
                    cls="striped"
                ),
                H2("Food Order History"),
                Table(
                    Thead(
                        Tr(
                            Th("Food"),
                            Th("Price"),
                            Th("Status"),
                        )
                    ),
                    Tbody(
                        *(Tr(
                            Td(", ".join([f"{item['name']} x{item['amount']}" for item in order.items])),
                            Td(f"฿{order.total if order.status != 'Cancelled' else 0}"),
                            Td(order.status),
                        ) for order in hotel.get_services_of_booking(booking, "Food Ordering"))
                    ),
                    Tfoot(
                        Tr(
                            Td("Total"),
                            Td(f"฿{sum(order.total if order.status != "Cancelled" else 0 for order in hotel.get_services_of_booking(booking, "Food Ordering"))}"),
                            Td(),
                        )
                    ),
                ),
                H2("Laundry Order History"),
                Table(
                    Thead(
                        Tr(
                            Th("Cloth"),
                            Th("Price"),
                            Th("Status"),
                        )
                    ),
                    Tbody(
                        *(Tr(
                            Td(", ".join([f"{item['name']} x{item['amount']}" for item in order.items])),
                            Td(f"฿{order.total if order.status != 'Cancelled' else 0}"),
                            Td(order.status),
                        ) for order in hotel.get_services_of_booking(booking, "Laundry"))
                    ),
                    Tfoot(
                        Tr(
                            Td("Total"),
                            Td(f"฿{sum(order.total if order.status != "Cancelled" else 0 for order in hotel.get_services_of_booking(booking, "Laundry"))}"),
                            Td(),
                        )
                    ),
                ),
                H2("Cleaning Order History"),
                Table(
                    Thead(
                        Tr(
                            Th("Appointment Time"),
                            Th("Status")
                        )
                    ),
                    Tbody(
                        *(Tr(
                            Td(order.appointment_date, " ", order.appointment_time),
                            Td(order.status),
                        ) for order in hotel.get_services_of_booking(booking, "Cleaning Service"))
                    ),
                ),
                H2("Repair Service Order History"),
                Table(
                    Thead(
                        Tr(
                            Th("Appointment Time"),
                            Th("Item"),
                            Th("Issue"),
                            Th("Fee"),
                            Th("Status"),
                        )
                    ),
                    Tbody(
                        *(Tr(
                            Td(order.appointment_date, " ", order.appointment_time),
                            Td(order.item.name),
                            Td(order.repair_issue),
                            Td(f"฿{order.total if order.status != 'Cancelled' else 0}"),
                            Td(order.status),
                        ) for order in hotel.get_services_of_booking(booking, "Repair Service"))
                    ),
                    Tfoot(
                        Tr(
                            Td("Total"),
                            Td(),
                            Td(),
                            Td(f"฿{sum(order.total if order.status != "Cancelled" else 0 for order in hotel.get_services_of_booking(booking, "Repair Service"))}"),
                            Td(),
                        )
                    ),
                ),
                style="text-align: center;"
            )
        )
    )


@rt("/profile/booking/{booking_id}/cancel")
def post(booking_id: int, session):
    redirect =  check_login(session, "profile")

    if redirect:
        return redirect

    if booking_belongs_to_user(session, booking_id) == False:
        return P("Invalid Booking ID")
    
    booking = hotel.get_booking_by_id(booking_id)
    if booking is None:
        return P("Invalid Booking ID")
    
    if booking.cancel_booking() == "Success":
        return Redirect("/profile")
    else:
        return P("Cancellation Failed")


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
                        Input(id="togglePassword", type="password", name="password", required=True)),
                    Label("Confirm Password",
                        Input(id="togglePassword", type="password", name="confirm-password", required=True)),
                    Script("""
                            document.getElementById('togglePassword').addEventListener('change', function () {
                            var passwordField = document.getElementById('password');
                            passwordField.type = this.checked ? 'text' : 'password';
                        });
                    """),
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

    status_message = hotel.create_guest(username, real_name, email, password)

    if status_message == "Success":
        return Redirect("/login")
    else:
        return P(f"{status_message}")


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
                        Input(id="password", type="password", name="password", required=True)),
                    Label(Input(id="togglePassword", type="checkbox")," Show Password"),
                    Script("""
                            document.getElementById('togglePassword').addEventListener('change', function () {
                            var passwordField = document.getElementById('password');
                            passwordField.type = this.checked ? 'text' : 'password';
                        });
                    """),
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

    if account is not None: 
        session["user_id"] = account.user_id
        return Redirect(hidden_redirect)
    else:
        return P("Invalid credentials", style="color: red;")


@rt("/logout")
def get(session):
    session.pop("user_id", None)
    return Redirect("/")


######################
#    Staff  Routes   #
######################


@rt("/staff")
def get(session):
    redirect = check_login(session)

    if redirect:
        return redirect

    for staff in hotel.staffs:
        if staff.user_id == session["user_id"]:
            return Title("Staff Home"), (menu(session), Br(),
                Container(
                    Card(
                        H1("Staff Home"),
                        P("Welcome to the staff home page"),
                        H2("Staff Services"),
                        A("Room Management", href="/staff/room-management"), Br(),
                        A("Check In", href="/staff/check-in"), Br(),
                        A("Check Out", href="/staff/check-out"), Br(),
                        A("Assigned Service", href="/staff/services"), Br(),
                        A("Create new staff account", href="/staff/signup"), Br(),
                        style="text-align: center;"
                    )
                )
            )
    return RedirectResponse("/", status_code=303)


@rt("/staff/room-management")
async def get(session):
    return Title("Room Editor"), menu(session), Br(), Container(
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
                Label("Items"),
                    *((Input(type="checkbox", name=f"items-{item.name}", value=item.name), Label(item.name)) for item in hotel.items),
                Br(),
                Label("Image"),
                Input(type="text", name="image", required=True
                ),
                Button("Add", type="submit", cls="btn btn-primary", hx_post=f"/add-room", hx_target="#return-message"),
                id="room-filter",
                style=""
            ),
            P(id="return-message"),
            H2("Edit Room"),
            Form(
                Label("Room ID"),
                Input(type="number", name="search-room-id", required=True),
                Button("Search", type="submit", cls="btn btn-primary", hx_post=f"/find-room", hx_target="#return-form"),
                P(id="return-form"),
            )
        )
    
@rt("/add-room")
async def post(request):
    form_data = await request.form()
    room_id = form_data.get("room-id")
    room_type = form_data.get("room-type")
    size = form_data.get("size")
    price = form_data.get("price")
    status = form_data.get("status")
    items = []
    for item in hotel.items:
        if form_data.get(f"items-{item.name}"):
            items.append(item)
    image = form_data.get("image")

    print(room_id, room_type, size, price, status, items, image)

    if (room_id in [room.room_id for room in hotel.rooms]):
        return P("Room ID already in use, try another ID")
    
    hotel.create_room(int(room_id), room_type, int(size), int(price), bool(status), items, image)
    return P("Room Added")


@rt("/find-room")
async def post(request):
    form_data = await request.form()
    room_id = form_data.get("search-room-id")

    room = hotel.get_room_by_id(int(room_id))
    if room is None:
        return P("Room not found")

    return Form(
        Label("Room ID"),
        Input(type="number", name="room-id", value=room.room_id, required=True),
        Label("Room Type"),
        Select(
            Option("Single", value="Single", selected=room.type == "Single"),
            Option("Double", value="Double", selected=room.type == "Double"),
            Option("Family", value="Family", selected=room.type == "Family"),
            Option("Suite", value="Suite", selected=room.type == "Suite"),
            name="room-type",
            requires=True
        ),
        Label("Size"),
        Input(type="number", name="size", value=room.size, required=True),
        Label("Price"),
        Input(type="number", name="price", value=room.price, required=True),
        Label("Status"),
        Select(
            Option("Available", value="1", selected=room.status == 1),
            Option("Unavailable", value="0", selected=room.status == 0),
            name="status",
            required=True
        ),
        Label("Items"),
            *((Input(type="checkbox", name=f"items-{item.name}", value=item.name, checked=item in room.items), Label(item.name)) for item in hotel.items),
        Br(),
        Label("Image"),
        Input(type="text", name="image", value=room.image, required=True
        ),
        Button("Edit", type="submit", cls="btn btn-primary", hx_post=f"/edit-room", hx_target="#edit-return-message"),
        P(id="edit-return-message"),
        id="room-filter",
    )


@rt("/edit-room")
async def post(request):
    form_data = await request.form()
    room_id = form_data.get("room-id")
    room_type = form_data.get("room-type")
    size = form_data.get("size")
    price = form_data.get("price")
    status = form_data.get("status")
    items = []
    for item in hotel.items:
        if form_data.get(f"items-{item.name}"):
            items.append(item)
    image = form_data.get("image")
    
    if (room_id in [room.room_id for room in hotel.rooms]):
        return P("Room ID already in use, try another ID")
    
    hotel.edit_room(int(room_id), room_type, int(size), int(price), bool(status), items, image)
    return P("Room Edited")


@rt("/staff/check-in")
def get(session):
    redirect =  check_login(session)

    if redirect:
        return redirect

    valid_booking = hotel.filter_check_in()

    for staff in hotel.staffs:
        if staff.user_id == session["user_id"]:
            return (Title("Check In"),
                menu(session),
                Br(),
                Container(
                    H1("Check In"),
                    Form(
                        Group(Input(type="number", name="room-id", placeholder="Room ID"),
                            Input(type="text", name="guest-name", placeholder="Guest Name"),
                            Input(type="date", name="check-in-date"),
                            Input(type="date", name="check-out-date"),
                            Button("Search", type="submit", cls="btn btn-primary", hx_post="/staff/check-in", hx_target="#table-body"),
                            id="check-in-form")
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
                    Tbody(*(checkin_table(booking) for booking in valid_booking), id="table-body"), cls="striped"),
                    style="text-align: center;"
                
            ))
    return RedirectResponse("/", status_code=303)

@rt("/staff/check-in")
async def post(request, session):
    redirect =  check_login(session)

    try:
        form_data = await request.form()
        # optional parameter
        room_id = int(form_data.get("room-id")) if form_data.get("room-id") else None
        guest_name = form_data.get("guest-name") if form_data.get("guest-name") else None
        check_in_date = datetime.strptime(form_data.get("check-in-date"), "%Y-%m-%d") if form_data.get("check-in-date") else None
        check_out_date = datetime.strptime(form_data.get("check-out-date"), "%Y-%m-%d") if form_data.get("check-out-date") else None
    except:
        return Tbody(Tr(Td("Invalid Form Data", colspan=6)), id="table-body")

    valid_booking = hotel.filter_check_in(room_id, guest_name, check_in_date, check_out_date)

    return [*(checkin_table(booking) for booking in valid_booking)]


@rt("/staff/check-in/{booking_id}")
def post(booking_id: int, session):
    redirect =  check_login(session)

    if redirect:
        return redirect

    if hotel.check_in_booking(booking_id) == "Success":
        return Redirect("/staff/check-in")
    else:
        return Redirect("/staff/check-in")


@rt("/staff/check-out")
def get(session):
    redirect =  check_login(session, "booking")

    if redirect:
        return redirect

    valid_booking = hotel.filter_check_out()

    for staff in hotel.staffs:
        if staff.user_id == session["user_id"]:
            return (Title("Check Out"),
                menu(session),
                Br(),
                Container(
                    H1("Check Out"),
                    Form(
                        Group(Input(type="number", name="room-id", placeholder="Room ID"),
                            Input(type="text", name="guest-name", placeholder="Guest Name"),
                            Button("Search", type="submit", cls="btn btn-primary", hx_post="/staff/check-out", hx_target="#table-body"),
                            id="check-out-form")
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
                    Tbody(*(checkout_table(booking) for booking in valid_booking), id="table-body"), cls="striped"),
                    style="text-align: center;"
                
            ))
    return RedirectResponse("/", status_code=303)

@rt("/staff/check-out")
async def post(request, session):
    redirect =  check_login(session)

    if redirect:
        return redirect

    try:
        form_data = await request.form()
        # optional parameter
        room_id = int(form_data.get("room-id")) if form_data.get("room-id") else None
        guest_name = form_data.get("guest-name") if form_data.get("guest-name") else None
    except:
        return Tbody(Tr(Td("Invalid Form Data", colspan=6)), id="table-body")
    
    valid_booking = hotel.filter_check_out(room_id, guest_name)

    return [*(checkout_table(booking) for booking in valid_booking)]


@rt("/staff/check-out/{booking_id}")
def post(booking_id: int, session):
    redirect =  check_login(session)

    if redirect:
        return redirect

    hotel.check_out_booking(booking_id)

    return Redirect("/staff/check-out")


@rt("/staff/booking")
def get(session):
    redirect =  check_login(session)

    if redirect:
        return redirect

    for staff in hotel.staffs:
        if staff.user_id == session["user_id"]:
            return (Title("Booking Management"),
                menu(session),
                Br(),
                Container(
                    H1("Booking Management"),
                    Table(
                        Thead(
                            Tr(
                                Th("Booking ID"),
                                Th("Room ID"),
                                Th("Guest Name"),
                                Th("Check-in Date"),
                                Th("Check-out Date"),
                                Th("Status")
                            )
                        ),
                        Tbody(
                            *(Tr(
                                Td(booking.booking_id),
                                Td(booking.room.room_id),
                                Td(booking.guest.real_name),
                                Td(booking.start_date),
                                Td(booking.end_date),
                                Td(booking.status)
                            ) for booking in hotel.bookings),
                            id="table-body"
                        ),
                        cls="striped"
                    ),
                    style="text-align: center;"
                )
            )
    return RedirectResponse("/", status_code=303)

@rt("/staff/services")
def get(session):
    redirect =  check_login(session)

    if redirect:
        return redirect

    if get_user_role(session) != "Staff":
        return RedirectResponse("/", status_code=303)
    
    return Title("Service"), menu(session), Br(), Container(
        Button("▲", id="toggle-btn",
               onclick="""
                   var content = document.getElementById('collapsible-container');
                   if (content.style.maxHeight && content.style.maxHeight !== '0px'){
                       content.style.maxHeight = '0px';
                       this.innerHTML = '▼';
                   } else {
                       content.style.maxHeight = '700px';
                       this.innerHTML = '▲';
                   }
               """,
              style="background: none; border: none; font-size: 12px; cursor: pointer; margin-bottom: 5px; color: #000;"
        ),
        Card(
            H1("Choose Service", style="text-align: center; color: #2196f3; margin: 20px 0; font-weight: 800;"),
            Grid(
                Card(
                    H3("Transportation"),
                    Button("Choose", hx_get="/staff/transport", hx_target="#main-content", hx_swap="innerHTML"),
                    style="none; border-radius: 10px; padding: 20px; margin: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);"
                ),
                Card(
                    H3("Laundry Service"),
                    Button("Choose", hx_get="/staff/laundry", hx_target="#main-content", hx_swap="innerHTML"),
                    style="none; border-radius: 10px; padding: 20px; margin: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);"
                ),
                Card(
                    H3("Order Foods"),
                    Button("Choose", hx_get="/staff/foods", hx_target="#main-content", hx_swap="innerHTML"),
                    style="none; border-radius: 10px; padding: 20px; margin: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);"
                ),
                Card(
                    H3("Cleaning Service"),
                    Button("Choose", hx_get="/staff/cleaning", hx_target="#main-content", hx_swap="innerHTML"),
                    style="none; border-radius: 10px; padding: 20px; margin: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);"
                ),
                Card(
                    H3("Repair Service"),
                    Button("Choose", hx_get="/staff/repair", hx_target="#main-content", hx_swap="innerHTML"),
                    style="none; border-radius: 10px; padding: 20px; margin: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);"
                )
            ),
            id="collapsible-container",
            style="max-height: 700px; overflow: hidden; transition: max-height 0.5s ease-out; border: 1px solid #ccc; border-radius: 5px; padding: 10px; margin-bottom: 20px;"
        ),
        Div(id="main-content"),
        Div(
            P("Action Completed"),
            Button("Close", onclick="document.getElementById('orderModal').style.display='none';"),
            id="orderModal",
            style="""
                display: none;
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                background: #fff;
                padding: 30px;
                border: 2px solid #2196f3;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
                z-index: 1000;
                text-align: center;
                font-size: 18px;
                color: #333;
            """
        )
    )

@rt("/staff/transport")
def get(session):
    redirect =  check_login(session)

    if redirect:
        return redirect

    if get_user_role(session) != "Staff":
        return RedirectResponse("/", status_code=303)
    
    staff = hotel.get_staff_by_id(session["user_id"])
    
    return Title("Transportation"), Br(), Container(
        H1("Transportation"),
        Table(
            Thead(
                Tr(
                    Th("Order ID"),
                    Th("Timestamp"),
                    Th("Guest Name"),
                    Th("Route"),
                    Th("Appointment Time"),
                    Th("Assigned Staff"),
                    Th("Action")
                )
            ),
            Tbody(
                *(Tr(
                    Td(reservation.id),
                    Td(str(reservation.timestamp)),
                    Td(reservation.guest.real_name),
                    Td(reservation.route.name),
                    Td(reservation.assigned_time),
                    Td(reservation.staff.real_name if reservation.staff else "Not Assigned"),
                    Td(Button("Assign Self", type="button", hx_post=f"/staff/transport/assign/{reservation.id}", hx_target="#transport-confirmation", hx_swap="outerHTML", disabled=(staff.current_service is not None or reservation.staff is not None)),
                       Button("Unassign Self", type="button", hx_post=f"/staff/transport/unassign/{reservation.id}", hx_target="#transport-confirmation", hx_swap="outerHTML", disabled=(staff.current_service is None or staff.current_service.id != reservation.id)),
                        Button("Complete", type="button", hx_post=f"/staff/transport/complete/{reservation.id}", hx_target="#transport-confirmation", hx_swap="outerHTML", disabled=(staff.current_service is None or staff.current_service.id != reservation.id)),
                        Button("Cancel", type="button", hx_post=f"/staff/transport/cancel/{reservation.id}", hx_target="#transport-confirmation", hx_swap="outerHTML", disabled=(staff.current_service is None or staff.current_service.id != reservation.id)),
                        id=f"row-{reservation.id}"
                    )
                ) for reservation in hotel.transport.get_reserved_reservation())
            ),
            Div(id="transport-confirmation"),
            cls="striped"
        )
    )

@rt("/staff/transport/assign/{reservation_id}")
def post(reservation_id: int, session):
    redirect =  check_login(session)

    if redirect:
        return redirect

    if get_user_role(session) != "Staff":
        return RedirectResponse("/", status_code=303)
    
    staff = hotel.get_staff_by_id(session["user_id"])

    hotel.transport.assign_reservation(reservation_id, staff)

    return Div(
        Script("""
            document.getElementById('orderModal').style.display = 'block';
            htmx.ajax('GET', '/staff/transport', {target: '#main-content'});
        """),
        H3("Assigned"),
        P(f"Reservation ID: {reservation_id}"),
        hx_swap_oob="outerHTML",
        id="transport-confirmation"
    )


@rt("/staff/transport/unassign/{reservation_id}")
def post(reservation_id: int, session):
    redirect =  check_login(session)

    if redirect:
        return redirect

    if get_user_role(session) != "Staff":
        return RedirectResponse("/", status_code=303)
    
    staff = hotel.get_staff_by_id(session["user_id"])

    hotel.transport.unassign_reservation(reservation_id, staff)

    return Div(
        Script("""
            document.getElementById('orderModal').style.display = 'block';
            htmx.ajax('GET', '/staff/transport', {target: '#main-content'});
        """),
        H3("Unassigned"),
        P(f"Reservation ID: {reservation_id}"),
        hx_swap_oob="outerHTML",
        id="transport-confirmation"
    )


@rt("/staff/transport/complete/{reservation_id}")
def post(reservation_id: int, session):
    redirect =  check_login(session)

    if redirect:
        return redirect

    if get_user_role(session) != "Staff":
        return RedirectResponse("/", status_code=303)

    staff = hotel.get_staff_by_id(session["user_id"])

    hotel.transport.complete_reservation(reservation_id, staff)

    return Div(
        Script("""
            document.getElementById('orderModal').style.display = 'block';
            htmx.ajax('GET', '/staff/transport', {target: '#main-content'});
        """),
        H3("Marked as done!"),
        P(f"Reservation ID: {reservation_id}"),
        hx_swap_oob="outerHTML",
        id="transport-confirmation"
    )


@rt("/staff/transport/cancel/{reservation_id}")
def post(reservation_id: int, session):
    redirect =  check_login(session)

    if redirect:
        return redirect

    if get_user_role(session) != "Staff":
        return RedirectResponse("/", status_code=303)

    staff = hotel.get_staff_by_id(session["user_id"])

    hotel.transport.cancel_reservation(reservation_id, staff)

    return Div(
        Script("""
            document.getElementById('orderModal').style.display = 'block';
            htmx.ajax('GET', '/staff/transport', {target: '#main-content'});
        """),
        H3("Cancelled"),
        P(f"Reservation ID: {reservation_id}"),
        hx_swap_oob="outerHTML",
        id="transport-confirmation"
    )


@rt("/staff/laundry")
def get(session):
    redirect =  check_login(session)

    if redirect:
        return redirect

    if get_user_role(session) != "Staff":
        return RedirectResponse("/", status_code=303)
    
    staff = hotel.get_staff_by_id(session["user_id"])
    
    return Title("Laundry Service"), Br(), Container(
        H1("Add new clothes type"),
        Form(
            Label("Cloth Name"),
            Input(type="text", name="cloth-name", required=True),
            Label("Price"),
            Input(type="number", name="price", required=True, min=1, max=1000),
            Button("Add", type="submit"),
            Div(id="return-message"),
            id="room-filter",
            style="",
            required=True,
            hx_post="/staff/laundry/add", hx_target="#return-message"
        ),
        H1("Laundry Service"),
        Table(
            Thead(
                Tr(
                    Th("Order ID"),
                    Th("Timestamp"),
                    Th("Guest Name"),
                    Th("Items"),
                    Th("Assigned Staff"),
                    Th("Action")
                )
            ),
            Tbody(
                *(Tr(
                    Td(reservation.id),
                    Td(str(reservation.timestamp)),
                    Td(reservation.guest.real_name),
                    Td(", ".join([f"{item['name']} x{item['amount']}" for item in reservation.items])),
                    Td(reservation.staff.real_name if reservation.staff else "Not Assigned"),
                    Td(
                        Button("Assign Self", type="button", hx_post=f"/staff/laundry/assign/{reservation.id}", hx_target="#laundry-confirmation", hx_swap="outerHTML", disabled=(staff.current_service is not None or reservation.staff is not None)),
                        Button("Unassign Self", type="button", hx_post=f"/staff/laundry/unassign/{reservation.id}", hx_target="#laundry-confirmation", hx_swap="outerHTML", disabled=(staff.current_service is None or staff.current_service.id != reservation.id)),
                        Button("Complete", type="button", hx_post=f"/staff/laundry/complete/{reservation.id}", hx_target="#laundry-confirmation", hx_swap="outerHTML", disabled=(staff.current_service is None or staff.current_service.id != reservation.id)),
                        Button("Cancel", type="button", hx_post=f"/staff/laundry/cancel/{reservation.id}", hx_target="#laundry-confirmation", hx_swap="outerHTML", disabled=(staff.current_service is None or staff.current_service.id != reservation.id)),
                        id=f"row-{reservation.id}"
                    )
                ) for reservation in hotel.laundry.get_reserved_reservation())
            ),
            Div(id="laundry-confirmation"),
            cls="striped"
        )
    )


@rt("/staff/laundry/add")
async def post(request):
    form_data = await request.form()
    cloth_name = form_data.get("cloth-name")
    price = int(form_data.get("price"))

    print("Works")

    if hotel.laundry.get_cloth_type(cloth_name) is not None:
        return P("Cloth already exists")
    
    if price < 1:
        return P("Invalid Pricing")

    hotel.laundry.create_cloth(cloth_name, price)

    return P("Cloth Added")


@rt("/staff/laundry/assign/{reservation_id}")
def post(reservation_id: int, session):
    redirect =  check_login(session)

    if redirect:
        return redirect

    if get_user_role(session) != "Staff":
        return RedirectResponse("/", status_code=303)
    
    staff = hotel.get_staff_by_id(session["user_id"])
    
    hotel.laundry.assign_reservation(reservation_id, staff)

    return Div(
        Script("""
            document.getElementById('orderModal').style.display = 'block';
            htmx.ajax('GET', '/staff/laundry', {target: '#main-content'});
        """),
        H3("Assigned"),
        P(f"Reservation ID: {reservation_id}"),
        hx_swap_oob="outerHTML",
        id="laundry-confirmation"
    )


@rt("/staff/laundry/unassign/{reservation_id}")
def post(reservation_id: int, session):
    redirect =  check_login(session)

    if redirect:
        return redirect

    if get_user_role(session) != "Staff":
        return RedirectResponse("/", status_code=303)
    
    staff = hotel.get_staff_by_id(session["user_id"])

    hotel.laundry.unassign_reservation(reservation_id, staff)

    return Div(
        Script("""
            document.getElementById('orderModal').style.display = 'block';
            htmx.ajax('GET', '/staff/laundry', {target: '#main-content'});
        """),
        H3("Unassigned"),
        P(f"Reservation ID: {reservation_id}"),
        hx_swap_oob="outerHTML",
        id="laundry-confirmation"
    )


@rt("/staff/laundry/complete/{reservation_id}")
def post(reservation_id: int, session):
    redirect =  check_login(session)

    if redirect:
        return redirect

    if get_user_role(session) != "Staff":
        return RedirectResponse("/", status_code=303)
    
    staff = hotel.get_staff_by_id(session["user_id"])

    hotel.laundry.complete_reservation(reservation_id, staff)

    return Div(
        Script("""
            document.getElementById('orderModal').style.display = 'block';
            htmx.ajax('GET', '/staff/laundry', {target: '#main-content'});
        """),
        H3("Marked as done!"),
        P(f"Reservation ID: {reservation_id}"),
        hx_swap_oob="outerHTML",
        id="laundry-confirmation"
    )


@rt("/staff/laundry/cancel/{reservation_id}")
def post(reservation_id: int, session):
    redirect =  check_login(session)

    if redirect:
        return redirect

    if get_user_role(session) != "Staff":
        return RedirectResponse("/", status_code=303)
    
    staff = hotel.get_staff_by_id(session["user_id"])

    hotel.laundry.cancel_reservation(reservation_id, staff)

    return Div(
        Script("""
            document.getElementById('orderModal').style.display = 'block';
            htmx.ajax('GET', '/staff/laundry', {target: '#main-content'});
        """),
        H3("Cancelled"),
        P(f"Reservation ID: {reservation_id}"),
        hx_swap_oob="outerHTML",
        id="laundry-confirmation"
    )


@rt("/staff/foods")
def get(session):
    redirect =  check_login(session)

    if redirect:
        return redirect

    if get_user_role(session) != "Staff":
        return RedirectResponse("/", status_code=303)
    
    staff = hotel.get_staff_by_id(session["user_id"])
    
    return Title("Food Orders"), Br(), Container(
        H1("Restock Food"),
        Table(
            Thead(
                Tr(
                    Th("Item Name"),
                    Th("Amount"),
                    Th("Action")
                )
            ),
            Tbody(
                *(Tr(
                    Td(food.name),
                    Td(food.amount),
                    Td(
                        Form(
                            Input(type="hidden", name="item-name", value=food.name),
                            Group(Input(type="number", name="amount", value=1, required=True, min=1, max=100),
                            Button("Restock", type="submit", cls="btn btn-primary", hx_post="/staff/foods/restock", hx_target="#foods-confirmation"), style="margin: 0; width: 350px;"),
                            id=f"row-{food.name}"
                        )
                    )
                ) for food in hotel.food_ordering.dishes)
            ),
            Div(id="foods-confirmation"),
            cls="striped"
        ),
        H1("Add new dish"),
        Form(
            Label("Dish Name",
                Input(type="text", name="dish-name", required=True)),
            Label("Price",
                Input(type="number", name="price", required=True, min=1, max=100)),
            Label("Amount",
                Input(type="number", name="amount", required=True, min=1, max=100)),
            Button("Add", type="submit", cls="btn btn-primary"),
            id="add-dish-form",
            hx_post="/staff/foods/add-dish", hx_target="#foods-confirmation",
        ),
        H1("Food Orders"),
        Table(
            Thead(
                Tr(
                    Th("Order ID"),
                    Th("Timestamp"),
                    Th("Guest Name"),
                    Th("Items"),
                    Th("Assigned Staff"),
                    Th("Action")
                )
            ),
            Tbody(
                *(Tr(
                    Td(reservation.id),
                    Td(str(reservation.timestamp)),
                    Td(reservation.guest.real_name),
                    Td(", ".join([f"{item['name']} x{item['amount']}" for item in reservation.items])),
                    Td(reservation.staff.real_name if reservation.staff else "Not Assigned"),
                    Td(Button("Assign Self", type="button", hx_post=f"/staff/foods/assign/{reservation.id}", hx_target="#foods-confirmation", hx_swap="outerHTML", disabled=(staff.current_service is not None or reservation.staff is not None)),
                       Button("Unassign Self", type="button", hx_post=f"/staff/foods/unassign/{reservation.id}", hx_target="#foods-confirmation", hx_swap="outerHTML", disabled=(staff.current_service is None or staff.current_service.id != reservation.id)),
                        Button("Complete", type="button", hx_post=f"/staff/foods/complete/{reservation.id}", hx_target="#foods-confirmation", hx_swap="outerHTML", disabled=(staff.current_service is None or staff.current_service.id != reservation.id)),
                        Button("Cancel", type="button", hx_post=f"/staff/foods/cancel/{reservation.id}", hx_target="#foods-confirmation", hx_swap="outerHTML", disabled=(staff.current_service is None or staff.current_service.id != reservation.id)),
                        id=f"row-{reservation.id}"
                    )
                ) for reservation in hotel.food_ordering.get_reserved_reservation())
            ),
            Div(id="foods-confirmation"),
            cls="striped"
        )
    )


@rt("/staff/foods/restock")
async def post(request):
    form_data = await request.form()
    item_name = form_data.get("item-name")
    amount = int(form_data.get("amount"))

    if amount <= 0:
        return Div(
            Script("""
                document.getElementById('orderModal').style.display = 'block';
                htmx.ajax('GET', '/staff/foods', {target: '#main-content'});
            """),
            H3("Invalid amount"),
            hx_swap_oob="outerHTML",
            id="foods-confirmation"
        )

    hotel.food_ordering.restock(item_name, amount)

    return Div(
        Script("""
            document.getElementById('orderModal').style.display = 'block';
            htmx.ajax('GET', '/staff/foods', {target: '#main-content'});
        """),
        H3("Restocked"),
        P(f"Item: {item_name}"),
        hx_swap_oob="outerHTML",
        id="foods-confirmation"
    )


@rt("/staff/foods/add-dish")
async def post(request):
    form_data = await request.form()
    dish_name = form_data.get("dish-name")
    price = int(form_data.get("price"))
    amount = int(form_data.get("amount"))

    if price <= 0 or amount <= 0:
        return Div(
            Script("""
                document.getElementById('orderModal').style.display = 'block';
                htmx.ajax('GET', '/staff/foods', {target: '#main-content'});
            """),
            H3("Invalid price or amount"),
            hx_swap_oob="outerHTML",
            id="foods-confirmation"
        )

    hotel.food_ordering.add_new_menu(dish_name, price, "https://placehold.co/200x150")

    return Div(
        Script("""
            document.getElementById('orderModal').style.display = 'block';
            htmx.ajax('GET', '/staff/foods', {target: '#main-content'});
        """),
        H3("Added"),
        P(f"Dish: {dish_name}"),
        hx_swap_oob="outerHTML",
        id="foods-confirmation"
    )


@rt("/staff/foods/assign/{reservation_id}")
def post(reservation_id: int, session):
    redirect =  check_login(session)

    if redirect:
        return redirect

    if get_user_role(session) != "Staff":
        return RedirectResponse("/", status_code=303)
    
    staff = hotel.get_staff_by_id(session["user_id"])
    
    hotel.food_ordering.assign_reservation(reservation_id, staff)

    return Div(
        Script("""
            document.getElementById('orderModal').style.display = 'block';
            htmx.ajax('GET', '/staff/foods', {target: '#main-content'});
        """),
        H3("Assigned"),
        P(f"Reservation ID: {reservation_id}"),
        hx_swap_oob="outerHTML",
        id="foods-confirmation"
    )


@rt("/staff/foods/unassign/{reservation_id}")
def post(reservation_id: int, session):
    redirect =  check_login(session)

    if redirect:
        return redirect

    if get_user_role(session) != "Staff":
        return RedirectResponse("/", status_code=303)
    
    staff = hotel.get_staff_by_id(session["user_id"])

    hotel.food_ordering.unassign_reservation(reservation_id, staff)

    return Div(
        Script("""
            document.getElementById('orderModal').style.display = 'block';
            htmx.ajax('GET', '/staff/foods', {target: '#main-content'});
        """),
        H3("Unassigned"),
        P(f"Reservation ID: {reservation_id}"),
        hx_swap_oob="outerHTML",
        id="foods-confirmation"
    )


@rt("/staff/foods/complete/{reservation_id}")
def post(reservation_id: int, session):
    redirect =  check_login(session)

    if redirect:
        return redirect

    if get_user_role(session) != "Staff":
        return RedirectResponse("/", status_code=303)
    
    staff = hotel.get_staff_by_id(session["user_id"])

    hotel.food_ordering.complete_reservation(reservation_id, staff)

    return Div(
        Script("""
            document.getElementById('orderModal').style.display = 'block';
            htmx.ajax('GET', '/staff/foods', {target: '#main-content'});
        """),
        H3("Marked as done!"),
        P(f"Reservation ID: {reservation_id}"),
        hx_swap_oob="outerHTML",
        id="foods-confirmation"
    )


@rt("/staff/foods/cancel/{reservation_id}")
def post(reservation_id: int, session):
    redirect =  check_login(session)

    if redirect:
        return redirect

    if get_user_role(session) != "Staff":
        return RedirectResponse("/", status_code=303)
    
    staff = hotel.get_staff_by_id(session["user_id"])

    hotel.food_ordering.cancel_reservation(reservation_id, staff)

    return Div(
        Script("""
            document.getElementById('orderModal').style.display = 'block';
            htmx.ajax('GET', '/staff/foods', {target: '#main-content'});
        """),
        H3("Cancelled"),
        P(f"Reservation ID: {reservation_id}"),
        hx_swap_oob="outerHTML",
        id="foods-confirmation"
    )


@rt("/staff/cleaning")
def get(session):
    redirect =  check_login(session)

    if redirect:
        return redirect

    if get_user_role(session) != "Staff":
        return RedirectResponse("/", status_code=303)
    
    staff = hotel.get_staff_by_id(session["user_id"])
    
    return Title("Cleaning Service"), Br(), Container(
        H1("Cleaning Service"),
        Table(
            Thead(
                Tr(
                    Th("Order ID"),
                    Th("Timestamp"),
                    Th("Guest Name"),
                    Th("Room ID"),
                    Th("Appointment Time"),
                    Th("Assigned Staff"),
                    Th("Action")
                )
            ),
            Tbody(
                *(Tr(
                    Td(reservation.id),
                    Td(str(reservation.timestamp)),
                    Td(reservation.guest.real_name),
                    Td(reservation.room_id),
                    Td(reservation.appointment_date, " ", reservation.appointment_time),
                    Td(reservation.staff.real_name if reservation.staff else "Not Assigned"),
                    Td(Button("Assign Self", type="button", hx_post=f"/staff/cleaning/assign/{reservation.id}", hx_target="#cleaning-confirmation", hx_swap="outerHTML", disabled=(staff.current_service is not None or reservation.staff is not None)),
                       Button("Unassign Self", type="button", hx_post=f"/staff/cleaning/unassign/{reservation.id}", hx_target="#cleaning-confirmation", hx_swap="outerHTML", disabled=(staff.current_service is None or staff.current_service.id != reservation.id)),
                        Button("Complete", type="button", hx_post=f"/staff/cleaning/complete/{reservation.id}", hx_target="#cleaning-confirmation", hx_swap="outerHTML", disabled=(staff.current_service is None or staff.current_service.id != reservation.id)),
                        Button("Cancel", type="button", hx_post=f"/staff/cleaning/cancel/{reservation.id}", hx_target="#cleaning-confirmation", hx_swap="outerHTML", disabled=(staff.current_service is None or staff.current_service.id != reservation.id)),
                        id=f"row-{reservation.id}"
                    )
                ) for reservation in hotel.cleaning.get_reserved_reservation())
            ),
            Div(id="cleaning-confirmation"),
            cls="striped"
        )
    )


@rt("/staff/cleaning/assign/{reservation_id}")
def post(reservation_id: int, session):
    redirect =  check_login(session)

    if redirect:
        return redirect

    if get_user_role(session) != "Staff":
        return RedirectResponse("/", status_code=303)
    
    staff = hotel.get_staff_by_id(session["user_id"])
    
    hotel.cleaning.assign_reservation(reservation_id, staff)

    return Div(
        Script("""
            document.getElementById('orderModal').style.display = 'block';
            htmx.ajax('GET', '/staff/cleaning', {target: '#main-content'});
        """),
        H3("Assigned"),
        P(f"Reservation ID: {reservation_id}"),
        hx_swap_oob="outerHTML",
        id="cleaning-confirmation"
    )


@rt("/staff/cleaning/unassign/{reservation_id}")
def post(reservation_id: int, session):
    redirect =  check_login(session)

    if redirect:
        return redirect

    if get_user_role(session) != "Staff":
        return RedirectResponse("/", status_code=303)
    
    staff = hotel.get_staff_by_id(session["user_id"])

    hotel.cleaning.unassign_reservation(reservation_id, staff)

    return Div(
        Script("""
            document.getElementById('orderModal').style.display = 'block';
            htmx.ajax('GET', '/staff/cleaning', {target: '#main-content'});
        """),
        H3("Unassigned"),
        P(f"Reservation ID: {reservation_id}"),
        hx_swap_oob="outerHTML",
        id="cleaning-confirmation"
    )


@rt("/staff/cleaning/complete/{reservation_id}")
def post(reservation_id: int, session):
    redirect =  check_login(session)

    if redirect:
        return redirect

    if get_user_role(session) != "Staff":
        return RedirectResponse("/", status_code=303)
    
    staff = hotel.get_staff_by_id(session["user_id"])

    hotel.cleaning.complete_reservation(reservation_id, staff)

    return Div(
        Script("""
            document.getElementById('orderModal').style.display = 'block';
            htmx.ajax('GET', '/staff/cleaning', {target: '#main-content'});
        """),
        H3("Marked as done!"),
        P(f"Reservation ID: {reservation_id}"),
        hx_swap_oob="outerHTML",
        id="cleaning-confirmation"
    )


@rt("/staff/cleaning/cancel/{reservation_id}")
def post(reservation_id: int, session):
    redirect =  check_login(session)

    if redirect:
        return redirect

    if get_user_role(session) != "Staff":
        return RedirectResponse("/", status_code=303)
    
    staff = hotel.get_staff_by_id(session["user_id"])

    hotel.cleaning.cancel_reservation(reservation_id, staff)

    return Div(
        Script("""
            document.getElementById('orderModal').style.display = 'block';
            htmx.ajax('GET', '/staff/cleaning', {target: '#main-content'});
        """),
        H3("Cancelled"),
        P(f"Reservation ID: {reservation_id}"),
        hx_swap_oob="outerHTML",
        id="cleaning-confirmation"
    )


@rt("/staff/repair")
def get(session):
    redirect =  check_login(session)

    if redirect:
        return redirect

    if get_user_role(session) != "Staff":
        return RedirectResponse("/", status_code=303)

    staff = hotel.get_staff_by_id(session["user_id"])

    return Title("Repair Service"), Br(), Container(
        H1("Repair Service"),
        Table(
            Thead(
                Tr(
                    Th("Order ID"),
                    Th("Timestamp"),
                    Th("Guest Name"),
                    Th("Room ID"),
                    Th("Appointment Time"),
                    Th("Item"),
                    Th("Issue"),
                    Th("Assigned Staff"),
                    Th("Action")
                )
            ),
            Tbody(
                *(Tr(
                    Td(reservation.id),
                    Td(str(reservation.timestamp)),
                    Td(reservation.guest.real_name),
                    Td(reservation.room_id),
                    Td(reservation.appointment_date, " ", reservation.appointment_time),
                    Td(reservation.item.name),
                    Td(reservation.repair_issue),
                    Td(reservation.staff.real_name if reservation.staff else "Not Assigned"),
                    Td(Button("Assign Self", type="button", hx_post=f"/staff/repair/assign/{reservation.id}", hx_target="#repair-confirmation", hx_swap="outerHTML", disabled=(staff.current_service is not None or reservation.staff is not None)),
                          Button("Unassign Self", type="button", hx_post=f"/staff/repair/unassign/{reservation.id}", hx_target="#repair-confirmation", hx_swap="outerHTML", disabled=(staff.current_service is None or staff.current_service.id != reservation.id)),
                        Button("Complete", type="button", hx_post=f"/staff/repair/complete/{reservation.id}", hx_target="#repair-confirmation", hx_swap="outerHTML", disabled=(staff.current_service is None or staff.current_service.id != reservation.id)),
                        Button("Cancel", type="button", hx_post=f"/staff/repair/cancel/{reservation.id}", hx_target="#repair-confirmation", hx_swap="outerHTML", disabled=(staff.current_service is None or staff.current_service.id != reservation.id)),
                        id=f"row-{reservation.id}"
                    )
                ) for reservation in hotel.repair_service.get_reserved_reservation())
            ),
            Div(id="repair-confirmation"),
            cls="striped"
        )
    )


@rt("/staff/repair/assign/{reservation_id}")
def post(reservation_id: int, session):
    redirect =  check_login(session)

    if redirect:
        return redirect

    if get_user_role(session) != "Staff":
        return RedirectResponse("/", status_code=303)
    
    staff = hotel.get_staff_by_id(session["user_id"])
    
    hotel.repair_service.assign_reservation(reservation_id, staff)

    return Div(
        Script("""
            document.getElementById('orderModal').style.display = 'block';
            htmx.ajax('GET', '/staff/repair', {target: '#main-content'});
        """),
        H3("Assigned"),
        P(f"Reservation ID: {reservation_id}"),
        hx_swap_oob="outerHTML",
        id="repair-confirmation"
    )


@rt("/staff/repair/unassign/{reservation_id}")
def post(reservation_id: int, session):
    redirect =  check_login(session)

    if redirect:
        return redirect

    if get_user_role(session) != "Staff":
        return RedirectResponse("/", status_code=303)
    
    staff = hotel.get_staff_by_id(session["user_id"])

    hotel.repair_service.unassign_reservation(reservation_id, staff)

    return Div(
        Script("""
            document.getElementById('orderModal').style.display = 'block';
            htmx.ajax('GET', '/staff/repair', {target: '#main-content'});
        """),
        H3("Unassigned"),
        P(f"Reservation ID: {reservation_id}"),
        hx_swap_oob="outerHTML",
        id="repair-confirmation"
    )


@rt("/staff/repair/complete/{reservation_id}")
def post(reservation_id: int, session):
    redirect =  check_login(session)

    if redirect:
        return redirect

    if get_user_role(session) != "Staff":
        return RedirectResponse("/", status_code=303)
    
    staff = hotel.get_staff_by_id(session["user_id"])
    
    hotel.repair_service.complete_reservation(reservation_id, staff)

    return Div(
        Script("""
            document.getElementById('orderModal').style.display = 'block';
            htmx.ajax('GET', '/staff/repair', {target: '#main-content'});
        """),
        H3("Marked as done!"),
        P(f"Reservation ID: {reservation_id}"),
        hx_swap_oob="outerHTML",
        id="repair-confirmation"
    )


@rt("/staff/repair/cancel/{reservation_id}")
def post(reservation_id: int, session):
    redirect =  check_login(session)

    if redirect:
        return redirect
    
    if get_user_role(session) != "Staff":
        return RedirectResponse("/", status_code=303)
    
    staff = hotel.get_staff_by_id(session["user_id"])

    hotel.repair_service.cancel_reservation(reservation_id, staff)

    return Div(
        Script("""
            document.getElementById('orderModal').style.display = 'block';
            htmx.ajax('GET', '/staff/repair', {target: '#main-content'});
        """),
        H3("Cancelled"),
        P(f"Reservation ID: {reservation_id}"),
        hx_swap_oob="outerHTML",
        id="repair-confirmation"
    )


@rt('/staff/profile')
def get(session):
    redirect =  check_login(session)

    if redirect:
        return redirect

    if get_user_role(session) != "Staff":
        return RedirectResponse("/", status_code=303)

    staff = hotel.get_staff_by_id(session["user_id"])

    is_available = staff.status == "Available"

    status_text = "Available" if is_available else "Busy"
    status_color = "green" if is_available else "orange"

    return Title("Profile"), menu(session), Br(), Container(
        Card(
            
            H1(staff.real_name),
            P(
                B("Staff ID: "),
                Span(staff.user_id, id="staff-id", style="font-weight: bold;")
            ),
            P(
                B("Status: "), 
                Span(status_text, id="staff-status", style=f"color: {status_color}; font-weight: bold;")
            ),

            header=H2("Staff profile"),
            footer=P(
                Button("Check work", type="button", hx_get="/staff/check_work", hx_target="#work-details", hx_swap="outerHTML", style="margin-right: 10px;"),
                Span(Button("View History", type="button", hx_get="/staff/history", hx_target="#work-details", hx_swap="outerHTML")),
                
            )
        ),
        Div(id="work-details")
    )


@rt('/staff/check_work')
def get(session):
    redirect =  check_login(session)

    if redirect:
        return redirect
    
    if get_user_role(session) != "Staff":
        return RedirectResponse("/", status_code=303)
    
    staff = hotel.get_staff_by_id(session["user_id"])
    # current_work = staff.current_work

    current_work = None
    return Container(
        Table(
            Thead(Tr(Th("Order"), Th("Assigned Job Type"), Th("Ordered Time"), Th("Action"))),
            Tbody(
                *[
                    Tr(
                        Td(str(order_id)),
                        Td(job_type),
                        Td(order_time),
                        Td(
                            Button(
                                "Finish Work" if current_work == order_id else "Work",
                                type="button",
                                hx_post=f"/toggle_work/{order_id}", 
                                hx_target="#work-table", 
                                hx_swap="outerHTML",
                                disabled=(current_work is not None and current_work != order_id),
                                style="background-color: green;" if current_work == order_id else ""
                            ),
                            id=f"row-{order_id}"
                        ),
                    )
                    for order_id, job_type, order_time in staff.get_schedule()
                ]
            ),
            id="work-table"
        ) if staff.get_schedule() else Div("No work to do.", id="no-work-message", style="margin-top: 10px; color: gray;")
    )


@rt('/staff/history')
def get(session):
    redirect =  check_login(session)

    if redirect:
        return redirect

    if get_user_role(session) != "Staff":
        return RedirectResponse("/", status_code=303)

    staff = hotel.get_staff_by_id(session["user_id"])
    history = staff.get_history()

    return Container(
        Table(
            Thead(Tr(Th("Order"), Th("Assigned Job Type"), Th("Ordered Time"), Th("Action"))),
            Tbody(
                *[
                    Tr(
                        Td(str(order_id)),
                        Td(job_type),
                        Td(order_time),
                        Td(
                            Button("View", type="button", hx_get=f"/staff/history/{order_id}", hx_target="#work-details", hx_swap="outerHTML"),
                            id=f"row-{order_id}"
                        ),
                    )
                    for order_id, job_type, order_time in history
                ]
            ),
            id="work-table"
        ) if history else Div("No work history.", id="no-work-message", style="margin-top: 10px; color: gray;")
    )


@rt("/staff/signup")
def get(session, request):
    redirect = check_login(session, "staff/signup")

    if redirect:
        return redirect
    
    if get_user_role(session) != "Staff":
        return RedirectResponse("/", status_code=303)
        
    return (Title("Create New Staff Account"),
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
                        Input(id="togglePassword", type="password", name="password", required=True)),
                    Label("Confirm Password",
                        Input(id="togglePassword", type="password", name="confirm-password", required=True)),
                    Script("""
                            document.getElementById('togglePassword').addEventListener('change', function () {
                            var passwordField = document.getElementById('password');
                            passwordField.type = this.checked ? 'text' : 'password';
                        });
                    """),
                    P(id="return-message", style="color: red;"),
                    Button("Sign Up", type="submit", cls="btn btn-primary", required=True, style="width: 150px;"),
                    hx_post="/staff/signup", hx_target="#return-message"
                ),
                Hr(),
                A("Login", href="/login", style="text-align: center;"),
                style="text-align: center; max-width: 400px; margin: 0 auto"
            )
        )
    )


@rt("/staff/signup")
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

    status_message = hotel.create_staff(username, real_name, email, password)

    if status_message == "Success":
        return Redirect("/staff")
    else:
        return P(f"{status_message}")


@rt('/services')
def get(session):
    redirect = check_login(session, "services")

    if redirect:
        return redirect
    
    if get_user_role(session) == "Staff":
        return RedirectResponse("/staff", status_code=303)
    
    booking = get_guest_staying_booking(session)

    if booking is None:
        return RedirectResponse("/booking", status_code=303)

    return Title("Service"), menu(session), Br(), Container(
        Button("▲", id="toggle-btn",
               onclick="""
                   var content = document.getElementById('collapsible-container');
                   if (content.style.maxHeight && content.style.maxHeight !== '0px'){
                       content.style.maxHeight = '0px';
                       this.innerHTML = '▼';
                   } else {
                       content.style.maxHeight = '700px';
                       this.innerHTML = '▲';
                   }
               """,
              style="background: none; border: none; font-size: 12px; cursor: pointer; margin-bottom: 5px; color: #000;"
        ),
        Card(
            H1("Choose Service", style="text-align: center; color: #2196f3; margin: 20px 0; font-weight: 800;"),
            Grid(
                Card(
                    H3("Transportation"),
                    Button("Choose", hx_get="/transport", hx_target="#main-content", hx_swap="innerHTML"),
                    style="none; border-radius: 10px; padding: 20px; margin: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);"
                ),
                Card(
                    H3("Laundry Service"),
                    Button("Choose", hx_get="/laundry", hx_target="#main-content", hx_swap="innerHTML"),
                    style="none; border-radius: 10px; padding: 20px; margin: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);"
                ),
                Card(
                    H3("Order Foods"),
                    Button("Choose", hx_get="/foods", hx_target="#main-content", hx_swap="innerHTML"),
                    style="none; border-radius: 10px; padding: 20px; margin: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);"
                ),
                Card(
                    H3("Cleaning Service"),
                    Button("Choose", hx_get="/cleaning", hx_target="#main-content", hx_swap="innerHTML"),
                    style="none; border-radius: 10px; padding: 20px; margin: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);"
                ),
                Card(
                    H3("Repair Service"),
                    Button("Choose", hx_get="/repair", hx_target="#main-content", hx_swap="innerHTML"),
                    style="none; border-radius: 10px; padding: 20px; margin: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);"
                )
            ),
            id="collapsible-container",
            style="max-height: 700px; overflow: hidden; transition: max-height 0.5s ease-out; border: 1px solid #ccc; border-radius: 5px; padding: 10px; margin-bottom: 20px;"
        ),
        Div(id="main-content"),
        Div(
            P("Order placed successfully!"),
            Button("Close", onclick="document.getElementById('orderModal').style.display='none';"),
            id="orderModal",
            style="""
                display: none;
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                background: #fff;
                padding: 30px;
                border: 2px solid #2196f3;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
                z-index: 1000;
                text-align: center;
                font-size: 18px;
                color: #333;
            """
        )
    )

def mk_opts(nm, items, key_attr='name'):
    return (
        Option(f'-- select {nm} --', disabled='', selected='', value=''),
        *map(lambda item: Option(getattr(item, key_attr)), items)
    )

@rt
def get_route_price(route: str):
    route = next((r for r in hotel.transport.routes if r.name == route), None)
    if route:
        return Div(f"Price: ฿{route.price}", id="route_price")
    return Div("Price: ฿--", id="route_price")  # Default if no selection

    
@rt('/transport')
def get(session):
    redirect = check_login(session, "services")

    if redirect:
        return redirect
    
    if get_user_role(session) == "Staff":
        return RedirectResponse("/staff", status_code=303)

    route_dropdown = Select(
        *mk_opts('route', hotel.transport.routes),
        name='route',
        get='get_route_price',
        hx_target='#route_price'
    )

    return Titled(
        "Transportation",
        Div(
            Form(
                Div(Label("Select Route:", for_="route"), route_dropdown),
                Div(Div("Price: ฿--", id="route_price")),  # Price placeholder
                Label("Date and Time", for_="datetime"),
                Input(
                    type="datetime-local",
                    name="datetime",
                    min=f"{datetime.today().strftime('%Y-%m-%dT%H:%M')}",
                    required=True
                ),
                Button("Reserve", type="submit"),
                hx_post="/transport/reserve",
                hx_target="#transport-confirmation",
                hx_swap="outerHTML",
                hx_trigger="submit",
                hx_include="input[name='route'], input[name='datetime']"
            ),
        ),
        Div(id="transport-confirmation")  # This will update with confirmation
    )

@rt('/transport/reserve')
def post(session, route: str, datetime: str):
    redirect = check_login(session, "services")

    if redirect:
        return redirect

    booking = get_guest_staying_booking(session)

    if booking is None:
        return RedirectResponse("/booking", status_code=303)

    print(route, datetime)

    user = hotel.get_guest_by_id(session["user_id"])
    order = hotel.transport.create_reservation(user, route, datetime, booking)

    if order == "Route not found":
        return Div(
            P(order),
            hx_swap_oob="outerHTML",
            id="transport-confirmation"
        )

    return Div(
        Script("""
            document.getElementById('orderModal').style.display = 'block';
            htmx.ajax('GET', '/transport', {target: '#main-content'});
        """),
        H3("Reservation Confirmed"),
        P(f"Your transportation reservation for {route} has been confirmed for guest: {user.username}."),
        hx_swap_oob="outerHTML",
        id="transport-confirmation"
    )


@rt('/laundry')
def get(session):
    redirect = check_login(session, "services")

    if redirect:
        return redirect
    
    if get_user_role(session) == "Staff":
        return RedirectResponse("/staff", status_code=303)

    user = hotel.get_guest_by_id(session["user_id"])

    booking = get_guest_staying_booking(session)

    if booking is None:
        return RedirectResponse("/booking", status_code=303)

    return Titled(
        "Choose Clothes Type",
        Div(
            Div(
                Div(
                    *[cloth_card(d) for d in hotel.laundry.clothes],
                    id="cloth-list",
                    style="overflow-y: auto; max-height: 80vh;"
                ),
                style="flex: 3;"
            ),
            Div(
                H3("Your Order"),
                Div(render_cart_items(user.laundry_cart, "/laundry/remove"), id="cloth_cart_items"),
                Div(f"Cart Total: ฿{user.laundry_cart.total():.2f}", id="cloth_cart_total"),
                render_order_button(user.laundry_cart, "/laundry/order"),
                id="cart-display",
                style="width: 300px; margin-left: 20px; border-left: 1px solid #ccc; padding-left: 10px; position: sticky; top: 20px;"
            ),
            style="display: flex; gap: 20px;"
        )
    )

@rt('/laundry/add/{cloth_type}')
def post(session, cloth_type: str):
    redirect = check_login(session, "services")

    if redirect:
        return redirect

    user = hotel.get_guest_by_id(session["user_id"])

    booking = get_guest_staying_booking(session)

    if booking is None:
        return RedirectResponse("/booking", status_code=303)

    cloth = hotel.laundry.get_cloth_type(cloth_type)
    if cloth:
        user.laundry_cart.add(cloth)
    return (
        Div(*[cloth_card(d) for d in hotel.laundry.clothes], id="cloth-list"),
        Div(
            H3("Your Order:"),
            Div(render_cart_items(user.laundry_cart, "/laundry/remove"), id="cloth_cart_items"),
            Div(f"Cart Total: ฿{user.laundry_cart.total():.2f}", id="cloth_cart_total"),
            render_order_button(user.laundry_cart, "/laundry/order"),
            hx_swap_oob="outerHTML",
            id="cart-display"
        )
    )

@rt('/laundry/remove/{cloth_type}')
def post(session, cloth_type: str):
    redirect = check_login(session, "services")

    if redirect:
        return redirect

    user = hotel.get_guest_by_id(session["user_id"])

    booking = get_guest_staying_booking(session)

    if booking is None:
        return RedirectResponse("/booking", status_code=303)

    cloth = hotel.laundry.get_cloth_type(cloth_type)

    if cloth:
        user.laundry_cart.remove(cloth)
    return Div(
        H3("Your Order"),
        Div(render_cart_items(user.laundry_cart, "/laundry/remove"), id="cloth_cart_items"),
        Div(f"Cart Total: ฿{user.laundry_cart.total():.2f}", id="cloth_cart_total"),
        render_order_button(user.laundry_cart, "/laundry/order"),
        hx_swap_oob="outerHTML",
        id="cart-display"
    )

@rt('/laundry/order')
def post_laundry_order(session):
    redirect = check_login(session, "services")

    if redirect:
        return redirect

    user = hotel.get_guest_by_id(session["user_id"])

    booking = get_guest_staying_booking(session)

    if booking is None:
        return RedirectResponse("/booking", status_code=303)

    order = hotel.laundry.create_reservation(user, user.laundry_cart, booking)

    return Div(
         Script("var modal = document.getElementById('orderModal'); modal.style.display = 'block';"),
         H3(f"Your Laundry Order Confirmed for guest: {user.real_name}"),
         Div(render_cart_items(user.laundry_cart, "/laundry/remove"), id="cloth_cart_items"),
         Div(f"Cart Total: ฿{user.laundry_cart.total():.2f}", id="cloth_cart_total"),
         render_order_button(user.laundry_cart, "/laundry/order"),
         hx_swap_oob="outerHTML",
         id="cart-display"
    )

@rt('/foods')
def get(session):
    redirect = check_login(session, "services")

    if redirect:
        return redirect

    if get_user_role(session) == "Staff":
        return RedirectResponse("/staff", status_code=303)

    user = hotel.get_guest_by_id(session["user_id"])

    booking = get_guest_staying_booking(session)

    if booking is None:
        return RedirectResponse("/booking", status_code=303)

    return Titled(
        "Choose Menu",
        Div(
            Div(
                Input(
                    type="text",
                    name="q",  
                    placeholder="Search dishes...",
                    hx_get="/foods/search",
                    hx_trigger="keyup changed delay:500ms",
                    hx_target="#dish-list",
                    style="width: 100%; padding: 8px; margin-bottom: 10px;"
                ),
                Div(
                    *[food_card(d,user.food_cart) for d in hotel.food_ordering.dishes],
                    id="dish-list",
                    style="overflow-y: auto; max-height: 80vh;"
                ),
                style="flex: 3;"
            ),
            Div(
                H3("Your Cart"),
                Div(render_cart_items(user.food_cart, "/foods/remove"), id="user.food_cart_items"),
                Div(f"Cart Total: ฿{user.food_cart.total():.2f}", id="user.food_cart_total"),
                render_order_button(user.food_cart, "/foods/order"),
                id="cart-display",
                style="width: 300px; margin-left: 20px; border-left: 1px solid #ccc; padding-left: 10px; position: sticky; top: 20px;"
            ),
            style="display: flex; gap: 20px;"
        )
    )

@rt('/foods/search')
def search(session, q: str = ""):
    redirect = check_login(session, "services")

    if redirect:
        return redirect

    user = hotel.get_guest_by_id(session["user_id"])

    booking = get_guest_staying_booking(session)

    if booking is None:
        return RedirectResponse("/booking", status_code=303)
    
    filtered_dishes = [d for d in hotel.food_ordering.dishes if q.lower() in d.name.lower()]
    return Div(*[food_card(d,user.food_cart) for d in filtered_dishes], id="dish-list")

@rt('/foods/add/{dish_name}')
def post(session, dish_name: str):
    redirect = check_login(session, "services")

    if redirect:
        return redirect

    user = hotel.get_guest_by_id(session["user_id"])


    booking = get_guest_staying_booking(session)

    if booking is None:
        return RedirectResponse("/booking", status_code=303)

    dish = hotel.food_ordering.find_dish(dish_name)

    if dish:
        current_quantity = user.food_cart.items.get(dish_name, {'quantity': 0})['quantity']
        if current_quantity < dish.amount:
            user.food_cart.add(dish)

    return (
        Div(*[food_card(d, user.food_cart) for d in hotel.food_ordering.dishes], id="dish-list"),
        Div(
            H3("Your Cart"),
            Div(render_cart_items(user.food_cart, "/foods/remove"), id="user.food_cart_items"),
            Div(f"Cart Total: ฿{user.food_cart.total():.2f}", id="user.food_cart_total"),
            render_order_button(user.food_cart, "/foods/order"),
            hx_swap_oob="outerHTML",
            id="cart-display"
        )
    )
@rt('/foods/remove/{dish_name}')
def post(session, dish_name: str):
    redirect = check_login(session, "services")

    if redirect:
        return redirect

    user = hotel.get_guest_by_id(session["user_id"])

    booking = get_guest_staying_booking(session)

    if booking is None:
        return RedirectResponse("/booking", status_code=303)

    dish = hotel.food_ordering.find_dish(dish_name)
    if dish:
        user.food_cart.remove(dish)
    return (
        Div(
            *[food_card(d, user.food_cart) for d in hotel.food_ordering.dishes],
            id="dish-list",
            hx_swap_oob="outerHTML"  # Force the dish list to update
        ),
        Div(
            H3("Your Cart"),
            Div(render_cart_items(user.food_cart, "/foods/remove"), id="user.food_cart_items"),
            Div(f"Cart Total: ฿{user.food_cart.total():.2f}", id="user.food_cart_total"),
            render_order_button(user.food_cart, "/foods/order"),
            hx_swap_oob="outerHTML",
            id="cart-display"
        )
    )

@rt('/foods/order')
def post_food_order(session):
    redirect = check_login(session, "services")

    if redirect:
        return redirect

    user = hotel.get_guest_by_id(session["user_id"])

    booking = get_guest_staying_booking(session)

    if booking is None:
        return RedirectResponse("/booking", status_code=303)

    hotel.food_ordering.create_food_order(user, user.food_cart, booking)

    return Div(
        Script("""
            document.getElementById('orderModal').style.display = 'block';
            htmx.ajax('GET', '/foods', {target: '#main-content'});
        """),
        H3(f"Food Order Confirmed for guest: {user.real_name}"),
        Div(render_cart_items(user.food_cart, "/foods/remove"), id="food_cart_items"),
        Div(f"Cart Total: ฿{user.food_cart.total():.2f}", id="food_cart_total"),
        render_order_button(user.food_cart, "/foods/order"),
        hx_swap_oob="outerHTML",
        id="cart-display"
    )

@rt('/cleaning')
def cleaning_page(session):
    redirect = check_login(session, "services")

    if redirect:
        return redirect
    
    if get_user_role(session) == "Staff":
        return RedirectResponse("/staff", status_code=303)

    user = hotel.get_guest_by_id(session["user_id"])

    booking = get_guest_staying_booking(session)

    if booking is None:
        return RedirectResponse("/booking", status_code=303)

    today = datetime.today()
    min_date = today + timedelta(days=1)
    max_date = today + timedelta(days=3)
    
    return Titled("Cleaning Service Appointment",
        Form(
            Div(
                H3("Schedule a Cleaning Appointment"),
                Input(
                    type="date", 
                    name="appointment_date", 
                    min=f"{min_date.strftime('%Y-%m-%d')}",
                    max=f"{max_date.strftime('%Y-%m-%d')}",
                    placeholder="Select a date", 
                    style="margin-bottom: 10px;",
                    required=True
                ),
                Select(
                    Option("07:00", value="07:00"),
                    Option("08:00", value="08:00"),
                    Option("09:00", value="09:00"),
                    Option("10:00", value="10:00"),
                    Option("11:00", value="11:00"),
                    Option("12:00", value="12:00"),
                    Option("13:00", value="13:00"),
                    Option("14:00", value="14:00"),
                    Option("15:00", value="15:00"),
                    Option("16:00", value="16:00"),
                    Option("17:00", value="17:00"),
                    Option("18:00", value="18:00"),
                    name="appointment_time",
                    style="margin-bottom: 10px;",
                    required=True
                ),
                Button(
                    "Confirm Appointment", 
                    type="submit",
                    hx_post="/cleaning/confirm", 
                    hx_target="#cleaning-confirmation", 
                    hx_swap="outerHTML",
                    id="cleaning-confirm-btn",
                    disabled=True,
                    style="margin-top: 10px;"
                )
            ),
            id="cleaning-form",
            oninput="document.getElementById('cleaning-confirm-btn').disabled = !this.checkValidity();"
        ),
        Div(id="cleaning-confirmation")
    )

@rt('/cleaning/confirm')
def confirm_cleaning(session, appointment_date: str, appointment_time: str):
    redirect = check_login(session, "services")

    if redirect:
        return redirect

    user = hotel.get_guest_by_id(session["user_id"])

    booking = get_guest_staying_booking(session)

    if booking is None:
        return RedirectResponse("/booking", status_code=303)

    today = datetime.today()
    min_date = today + timedelta(days=1)
    max_date = today + timedelta(days=3)

    try:
        date.fromisoformat(appointment_date)
    except ValueError:
        msg = "The provided appointment date is invalid."
        html = f"<h3>Invalid Date</h3><p>{msg}</p><button onclick=\"document.getElementById('orderModal').style.display='none';\">Close</button>"
        return Div(
            Script(f"document.getElementById('orderModal').innerHTML = `{html}`; document.getElementById('orderModal').style.display = 'block';"),
            Script("htmx.ajax('GET', '/cleaning', {target: '#main-content'});")
        )
    
    # Check for existing appointment in the open period.
    for order in hotel.cleaning.reservations:
        if order.guest.real_name == user.real_name and order.status not in ["Cancelled", "Complete"]:
            print(order.appointment_date, order.appointment_time)
            existing_date = order.appointment_date
            if min_date.date() <= existing_date <= max_date.date():
                msg = f"You already have an appointment on {order.appointment_date} at {order.appointment_time}."
                html = f"<h3>Appointment Denied</h3><p>{msg}</p><button onclick=\"document.getElementById('orderModal').style.display='none';\">Close</button>"
                return Div(
                    Script(f"document.getElementById('orderModal').innerHTML = `{html}`; document.getElementById('orderModal').style.display = 'block';"),
                    Script("htmx.ajax('GET', '/cleaning', {target: '#main-content'});")
                )
    
    # No conflict, confirm the appointment.
    order = hotel.cleaning.create_reservation(user, appointment_date, appointment_time, booking)
    msg = f"Your cleaning appointment is scheduled on {appointment_date} at {appointment_time}."
    html = f"<h3>Appointment Confirmed</h3><p>{msg}</p><button onclick=\"document.getElementById('orderModal').style.display='none';\">Close</button>"
    return Div(
         Script(f"document.getElementById('orderModal').innerHTML = `{html}`; document.getElementById('orderModal').style.display = 'block';"),
         Script("htmx.ajax('GET', '/cleaning', {target: '#main-content'});")
    )

@rt
def get_item_price(item: str):
    item = next((r for r in hotel.items if r.name == item), None)
    if item:
        return Div(f"Price: ฿{item.price}", id="item_price")
    return Div("Price: ฿--", id="item_price")  # Default if no selection

@rt('/repair')
def repair_page(session):
    redirect = check_login(session, "services")

    if redirect:
        return redirect
    
    if get_user_role(session) == "Staff":
        return RedirectResponse("/staff", status_code=303)

    user = hotel.get_guest_by_id(session["user_id"])

    booking = get_guest_staying_booking(session)

    if booking is None:
        return RedirectResponse("/booking", status_code=303)

    today = datetime.today()
    min_date = today + timedelta(days=1)
    max_date = today + timedelta(days=3)
    return Titled("Repair Service Appointment",
        Form(
            Div(
                H3("Schedule a Repair Appointment"),
                Input(
                    type="date", 
                    name="appointment_date", 
                    min=f"{min_date.isoformat()}",
                    max=f"{max_date.isoformat()}",
                    placeholder="Select a date", 
                    style="margin-bottom: 10px;",
                    required=True
                ),
                Select(
                    Option("07:00", value="07:00"),
                    Option("08:00", value="08:00"),
                    Option("09:00", value="09:00"),
                    Option("10:00", value="10:00"),
                    Option("11:00", value="11:00"),
                    Option("12:00", value="12:00"),
                    Option("13:00", value="13:00"),
                    Option("14:00", value="14:00"),
                    Option("15:00", value="15:00"),
                    Option("16:00", value="16:00"),
                    Option("17:00", value="17:00"),
                    Option("18:00", value="18:00"),
                    name="appointment_time",
                    style="margin-bottom: 10px;",
                    required=True
                ),
                # Hotel items to repair hotel item.name and item.price
                Select(
                    *mk_opts('item', hotel.items),
                    name='item',
                    get='get_item_price',
                    hx_target='#item_price',  
                    required=True,
                ),
                Div(Div("Price: ฿--", id="item_price")),  # Price placeholder
                Input(
                    type="text", 
                    name="repair_issue", 
                    placeholder="Describe the issue",
                    style="margin-bottom: 10px;",
                    required=True
                ),
                Button(
                    "Confirm Appointment", 
                    type="submit",
                    hx_post="/repair/confirm", 
                    hx_target="#repair-confirmation", 
                    hx_swap="outerHTML",
                    id="repair-confirm-btn",
                    disabled=True,
                    style="margin-top: 10px;"
                )
            ),
            id="repair-form",
            oninput="document.getElementById('repair-confirm-btn').disabled = !this.checkValidity();"
        ),
        Div(id="repair-confirmation")
    )

@rt('/repair/confirm')
def confirm_repair(session, appointment_date: str, appointment_time: str, item: str, repair_issue: str):
    user = hotel.get_guest_by_id(session["user_id"])

    booking = get_guest_staying_booking(session)

    if booking is None:
        return RedirectResponse("/booking", status_code=303)

    # (Optional: add any additional validation if needed)
    hotel.repair_service.create_reservation(user, appointment_date, appointment_time, hotel.get_item_by_name(item), repair_issue, booking)
    msg = f"Your repair appointment is scheduled on {appointment_date} at {appointment_time} with issue: {repair_issue}."
    html = f"<h3>Appointment Confirmed</h3><p>{msg}</p><button onclick=\"document.getElementById('orderModal').style.display='none';\">Close</button>"
    return Div(
         Script(f"document.getElementById('orderModal').innerHTML = `{html}`; document.getElementById('orderModal').style.display = 'block';"),
         Script("htmx.ajax('GET', '/repair', {target: '#main-content'});")
    )



serve()