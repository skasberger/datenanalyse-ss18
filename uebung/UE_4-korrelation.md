# Übung #4

**[Folien](slides_aufgabe-4.pdf)**

* Abgabetermin Erste Version (für Feedback): 9. Juni 2018, 24h
* Abgabetermin Finale Version (wird beurteilt): 17. Juni 2018, 24h

## 4.1 Korrelation ansehen

Berechnen der Korrelation mitsamt Scatterplot zu den ausgewählten Merkmalen im Bezirk.
 

Typ: Individualarbeit


Ungefährer Aufwand: 30min

#### 4.1.1. Korrelationen berechnen

* Erstelle ein eigenes Worksheet mit dem Namen "korrelation", in dem die folgenden Aufgaben umgesetzt werden. 
* Berechne den Korrelations-Koeffizienten zwischen den drei Merkmals-Kombinationen (Korrelation zwischen Merkmal 1 & 2, 1 & 3, 2 & 3) für euren Bezirk. Wähle dazu alle benötigten Datenpunkte der Gemeinden aus eurem Bezirk aus, bzw. kopiere sie in das Worksheet.
* Tipp: Du findest den Befehl um den Korrelations-Koeffizienten in Libre Office zu berechnen in den Beispielen aus der Vorlesung. Sonst kannst du auch im Internet danach suchen. 
* Wandle das quantitative Ergebnis des Korrelations-Koeffizienten in die qualitative Stärke der Korrelation um (siehe Folien Vorlesung). 

#### 4.1.2. Scatterplots erstellen

* Erstelle zu jeder Merkmals-Kombination einen Scatterplot in Libre Office. Dies kann ebenfalls im "korrelations" Worksheet gemacht werden.
* Beachte: Bennen die Achsen korrekt nach den Merkmalen und wähle einen beschreibenden Titel für das Diagramm. 
* Füge eine Regressions-Gerade hinzu. Dazu auf das Diagramm bzw. auf einen Datenpunkt klicken, bis sich dessen Darstellung verändert. Dann einen Rechts-Klick auf einen Datenpunkt und im Drop-Down Menü das hinzufügen der Trend-Linie auswählen (oder so ähnlich, je nach Sprache. 
* Exportiere die drei Plots als PNG-Datei (`aufgabe-4_scatterplot_NACHNAME_MERKMAL_MERKMAL.png`). Dazu Rechts-Klick auf das Bild und "Exportieren als Grafik..." wählen
* Tipp: Falls du die Funktionen nicht gleich findest, oder es mit einer anderen Software arbeitest, suche im Internet nach einer passenden Lösung.
* Lade die drei Grafiken auf GitHub hoch.
* Dokumentiere den Zusammenhang im Bericht (`aufgabe-4_bericht_NACHNAME.md`).

#### 4.1.3. Bericht schreiben

* Beantworte folgende Frage: Scheint dir der gefundene Zusammenhang zwischen den Merkmalen plausibel? Beschreibe in eigenen Worten wieso bzw. wieso nicht?
* Beachte: Es kann sich hier nur um erste Vermutungen handeln, da wir keine statistischen Tests oder eine tiefergehende Recherche durchgeführt haben, welche dies überprüfen würden.
* Dokumentiere deine Vermutungen zu den Zusammenhängen im Bericht (`aufgabe-4_bericht_NACHNAME.md`). Gib statt MERKMAL in den Überschriften den Namen der Merkmale an und ändere so die Überschriften ab. Gib weiters die Stärke der Korrelation, den Korrelations-Koeffizienten sowie die Richtung der Korrelation (positiv/negativ) an.
* Verwende dazu als Vorlage [aufgabe-4_bericht_NACHNAME.md](templates/aufgabe-4_bericht_NACHNAME.md). Trage deinen Namen oben ein. Befülle die Korrelations-Tabelle mit den Ergebnissen. Gib dabei den Namen der Merkmale statt "MERKMAL" an.
* Lade den Bericht in das GitHub Repository hoch.

**Resourcen**

* Vorlesung: [Folien Daten auswerten](../vorlesung/slides_4-daten-auswerten.pdf)
* Vorlesung: [Beispiele Korrelation](../data/theorie/korellation_beispiele.ods)

## 4.2 Aufgaben updaten

Vergangene Aufgaben aktualisieren bzw. komplettieren.


Typ: Individualarbeit


Ungefährer Aufwand: 90min

* Lies dir die Angaben zu den einzelnen Aufgaben noch einmal durch.
* Finalisiere die bisherigen Aufgaben, wenn noch nicht fertig.
* Sieh dir die Issues zu deiner/eurer Arbeit bei der ersten Aufgabe an, welche im Zuge des Peer Reviews erstellt wurden.
* Sieh die dir ein paar Abgaben der anderen Studierenden bzw. Gruppen an.
* Aktualisiere deine bzw. eure Abgaben.

## 4.3 Interpretation 

Interpretieren und zusammen fügen der einzelnen Ergebnisse aus der Datenanalyse.

Typ: Gruppenarbeit


Ungefährer Aufwand: 60min

* Seht euch die Ergebnisse eures Bezirkes sowie jene der gesamten Steiermark an. Vergleicht die Ergebnisse um so zu Aussagen wie "Der Bezirk XYZ hat überdurchschnittlich viele 3 Personen Haushalte im Vergleich zur restlichen Steiermark" zu bekommen. Tipp: sieh dir die [Boxplots der Merkmale für die Steiermark](img/) bzw. die Verteilungen der Daten an.
* Versucht repräsentative Gemeinden für eure Geschichte zu finden: Seht euch Gemeinden an, die nahe am Mittelwert liegen, sowie welche mit sehr kleinen und sehr großen Werten an (vor allem Outlier!). Haltet dabei Ausschau nach Gründen, warum diese Gemeinden extrem bzw. durchschnittlich sind.
* Bei der Korrelation: Ist der Zusammenhang stark bzw. scheint er plausibel?
* Versuche die gesamelten Informationen in eine "Geschichte" zusammen zu fassen. Denkt die gesamte Datenanalyse zusammen - von Daten inspizieren über die Metriken mitsamt Boxplots bis zu den Korrelationen: Was habt ihr durch eure Datenanalyse über die Demographie und das Wahlverhalten in eurem Bezirk raus gefunden? 
* Beantworte folgende Frage:
  * Welche Aussagen können mit der Datenbasis von den Bezirksgemeinden getroffen werden?
* Dies als journalistischen Artikel (~200 Wörter, `aufgabe-4_bericht.md`) kurz und knackig nieder schreiben und die nötigen Grafiken dazu verlinken. Wählt wenn hilfreich einen Boxplot oder einen Scatterplot aus, welche eure Interpretation untermauert. Bei den Aufgaben geht es darum, das ihr die Daten und die grundlegenden Ergebnisse der Analysen korrekt lest und interpretiert, nicht ob die Aussagen wissenschaftlich oder journalistisch gesehen absolut korrekt sind. Da wir keine statistischen Tests oder eine tiefergehende journalistische Recherche gemacht haben, macht nicht den Fehler definitive Aussagen zu treffen. Verwendet Formulierungen wie "Der Bezirk XYZ hat überdurchschnittlich viele 2 Personen Haushalte" oder "es könnte einen negativen/indirekten Zusammenhang zwischen der Anzahl an ausländischen Staatsbürgern und den Stimmen für die FPÖ geben", "Ein gutes Beispiel für eine Gemeinde mit sehr wenig Stimmen für die Grünen ist die ländliche Gemeinde XYZ", "Dies könnte an XYZ liegen". Verwendet das Konjunktiv bzw. unbestimmte Formulierungen, solange ihr euch nicht sicher seit.

**Ressourcen**

* Vorlesung: [Folien Daten](../vorlesung/slides_2-daten.pdf)
* Vorlesung: [Folien Daten nutzen](../vorlesung/slides_3-daten-nutzen.pdf)
* Vorlesung: [Folien Daten auswerten](../vorlesung/slides_4-daten-auswerten.pdf)

## 4.4 Präsentation erarbeiten

Ausarbeiten der Abschluss-Präsentation.


Typ: Gruppenarbeit


Ungefährer Aufwand: 60min


Näheres siehe [Aufgabe](UE_5-praesentation.md).

