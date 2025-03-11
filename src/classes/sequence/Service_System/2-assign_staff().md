# assign_staff()
```Mermaid
sequenceDiagram
    actor Customer

    Customer->>UI: //click to demand sth// (from step-1)
    activate UI

    UI->>Hotel: //demand sth// (from step-1)
    activate Hotel
    activate Any service

    Hotel->>Staff: assign_staff(any_service)
    activate Staff


    
    loop for all staff with (any_service) role in hotel
        Staff->>Staff: find_available_right_staff(any_service)
    end

    alt staff found
        Staff->>Staff: assign_work(staff)
            
        Staff-->>Hotel: return staff object

        Hotel->>Booking: record_service_usage(money, a ny_service_name,time?)

        Booking-->>Hotel: return
        

        Hotel-->>UI: return Any service

        UI-->>Customer: show Any service info
        

    else no available staff
        Staff-->>Any service: return fail
        deactivate Staff

        Staff-->>Hotel: return fail

        deactivate Any service

        Hotel-->>UI: return fail
        deactivate Hotel

        UI-->>Customer: show "no available staff"
        deactivate UI


    end