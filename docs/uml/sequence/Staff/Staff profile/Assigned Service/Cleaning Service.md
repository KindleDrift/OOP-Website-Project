# Cleaning Service
```Mermaid
sequenceDiagram
    actor Worker

    Worker->>UI: click Cleaning Service
    activate UI


    loop get reservations of CleaningService
        UI->>CleaningService: get_reserved_reservation()
        activate CleaningService

        CleaningService-->>UI: return reservation
    end
    UI-->>Worker: display reservations

    opt Assign Self
        Worker->>UI: assign self

        UI->>CleaningService: assign_reservation(reservation_id, staff)

        CleaningService->>Staff: assign_service(reservation)
        activate Staff

        Staff-->>CleaningService: return success

        CleaningService-->>UI: return success

        UI-->>Worker: display Action Completed

        
        opt Unassign Self
            Worker->>UI: unassign self

            UI->>CleaningService: unassign_reservation(reservation_id, staff)

            CleaningService->>Staff: complete_service(reservation)

            Staff-->>CleaningService: return success

            CleaningService-->>UI: return success

            UI-->>Worker: display Action Completed
        end

        opt Complete
            Worker->>UI: Complete

            UI->>CleaningService: complete_reservation(reservation_id, staff)

            CleaningService->>Staff: complete_service(reservation)

            Staff-->>CleaningService: return success

            CleaningService-->>UI: return success

            UI-->>Worker: display Action Completed
        end
    end
    opt Cancel
        Worker->>UI: cancel

        UI->>CleaningService: cancel_reservation(reservation_id, staff)

        CleaningService->>Staff: complete_service(reservation)

        Staff-->>CleaningService: return success
        deactivate Staff

        CleaningService-->>UI: return success
        deactivate CleaningService

        UI-->>Worker: display Action Completed
        deactivate UI
    end

    