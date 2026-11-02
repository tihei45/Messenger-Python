# Messenger-Python

Ein selbst entwickelter Messenger auf Basis von Flask, SQLite und JavaScript.

## Features

- Nachrichten senden
- Chats erstellen
- Mehrere Mitglieder pro Chat
- User-Autocomplete
- Chatwechsel
- Automatische Aktualisierung von Nachrichten (Polling alle 2 Sekunden)
- Automatische Datenbankerstellung beim ersten Start
- Automatische Erstellung von Testdaten für die Entwicklung

## Verwendete Technologien

- Python
- Flask
- SQLite
- JavaScript
- HTML
- CSS

## Installation

Repository klonen:

```bash
git clone https://github.com/tihei45/Messenger-Python.git
cd Messenger-Python
```

Abhängigkeiten installieren:

```bash
pip install -r requirements.txt
```

Anwendung starten:

```bash
python python/app.py
```

Anschließend im Browser öffnen:

```text
http://127.0.0.1:5000
```

## Datenbank

Beim ersten Start wird automatisch:

- die SQLite-Datenbank `nexus.db` erstellt
- die benötigten Tabellen angelegt
- Testbenutzer erstellt
- Testchats erstellt
- Testnachrichten erstellt

Es ist keine zusätzliche Datenbankinstallation notwendig.

## Projektstruktur

```text
Messenger-Python
│
├── python/
│   └── app.py
├── static/
│   ├── javascript/
│   └── style/
├── templates/
│   └── main.html
├── requirements.txt
├── README.md
└── .gitignore
```

## Aktueller Stand

✅ Chat-Erstellung

✅ Nachrichten senden

✅ Mehrere Mitglieder pro Chat

✅ User-Autocomplete

✅ SQLite-Datenbank

✅ Automatische Datenbankerstellung

✅ Automatische Testdaten

✅ Automatische Nachrichtenaktualisierung

✅ Läuft auf mehreren Geräten im lokalen Netzwerk

✅ Version 1.0 veröffentlicht

## Geplante Features

- Login & Registrierung
- Benutzerprofile
- Online-Status
- Benachrichtigungen
- Datei- und Bildversand
- Echtzeitkommunikation über WebSockets

## Projektstatus

🚀 Aktive Entwicklung

---

Projekt von Tilo Heinzmann