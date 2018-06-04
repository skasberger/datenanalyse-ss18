Name: Pirmin Steiner

Partei: Die Gruenen

Bezirk: Leoben

## Inspizieren

Struktur: Tabelle, weil Daten nach aufsteigender Gemeindekennzahl geordnet.

Merkmale:

| Merkmal | Inhalt | Skalierung |
|---------|---------|----------------|
| gkz | Gemeindekennzahl | Ordinalskala |
| gemeinde | Name der Gemeinde | Nominalskala |
| wahlberechtigt_abs | absolute Zahl der Wahlberechtigen | Verhaeltnisskala |
| abgegeben_abs | absolute Zahl der abgegebenen Stimmen | Veraeltnisskala |
| ungueltig_rel | relative Zahl der ungueltig Stimmen | Verhaeltnisskala |
| gueltig_abs | absolute Zahl der gueltigen Stimmen | Verhaeltnisskala |
| spoe_rel | SPOE-Stimmen im Verhaeltnis zu den abgegebenen Stimmen | Verhaeltnisskala |
| oevp_abs | OEVP-Stimmen im Verhaeltnis zu den abgegebenen Stimmen | Verhaeltnisskala |
| fpoe_rel | FPOE-Stimmen im Verhaeltnis zu den abgegebenen Stimmen | Verhaeltnisskala |
| gruene_rel | DIE GRUENEN-Stimmen im Verhaeltnis zu den abgegebenen Stimmen | Verhaeltnisskala |
| 0_14_rel | Anteil der 0-14-jaehrigen in der Gemeinde lebenden Personen im Verhaeltnis zur gesamten Einwohnerzahl | Verhaeltnisskala |
| 15_29_rel | Anteil der 15-29-jaehrigen in der Gemeinde lebenden Personen im Verhaeltnis zur gesamten Einwohnerzahl | Verhaeltnisskala |
| 30_44_rel | Anteil der 30-44-jaehrigen in der Gemeinde lebenden Personen im Verhaeltnis zur gesamten Einwohnerzahl | Verhaeltnisskala |
| 45_59_rel | Anteil der 45-59-jaehrigen in der Gemeinde lebenden Personen im Verhaeltnis zur gesamten Einwohnerzahl | Verhaeltnisskala |
| 60_74_rel | Anteil der 60-74-jaehrigen in der Gemeinde lebenden Personen im Verhaeltnis zur gesamten Einwohnerzahl | Verhaeltnisskala |
| 75_abs | Absolute Zahl der 75-jaehrigen in der Gemeinde lebenden Personen | Verhaeltnisskala |
| 1p_rel | Anteil der 1-Personen-Haushalte in der Gemeinde im Verhaeltnis zur Gesamtzahl der Haushalte in der Gemeinde | Verhaeltnisskala |
| 2p_rel | Anteil der 2-Personen-Haushalte in der Gemeinde im Verhaeltnis zur Gesamtzahl der Haushalte in der Gemeinde | Verhaeltnisskala |
| 3p_abs | Anzahl der 3-Personen-Haushalte in der Gemeinde | Verhaeltnisskala |
| 4p_rel | Anteil der 4-Personen-Haushalte in der Gemeinde im Verhaeltnis zur Gesamtzahl der Haushalte in der Gemeinde | Verhaeltnisskala |
| 5p_rel | Anteil der 5-Personen-Haushalte in der Gemeinde im Verhaeltnis zur Gesamtzahl der Haushalte in der Gemeinde | Verhaeltnisskala |
| oesterreich_abs | Absoluter Anteil der Personen mit oesterreichischer Staatsangehoerigkeit in der Gemeinde | Verhaeltnisskala |
| ausland_rel | Relativer Anteil der Personen mit nicht-oesterreichsicher Staatsangehoerigkeit in der Gemeinde | Verhaeltnisskala |

Komplett: Nicht komplett, da die Parteien nicht vollstaendig aufgelistet sind und bei einzelnen Merkmalen teilweise nur absolute oder relative Werte angegeben sind.

Korrekt: Nicht korrekt, da der Datensatz um korrekt zu sein, auch vollstaendig sein muss. 

## Metriken

| Metrik | MERKMAL | MERKMAL | MERKMAL |
|--------| gueltig_abs | gruene_rel | 15_29_rel |
| Min | 349 | 0,51 | 9,62 |
| Max | 11719 | 1,58 | 21,41 |
| Range | 11370 | 1,07 | 11,79 |
| Q1 | 707,25 | 0,7075 | 13,8725 |
| Median | 991 | 0,87 | 14,9275 |
| Q3 | 1481,25 | 1,125 | 14,9275 |
| Mean | 2016,375 | 0,92 | 14,53625 |


## Merkmale

Liste je 2-3 Gemeinden mit kleine,, durschschnittlichem und großem Zahlenwert auf.

| Merkmal | Klein | Durchschnitt | Groß |
|---------|-------|--------------|------|
| gueltig_abs | Wald am Schoberpass, Radmer | Eisenerz, Sankt Michael in Obersteiermark | Leoben, Trofaiach |
| gruene_rel | Kraubath an der Mur, Probleb | Sankt Stefan ob Leoben, Kammern im Liesingtal | Leoben, Trofaiach |
| 15_29_rel | Eisenerz, Proleb | Kraubath an der Mur, Sankt Peter-Freienstein | Leoben, Niklasdorf |

## Boxplot

| Eigenschaft | BOXPLOT | BOXPLOT | BOXPLOT |
|-------------| gueltig_abs | gruene_rel | 15_29_rel |
| Symmetrie | relativ symmetrisch | relativ symmetrisch | asymetrisch |
| Box:Range | klein | mittel | mittel |
| Outlier | zwei Ausreißer im oberen Bereich | keine Ausreißer | zwei Ausreißer nach oben und unten|


