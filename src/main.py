from fasthtml.common import *
from datetime import datetime, timedelta
from classes.hotel import *

app, rt = fast_app(debug=False, secret_key="secret")

def create_instance():
    #temporary create an instance of room
    global hotel
    hotel = Hotel()
    hotel.create_room(Room(101, "Single", 1, 100, 1, ["AC", "Wifi"], "room1.jpg"))
    hotel.create_room(Room(102, "Double", 2, 150, 1, ["TV", "AC", "Wifi"], "room2.jpg"))
    hotel.create_room(Room(103, "Family", 4, 200, 1, ["TV", "AC", "Wifi"], "room3.jpg"))
    hotel.create_room(Room(104, "Suite", 6, 300, 1, ["TV", "AC", "Wifi"], "room4.jpg"))
    hotel.create_room(Room(105, "Single", 1, 100, 1, ["TV", "AC", "Wifi"], "room5.jpg"))
    hotel.create_room(Room(106, "Double", 2, 150, 1, ["AC", "Wifi"], "room6.jpg"))
    hotel.create_room(Room(107, "Family", 4, 200, 1, ["TV", "AC", "Wifi"], "room7.jpg"))
    hotel.create_room(Room(108, "Suite", 6, 300, 1, ["TV", "AC", "Wifi"], "room8.jpg"))

    # user account
    hotel.create_staff("ManagerPaul", "Paul Howard", "paul.h@cozyhotel.com", "password")
    hotel.create_staff("DriverJoe", "Joe Speed", "joe.s@cozyhotel.com", "password")
    hotel.create_staff("ChefMike", "Mike Cowave", "mike.c@cozyhotel.com", "password")
    hotel.create_guest("JohnDoe", "John Doe", "john.d@domain.xyz", "password")
    hotel.create_guest("JaneDoe", "Jane Doe", "jane.d@domain.xyz", "password")

    hotel.create_booking(hotel.get_guest_by_id(1), hotel.get_room_by_id(101), datetime.today(), datetime.today() + timedelta(days=1))
    hotel.create_booking(hotel.get_guest_by_id(2), hotel.get_room_by_id(102), datetime.today(), datetime.today() + timedelta(days=1))
    hotel.create_booking(hotel.get_guest_by_id(1), hotel.get_room_by_id(103), datetime.today(), datetime.today() + timedelta(days=1))
    hotel.create_booking(hotel.get_guest_by_id(2), hotel.get_room_by_id(104), datetime.today(), datetime.today() + timedelta(days=1))

    driver = hotel.get_staff_by_id(2)
    hotel.transport.create_route("Airport", driver, "10:00 AM")
    hotel.transport.create_route("City Tour", driver, "2:00 PM")
    hotel.transport.create_route("Beach", driver, "4:30 PM")
    hotel.transport.create_route("Downtown Express", driver, "8:00 AM")
    hotel.transport.create_route("Suburban Shuttle", driver, "11:00 AM")
    hotel.transport.create_route("Nightlife Special", driver, "9:00 PM")
    hotel.transport.create_route("Train Station", driver, "6:00 AM")

    hotel.food_ordering.add_new_menu("Pasta Alfredo", 429,"https://images.aws.nestle.recipes/resized/0a0717810b73a1672a029c29788e557b_creamy_alfredo_pasta_long_left_1080_850.jpg")
    hotel.food_ordering.add_new_menu("Margherita Pizza", 329,"https://images.prismic.io/eataly-us/ed3fcec7-7994-426d-a5e4-a24be5a95afd_pizza-recipe-main.jpg?auto=compress,format")
    hotel.food_ordering.add_new_menu("Caesar Salad", 269,"https://www.cuisinart.com/dw/image/v2/ABAF_PRD/on/demandware.static/-/Sites-us-cuisinart-sfra-Library/default/dw92573286/images/recipe-Images/classic-caesar-salad-recipe.jpg?sw=1200&sh=1200&sm=fit")
    hotel.food_ordering.add_new_menu("Steak", 699,"https://www.seriouseats.com/thmb/-KA2hwMofR2okTRndfsKtapFG4Q=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/__opt__aboutcom__coeus__resources__content_migration__serious_eats__seriouseats.com__recipes__images__2015__05__Anova-Steak-Guide-Sous-Vide-Photos15-beauty-159b7038c56a4e7685b57f478ca3e4c8.jpg")
    hotel.food_ordering.add_new_menu("Spaghetti Carbonara", 399,"https://www.allrecipes.com/thmb/Vg2cRidr2zcYhWGvPD8M18xM_WY=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/11973-spaghetti-carbonara-ii-DDMFS-4x3-6edea51e421e4457ac0c3269f3be5157.jpg")
    hotel.food_ordering.add_new_menu("Chicken Parmesan", 469,"https://tastesbetterfromscratch.com/wp-content/uploads/2023/03/Chicken-Parmesan-1.jpg")
    hotel.food_ordering.add_new_menu("Bruschetta", 239,"https://kjsfoodjournal.com/wp-content/uploads/2020/07/tomato-bruschetta.jpg")
    hotel.food_ordering.add_new_menu("Tiramisu", 189,"https://sugarpursuit.com/wp-content/uploads/2023/03/Easy-tiramisu-recipe-thumbnail.jpg")
    hotel.food_ordering.add_new_menu("Gelato", 149,"https://emmaduckworthbakes.com/wp-content/uploads/2023/06/Chocolate-Gelato-Recipe.jpg")
    hotel.food_ordering.add_new_menu("Minestrone Soup", 269,"https://www.katiescucina.com/wp-content/uploads/2021/09/Olive-Garden-Minestrone-Soup-Square.jpg")
    hotel.food_ordering.add_new_menu("Focaccia Bread", 139,"https://handletheheat.com/wp-content/uploads/2014/08/Focaccia-Bread-SQUARE.jpg")
    hotel.food_ordering.add_new_menu("Lasagna", 429,"https://www.allrecipes.com/thmb/94MKwLbkHmG8Zp871AOy3GhZwv4=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/AR-19344-Homemade-Lasagna-beauty-4x3-450e3ec3bc454e4a805443bee77c5be8.jpg")
    hotel.food_ordering.add_new_menu("Risotto", 479,"https://cookingwithwineblog.com/wp-content/uploads/2024/04/Milanese-Style-Creamy-Saffron-Leek-Risotto-Recipe-Featured-1.jpg")
    hotel.food_ordering.add_new_menu("Caprese Salad", 299,"https://www.allrecipes.com/thmb/Usj7zOLJSQ5xqw-4dwWarvPNjJg=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/AR-228126-caprese-salad-with-balsamic-reduction-ddmfs-2644-4x3-f32ac2b2fb9d4234884a752490fb015b.jpg")

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


def route_card(route): 
    is_reserved = route.is_reserved
    button_text = "Already reserved" if is_reserved else "Reserve"
    button_disabled = "disabled" if is_reserved else ""
    button_color = "grey" if is_reserved else "#2196f3"  # blue as default
    text_color = "red" if is_reserved else "white"

    return Card(
        H3(route.name), 
        P("Driver Name: ", route.staff.real_name), 
        P("Departure: ", route.time),
        Button(
            button_text, 
            hx_post=f"/transport/reserve/{route.name}", 
            hx_target="#transport-confirmation", 
            hx_swap="outerHTML",
            disabled=button_disabled,
            style=f"outline: none; background-color: {button_color}; color: {text_color}; cursor: {'not-allowed' if is_reserved else 'pointer'};"
        ),
        style="box-shadow: 0 4px 8px rgba(0,0,0,0.2); border-radius: 10px; margin: 10px; padding: 10px;"
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
        return RedirectResponse(f"/login?redirect={page}" if page else "/login", status_code=303)
    

def get_user_role(session):
    if "user_id" not in session:
        return None
    return hotel.get_role_by_id(session["user_id"])



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
async def post(session, request):
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

    session["booking"] = {
        "start_date": start_date.strftime("%Y-%m-%d"),
        "end_date": end_date.strftime("%Y-%m-%d"),
    }

    matching_hotel = hotel.get_room_by_attribute(room_type, guest_size, max_price, things, start_date, end_date)

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


@rt("/booking/review")
async def get(session, request):
    print("login")
    check_login(session, "booking")

    if session["booking"] is None:
        return RedirectResponse("/booking", status_code=303)

    start_date = session["booking"]["start_date"]
    end_date = session["booking"]["end_date"]

    room_id = int(request.query_params.get("room-id"))
    print(room_id)

    formated_start = datetime.strptime(start_date, "%Y-%m-%d")
    formated_end = datetime.strptime(end_date, "%Y-%m-%d")

    if room_id not in [room.room_id for room in hotel.rooms]:
        return P("Invalid Room")
    # TODO check if room is available (class not implemented yet)
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
    room_id = int(request.query_params.get("room-id"))
    name = form_data.get("full-name")
    card_number = form_data.get("credit-card")
    expiration_month = int(form_data.get("expiration-month"))
    expiration_year = int(form_data.get("expiration-year"))
    cvv = form_data.get("cvv")

    if len(card_number) != 16:
        return P("Invalid Credit Card Number", id="return-message", style="color: red;")
    if not card_number.isdigit():
        return P("Invalid Credit Card Number", id="return-message", style="color: red;")
    if expiration_month not in range(1, 13):
        return P("Invalid Expiry Month", id="return-message", style="color: red;")
    if expiration_year not in range(0, 100):
        return P("Invalid Expiry Year", id="return-message", style="color: red;")
    if datetime.strptime(f"{str(expiration_month)}/{str(expiration_year)}", "%m/%y") < datetime.today():
        return P("Credit Card Expired", id="return-message", style="color: red;")
    if len(cvv) not in [3, 4]:
        return P("Invalid CVV", id="return-message", style="color: red;")
    
    start_date = datetime.strptime(session["booking"]["start_date"], "%Y-%m-%d")
    end_date = datetime.strptime(session["booking"]["end_date"], "%Y-%m-%d")

    hotel.create_booking(hotel.get_guest_by_id(1), hotel.get_room_by_id(room_id), start_date, end_date)

    return Redirect("/success")

@rt("/success")
def get(session):
    session["booking"] = None
    return (Title("Success"), menu(session), Br(),
        Container(
        H1("Booking Successful"),
        P("Thank you for booking with us"),
        style="text-align: center;"
    ))

@rt("/profile")
def get(session):
    check_login(session, "profile")

    if get_user_role(session) == "Staff":
        return P("You're staff")
    
    user = hotel.get_guest_by_id(session["user_id"])
    return (Title("Profile"),
            (menu(session), Br(),
            Container(Card(
                H1("Profile"),
                P(f"Username: {username}"),
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
    check_login(session, "profile")

    print("links says", booking_id)

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
                    P(f"Commodity: {', '.join(booking.room.things)}"),
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
                style="text-align: center;"
            ),
            Card(
                H2("Payment Details"),
                P(f"Total Room Price: ฿{(booking.end_date - booking.start_date).days * booking.room.price}"),
                P(f"Service Call: ฿100"),
                P(f"Total Price: ฿{(booking.end_date - booking.start_date).days * booking.room.price + 100}"),
                style="text-align: center;"
            )
        )
    )

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
    
#     hotel.create_room(Room(room_id, room_type, size, price, status, things.split(","), image))

#     return P("Room Added")


@rt('/service')
def get(session):
    check_login(session, "service")

    if get_user_role(session) == "Staff":
        return RedirectResponse("/staff", status_code=303)

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



@rt('/transport')
def get(session):
    check_login(session, "service")

    return Titled("Available Routes",
        Div(
            Input(
                type="text",
                name="q",
                placeholder="Search routes...",
                hx_get="/transport/search",
                hx_trigger="keyup changed delay:200ms",
                hx_target="#route-list",
                style="width: 100%; padding: 8px; margin-bottom: 10px;"
            ),
            Div(*[route_card(route) for route in hotel.transport.get_available_routes()], id="route-list"),
            Div(id="transport-confirmation")
        )
    )

@rt('/transport/search')
def get(q: str = ""):
    filtered_routes = [route for route in hotel.transport.routes_list if q.lower() in route.name.lower()]
    return Div(*[route_card(route) for route in filtered_routes], id="route-list")

@rt('/transport/reserve/{route_name}')
def post(route_name: str, session):
    guest_instance = hotel.get_guest_by_id(session["user_id"])
    order = hotel.transport.create_reservation(guest_instance, route_name)

    if order in ["Already booked", "Route not found"]:
        return Div(P(order), hx_swap_oob="outerHTML", id="transport-confirmation")

    return Div(
        Script("""
            document.getElementById('orderModal').style.display = 'block';
            htmx.ajax('GET', '/transport', {target: '#main-content'});
        """),
        H3("Reservation Confirmed"),
        P(f"Your transportation reservation for {route_name} has been confirmed for guest: {guest_instance.username}."),
        hx_swap_oob="outerHTML",
        id="transport-confirmation"
    )

@rt('/laundry')
def get(session):
    check_login(session, "service")

    user = hotel.get_guest_by_id(session["user_id"])

    return Titled(
        "Choose Clothes Type",
        Div(
            Div(
                Div(
                    *[cloth_card(d) for d in hotel.laundry.cloths],
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
    check_login(session, "service")

    user = hotel.get_guest_by_id(session["user_id"])

    cloth = hotel.laundry.get_cloth_type(cloth_type)
    if cloth:
        user.laundry_cart.add(cloth)
    return (
        Div(*[cloth_card(d) for d in hotel.laundry.cloths], id="cloth-list"),
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
    check_login(session, "service")

    user = hotel.get_guest_by_id(session["user_id"])

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
    check_login(session, "service")

    user = hotel.get_guest_by_id(session["user_id"])

    order = hotel.laundry.confirm_order(user, user.laundry_cart)

    user.laundry_cart.clear()
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
    check_login(session, "service")

    user = hotel.get_guest_by_id(session["user_id"])

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
    check_login(session, "service")

    user = hotel.get_guest_by_id(session["user_id"])

    filtered_dishes = [d for d in hotel.food_ordering.dishes if q.lower() in d.name.lower()]
    return Div(*[food_card(d,user.food_cart) for d in filtered_dishes], id="dish-list")

@rt('/foods/add/{dish_name}')
def post(session, dish_name: str):
    check_login(session, "service")

    user = hotel.get_guest_by_id(session["user_id"])

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
    check_login(session, "service")

    user = hotel.get_guest_by_id(session["user_id"])

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
    check_login(session, "service")

    user = hotel.get_guest_by_id(session["user_id"])

    hotel.food_ordering.create_food_order(user, user.food_cart)
    
    user.food_cart.clear()

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

serve()