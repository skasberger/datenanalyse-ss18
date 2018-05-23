**[Folien](uebung/slides_aufgabe-1.pdf)**

## Todo

**1. Setup**


Den Projekt-Ordner aufsetzen. Dazu folgende Ordner Struktur erstellen.


Typ: Gruppenarbeit


Aufwand: 5min


Ordner-Struktur:
```
PROJEKTNAME/
  data/: hier kommen erzeugte Datensets rein, die man für die Analyse bzw. Aufgaben benötigt.
    raw/: hier kommen die Rohdaten in ihrer Orginalform rein. Daten sollen nicht verändert werden.
  docs/: hier wird alles mögliche an Dokumenten gespeichert, die man für die Analyse braucht. Papers, eigens erstelle Notizen etc.
  aufgabe-1/: hier kommen sämtliche Dateien zur Aufgabe 1
  aufgabe-2/: hier kommen sämtliche  Dateien zur Aufgabe 2
  aufgabe-3/: hier kommen sämtliche  Dateien zur Aufgabe 3
  aufgabe-4/: hier kommen sämtliche  Dateien zur Aufgabe 4
  praesentation/: hier kommen sämtliche Daten zur Präsentation
  notes.md: Dokumentation für einen selbst. Interne Notizzen. (optional)
```

**2. Metadaten erstellen**


Erstellen der Metadaten als JSON-Datei.


Typ: Gruppenarbeit


Aufwand: 45min


Schritte:
* Beispiel-Datensatz aus Liste raus suchen.
* Überlegt euch in der Gruppe, welche (fiktiven) Metadaten nötig sind um das Datenset zu beschreiben.
* Metadaten als Key-Value Paare in Metadaten-Datei schreiben. Nehmt euch Zeit, dies wirklich gut und ausführlich zu machen. Selbsterklärende Key-Namen beachten.
* Validieren der JSON Datei auf [jsonlint](https://jsonlint.com/)
* Upload der Datei in das GitHub Repository


**3. Daten finden**


Selbständige Recherche nach einem Datensatz.


Typ: Individualarbeit


Aufwand:
* Recherche: 20min
* Bericht: 20min


Schritte:
* Datensatz aus Liste raus suchen.
* Selbstständig nach dem Datensatz recherchieren.
* Dokumentieren der Recherche als Markdown im Bericht.
* Upload der Datei in das GitHub Repository.

## Abgaben

Deadline: 22. Mai 2018, 24h


**Gruppeneinteilung und GitHub account**

Ergebnis der Gruppeneinteilung mitsamt dem eigenen User-Account in Spreadsheet eingeben.


**metadata.json**

Valdierte JSON File mit den Metadaten. 
* Keys auf Englisch, ohne Leerzeichen, alles klein, mit Underscore als Trennzeichen (z. B. `"date_created"`). 
* Metadaten sollen für Computer genauso wie für Menschen verständlich bzw. nützlich sein.
* jedes Key-Value Pair wird mit einem Beistrich abgeschlossen, ausser das letzte.
* JSON Dictionaries (Key-Value Pairs) werden mit einer geschwungenden Klammer gestartet und beendet.

**aufgabe-1_bericht_NACHNAME.md**

Kurzer Text, in dem folgende Fragen knapp und bündig zu beantworten sind (~200 Wörter). Gib bei der Antwort den Listenpunkt der Frage an und erstelle einen eigenen Absatz mit Überschrift (Header 2) zu jeder Frage.
1. Hast du den Datensatz gefunden?
2. Wenn ja:
  * a) Beschreibe deinen Recherche Weg: Wie wurdest du fündig? Welche Strategie hast du angewendet? Welche Tools bzw. Internet-Seiten haben dir dabei geholfen, etc.
  * b) Link zum Datenset
  * c) Unter welcher Urheberrechts-Lizenz steht der Datensatz? Falls nicht auffindbar oder schwer zu interpretieren (keine standardisierte Lizenz ala Creative Commons), kurz anführen.
  * d) Darfst du laut Lizenz die Daten für Bildungszwecke weiterverwenden?
  * e) Gibt es Metadaten zu dem Datensatz?
    * ja: Waren die Metadaten ausreichend, um das Datenset zu verstehen? (Weshalb, Weshalb nicht?) Link zu den Metadaten angeben.
    * nein: Welche Metadaten bräuchtest du?
3. Wenn nein:
  * a) Wo wurde überall gesucht?
  * b) Wie war deine Such-Strategie? Beschreibe die verschiedenen Recherchewege, die du eingeschlagen hast (Repository, Community, Suchmaschine, etc.)
  * c) Beschreibe, warum du glaubst, dass du das Datenset nicht gefunden hast?
  * d) Welche öffentlichen oder privaten Organisationen sind Eigentümer der Daten bzw. sollten diese haben? Warum?

Die Datei ist mit dem passenden Nachnamen im Dateinamen (`aufgabe-1_bericht_NACHNAME.md`) auf GitHub in den passenden Gruppen-Ordner hochzuladen.

z. B. `aufgabe-1_bericht_neumann.md`


