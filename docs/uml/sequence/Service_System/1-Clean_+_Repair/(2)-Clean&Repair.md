# Clean & Repair
``` mermaid
sequenceDiagram
    actor Customer
        
    Customer->>UI: click confirm
    activate UI
    
    UI->>Hotel: request_cleaning(date, time) / request_repairing(date, time)
    deactivate UI
    activate Hotel

    Hotel->>Hotel: get_staying_from_guest()
    activate Staying

    Hotel->>Staying: get_room_from_staying()

    Staying-->>Hotel: return room object
    deactivate Staying

    Hotel->>Staff: assign_staff() (to step-2)
    activate Staff
    deactivate Staff

    deactivate Hotel
        
```