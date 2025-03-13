# Worker Check-out Booking (check_in board)
```mermaid
sequenceDiagram
    actor Worker

    Worker->>UI: search booking
    activate UI

    UI->>Hotel: filter_check_out()
    activate Hotel

    Hotel-->>UI: return booking corresponding to info

    UI-->>Worker: display bookings

    Worker->>UI: click check_out booking

    UI->>Hotel: check_out_booking(booking_id)

    Hotel->>Hotel: get_booking_by_id(booking_id)

    Hotel->>Hotel: gain_money(money)

    Hotel->>Booking: change_booking_status(booking, "Checked Out")

    Booking-->>Hotel: return Success

    Hotel-->>UI: return Success

    UI-->>Worker: display Success

```