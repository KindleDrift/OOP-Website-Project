# Clean
``` mermaid
sequenceDiagram
    actor Customer
        
    Customer->>UI: click confirm
    activate UI
    
    UI->>CleaningService: *create_reservation()
    activate CleaningService

    create participant CleaningReservation
    CleaningService-->>CleaningReservation: <<create>>

    CleaningReservation-->>CleaningService: return appointment date&time

    CleaningService-->>UI: return appointment date&time
    deactivate CleaningService

    UI-->>Customer: show appointment date&time
    deactivate UI

```

*create_reservation(guest, appointment_date, appointment_time, booking)