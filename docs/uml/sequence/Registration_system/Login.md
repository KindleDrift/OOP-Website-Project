# Guest&Staff Login
```mermaid
sequenceDiagram
    actor Customer / Worker
    Customer / Worker->>UI: Login account
    activate UI
    UI->>Hotel: login(email, password)
    activate Hotel
    Hotel->>User: validate_user()
    activate User
    User-->>Hotel: return account_id
    deactivate User
    Hotel-->>UI: return account_id
    deactivate Hotel
    UI-->>Customer / Worker: Give account access
    deactivate UI
    %% fail
```