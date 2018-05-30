**[Folien](uebung/slides_aufgabe-2.pdf)**

## Abgabe EH 3

### Todo

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
  * Überlegen: Was wird in den Zellen gespeichert: Was stellt eine Zeile dar, was eine Spalte?
  * Skalierungen
  * Komplettheit 
  * Korrektheit
* Dokumentiere die Skalierungstypen und Fehler des Datensatzes im Bericht.

Die offenen Datensets, die für das Erstellen der Datei verwendet wurden mitsamt Metadaten:
* [Ergebnis Nationalratswahl 2017](https://www.data.gv.at/katalog/dataset/3179c5b2-9bb5-4a7f-a573-5491ccb0110b)
* [Altersgruppen 1. 1. 2017](https://www.data.gv.at/katalog/dataset/36f64070-396e-11e2-81c1-0800200c9a66)
* [Privathaushalte 31. 12. 2014](https://www.data.gv.at/katalog/dataset/7dbf4579-f7f1-41e6-a881-aef68cc5d58b)
* [Nationalität 1. 1. 2017](https://www.data.gv.at/katalog/dataset/6de28110-396f-11e2-81c1-0800200c9a66)

**NRW17 Steiermark**


Typ: Individualarbeit


Ungefährer Aufwand: 25min


Schritte:
* Sieh dir die Metriken aller Merkmale zur *Nationalratswahl 2017 in der Steiermark* in der Datei [data/nrw17.ods](../data/nrw17.ods) an: Min, Max, Range, Quartil 1, Mean, Quartil 3 und Median
* Überleg dir, was die Ergebnisse der Metriken über die Daten aussagen und dokumentiere dies im Bericht.

**NRW17 Bezirk: Wahl-Daten**


Typ: Individualarbeit


Ungefährer Aufwand: 20min


Schritte: 
* Wählt in der Gruppe einen Bezirk aus der Liste (Google Spreadsheet) aus. 
* Wähle ein Merkmal der Wahl (Partei, Wahlberechtigt, Abgegebene Stimmen, Gültig, Ungültig) aus (jedeR in der Gruppe hat eine andere Partei).
* Berechne die Metriken des selbst-gewählten Merkmals zum *Ergebnis der Nationalratswahl 2017 im Bezirk der eigenen Gruppe*: Min, Max, Range, Quartil 1, Mean, Quartil 3 und Median. Erstelle die Berechnung in einem eigenen Worksheet (`BEZIRK_PARTEI`). 
* Versuche die Ergebnisse zu verstehen, und was sie über das Datenset aussagen.

Tipp: Zum Verstehen der Gemeindekennzahl am besten auf [Wikipedia](https://de.wikipedia.org/wiki/Amtlicher_Gemeindeschl%C3%BCssel#%C3%96sterreich) nachlesen.

**NRW17 Bezirk: Sozio-ökonomische Daten**


Typ: Individualarbeit


Ungefährer Aufwand: 20min


Schritte:
* Wähle zwei sozio-ökonomische Merkmale aus dem Datenset aus (auch hier keine doppelten Auswahlen in einer Gruppe).
* Berechne die Metriken zu den beiden Merkmalen für das Ergebnis im gewählten Bezirk: Min, Max, Range, Quartil 1, Mean, Quartil 3 und Median. Erstelle die Berechnung in je einem eigenen Worksheet. (`BEZIRK_MERKMAL`)
* Versuche die Ergebnisse zu verstehen, und was sie über das Datenset aussagen.

**Boxplots**


Typ: Gruppenarbeit


Ungefährer Aufwand: 30min


Schritte:
* Exportiere die Daten zur gewählten Partei und den beiden sozio-ökonomischen Merkmalen für den eigenen Bezirk als CSV-File.
* Gehe auf [boxplotr](http://bit.ly/boxplotr) und lade die Daten der drei Merkmale einzeln hoch. Findet selbstständig einen Weg, wie ihr die Daten aus eurem Spreadsheet in den Web-Service bekommt, so dass ein Boxplot dargestellt wird.
* Wähle die passenden Einstellungen um die Daten bestmöglich als Boxplot darzustellen.
* Speichere die drei Boxplots als SVG-Datei und lade sie hoch.

### Abgaben

* Abgabetermin Erste Version (für Feedback): 9. Juni 2018, 24h
* Abgabetermin Finale Version (wird beurteilt): 17. Juni 2018, 24h

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
* Gib die Ergebnisse der Metriken an.

