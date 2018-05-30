# Bericht zur Einheit 3

## Partei: FPÖ
## Bezirk: Hartberg-Fürstenfeld

### Skalierungsniveaus:

* gkz = Nominalskala
* wahlberechtigt = Verhältnisskala
* abgegenen = Verhälnisskala
* ungültig = Verhältnisskala
* Partien = Verhälnisskala
* Altersgruppen = Verhälnisskala
* Personen / Haushalt = Verhältnisskala
* Nationalität = Verhälnisskala

__Zusammenfassung:__ Es handelt sich (mit Außnahme der gkz) um
Verhälnissskalen, da alle rechnerischen Operationen ausgeführt
werden können und es sich um quantitative Daten handelt.


### Korrektheit und Vollständigkeit des Datensatzes:

#### Prüfung auf Korrektheit anhand von Summenformel im Libre und Vergleichen mit
der Gesamtanzahl im Bezirk:

* Wahlberechtigte: korrekt
* abgegeben: Gesamtzahl (61757) weicht von Summe (54484) ab
* ungültig: Gesamtzahl (609) weicht von Summe (565) ab
* gültig: Gesamtzahl (61148) weicht von Summe (53919) ab
* spö: Gesamtzahl (10178) weicht von Summe (8796) ab
* övp: Gesamtzahl (24319) weicht von Summe (21520) ab
* fpö: Gesamtzahl (20766) weicht von Summe (18792) ab
* grüne: Gesamtzahl (1132) weicht von Summe (850) ab

__Zusammenfassung:__ Die zusammengerechneten Summenergebnisse der gültigen und ungültigen Stimmen 
ergeben allerdings die korrekte Gesamtzahl der abgegebenen Stimmen. Dies beruft
sich auf die Briefwahlstimmen.

#### Prüfung auf Gesamtheit des Datensatzes:

Es werden zum Beispiel nicht alle Parteien angegeben, die zur Wahl
angetreten sind. Es fehlen: Liste Gilt, Liste Pilz, KPÖ, Weiße, FLÖ, NBZ, ODP,
SLP, EUAUS, CPÖ, M, Neos;


### Interpretation der Metriken der Gesamtsteiermark:

* Wahlberechtigte: min = vieviel der Minimalwert der Wahlberechtigten in den steirischen 
		Gemeinden ist. max = Höstwert der Wahlberechtigten. range = Differenz 
		zwischen Maximal und Minimal. Quartil 1 = 25% der Gemeinden weniger oder
		oder gleich 1289 Wahlberechtigte haben. Quartil 3 = 25% der Gemeinden größer
		oder gleich  2359 Wahlberechtigte haben. Mean = Mittelwert der Wahlberechtigten
		pro Gemeinde in der Steiermark. Median = 1948 zeigt, dass 50% der Gemeinden weniger als diese
		Zahl an Wahlberechtigten haben und 50% der Gemeinden mehr als diese Zahl an 
		Wahlberechtigten haben.

* Abgegebene Stimmen: Quasi dasselbe wie im obrigen Beispiel. Der min zeigt den kleinsten Wert
		an abgebenen Stimmen an, der max die Höchstanzahl an abgegebenen Stimmen einer 
		Gemeinde in der Steiermark. Die Range ist die Differenz zwischen min und max.
		Q1 und Q3 zeigen jeweils wieder, dass weniger oder gleich 25% (Q1) bzw. mehr oder gleich
		25% (Q3) unter bzw über gleich diesem Wert sind. Mean ist wieder der arythmetische 
		Durchschnitt und der Median zeigt an, dass 50% der Gemeinden weniger als diese
		Zahl an Wahlberechtigten haben und 50% der Gemeinden mehr als diese Zahl an 
		Wahlberechtigten haben.

* Ungültig/Gültig: Wieder dasselbe. min zeigt den minimalen, max den maximalen der gültigen bzw ungültigen
		Stimmen. Range wieder die Differenz der min und max Werte. Q1 zeigt, dass 25% der Gemeinden
		weniger oder gleich 3673 (gültig) 31 (ungültig) gewählt haben, während Q3 zeigt, dass 25%
		der Gemeinden größer oder gleich 2341 (gültig) 21 (ungültig) gewählt haben. Der Mean gibt den Mittelwert
		der jeweils gültig/ungültig abgegebenen Stimmen an und der Median zeigt, dass 50% der Gemeinden
		jeweils über oder unter diesem Wert gültig/ungültig gewählt haben.

* ...für die Metriken der Parteien, Altersklassen, Haushaltszugehörigkeiten und Nationalitäten gelten prinzipiell
dieselben Regeln.

## Beantwortung der Fragen

### Welche Aussage bezüglich der Wahl kann mit der zugrundeliegenden Datenbasis getroffen werden?

* Welche Partei hat die Wahl gewonnen
* In welchem Bezirk wurde wie gewählt
* Wieviele Wahlberechtigte gab es 
* Wieviele Stimmen wurden (gültig + ungültig) abgegeben
* Wie wirkt sich das Alter auf das Wahlverhalten aus
* Wie wirkt sich Österreich/Ausland auf das Wahlverhalten aus
* Wie wirkt sich die Anzahl der Personen im Haushalt auf das Wahlverhalten aus
* Wieviele Briefwahlstimmen gab es (siehe Begründung oben)

### Sind alle Daten vorhanden, um das Wahlverhalten in der Steiermark bei der NRW17 zu beschreiben?

Prinzipiell ja. Man könnte noch weitere Faktoren wie zB. den Bildungsgrad, die Geschlechterverteilung und das Beschäftigungsverhältnis in den Datensatz aufnehmen, um noch genauere Interpretationen zu bekommen, aber für eine generelle Analyse des Wahlverhaltens der SteirerInnen reichen die angegebenen Daten durchaus aus. Die wichtigsten Daten empfinde ich hierbei die Ergebnisse auf Gemeindeebene, also in welcher Gemeinde welche Partei wie häufig gewählt wurde.

### Sind dir irgendwelche Besonderheiten bzgl. des Datensets aufgefallen bzw. gab es etwas für dich Unerwartetes?

Ja. Beim Summenzählen sind uns in jedem Bereich (bis auf die Zahlen der Wahlberechtigten) unterschiede zwischen der angegebenen Gesamtzahl und eben der Summe der Werte aufgefallen. Diese Unterschiede sind auf die Wahlkarten-Wähler zurückzuführen, da diese nicht pro Gemeinde ausgezählt werden.

### Welche Einstellungen hast du für den Boxplot gewählt und warum?

Die Boxplots sind vertikal, da sich der Boxplot so schön abzeichnet und man auch die Ausreißer gut erkennen kann.


## Ergebnisse der Metriken

### Partei FPÖ:
* min: 166
* max: 1443
* range: 1277
* mean: 522
*Q1: 311,25
* Median: 427
* Q3: 616

### 1-Personen-Haushalte:
* min: 60
* max: 1503
* range: 1443
* mean: 255,027
* Q1: 123,75
* Median: 176
* Q3: 273,5

### 30-44 Jahre:
* min: 152
* max: 1591
* range: 1439
* mean: 486,333
* Q1: 272,75
* Median: 406
* Q3: 521,25
