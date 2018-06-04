# Übung #3

**[Folien](slides_aufgabe-2.pdf)**

* Abgabetermin Erste Version (für Feedback): 9. Juni 2018, 24h
* Abgabetermin Finale Version (wird beurteilt): 17. Juni 2018, 24h

## 3.1 Daten inspizieren

Den Datensatz mit den Ergebnissen zur Nationalratswahl 2017 in der Steiermark inspizieren.


Typ: Individualarbeit

Ungefährer Aufwand: 30min

#### 3.1.1 Datei runterladen

* Lade das Spreadsheet [data/nrw17.ods](../data/nrw17.ods) herunter.
* Benenne die Datei in `aufgabe-3_NACHNAME.ods` um. 
* Öffne die Datei in Libre Office Calc.
* Tipp: Verändere im Zuge der folgenden Aufgaben nichts in den beiden Worksheets "data" und "metrics". Besser du erstellst entweder neue Worksheets dazu oder kopierst die bestehenden um die Berechnungen durchzuführen oder Diagramme zu erstellen.

#### 3.1.2 Daten inspizieren

* Inspiziere die Daten im Worksheet "data" bezüglich folgenden Eigenschaften:
    * Welche Struktur haben die vorliegenden Daten?
    * Was wird in den Zellen gespeichert: Was stellt eine Zeile dar, was eine Spalte?
    * Welche Skalierung haben die Merkmale in den Spalten?
    * Sind die Daten komplett (alle Gemeinde-Ergebnisse der Steiermark)?
    * Sind die Daten korrekt?
    
#### 3.1.2 Ergebnisse dokumentieren

* Fasse die Ergebnisse aus der Inspektion in einem Bericht (`aufgabe-3_bericht_NACHNAME.md`) zusammen. Liste darin auf, um was es sich bei den einzelnen Merkmalen handelt, welchen Skalierungstyp sie haben und gehe auf die inspizierten Eigenschaften von oben ein.
* Verwende dazu als Vorlage [aufgabe-3_bericht_NACHNAME.md](templates/aufgabe-3_bericht_NACHNAME.md). Trage deinen Namen oben ein. Befülle die Merkmals-Tabelle und komplettiere die Punkte.
* Lade den Bericht in das GitHub Repository.

Als Grundlage für die Erstellung des Datensatzes wurden folgende offene Daten von [data.gv.at](http://data.gv.at/) verwendet. Diese und deren Metadaten können verwendet werden, um die Merkmale besser zu verstehen, falls nötig.

* [Ergebnis Nationalratswahl 2017](https://www.data.gv.at/katalog/dataset/3179c5b2-9bb5-4a7f-a573-5491ccb0110b)
* [Altersgruppen 1. 1. 2017](https://www.data.gv.at/katalog/dataset/36f64070-396e-11e2-81c1-0800200c9a66)
* [Privathaushalte 31. 12. 2014](https://www.data.gv.at/katalog/dataset/7dbf4579-f7f1-41e6-a881-aef68cc5d58b)
* [Nationalität 1. 1. 2017](https://www.data.gv.at/katalog/dataset/6de28110-396f-11e2-81c1-0800200c9a66)

**Ressourcen**

* Vorlesung: [Folien Daten](../vorlesung/slides_2-daten.pdf)
* Vorlesung: [Folien Daten nutzen](../vorlesung/slides_3-daten-nutzen.pdf)

## 3.2 Wahl-Metrik des Bezirkes berechnen

Berechnen der Wahl-Metrik für den Bezirk.

Typ: Individualarbeit


Ungefährer Aufwand: 30min

#### 3.2.1 Metriken berechnen

* Wählt in eurer Gruppe einen Bezirk im Google Spreadsheet aus.
* Wählt je Gruppen-Mitglied ein Merkmal zur Wahl aus. JedeR in der Gruppe hat ein anderes Merkmal, also nichts doppelt.
* Erstelle ein eigenes Worksheet mit dem Namen des Merkmals und des Bezirkes (`BEZIRK_MERKMAL`), in dem die Berechnungen gemacht werden. 
* Berechne die Metriken Min, Max, Range, Quartil 1, Median, Quartil 3 und Mean zum selbst-gewählten Wahl-Merkmal im selbst-gewählten Bezirk. Wähle alle benötigten Datenpunkte von Gemeinden aus eurem Bezirk aus. Beispiel: Ihr habt euch für Voitsdorf als Bezirk entschieden und du hast die relativen Stimmen der SPÖ (`spoe_rel`) als Merkmal ausgewählt. Dann musst du die Metriken zum SPÖ-Ergebnis in allen Gemeinden die in Voitsdorf liegen berechnen.
* Tipp: Am sichersten und einfachsten findest du deine Gemeinden über die Gemeindekennzahl. Diese beinhaltet an Stelle 2 und 3 den Bezirk (siehe [Wikipedia](https://de.wikipedia.org/wiki/Amtlicher_Gemeindeschl%C3%BCssel#%C3%96sterreich)).

#### 3.2.2 Metriken ansehen

* Sieh dir die Metriken an und versuche das Ergebnis zu verstehen.
* Such je 2-3 Gemeinden mit sehr kleinen, großen und durchschnittlichen Werten.
* Tipp: du kannst die Reihen nach den Zahlenwerten sortieren lassen (data -> sort).

#### 3.2.3 Ergebnisse dokumentieren

* Dokumentiere die repräsentativen Gemeinden für groß, klein und Durchschnitt im Bericht (`aufgabe-3_bericht_NACHNAME.md`). Führe die Ergebnisse der Metriken in der Metrik-Tabelle an. Gib statt MERKMAL den Namen des Merkmals an. Gib die gewählte Partei und den Bezirk an.

**Ressourcen**

* Vorlesung: [Folien Daten auswerten](../vorlesung/slides_4-daten-auswerten.pdf)
* Vorlesung: [Beispiele Metriken](../data/theorie/statistik_beispiele.ods)

## 3.3 Sozio-ökonomische Metriken des Bezirkes berechnen

Berechnen der sozio-ökonomischen Metriken für den Bezirk.

Typ: Individualarbeit


Ungefährer Aufwand: 30min

#### 3.3.1 Metriken berechnen

* Wählt je Gruppen-Mitglied zwei sozio-ökonomische Merkmale (Haushalt, Nationalität und Altersgruppen) aus. JedeR in der Gruppe hat ein anderes Merkmal, also nichts doppelt.
* Erstelle ein eigenes Worksheet mit dem Namen des Merkmals und des Bezirkes (`BEZIRK_MERKMAL`), in dem die Berechnungen gemacht werden. 
* Berechne auch dazu die Metriken Min, Max, Range, Quartil 1, Median, Quartil 3 und Mean zu beiden Merkmalen - wieder nur zu eurem Bezirk. Wähle alle benötigten Datenpunkte von Gemeinden aus eurem Bezirk aus.
* Erstelle die Berechnung in einem eigenen Worksheet mit dem Namen des Merkmals und Bezirkes (`BEZIRK_MERKMAL`). 

#### 3.3.2 Metriken ansehen

* Sieh dir die Metriken an und versuche das Ergebnis zu verstehen.
* Such je 2-3 Gemeinden mit sehr kleinen, großen und durchschnittlichen Werten.

#### 3.3.3 Ergebnisse dokumentieren

* Dokumentiere die repräsentativen Gemeinden für groß, klein und Durchschnitt im Bericht (`aufgabe-3_bericht_NACHNAME.md`). Führe die Ergebnisse der Metriken in der Metrik-Tabelle an. Gib statt MERKMAL den Namen des Merkmals an.

**Ressourcen**

* Vorlesung: [Folien Daten auswerten](../vorlesung/slides_4-daten-auswerten.pdf)

## 3.4 Boxplots

Erstelle die Boxplots zu den Merkmalen.

Typ: Individualarbeit


Ungefährer Aufwand: 45min

#### 3.4.1 Daten aufbereiten

* Erstelle ein neues Worksheet "boxplots".
* Kopiere die Gemeindekennzahlen sowie die Daten der drei Merkmale in das "boxplots" Worksheet rüber. Gib in der ersten Zeile die Bezeichnung der einzelnen Merkmale an (Header-Zeile).
* Exportiere das "boxplots" Worksheet als CSV-Datei (`aufgabe-3_boxplot_NACHNAME.csv`). Falls du nicht weißt wie das geht, versuche es selbständig mittels Internet-Suche raus zu finden, wie das in deiner Software geht. Als Trennzeichen das Komma verwenden, Header sind die Merkmals-Namen.

#### 3.4.2 BoxPlotR

* Gehe auf [BoxPlotR](http://bit.ly/boxplotr) und lade die Daten der drei Merkmale nacheinander einzeln hoch um je einen Boxplot zu erstellen. 
* Tipp: du kannst einfach die Daten mitsamt Header-Zeile auswählen und mit Copy/Paste auf Boxplotr einfügen. Dazu immer nur ein Merkmal mitsamt Header-Zeile (Spaltenname) auswählen und kopieren. Dann unter "Data Upload" in der linken Seitenleiste "Paste data" auswählen und die Daten in das Fenster rein kopieren. Du kannst aber auch die Daten jeweils einzeln in einer CSV-Datei speichern und diese dann hochladen (ist halt etwas umständlicher).
* Folgende Optionen auswählen: 
    * Add data points: aktivieren
    * Bee swarm: aktivieren
    * add sample means: aktivieren
* Speichere die drei Boxplots als SVG-Datei (`aufgabe-3_boxplot_MERKMAL_NACHNAME.svg`).

#### 3.4.3 Ergebnisse dokumentieren

* Sieh dir die Boxplots an und versuche das Ergebnis zu verstehen.
    * Ist die Datenverteilung symmetrisch oder skewed?
    * Ist die Box schmal oder breit im Vergleich zur Range?
    * Gibt es Outlier?
* Dokumentiere die Fragen in der Boxplot-Tabelle im Bericht (`aufgabe-3_bericht_NACHNAME.md`). Gib statt BOXPLOT den Namen des Merkmals an.
* Lade die drei Boxplots und den Bericht in das GitHub Repository.

**Ressourcen**

* Vorlesung: [Folien Daten auswerten](../vorlesung/slides_4-daten-auswerten.pdf)
