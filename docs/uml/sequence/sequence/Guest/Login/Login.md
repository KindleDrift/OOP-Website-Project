# Guest&Staff Login
```mermaid
sequenceDiagram
    actor Customer / Worker

    Customer / Worker->>UI: Login account
    activate UI

    UI->>Hotel: validate_user(email, password)
    activate Hotel

        Hotel->>User: authenticate(email, password)
        activate User
    alt Correct Password

        User-->>Hotel: return account_id

        Hotel-->>UI: return account_id

        UI-->>Customer / Worker: Give account access

    else Incorrect Password
        User-->>Hotel: return fail
        deactivate User

        Hotel-->>UI: return fail
        deactivate Hotel

        UI-->>Customer / Worker: show fail
        deactivate UI
    end
```