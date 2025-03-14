# Booking(Home)
```mermaid
sequenceDiagram
    actor Customer

    Customer->>UI: Search Room
    activate UI

    UI->>Hotel: *get_room_by_attribute()
    activate Hotel


    loop for room in all corresponding room
        Hotel->>Hotel: *check_room_availability()

    end


    Hotel-->>UI:display room meeted condition

    UI-->>Customer: display rooms
    deactivate UI


    opt Confirm Room
        Customer->>UI: confirm room
        activate UI

        UI->>Hotel: *create_booking()

        Hotel->>Hotel: *check_room_availability()

        create participant Booking
        Hotel-->>Booking: <<create>>
        activate Booking


        Booking-->>Hotel: return

        Hotel-->>UI: return success
        deactivate Hotel

        UI-->Customer: show success
        deactivate UI
        
    end
    
```

*get_room_by_attribute(room_type,  guest_count, max_budget_perday, start_date, end_date)

*check_room_availability(room_id, start_date, end_date)

*create_booking(user, room, start_date, end_date)

