# Booking(Home)
```mermaid
sequenceDiagram
    actor Customer

    Customer->>UI: Search Room
    activate UI

    UI->>Hotel: get_room_by_attribute(room_type,  guest_count, max_budget_perday, Check-in Date, Check-out Date)
    activate Hotel


    loop for room in all room
        Hotel->>Hotel:check_room_availability(room_id, Check-in Date, Check-out Date)

    end


    Hotel-->>UI:display room meeted condition

    UI-->>Customer: display rooms
    deactivate UI


    opt confirm room Payment
        Customer->>UI: type payment info
        activate UI

        UI->>Hotel: pay_booking(name,creditcard_id, creditcard_expiration(M), creditcard_expiration(Y), CVV)

        Hotel-->>Booking: create_booking(guest)

        create participant Booking
        Hotel->>Hotel: money_gain()
        activate Booking
        deactivate Booking

        

        Booking-->>Hotel: return self
        
        

        Hotel-->>UI: return booking_detail
        deactivate Hotel

        UI-->Customer: Display "Booking Successful"
        deactivate UI
        
    end
    
```
