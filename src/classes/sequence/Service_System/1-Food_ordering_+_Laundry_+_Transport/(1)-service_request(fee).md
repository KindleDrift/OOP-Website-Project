# Service_request (fee)
## (Transport, Food_order, Laundry)
``` mermaid
    sequenceDiagram
        actor Customer

        Customer->>UI:click for service
        activate UI 
        UI->>Hotel:display_all_service()

        activate Hotel
        Hotel-->>UI:return service names
        deactivate Hotel
        
        UI-->>Customer:display all services
        deactivate UI
        

        opt choose service
            Customer->>UI:click to choose service
            activate UI

            UI->>Hotel:choose_service(Food_order/Laundry/Transport)
            activate Hotel

            Hotel->>Hotel:get_available(menu/route/cloth_type)()
            
            Hotel-->>UI:return (menu/route/cloth_type)[]
            deactivate Hotel
            
            UI-->>Customer:show (menu/route/cloth_type)[]
            deactivate UI

            
        end
```