# Laundry Service
```Mermaid
sequenceDiagram
    actor Worker

    Worker->>UI: click Laundry Service
    activate UI


    loop get reservations of Laundry
        UI->>Laundry: get_reserved_reservation()
        activate Laundry

        Laundry-->>UI: return reservation
    end


    UI-->>Worker: display reservations

    opt Add Cloth Type
        Worker->>UI: add cloth type and price

        UI->>Laundry: get_cloth_type(cloth_name)


        alt cloth don't exist
            Laundry-->>UI: return success

            UI->>Laundry:create_cloth(cloth_name, price)

            Laundry-->>UI: return Cloth Added

        else cloth already exists
            Laundry-->>UI: return cloth already exists
        
        end

    end

    opt Assign Self
        Worker->>UI: assign self

        UI->>Laundry: assign_reservation(reservation_id, staff)

        Laundry->>Staff: assign_service(reservation)
        activate Staff

        Staff-->>Laundry: return success

        Laundry-->>UI: return success

        UI-->>Worker: display Action Completed

        
        opt Unassign Self
            Worker->>UI: unassign self

            UI->>Laundry: unassign_reservation(reservation_id, staff)

            Laundry->>Staff: complete_service(reservation)

            Staff-->>Laundry: return success

            Laundry-->>UI: return success

            UI-->>Worker: display Action Completed
        end


        opt Complete
            Worker->>UI: Complete

            UI->>Laundry: complete_reservation(reservation_id, staff)

            Laundry->>Staff: complete_service(reservation)

            Staff-->>Laundry: return success

            Laundry-->>UI: return success

            UI-->>Worker: display Action Completed
        end


    end


    opt Cancel
        Worker->>UI: cancel

        UI->>Laundry: cancel_reservation(reservation_id, staff)

        Laundry->>Staff: complete_service(reservation)

        Staff-->>Laundry: return success
        deactivate Staff

        Laundry-->>UI: return success
        deactivate Laundry

        UI-->>Worker: display Action Completed
        deactivate UI
    end

    