# praxisnachbereitung-ss25

## Arbeitsablauf
- Aufgaben wurden nach und nach in der angegebenen Reihenfolge bearbeitet

## Entdeckte Probleme & Lösungen
### Aufgabe 4a: „Gesamtwert aller Geräte, die aktuell nicht im Einsatz sind“
- **Herausforderung:** Eine Gerätenummer kann mehrfach vorkommen (mehrere Ausleihen), teils mit leerem **„Rückgabe am“**. Wir müssen den **aktuellen Status** je Gerät bestimmen.
- **Lösung (Power Query):**
  - `Ausleihen_combined` nach **Gerätenummer (↑)** und **Ausgabe am (↓)** sortiert.
  - **Gruppieren nach** `Gerätenummer`
  - Im Filter wurden "NULL" Werte aus "Rückgabe am" entfernt
  - Mit Statistik wurde die Summe der übrigen Zeilen gezählt
- **Ergebnis:** Tabellenblatt mit Zeilensumme aller Geräte, die nicht aktiv ausgeliehen sind

## Wichtige Erkenntnisse
- Ausprobieren und Googlen helfen
- Bei Power Query lassen sich Abfragen leicht rückgängig machen und wir konnten durch Duplikation bei Abfragen Zwischenstände speichern
- Power Query war sehr hilfreich beim Lösen der Aufgaben
- Pivot Tabellen erlauben schnelle Erstellung von übersichtlichen Datenaggregationen 