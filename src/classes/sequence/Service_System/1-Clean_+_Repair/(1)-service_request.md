# Service_request
## (Clean, Repair)
``` mermaid
    sequenceDiagram
        actor Customer

        Customer->>UI:click for service
        activate UI 
        UI->>Hotel:get_all_service()

        activate Hotel
        Hotel-->>UI:return service names
        deactivate Hotel
        
        UI-->>Customer:display all services
        deactivate UI
        

        opt choose service
            Customer->>UI:click to choose service
            activate UI

            UI->>Hotel:choose_service(Clean/Repair)
            activate Hotel
            
            Hotel-->>UI:return need info
            deactivate Hotel
            
            UI-->>Customer:display "need info"
            deactivate UI

            
        end
```