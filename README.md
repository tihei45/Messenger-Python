# Messenger-Python

Ein selbst entwickelter Messenger auf Basis von Flask, SQLite und JavaScript.

## Features

- Nachrichten senden
- Chats erstellen
- Mehrere Mitglieder pro Chat
- User-Autocomplete
- Chatwechsel
- Automatische Aktualisierung von Nachrichten alle 2 Sekunden

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
- die Tabellen angelegt
- Testdaten für Benutzer, Chats und Nachrichten eingefügt

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
├── .gitignore
└── nexus.db
```

## Projektstatus

🚀 Aktive Entwicklung

## Geplante Features

- Benutzeranmeldung
- Eigene Profile
- Live-Updates für Nachrichten
- Datei-Uploads
- Benachrichtigungen

---

Projekt von Tilo Heinzmann
