# Übung #1

**[Folien Übung](slides_aufgabe-1.pdf)**


**Abgabetermine**

* Abgabetermin Erste Version (für Peer Review in zweiter Übungs-Einheit): 22. Mai 2018, 24h
* Finale Version (wird beurteilt): 17. Juni 2018, 24h

## 1.1. Metadaten erstellen

Erstelle die Metadaten zu einem Werk.


Typ: Gruppenarbeit


Aufwand: 45min


* Werkstyp aus Google Spreadsheet raus suchen.

#### 1.1.1. Diskussion Metadaten

* Überlegt euch als Gruppe, welche Metadaten nötig sind um das gewählte Werk zu beschreiben bzw. es besser zu verstehen. Sammelt möglichst viele Attribute.

#### 1.1.2 Metadaten-Datei erstellen

* Verfasst gemeinsam ein Metadaten-Datei (`aufgabe-1_metadata.json`) für ein fiktives Werk des oben gewählten Werkstypen. Überlegt euch passende Key-Value Paare, die in echt auch auftreten könnten und somit logisch konsistent sind. 
* Beachtet bei den Keys: alles klein,  zusammen und auf Englisch geschrieben. Als Trennzeichen einen Underscore (`_`) verwenden, z. B. `date_created`.
* Key-Value Paare werden durch ein Komma hinten voneinander getrennt. Daher beim letzten Key-Value Paar kein Komma mehr, da kein weiteres Paar mehr folgt.
* Die Metadaten sollen für den Computer genauso wie für den Menschen lesbar bzw. nutzbar sein.
* Verwendet dazu als Vorlage [aufgabe-1_metadata.json](templates/aufgabe-1_metadata.json).
* Wenn ihr die gesamte Datei fertig habt, ist der Inhalt noch auf [jsonlint](https://jsonlint.com/) zu validieren
* Ladet die fertige Datei auf GitHub hoch.

**Resourcen:**

* Vorlesung: [Folien Daten](../vorlesung/slides_2-daten.pdf)
* Vorlesung: [Metadaten Umfrage Herrengasse](../data/theorie/metadata_umfrage-herrengasse.json)
* Vorlesung: [Metadaten Wetterstation](../data/theorie/metadata_wetterstation.json)
* [Was ist eine JSON-Datei?](https://de.wikipedia.org/wiki/JavaScript_Object_Notation)
* [Wikipedia: Metadaten](https://de.wikipedia.org/wiki/Metadaten)

## 1.2. Datenset finden

Suche nach einem Datensatz.


Typ: Individualarbeit


Aufwand:

* Recherche: 20min
* Bericht: 20min

#### 1.2.1 Recherche

* Datensatz aus Google Spreadsheet raus suchen.
* Recherchiere selbstständig nach dem Datensatz. 
* Wenn du mehrere Quellen gefunden hast, wähle die für dich beste Quelle aus Sicht der Datenqualität aus.

#### 1.2.2 Bericht

* Dokumentiere deinen Rechercheweg im Bericht (`aufgabe-1_bericht_NACHNAME.md`).
* Beantworte darin folgende Fragen kurz und bündig:

```
1. Hast du den Datensatz gefunden?
2. Wenn ja:
  a) Beschreibe deinen Rechercheweg: Wie wurdest du fündig? Welche Such-Strategie hast du angewendet? Welche Tools bzw. Internet-Seiten haben dir dabei geholfen? Was waren Probleme die dabei auftraten?
  b) Link zum Datenset
  c) Unter welcher UrheberInnenrechts-Lizenz steht der Datensatz? Falls die Lizenz nicht direkt auffindbar oder schwer zu interpretieren ist (z. B. keine standardisierte Lizenz ala Creative Commons), führe dies bitte an.
  d) Darfst du laut Lizenz die Daten für Bildungszwecke weiterverwenden?
  e) Gibt es Metadaten zu dem Datensatz?
    ja: Waren die Metadaten ausreichend, um das Datenset zu verstehen? Link zu den Metadaten angeben.
    nein: Liste Metadaten auf, die hilfreich wären, um das Datenset besser zu verstehen.
3. Wenn nein:
  a) Wo hast du überall gesucht? Liste die Orte auf.
  b) Wie war deine Such-Strategie? Beschreibe die verschiedenen Recherchewege, die du eingeschlagen hast (z. B. bekannte Repositories, Community, Suchmaschine, etc.)
  c) Warum glaubst du, konntest du das Datenset nicht finden?
  d) Welche Institution sollte die Daten besitzen und warum?
```

* Verwende dazu als Vorlage [aufgabe-1_bericht_NACHNAME.md](templates/aufgabe-1_bericht_NACHNAME.md). Gib oben deinen Namen an. Erstelle für jede Frage-Antwort-Kombination einen eigenen Absatz. Schreibe neben `Q` die Frage, und neben `A` die Antwort. Trenne jedes Frage-Antwort Paar durch drei Minus (`---`) darunter, um so eine Trennlinie zu erzeugen. 
* Ändere im Dateinamen `NACHNAME` auf deinen Nachnamen ab (alles klein und zusammen geschrieben, z. B. `aufgabe-1_bericht_neumann.md`).
* Lade den Bericht auf GitHub hoch.

**Ressourcen**

* Vorlesung: [Folien Daten](../vorlesung/slides_2-daten.pdf)




