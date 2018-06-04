# Übung #2

**[Folien](slides_aufgabe-2.pdf)**

* Abgabetermin Erste Version (für Feedback): 9. Juni 2018, 24h
* Abgabetermin Finale Version (wird beurteilt): 17. Juni 2018, 24h

## 2.1. Review Datenrecherche

Berichte zur Datenrecherchen aus letzter Einheit reviewen und zusammenfassen.


Typ: Individual- und Gruppenarbeit


Ungefährer Aufwand: 

* Berichte lesen: 15min
* Diskutieren: 15min
* Bericht: 15min

#### 2.1.1 Berichte durchlesen

* Jedes Gruppenmitglied sucht sich die zugewiesenen Studierenden-Berichte über die Datenrecherche aus letzter Einheit im Google Spreadsheet raus.
* Suchen des Berichts der jeweiligen Person. Dazu die Gruppe der Person aus dem Gruppeneinteilungs-Spreadsheet raus suchen und dann im Abgaben-Ordner der Gruppe auf GitHub nachsehen. Es kann sein, dass der Dateiname nicht korrekt benannt wurde, dann die unbekannten Dateien durchgehen und nach dem Ersteller bzw. Uploader nachsehen.
* Lesen des Berichtes. 
* Die Schritte 2 + 3 für Person 1-3 wiederholen.

#### 2.1.2 Gruppendiskussion

* Nach den unterschiedlichen Recherchen, soll in der Gruppe über die verschiedenen Recherchewege und -erfahrungen diskutiert werden, um so eine Meta-Ebene zu erreichen.
* Folgende Fragen sind dabei zu diskutieren:
    * Welche Recherche-Strategien gab es?
    * zu gefundenen Datensets:
        * Waren die Metadaten ausreichend?
        * Wurden neue, euch unbekannte Datenquellen gefunden?
        * Wie verlief die Suche nach der UrheberInnenrechts-Lizenz?
    * zu nicht-gefundenen Datensets:
        * Was waren wiederkehrende Probleme bei der Suche?
        * Was waren die Vermutungen, warum Daten nicht gefunden werden konnten? Waren diese plausibel?
    * Wie war das Verhältnis zwischen gefundenen Daten und nicht gefundenen Daten?

Beachtet: Die Antworten müssen nachher im Bericht dokumentiert werden.

#### 2.1.3 Bericht verfassen

* Fasse die Diskussion aus Punkt 1.2 im Bericht kurz und bündig zusammen. Dies soll wieder in Form von Frage-Antwort-Paaren geschehen.
* Verwendet dazu als Vorlage [aufgabe-2_bericht.md](templates/aufgabe-2_bericht.md). Tragt euren Gruppennamen oben ein. Erstelle für jede Frage-Antwort-Kombination einen eigenen Absatz. Schreibe neben `Q` die Frage, und neben `A` die Antwort. Trenne jedes Frage-Antwort Paar durch drei Minus (`---`) darunter, um so eine Trennlinie zu erzeugen. 
* Upload der Datei (`aufgabe-2_bericht.md`) in das GitHub Repository.

**Resourcen:**

* Übung: [Beschreibung Aufgabe #1](UE_1-daten.md)
* Vorlesung: [Folien Daten](../vorlesung/slides_2-daten.pdf)

## 2.2. Peer Review Metadaten

Peer Review der JSON-Metadaten aus letzer Einheit mitsamt Beurteilung.


Typ: Individualarbeit


Ungefährer Aufwand: 

* 2 Reviews mitsamt Issue: 30min
* Email mit Beurteilung: 10min
* Bericht: 15min


#### 2.2.1 Peer Review mittels GitHub Issue

* Jedes Gruppenmitglied sucht sich die zugewiesenen Metadaten-Gruppen aus letzter Einheit im Google Spreadsheet raus.
* zu jeder Metadaten-Datei einen Review mittels GitHub Issue auf  dem LV Repository verfassen.
    * such dir die zugehörige `aufgabe-1_metadata.json` im GitHub Repository.
    * neues [Issue erstellen](https://github.com/skasberger/datenanalyse-ss18/issues/new)
    * wähle als `label` `peer-review` aus.
    * wähle als `project` die Gruppe, von welcher du die Metadaten reviewst, aus. Die Gruppen sind in dem Reiter `repository` zu finden.
    * Titel: "Metadaten Peer Review zu Gruppe GRUPPENNAME"
    * gib Feedback zu der `aufgabe-1_metadata.json`. Gehe dabei auf folgende Punkte ein (soweit sinnvoll):
        * Waren die Metadaten für dich ausreichend, um das Datenset zu verstehen? 
    	* Sind die Key-Value Paare gut gewählt bzw. korrekt?
        * Mindestens eine Sache die gut gemacht wurde angeben.
        * Mindestens eine Verbesserungsmöglichkeit angeben.
        * Link zur Metadaten-Datei.
        * Mentioning der Accounts aller Gruppenmitglieder der Gruppe, zu welcher man die Metadaten gerieviewed hat. Dadurch bekommen alle die Info zum Review vermittelt.
    	* Beachte: Gib konkrete Beispiele an, statt pauschale Urteile. Beispiel: "Mir hat das Key-Value Paar `license_uri` gefallen, da dies das auffinden der UrheberInnenrechts-Lizenz vereinfacht und die verwendete Lizenz klar macht", anstatt Aussagen wie "die Metadaten sind gut". -> Warum sind sie gut?
    	* Beachte: **freundliche, konstruktive Sprache verwenden**.
    	* Als Hilfe werden die [Aufgabenbeschreibung Übung #1](UE_1-daten.md) und [Vorlesungs-Folien zu Daten](../vorlesung/slides_2-daten.pdf) empfohlen.

#### 2.2.2 Peer Grading via Email

* Überleg dir eine Note für jede Metadaten-Aufgabe, die du gereviewed hast. Ziehe folgende Punkte als Kriterien dazu heran:
  * Wieviel Information hast du aus den Metadaten über das Datenset erhalten, um es selber verwenden zu können?
  * Sind die Key-Value Paare gut gewählt bzw. korrekt?
  * War die Datei korrekt benannt?
  * Wie umfangreich sind die Metadaten?
  * Handelt es sich um valides JSON?
* Tipp: Zuerst alle Gruppenarbeiten ansehen, und dannach erst die Beurteilung durchführen, so dass alle gleich beurteilt werden.
* Sende folgende Infos zu jeder Beurteilung an edu@stefankasberger.at:
   * Betreff: Benotung LV Datenanalyse, Aufgabe #2
   * deinen Namen
   * Gruppenname
    * Beurteilung (Sehr Gut bis Nicht Genügend)
   * Link Issue

Was nicht dabei sein soll: die Begründung der Note.

#### 2.2.3 Bericht Peer Review und Peer Grading

* Verfasse einen kurzen, persönlichen Text mit ~200 Wörter (`aufgabe-2_bericht_NACHNAME.md`) mit den Erfahrungen zum Peer Review und Peer Grading. Gehe dabei auf folgende Punkte ein.
    * Wie war die Erfahrung des Peer Reviews für dich (nicht der Beurteilung)?
    * Hast du von den Anderen etwas gelernt? 
    * Wie ist es dir bei der Beurteilung gegangen?
    * Gab es Schwierigkeiten beim Review bzw. beim Beurteilen?
* Links zu den Issues an.
* Verwende dazu als Vorlage [aufgabe-2_bericht_NACHNAME.md](templates/aufgabe-2_bericht_NACHNAME.md). Trag deinen Namen oben ein.
* Upload des Berichtes in das GitHub Repository.

**Resourcen:**

* Übung: [Beschreibung Aufgabe #1](UE_1-daten.md)
* Vorlesung: [Folien Daten](../vorlesung/slides_2-daten.pdf)
* Vorlesung: [Metadaten Umfrage Herrengasse](../data/theorie/metadata_umfrage-herrengasse.json)
* Vorlesung: [Metadaten Wetterstation](../data/theorie/metadata_wetterstation.json)
* [Was ist eine JSON-Datei?](https://de.wikipedia.org/wiki/JavaScript_Object_Notation)
* [Wikipedia: Metadaten](https://de.wikipedia.org/wiki/Metadaten)
