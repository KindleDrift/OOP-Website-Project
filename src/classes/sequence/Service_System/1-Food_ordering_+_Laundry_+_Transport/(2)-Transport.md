# Transport
``` mermaid
    sequenceDiagram
        Customer->>UI: click to choose route

        UI->>Hotel: confirm_order()

        Hotel->>Staff: assign_staff() (to step-2)
```