# Order Food
``` mermaid
sequenceDiagram
    actor Customer
    

    loop Add Dish To Cart
        Customer->>UI: add Dish to cart
        activate UI

        UI->>FoodOrdering: find_Dish(Dish_name)
        activate FoodOrdering

        FoodOrdering-->>UI: return Dish

        UI->>Cart: add(Dish)
        activate Cart

        Cart->>Cart: Total()

        Cart-->>UI: return update cart

        UI-->>Customer: show Dishes in cart and total price
        
    end


    loop Remove Food From Cart
        Customer->>UI: add Dish to cart

        UI->>FoodOrdering: find_Dish(Dish_name)

        FoodOrdering-->>UI: return Dish

        UI->>Cart: Remove(Dish)

        Cart->>Cart: Total()

        Cart-->>UI: return update cart

        UI-->>Customer: show Dishes in cart and total price

    end


    opt Clear Dish In Cart
        Customer->>UI: clear

        UI->>Cart: clear(Cart)

        Cart-->>UI: return empty cart

        UI-->>Customer: show empty cart

    end


    opt Confirm Cart
        Customer->>UI: click confirm
        
        UI->>FoodOrdering: create_food_order(guest, cart, booking)

        create participant FoodReservation
        FoodOrdering-->>FoodReservation: <<create>>

        FoodReservation-->>FoodOrdering: return success

        FoodOrdering->>Cart: clear(art)

        Cart-->>FoodOrdering: return
        deactivate Cart

        FoodOrdering-->>UI: return success
        deactivate FoodOrdering

        UI-->>Customer: return success
        deactivate UI
    
    end

```