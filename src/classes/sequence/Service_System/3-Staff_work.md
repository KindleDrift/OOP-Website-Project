# Staff work
``` mermaid
    sequenceDiagram
    actor Worker

    
    Worker->>UI: click to check for work
    activate UI

    UI->>Staff:check_work(staff)
    activate Staff


    alt got work todo
        Staff-->>UI:return todo work

        UI-->>Worker:show todo work


        opt do work

            Worker->>UI:click work

            UI->>Staff:working()

            Staff->>Staff:swap_status()

            Staff-->>UI: return

            UI-->>Worker: show currently working

        opt finish work
            Worker->>UI: click done work

            UI->>Staff: done_work(staff)

            Staff->>Staff:swap_status()

            Staff-->>UI: return

            UI-->>Worker: show work done

        end

        end
    else no work todo
        Staff-->>UI:return no work
        deactivate Staff

        UI-->>Worker:show no work
        deactivate UI
    end
```