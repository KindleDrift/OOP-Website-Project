# Transport
``` mermaid
sequenceDiagram
    actor Customer
        
    Customer->>UI: click confirm
    activate UI
    
    UI->>TransportService: *create_reservation()
    activate TransportService

    create participant TransportReservation
    TransportService-->>TransportReservation: <<create>>

    TransportReservation-->>TransportService: return appointment date&time

    TransportService-->>UI: return appointment date&time
    deactivate TransportService

    UI-->>Customer: show appointment date&time
    deactivate UI

```

*create_reservation(guest, guest, route_name, date, booking)