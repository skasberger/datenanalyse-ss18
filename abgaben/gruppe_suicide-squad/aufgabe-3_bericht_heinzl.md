Aufgabe 3: Daten inspizieren (04. Juni 2018)
======================================================================

# Daten inspizieren
## Welche Struktur haben die vorliegenden Daten?
Hierbei handelt es sich um strukturierte Daten

## Was wird in den Zellen gespeichert: Was stellt eine Zeile dar, was eine Spalte?
Die Zeilen stellen die unterschiedlichen Bezirke der Steiermark dar und die Spalten verschiedene Angaben zur Wahl wie etwa (un)gültige Stimmen, Unterscheidung nach Parteien oder Altersgruppen. 

## Welche Skalierung haben die Merkmale in den Spalten?
Siehe Tabelle unten.

## Sind die Daten komplett (alle Gemeinde-Ergebnisse der Steiermark)?
Siehe unten.

## Sind die Daten korrekt?
Siehe unten.

Name: Anna Heinzl
Partei: Grüne
Bezirk: Südoststeiermark


## Inspizieren

Struktur: strukturiertes Datenset in Form einer Tabelle

Merkmale: gruene_rel, 0_14_rel, 15_29_rel

| Merkmal | Inhalt | Skalierung |
|---------|---------|----------------|
| gkz | Gemeindekennzahlen | Ordinalskala |
| gemeinde |Gemeindenamen | Nominalskala |
| wahlberechtigt_abs | Wahlberechtigte Personen in absoluten Zahlen | Verhältnisskala |
| abgegeben_abs | Abgegebene Stimmen in absoluten Zahlen | Verhältnisskala |
| ungueltig_rel | Ungültige Stimmen in relativen Zahlen | Verhältnisskala |
| gueltig_abs | Gültige Stimmen in absoluten Zahlen | Verhältnisskala |
| spoe_rel | Stimmen für die SPÖ in relativen Zahlen | Verhältnisskala |
| oevp_abs |Stimmen für die ÖVP in absoluten Zahlen | Verhältnisskala |
| fpoe_rel | Stimmen für die FPÖ in relativen Zahlen | Verhältnisskala |
| gruene_rel | Stimmen für die Grünen in relativen Zahlen | Verhältnisskala |
| 0_14_rel | Anzahl der Personen der Altersgruppe 0 bis 14 Jahre in relativen Zahlen | Verhältnisskala |
| 15_29_rel | Anzahl der Personen der Altersgruppe 15 bis 29 Jahre in relativen Zahlen | Verhältnisskala |
| 30_44_rel | Anzahl der Personen der Altersgruppe 30 bis 44 Jahre in relativen Zahlen | Verhältnisskala |
| 45_59_rel | Anzahl der Personen der Altersgruppe 45 bis 59 Jahre in relativen Zahlen | Verhältnisskala |
| 60_74_rel | Anzahl der Personen der Altersgruppe 60 bis 74 Jahre in relativen Zahlen | Verhältnisskala |
| 75_abs | Anzahl der Personen der Altersgruppe ab 75 Jahren in absoluten Zahlen | Verhältnisskala |
| 1p_rel | Anzahl der Privathaushalte mit 1 Person in relativen Zahlen| Verhältnisskala |
| 2p_rel | Anzahl der Privathaushalte mit 2 Personen in relativen Zahlen | Verhältnisskala |
| 3p_abs | Anzahl der Privathaushalte mit 3 Personen in absoluten Zahlen | Verhältnisskala |
| 4p_rel | Anzahl der Privathaushalte mit 4 Personen in relativen Zahlen | Verhältnisskala |
| 5p_rel | Anzahl der Privathaushalte mit 5 Personen in relativen Zahlen| Verhältnisskala |
| oesterreich_abs | Bewohner mit österreichischer Staatsangehörigkeit in absoluten Zahlen | Verhältnisskala | 
| ausland_rel |Bewohner mit ausländischer Staatsangehörigkeit in relativen Zahlen| Verhältnisskala |

Komplett: Es fehlen Parteien (Bsp. Grüne, Neos, Liste, Pilz), außerdem wurde nicht zwischen männlichen und weiblichen Wähler unterschieden und die Ausbildung der Wähler ist ebenso nicht angegeben. Die absoluten Zahlen könnte man zusätzlich noch in relativen Zahlen anführen und umgekehrt. Ansonsten ist der Datensatz komplett.

Korrekt: Der Datensatz scheint korrekt. 
 
 
## Metriken

| Metrik | gruene_rel | 0_14_rel | 15_29_rel |
|--------|------------|----------|------------|
| Min | 0,27 | 10,61 | 12,12 |
| Max | 2,71 | 15,96 | 17,67 |
| Range | 2,44 | 5,35 | 5,55 |
| Q1 | 1,035 | 12,2125 | 15,2475 |
| Median | 1,345 | 13,19 | 15,78 |
| Q3 | 1,7975 | 14,1775 | 16,41 |
| Mean | 1,353077 | 13,2288462 | 15,6130769 |


## Merkmal 

Liste je 2-3 Gemeinden mit kleinem, durchschschnittlichem und großem Zahlenwert auf.

| Merkmal | Klein | Durchschnitt | Groß |
|---------|-------|--------------|------|
| gruen_rel | Unterlamm, Murfeld, Tieschen | Riegersburg, Bad Gleichenberg, Kirchbach-Zerlach | Edelsbach bei Feldbach, Mureck, Deutsch Goritz|
| 0_14_rel | Halbenrain, Sankt Anna am Aigen, Bad Radkersburg| Edelsbach bei Feldbach, Kirchbeach-Zerlach, Bad Gleichenberg |Pirching am Taubenberg, Kapfenberg, Eichkögl |
| 15_29_rel | Bad Radkersburg, Tieschen, Klöch| Jagerberg, Mureck, Straden | Edelsbach bei Feldbach, Feldbach, Gnas|



## Boxplot

Gib zu den Eigenschaften Symmetrie, Box-Range Verhältnis und Outlier kurz an, was du gefunden hast.

| Eigenschaft | gruene_rel | 0_14_rel | 15_29_rel |
|-------------|---------|---------|---------|
| Symmetrie | ja, sehr symmetrisch | ja, ziemlich symmetrisch| ja, relativ symmetrisch |  
| Box:Range Verhältnis | sieht normalverteilt aus; Median liegt genau in der Mitte; 50 % der Daten liegt in einem recht engen Verhältnis, das bedeutet eine steile Glockenkurve (peak) | der Median liegt in der Mitte; Box-Range ist der Abstand fast gleich groß, die Daten also normalverteilt; die Box ist schmal, das bedeutet die Daten sind stark zentriert (peak) |die Box ist recht eng, das bedeutet, dass rund 50 % der Daten eng beieinander liegen; die gesamte Box und der Median sind skewed rechts | 
| Outlier | keiner vorhanden | keiner vorhanden |ja, zwei Outlier links vorhanden | 




