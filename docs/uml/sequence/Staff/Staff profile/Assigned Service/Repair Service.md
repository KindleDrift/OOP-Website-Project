# Repair Service
```Mermaid
sequenceDiagram
    actor Worker

    Worker->>UI: click Repair Service
    activate UI


    loop get reservations of RepairService
        UI->>RepairService: get_reserved_reservation()
        activate RepairService

        RepairService-->>UI: return reservation
    end
    UI-->>Worker: display reservations

    opt Assign Self
        Worker->>UI: assign self

        UI->>RepairService: assign_reservation(reservation_id, staff)

        RepairService->>Staff: assign_service(reservation)
        activate Staff

        Staff-->>RepairService: return success

        RepairService-->>UI: return success

        UI-->>Worker: display Action Completed

        
        opt Unassign Self
            Worker->>UI: unassign self

            UI->>RepairService: unassign_reservation(reservation_id, staff)

            RepairService->>Staff: complete_service(reservation)

            Staff-->>RepairService: return success

            RepairService-->>UI: return success

            UI-->>Worker: display Action Completed
        end

        opt Complete
            Worker->>UI: Complete

            UI->>RepairService: complete_reservation(reservation_id, staff)

            RepairService->>Staff: complete_service(reservation)

            Staff-->>RepairService: return success

            RepairService-->>UI: return success

            UI-->>Worker: display Action Completed
        end
    end
    opt Cancel
        Worker->>UI: cancel

        UI->>RepairService: cancel_reservation(reservation_id, staff)

        RepairService->>Staff: complete_service(reservation)

        Staff-->>RepairService: return success
        deactivate Staff

        RepairService-->>UI: return success
        deactivate RepairService

        UI-->>Worker: display Action Completed
        deactivate UI
    end

    