# Transportation
```Mermaid
sequenceDiagram
    actor Worker

    Worker->>UI: click transport
    activate UI


    loop get reservations of Transport
        UI->>Transport: get_reserved_reservation()
        activate Transport

        Transport-->>UI: return reservation
    end
    UI-->>Worker: display reservations

    opt Assign Self
        Worker->>UI: assign self

        UI->>Transport: assign_reservation(reservation_id, staff)

        Transport->>Staff: assign_service(reservation)
        activate Staff

        Staff-->>Transport: return success

        Transport-->>UI: return success

        UI-->>Worker: display Action Completed

        
        opt Unassign Self
            Worker->>UI: unassign self

            UI->>Transport: unassign_reservation(reservation_id, staff)

            Transport->>Staff: complete_service(reservation)

            Staff-->>Transport: return success

            Transport-->>UI: return success

            UI-->>Worker: display Action Completed
        end

        opt Complete
            Worker->>UI: Complete

            UI->>Transport: complete_reservation(reservation_id, staff)

            Transport->>Staff: complete_service(reservation)

            Staff-->>Transport: return success

            Transport-->>UI: return success

            UI-->>Worker: display Action Completed
        end
    end
    opt Cancel
        Worker->>UI: cancel

        UI->>Transport: cancel_reservation(reservation_id, staff)

        Transport->>Staff: complete_service(reservation)

        Staff-->>Transport: return success
        deactivate Staff

        Transport-->>UI: return success
        deactivate Transport

        UI-->>Worker: display Action Completed
        deactivate UI
    end

    