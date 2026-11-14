Nexus Messenger
Ein selbst entwickelter Messenger auf Basis von Flask, SQLite und JavaScript.

Nexus ist ein lokales Messenger-Projekt mit Benutzerkonten, Gruppenchats und Dateiversand. Der Fokus liegt auf einer einfachen Architektur mit Flask und SQLite ohne zusätzliche externe Dienste.

Features
Benutzerregistrierung
Login-System mit Sessions
Nachrichten senden und empfangen
Gruppenchats erstellen
Mehrere Mitglieder pro Chat
User-Autocomplete beim Hinzufügen von Mitgliedern
Datei-Upload
Datei-Download
Dateianhänge in Nachrichten
Speicherung hochgeladener Dateien auf dem Server
Sichere Speicherung von Dateien über UUID-Dateinamen
Automatische Aktualisierung von Nachrichten (Polling alle 2 Sekunden)
Automatische Datenbankerstellung beim ersten Start
Automatische Erstellung von Testdaten
Nutzung auf mehreren Geräten im lokalen Netzwerk
Verwendete Technologien
Backend
Python
Flask
SQLite
Frontend
HTML
CSS
JavaScript
Sicherheit
Passwort-Hashing
Session-basierte Authentifizierung
Installation
Repository klonen
git clone https://github.com/tihei45/Messenger-Python.git
cd Messenger-Python
Abhängigkeiten installieren
pip install -r requirements.txt
Anwendung starten
python python/app.py
Browser öffnen
http://127.0.0.1:3000
oder über die lokale Netzwerk-IP:

http://<deine-ip>:3000
Datenbank
Beim ersten Start wird automatisch:

die SQLite-Datenbank nexus.db erstellt
die benötigten Tabellen angelegt
Testbenutzer erstellt
Testchats erstellt
Testnachrichten erstellt
Es ist keine zusätzliche Datenbankinstallation erforderlich.

Tabellen
users
Speichert die Benutzerkonten.

Feld	Beschreibung
userid	Benutzer-ID
username	Benutzername
password_hash	Passwort-Hash
chats
Speichert alle Chats.

Feld	Beschreibung
chatid	Chat-ID
chatname	Name des Chats
chat_members
Verknüpft Benutzer mit Chats.

Feld	Beschreibung
chatid	Chat-ID
userid	Benutzer-ID
messages
Speichert Nachrichten.

Feld	Beschreibung
messageid	Nachrichten-ID
chatid	Zugehöriger Chat
userid	Absender
content	Nachrichteninhalt
fileid	Dateianhang
files
Speichert Dateimetadaten.

Feld	Beschreibung
fileid	Datei-ID
original_name	Ursprünglicher Dateiname
stored_name	Interner Dateiname
mime_type	MIME-Type
size	Dateigröße
Dateiversand
Dateien werden nicht direkt in der Datenbank gespeichert.

Beim Upload:

Die Datei wird im Ordner uploads/ gespeichert.
Es wird ein eindeutiger UUID-Dateiname erzeugt.
Die Dateimetadaten werden in der Tabelle files gespeichert.
Die Nachricht wird über fileid mit der Datei verknüpft.
Beispiel:

Original:
index.html

Intern gespeichert:
56351ee4-7e6a-4975-89de-6c646845e381_index.html
Beim Download erhält der Nutzer automatisch wieder den ursprünglichen Dateinamen.

Projektstruktur
Messenger-Python
│
├── uploads/
│
├── python/
│   └── app.py
│
├── static/
│   ├── javascript/
│   │   └── main.js
│   │
│   └── style/
│       ├── main.css
│       ├── layout.css
│       └── variables.css
│
├── templates/
│   ├── main.html
│   ├── login.html
│   └── register.html
│
├── requirements.txt
├── README.md
└── .gitignore
Aktueller Stand
✅ Benutzerregistrierung

✅ Login-System

✅ Session-Verwaltung

✅ Gruppenchats

✅ Mehrere Mitglieder pro Chat

✅ User-Autocomplete

✅ Nachrichtenversand

✅ Dateiupload

✅ Dateidownload

✅ Dateianhänge

✅ SQLite-Datenbank

✅ Automatische Datenbankerstellung

✅ Automatische Testdaten

✅ Nachrichtenaktualisierung (2 Sekunden Polling)

✅ Lokale Mehrgerätenutzung

✅ Version 1.1

Geplante Features
Online-Status
Letzte Nachricht in der Chatliste
Nachrichten löschen
Nachrichten bearbeiten
Bildvorschau im Chat
Profilbilder
Benachrichtigungen
WebSockets für Echtzeitkommunikation
Responsive Mobile UI
Projektstatus
🚀 Aktive Entwicklung

Autor
Tilo Heinzmann

Entwicklung und Wartung von Nexus Messenger.