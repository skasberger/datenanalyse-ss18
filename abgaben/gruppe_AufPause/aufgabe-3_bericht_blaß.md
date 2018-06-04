# Aufgabe 3 

----
## Nationalratswahlen 2017: Bericht
Name: Katrin Blaß 

Ich habe folgende Partei ausgewählt: Die Grünen

Analysierter Bezirk: Voitsberg




----
## 1) Daten inspizieren
**Welche Struktur haben die vorliegenden Daten?**

Die zu verarbeitenden Daten werden in einer Tabelle dargestellt. 

**Was wird in den Zellen gespeichert: Was stellt eine Zeile dar, was eine Spalte?**

Jede Gemeinde hat ihre eigene Zeile. Hier werden die zugehörigen Daten angegeben. Insgesamt setzt sich der Bezirk Voitsberg aus 15  Gemeinden zusammen. Das bedeutet, es gibt auch 15 Zeilen. In den Spalten 

Die 15 Gemeinden sind: 

Krottendorf-Gaisfeld, Ligist, Mooskirchen, Rosental an der Kainach, Sankt Martin am Wöllmißberg, Stallhofen, Voitsberg, Bärnbach, Edelschrott, Geistthal-Södingberg, Hirschegg-Pack, Kainach bei Voitsberg, Köflach, Maria Lankowitz, Söding-Sankt Johann

**Welche Skalierung haben die Merkmale in den Spalten?**

Ordinalskaliert: Gemeindekennzahlen, Namen der Gemeinden

Verältnisskaliert: Wahlberechtigte, Stimmenverteilung (gewählte Partei, Stimmenanzahl, gültige und ungültige Stimmen)

Nominalskaliert: Parteiauflistung



**Sind die Daten komplett (alle Gemeinde-Ergebnisse der Steiermark)?**

Im Datensatz differenziert man nicht nach Geschlecht - männlich und weiblich wird nicht angegeben. Es gibt auch keine Angaben zum Bildungsgrad der befragten Personen. 
Weiters fehlen die Parteien NEOS, die Liste Pilz und alle weiteren Kleinparteien.  


**Sind die Daten korrekt?**

Ja, die Daten sind korrekt. 



----
## 2) Wahl-Metriken des Bezirkes berechnen





| Metrik | grüne_rel | Altersgruppe (15-29 Jahre) | 1P_rel|
|--------|---------|---------|---------|
| Min |  0,11 |14,77  | 22,33  |
| Max | 2,08 | 17,06 | 38,95 |
| Range |  1,97 | 2,29 |  16,62 |
| Q1 |0,86|  15,23| 25,06 |
| Median |1,13  | 15,45| 28,43 |
| Q3 |1,51|  15,82| 33,10 |
| Mean | 1,15 | 15,55 | 29,35 |



## 3) Merkmale
Liste die Gemeinde mit kleinem, durschschnittlichem und großem Zahlenwert auf.

| Merkmal | Klein | Durchschnitt | Groß |
|---------|-------|--------------|------|
| grüne_rel | Geistthal-Södingberg | Köflach| Ligist |
| Altersgruppe (15-29 Jahre) | Stallhofen | Sankt Martin am Wöllmißberg | Rosental an der Kainach |
| 1-Personenhaushalt | Stallhofen | Limits | Köflach |





## 4) Boxplots Ergebnisse

Gib zu den Eigenschaften Symmetrie, Box-Range Verhältnis und Outlier kurz an, was du gefunden hast.

| Eigenschaft | grüne_rel | Altersgruppe (15-29) | 1P_rel |
|-------------|---------|---------|---------|
| Symmetrie | annähernd symmetrisch | nein | nein |
| Box:Range Verhältnis | normal | schmal | breit |
| Outlier | nein | nein | nein |




