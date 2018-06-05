Name: Laura Reibenschuh

Partei: FPÖ

Bezirk: Leibnitz

## Inspizieren

Struktur: Die Daten sind als Excel-Tabelle, also sturkturiert vorhanden.

Merkmale:

| Merkmal | Inhalt | Skalierung |
|---------|---------|----------------|
| gkz | Gmeindekennzahl der Gemeinde | Ordinalskala |
| gemeinde | Gemeindename | Nominalskala |
| wahlberechtigt_abs | Absolute Anzahl der Wahlberechtigten | Verhältnisskala |
| abgegeben_abs | Absolute Anzahl der abgegebenen Stimmen | Verhältnisskala |
| ungueltig_rel | Relative Anzahl der ungültigen Stimmen | Verhältnisskala |
| gueltig_abs | Absolute Anzahl der gültigen Stimmen | Verhältnisskala |
| spoe_rel | Relativer Anteil der Stimmen fuer die SPÖ | Verhältnisskala |
| oevp_abs | Absoluter Anteil der Stimmen fuer die ÖVP | Verhältnisskala |
| fpoe_rel | Relativer Anteil der Stimmen fuer die FPÖ | Verhältnisskala |
| gruene_rel | Relativer Anteil der Stimmen fuer die Grünen | Verhältnisskala |
| 0_14_rel | Relativer Anteil der 0- bis 14- Jährigen in der Gemeinde an der Gesamteinwohnerzahl der Gemeinde | Verhältnisskala |
| 15_29_rel | Relativer Anteil der 15- bis 29- Jährigen in der Gemeinde an der Gesamteinwohnerzahl der Gemeinde | Verhältnisskala |
| 30_44_rel | Relativer Anteil der 30- bis 44- Jährigen in der Gemeinde  an der Gesamteinwohnerzahl der Gemeinde | Verhältnisskala |
| 45_59_rel | Relativer Anteil der 45- bis 59- Jährigen in der Gemeinde lebenden Personen an der Gesamteinwohnerzahl der Gemeinde | Verhältnisskala |
| 60_74_rel | Relativer Anteil der 60- bis 74- Jährigen in der Gemeinde lebenden Personen an der Gesamteinwohnerzahl der Gemeinde | Verhältnisskala |
| 75_abs | Absoluter Anteil der über 75-Jährigen in der Gemeinde lebenden Personen an der Gesamteinwohnerzahl der Gemeinde | Verhältnisskala |
| 1p_rel | Relativer Anteil der 1-Personen-Haushalte in der Gemeinde | Verhältnisskala |
| 2p_rel | Relativer Anteil der 2-Personen-Haushalte in der Gemeinde | Verhältnisskala |
| 3p_abs | Absoluter Anteil der 3-Personen-Haushalte in der Gemeinde | Verhältnisskala |
| 4p_rel | Relativer Anteil der 4-Personen-Haushalte in der Gemeinde | Verhältnisskala |
| 5p_rel | Relativer Anteil der 5-Personen-Haushalte in der Gemeinde | Verhältnisskala |
| oesterreich_abs | Absoluter Anteil der Personen mit österreichischer Staatsangehörigkeit in der Gemeinde | Verhältnisskala |
| ausland_rel | Relativer Anteil der Personen mit nicht-österreichischer Staatsangehörigkei in der Gemeinde | Verhältnisskala |

Komplett: Meiner Meinung nach sind die Daten zu den einzelnen Merkmalen komplett, weil es Daten zu allen Gemeinden im Bezirk Leibnitz gibt. Allerdings würde ich den Datensatz insgesamt nicht als vollkommen komplett bezeichnen, weil einige Merkmale fehlen, wie z.B. einige Parteien (NEOS, BZÖ,...) oder andere sozioökonomische Merkmale.

Korrekt: Ja.

## Metriken

Gib die Metriken zu den einzelnen Merkmalen an.

| Metrik | fpoe-rel | 0-14-rel | 1p-rel |
|--------|---------|---------|---------|
| Min | 29,09 | 11,67 | 19,92 |
| Max | 41,44 | 15,97 | 37,93 |
| Range | 12,35 | 4,3 | 18,01 |
| Q1 | 34,05 | 13,31 | 23,93 |
| Median | 36,99 | 14,11 | 26,48 |
| Q3 | 38,81 | 14,97 | 28,16 |
| Mean | 36,41655172 | 13,97482759 | 26,45551724 |


## Merkmale

Liste je 2-3 Gemeinden mit kleinem, durschschnittlichem und großem Zahlenwert auf.

| Merkmal | Klein | Durchschnitt | Groß |
|---------|-------|--------------|------|
| fpoe-rel | Lang, St. Georgen, Allerheiligen | St. Nikolai, Ragnitz, Gamlitz | Gralla, St. Andrä-Höch |
| 0-14-rel | St. Andrä-Höch, St. Nikolai, Tillmitsch | Wagna, Großklein, Lang | Gralla, Hengsberg, Gabersdorf |
| 1p-rel | Hengsberg, Schwarzautal, St. Veit | Lebring, St. Georgen | Leibnitz, Wagna, Ehrenhausen |

## Boxplot

Gib zu den Eigenschaften Symmetrie, Box-Range Verhältnis und Outlier kurz an, was du gefunden hast.

| Eigenschaft | fpoe-rel | 0-14-rel | 1p-rel |
|-------------|---------|---------|---------|
| Symmetrie | skewed nach oben | symmetrisch | symmetrisch |
| Box:Range Verhältnis | mittel | mittel | gering |
| Outlier | keine | keine | ein Ausreißer nach oben |
