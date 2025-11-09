# Inventar – ER-Modell (Mermaid)

## ER-Diagramm
```mermaid
erDiagram
  Person      ||--o{ Assignment : receives
  Device      ||--o{ Assignment : is_assigned_to
  DeviceType  ||--o{ Device     : classifies
  Location    ||--o{ Device     : located_at

  Person {
    int    person_id PK
    string personal_nr UK
    string first_name
    string last_name
  }

  DeviceType {
    int    device_type_id PK
    string code UK
    string name
  }

  Location {
    int    location_id PK
    string location_code UK
    string name
  }

  Device {
    int      device_id PK
    string   inventory_nr UK
    int      device_type_id FK
    int      location_id FK
  }

  Assignment {
    int       assignment_id PK
    int       device_id FK
    int       person_id FK
    datetime  assigned_from
    datetime  assigned_to
  }
```

## Regeln

**R1 – Eindeutigkeit (UK)**
- `Device.inventory_no` (**= inventory_nr im ERD**) ist eindeutig.
- `Person.personnel_no` (**= personal_nr im ERD**) ist eindeutig.
- `DeviceType.code` ist eindeutig.
- `Location.code` ist eindeutig.

**R2 – max. 1 Zuweisung je Device**
- zu jedem Zeitpunkt darf ein Device höchstens eine aktive Zuweisung haben 

**R3 – assigned_to darf leer sein**
- `Assignment.assigned_to` darf leer sein (aktiver Zustand)
