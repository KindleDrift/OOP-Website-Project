# Order Laundry
``` mermaid
sequenceDiagram
    actor Customer
    

    loop Add Cloth To Cart
        Customer->>UI: add Cloth to cart
        activate UI

        UI->>Laundry: find_Cloth(Cloth_name)
        activate Laundry

        Laundry-->>UI: return Cloth

        UI->>Cart: add(Cloth)
        activate Cart

        Cart->>Cart: Total()

        Cart-->>UI: return update cart

        UI-->>Customer: show Clothes in cart and total price
        
    end


    loop Remove Laundry From Cart
        Customer->>UI: add Cloth to cart

        UI->>Laundry: find_Cloth(Cloth_name)

        Laundry-->>UI: return Cloth

        UI->>Cart: Remove(Cloth)

        Cart->>Cart: Total()

        Cart-->>UI: return update cart

        UI-->>Customer: show Clothes in cart and total price

    end


    opt Clear Cloth In Cart
        Customer->>UI: clear

        UI->>Cart: clear()

        Cart-->>UI: return empty cart

        UI-->>Customer: show empty cart

    end


    opt Confirm Cart
        Customer->>UI: click confirm
        
        UI->>Laundry: create_reservation(guest, cart, booking)

        create participant LaundryReservation
        Laundry-->>LaundryReservation: <<create>>

        LaundryReservation-->>Laundry: return success

        Laundry->>Cart: clear(art)

        Cart-->>Laundry: return
        deactivate Cart

        Laundry-->>UI: return success
        deactivate Laundry

        UI-->>Customer: return success
        deactivate UI
    
    end

```