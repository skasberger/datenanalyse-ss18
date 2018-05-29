## Abgabe EH 3

### Todo

Deadline: 
* DJ: 6. Juni 2018, 24h
* OK: 1. Juni 2018, 24h

**Aufgabenstellung durchlesen**

Typ: Individualarbeit

Aufwand: 10min

* Lese dir die gesamte Aufgabenstellung konzentriert durch und versuche sie komplett zu verstehen. Wenn es Fragen gibt, gemeinsam diskutieren und eventuell Lehrenden fragen.

**Inspizieren**

Typ: Individualarbeit

Ungefährer Aufwand: 20min

Schritte:
* Lade das Spreadsheet runter
* Benenne das Spreadsheet um in `aufgabe-3_NACHNAME.ods`.
* Inspiziere die Daten bezüglich folgender Eigenschaften:
  * Skalierungen
  * Komplettheit 
  * Korrektheit
* Dokumentiere die Skalierungstypen und Fehler des Datensatzes im Bericht.

Die offenen Datensets, die für das Erstellen der Datei verwendet wurden mitsamt Metadaten:
* [Ergebnis Nationalratswahl 2017](https://www.data.gv.at/katalog/dataset/3179c5b2-9bb5-4a7f-a573-5491ccb0110b)
* [Altersgruppen](https://www.data.gv.at/katalog/dataset/36f64070-396e-11e2-81c1-0800200c9a66)
* [Privathaushalte](https://www.data.gv.at/katalog/dataset/7dbf4579-f7f1-41e6-a881-aef68cc5d58b)
* [Nationalität](https://www.data.gv.at/katalog/dataset/6de28110-396f-11e2-81c1-0800200c9a66)

**Ergebnis Steiermark**


Typ: Individualarbeit


Ungefährer Aufwand: 25min


Schritte:
* Sieh dir die Metriken aller Merkmale zur *Nationalratswahl 2017 in der Steiermark* in der Datei [data/nrw17.ods](data/nrw17.ods) an: Min, Max, Range, Quartil 1, Mean, Quartil 3 und Median
* Überleg dir, was die Daten aussagen und dokumentiere dies im Bericht.

**Ergebnis Bezirk**


Typ: Individualarbeit


Ungefährer Aufwand: 20min


Schritte: 
* Wählt in der Gruppe einen Bezirk aus der Liste (Google Spreadsheet) aus. 
* Wähle eine Partei aus (jedeR in der Gruppe hat eine andere Partei).
* Berechne die Metriken der selbst-gewählten Partei zum *Ergebnis der Nationalratswahl 2017 im Bezirk der eigenen Gruppe*: Min, Max, Range, Quartil 1, Mean, Quartil 3 und Median. Erstelle die Berechnung in einem eigenen Worksheet (`BEZIRK_PARTEI`). 
* Versuche die Ergebnisse zu verstehen, und was sie über das Datenset aussagen.

Tipp: Zum Verstehen der Gemeindekennzahl am besten auf [Wikipedia](https://de.wikipedia.org/wiki/Amtlicher_Gemeindeschl%C3%BCssel#%C3%96sterreich) nachlesen.

**Sozio-ökonomische Daten**


Typ: Individualarbeit


Ungefährer Aufwand: 20min


Schritte:
* Wähle zwei sozio-ökonomische Merkmale aus dem Datenset aus (auch hier keine doppelten Auswahlen in der Gruppe).
* Berechne die Metriken zu den beiden Merkmalen für das Ergebnis im gewählten Bezirk: Min, Max, Range, Quartil 1, Mean, Quartil 3 und Median. Erstelle die Berechnung in je einem eigenen Worksheet. (`BEZIRK_MERKMAL`)
* Versuche die Ergebnisse zu verstehen, und was sie über das Datenset aussagen.

**Boxplots**


Typ: Gruppenarbeit


Ungefährer Aufwand: 30min


Schritte:
* Exportiere die Daten zur gewählten Partei und den beiden sozio-ökonomischen Merkmalen für den eigenen Bezirk als CSV-File.
* Gehe auf [boxplotr](http://bit.ly/boxplotr) und lade die Daten der drei Merkmale einzeln hoch.
* Wähle die passenden Einstellungen um die Daten bestmöglich als Boxplot darzustellen.
* Speichere die drei Boxplots als SVG-Datei und lade sie hoch.

### Abgaben

**aufgabe-3_boxplot_NACHNAME.csv**

* CSV Datei mit allen drei selbst-ausgewählten Merkmalen (1x Partei, 2x Sozio-ökonomisch) als Spalten.
* Trennzeichen: Komma
* Header-Zeile: Merkmals-Bezeichnung

**aufgabe-3_boxplot_MERKMAL_NACHNAME.svg**

* Je einen Boxplot zu den drei Merkmalen.
* Selbst-gewählte Darstellungsoptionen.

**aufgabe-3_bericht_NACHNAME.md**

* Gib die gewählte Partei und den Bezirk an.
* Liste die Skalierungsniveaus der einzelnen Merkmale auf (z. B. gkz = nominal).
* Beantworte folgende Fragen: Welche Aussage bezüglich der Wahl kann mit der zugrundeliegenden Datenbasis getroffen werden? Sind alle Daten vorhanden, um das Wahlverhalten in der Steiermark bei der NRW17 zu beschreiben? Sind dir irgendwelche Besonderheiten bzgl. des Datensets aufgefallen bzw. gab es etwas für dich Unerwartetes?
* Gib an, warum welche Einstellungen du warum beim Boxplot gewählt/nicht gewählt hast.

