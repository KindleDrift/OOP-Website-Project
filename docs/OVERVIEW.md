# OOP Hotel Management System Overview

## Overview

This project is a comprehensive hotel management system built using Object-Oriented Programming principles. The system provides functionality for both guests and staff members to manage hotel operations through a web interface. The application uses a custom web framework called `fasthtml` for rendering HTML and handling HTTP requests.

## Core Components

### Hotel Class

The central class that manages all hotel operations:
- Rooms and bookings
- User management (guests and staff)
- Service modules (transport, food, laundry, cleaning, repair)

### User Management

- Two user types: `Guest` and `Staff` (both inherit from `User`)
- Authentication system with username/email and password
- Role-based access control

### Room Management

- Rooms with properties: ID, type, size, price, status, amenities
- Availability checking and booking system
- Room filtering by various attributes

### Booking System

- Create, view, and cancel bookings
- Check-in and check-out functionality
- Service association with bookings

### Services

1. **Transport Service**
   - Route management
   - Reservation system

2. **Food Ordering**
   - Menu management
   - Cart system
   - Order processing

3. **Laundry Service**
   - Cloth type management
   - Cart system
   - Reservation processing

4. **Cleaning Service**
   - Appointment scheduling
   - Service assignment

5. **Repair Service**
   - Issue reporting
   - Repair scheduling

## Route Structure

### Public Routes

- **`/`**: Home page
- **`/login`**: User login
- **`/signup`**: User registration
- **`/services`**: Overview of hotel services

### Guest Routes

- **`/booking`**: Search and book rooms
- **`/booking/review`**: Review and confirm bookings
- **`/profile`**: View guest profile and booking history
- **`/profile/booking/{booking_id}`**: View booking details
- **`/profile/booking/{booking_id}/cancel`**: Cancel a booking

### Staff Routes

- **`/staff`**: Staff dashboard
- **`/staff/room-management`**: Add and edit rooms
- **`/staff/check-in`**: Process guest check-ins
- **`/staff/check-out`**: Process guest check-outs
- **`/staff/services`**: Service management dashboard
- **`/staff/transport`**: Transport service management
- **`/staff/laundry`**: Laundry service management
- **`/staff/foods`**: Food service management
- **`/staff/cleaning`**: Cleaning service management
- **`/staff/repair`**: Repair service management
- **`/staff/signup`**: Create new staff accounts

## Route Logic

### Authentication and Authorization

```python
@rt("/login")
async def post(request, session):
    # Get credentials from form
    # Validate user
    # Set session if valid
    # Redirect to appropriate page
```

```python
def check_login(session, page=None):
    # Check if user is logged in
    # Redirect to login if not
```

### Room Booking Flow

1. **Search for Rooms**
```python
@rt("/get-rooms")
async def post(session, request):
    # Get search parameters
    # Find available rooms matching criteria
    # Return room listing
```

2. **Book Room**
```python
@rt("/booking/review")
async def post(session, request):
    # Process payment information
    # Create booking record
    # Redirect to confirmation page
```

### Staff Service Management

```python
@rt("/staff/transport/assign/{reservation_id}")
def post(reservation_id: int, session):
    # Assign staff to a transport reservation
    # Update reservation status
    # Return confirmation
```

Similar patterns exist for other services (laundry, food, cleaning, repair).

## Data Flow

1. **Room Booking**:
   - Guest searches for available rooms
   - System filters rooms by criteria
   - Guest selects a room and confirms booking
   - System creates a booking record
   - Email confirmation is sent (future feature)

2. **Service Request**:
   - Guest requests a service (food, transport, etc.)
   - Request is associated with their booking
   - Staff is assigned to fulfill request
   - Staff marks request as complete
   - Service fee is added to the booking

## Helper Functions

The system includes several UI helper functions:
- `menu()`: Renders navigation menu
- `display_room()`: Formats room data for display
- `reciept_card()`: Formats booking receipt
- `food_card()`: Formats food menu item
- `cloth_card()`: Formats laundry service item
- Various table rendering functions for staff interfaces

## Important Notes

- The system uses session management to maintain user state
- Role-based authorization restricts access to appropriate routes
- Service status flows: Pending → Ongoing → Complete/Cancelled
- Staff can only be assigned to one service at a time

This hotel management system demonstrates OOP principles with clear class hierarchies, encapsulation, inheritance, and polymorphism, particularly in the service system architecture.