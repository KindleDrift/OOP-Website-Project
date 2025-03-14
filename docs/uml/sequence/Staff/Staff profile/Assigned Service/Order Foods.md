# Order Foods
```Mermaid
sequenceDiagram
    actor Worker

    Worker->>UI: click Order Foods
    activate UI

    loop get dishes
        UI->>FoodOrdering: FoodOrdering.dishes()
        activate FoodOrdering
        
        FoodOrdering-->>UI: return dishes
    end


    loop get reservations of FoodOrdering
        UI->>FoodOrdering: get_reserved_reservation()

        FoodOrdering-->>UI: return reservation
    end


    UI-->>Worker: display dishes' name and reservations

    opt Restock
        Worker->>UI: restock

        UI->>FoodOrdering: restock(item_name, amount)

        FoodOrdering->>FoodOrdering: find_dish(dish_name)

        FoodOrdering-->>UI: return dish Added

        UI-->>Worker: display dish Added

    end


    opt Add dish
        Worker->>UI: add dish and price

        UI->>FoodOrdering: add_new_menu(dish_name, price, image_url)

        FoodOrdering-->>UI: return dish Added

        UI-->>Worker: display dish Added

    end

    opt Assign Self
        Worker->>UI: assign self

        UI->>FoodOrdering: assign_reservation(reservation_id, staff)

        FoodOrdering->>Staff: assign_service(reservation)
        activate Staff

        Staff-->>FoodOrdering: return success

        FoodOrdering-->>UI: return success

        UI-->>Worker: display Action Completed

        
        opt Unassign Self
            Worker->>UI: unassign self

            UI->>FoodOrdering: unassign_reservation(reservation_id, staff)

            FoodOrdering->>Staff: complete_service(reservation)

            Staff-->>FoodOrdering: return success

            FoodOrdering-->>UI: return success

            UI-->>Worker: display Action Completed
        end


        opt Complete
            Worker->>UI: Complete

            UI->>FoodOrdering: complete_reservation(reservation_id, staff)

            FoodOrdering->>Staff: complete_service(reservation)

            Staff-->>FoodOrdering: return success

            FoodOrdering-->>UI: return success

            UI-->>Worker: display Action Completed
        end


    end


    opt Cancel
        Worker->>UI: cancel

        UI->>FoodOrdering: cancel_reservation(reservation_id, staff)

        FoodOrdering->>Staff: complete_service(reservation)

        Staff-->>FoodOrdering: return success
        deactivate Staff

        FoodOrdering-->>UI: return success
        deactivate FoodOrdering

        UI-->>Worker: display Action Completed
        deactivate UI
    end

    