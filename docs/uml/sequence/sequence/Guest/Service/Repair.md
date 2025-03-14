# Repair
``` mermaid
sequenceDiagram
    actor Customer
        
    Customer->>UI: click confirm
    activate UI
    
    UI->>RepairService: *create_reservation()
    activate RepairService

    create participant RepairReservation
    RepairService-->>RepairReservation: <<create>>

    RepairReservation-->>RepairService: return appointment date&time issue

    RepairService-->>UI: return appointment date&time issue
    deactivate RepairService

    UI-->>Customer: show appointment date&time issue
    deactivate UI

```

*create_reservation(guest, appointment_date, appointment_time, item, repair_issue, booking)