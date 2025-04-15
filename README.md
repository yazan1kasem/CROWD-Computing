# CROWD-Computing – Verteiltes Rechnen mit simulierten Clients

## Projektbeschreibung

Das Projekt CROWD-Computing ist eine Python-basierte Simulation zur Demonstration von verteiltem Rechnen mithilfe mehrerer lokaler Clients, die über Sockets mit einem zentralen Server kommunizieren. Ziel ist es, den Mechanismus hinter Crowd Computing zu visualisieren – einer Technik, bei der große Rechenaufgaben auf mehrere Teilnehmer verteilt werden, um Effizienz und Geschwindigkeit zu steigern.

In dieser Simulation wird exemplarisch die Faktorisierung großer Zahlen verwendet. Der Server generiert dabei semi-prime Zahlen (Produkte zweier großer Zahlen), verteilt diese an die verbundenen Clients und sammelt deren Ergebnisse.

## Aufbau und Funktionsweise

Das Projekt besteht aus zwei zentralen Komponenten:

### 1. main.py

- Startet einen TCP-Server auf localhost:65432
- Generiert eine vordefinierte Anzahl großer Zahlen
- Verwaltet eine Aufgabenwarteschlange
- Startet automatisch mehrere Client-Prozesse im Hintergrund
- Empfängt, prüft und speichert die Ergebnisse der Clients

### 2. client.py

- Stellt eine Verbindung zum Server her
- Empfängt eine Zahl zur Faktorisierung
- Berechnet zwei Faktoren und sendet das Ergebnis zurück
- Trennt sich automatisch, sobald keine Aufgaben mehr vorhanden sind

## Beispielhafter Ablauf

Beim Start von `main.py` wird der Server aktiviert und beginnt, Aufgaben an Clients zu verteilen. Clients lösen die Aufgaben und senden Ergebnisse wie:

![image](https://github.com/user-attachments/assets/40f0b7d9-7e15-4fb7-8899-3c983d7d3391)

*Abbildung: Beispielausgabe*

Die Kommunikation erfolgt über das `socket`-Modul, während Threads und Subprozesse für parallele Abläufe sorgen.

## Technologischer Überblick

- Programmiersprache: Python 3.x
- Kommunikation: socket
- Nebenläufigkeit: threading, subprocess
- Aufgabenverwaltung: queue.Queue
- Plattform: plattformunabhängig (Windows/Linux)

## Anwendung

1. Stelle sicher, dass Python 3.x installiert ist.
2. Lege `main.py` und `client.py` im selben Ordner ab.
3. Starte das System über:

```
python main.py
```

Der Server erzeugt dann mehrere Clients automatisch, verteilt Aufgaben und verarbeitet deren Ergebnisse.
