## Repository zur Bachelor-Arbeit mit dem Titel: 

Experimentelle Evaluierung spezialisierter und generalistischer Large Language Models bei der funktionalen Codegenerierung anhand eines ausgewählten Testdatensatzes

## Verfasser:

Finn Luis von Heesen

## Kurzbeschreibung des Experiments:

Dieses Repository dient der Durchführung eines kontrollierten Laborexperiments, bei dem verschiedene spezialisierte Coding-Modelle und generalistische Sprachmodelle im Hinblick auf ihre Leistungsfähigkeit in der funktionalen Codegenerierung verglichen werden.
Getestet wurden die Modelle unter standardisierten Bedingungen auf einem lokalen Ollama-Server.

Im Rahmen des Experiments wurden zehn Large Language Models mit dem HumanEval-Datensatz getestet.
Es wurden jeweils fünf für Coding-Aufgaben feinabgestimmte bzw. generalistische Modelle getestet.
Die Größe der Modelle bezieht sich jeweils auf ca 7 Milliarden Parameter.
Ziel war es, die Pass@1-Erfolgsraten der Modelle zu ermitteln und die Leistungsunterschiede zwischen spezialisierter und generalistischer Modellarchitektur zu analysieren.
Die Temperatur wurde konstant auf 0.0 gesetzt, um deterministische Ergebnisse zu gewährleisten.
Für die einheitliche Verständlichkeit der Test-Aufgaben wurde zusätzlich zu den jeweiligen Aufgaben-Prompts ein Prompt-Template entwickelt, welches den Modellen neben der eigentlichen Aufgabe weitere essenzielle Hinweise zur Lösungsgenerierung gibt.
Alle Modellantworten wurden gespeichert, automatisiert evaluiert und in lokalen SQLite-Datenbanken dokumentiert.

## Lokale Infrastruktur:

Die Modelle wurden von einem Server des IT-Unternehmens Hewlett Packard Enterprise aufgerufen.

Virtual Maschine GPU: NVIDIA L40S (48 GB)

Lokaler Ollama-Server: vertraulich

Temperatureinstellung: 0.0

## Projektstruktur:

| Ordner / Datei                | Beschreibung |
|--------------------------------|--------------|
| `common/`                      | Allgemeine Hilfsfunktionen |
| ├── `query.py`                 | Query-Funktionen für Modellzugriffe |
| `dataset_configs/`             | Konfigurationsdateien für Benchmarks und lokale Daten |
| ├── `databases/`               | SQLite-Datenbanken und zugehörige Skripte |
| │   ├── `db_commun.py`         | Verwaltung und Abfragen der Datenbank |
| │   └── `humaneval.db`         | Testergebnisse der Modelle für den HumanEval Datensatz |
| `exports/`                     | Exportierte Ergebnisse |
| `local_data/`                  | Lokale Vorbereitung und Speicherung der Benchmarkdaten |
| `statistics/`                  | Statistische Auswertungen: Mittelwert, Median, Standardabweichung, U-Test |
| `visualizations/`              | Visualisierung der Ergebnisse (z. B. Balkendiagramme, Radarcharts) |
| `evaluate.py`                  | Hauptskript zur Evaluation der Modellantworten |
| `main.py`                      | Hauptsteuerung des Experiments |
| `requirements.txt`             | Python-Abhängigkeiten für das Projekt |


