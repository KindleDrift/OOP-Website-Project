# Laundry
``` mermaid
    sequenceDiagram
        actor Customer

            loop get all requested Food
                Customer->>UI: click add Food to cart
                activate UI
                
            
                UI->>Hotel:add_Food(Food)
                activate Hotel

                Hotel-->>UI: return

                UI-->>Customer: return
            end
            opt confirm
                Customer->>UI: click confirm
                

                UI->>Hotel: confirm_order()
                deactivate UI
                
                Hotel->>Food_reservation: reserve(guest, [food, amount])

                Food_reservation-->>Hotel: return
                

                Hotel->>Staff: assign_staff() (to step-2)
                deactivate Hotel

            end
```