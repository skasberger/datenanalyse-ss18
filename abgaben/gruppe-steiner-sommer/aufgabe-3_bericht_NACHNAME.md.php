Name: Michael Sommer

Partei: SPOE

Bezirk: Leoben

## Inspizieren

Struktur:  Es handelt sich um eine Tabelle – die Datensätze sind geordnet nach aufsteigender Gemeindekennzahl

Merkmale:

| Merkmal | Inhalt | Skalierung |
|---------|---------|----------------|
| gkz | Gemeindekennzahl | Ordinalskala |
| gemeinde | Name der Gemeinde | Nominalskala  |
| wahlberechtigt_abs | absolute Anzahl an Wahlberechtigten im Bezirk  | Verhaeltnisskala  |
| abgegeben_abs | absolute Anzahl der abgegebenen Stimmen | Verhaeltnisskala |
| ungueltig_rel | relative Anzahl der ungültigen Stimmen | Verhaeltnisskala |
| gueltig_abs | Absolute Anzahl der gueltigen Stimmen  | Verhaeltnisskala  |
| spoe_rel | Relative Anzahl der Stimmen für die SPOE  | Verhaeltnisskala |
| oevp_abs | Absolute Anzahl der Stimmen für die OEVP  |Verhaeltnisskala  |
| fpoe_rel | Relative Anzahl der Stimmen für die FPOE | Verhaeltnisskala |
| gruene_rel | Relative Anzahl der Stimmen für die GRUENEN |Verhaeltnisskala  |
| 0_14_rel | Relative Anzahl der Einwohner, die zwischen 0 und 14 Jahre alt sind |Verhaeltnisskala  |
| 15_29_rel | Relative Anzahl der Einwohner, die zwischen 15 und 29 Jahre alt sind | Verhaeltnisskala |
| 30_44_rel | Relative Anzahl der Einwohner, die zwischen 30 und 44 Jahre alt sind  | Verhaeltnisskala |
| 45_59_rel | Relative Anzahl der Einwohner, die zwischen 45 und 59 Jahre alt sind |Verhaeltnisskala  |
| 60_74_rel | Relative Anzahl der Einwohner, die zwischen 60 und Jahre alt sind  | Verhaeltnisskala |
| 75_abs | Relative Anzahl der Einwohner, die aelter als 75 Jahre alt sind |Verhaeltnisskala  |
| 1p_rel | Anzahl der 1-Personen Haushalte in relativem Verhaltnis zur Gesamtanzahl der Haushalte in der Gemeinde  |Verhaeltnisskala  |
| 2p_rel | Anzahl der 2-Personen Haushalte in relativem Verhaltnis zur Gesamtanzahl der Haushalte in der Gemeinde |Verhaeltnisskala  |
| 3p_abs | Anzahl der 3-Personen Haushalte in relativem Verhaltnis zur Gesamtanzahl der Haushalte in der Gemeinde |Verhaeltnisskala  |
| 4p_rel | Anzahl der 4-Personen Haushalte in relativem Verhaltnis zur Gesamtanzahl der Haushalte in der Gemeinde  |Verhaeltnisskala  |
| 5p_rel | Anzahl der 5-Personen Haushalte in relativem Verhaltnis zur Gesamtanzahl der Haushalte in der Gemeinde  |Verhaeltnisskala  |
| oesterreich_abs | Absolute Anzahl an OesterreicherInnen im Ort  | Verhaeltnisskala |
| ausland_rel | Relative Anzahl an AuslaenderInnen im Ort   | Verhaeltnisskala  |

Komplett: Nein, der Datensatz ist nicht korrekt. Es fehlen zwei Parteien in der Auflistung. Man hätte zudem noch andere Merkmals hinzufügen können, wie die Anzahl der Briefwähler.

Korrekt: Ja

## Metriken

| Metrik | spoe_rel
 | abgegeben_abs
 | wahlberechtigt_abs |
|--------|---------|---------|---------|
| Min | 23,29 | 354 | 490 |
| Max | 52,12 | 11802 | 18967 |
| Range | 28,83 | 11448 | 18477  |
| Q1 | 27,1525  | 817,25 | 1037,25 |
| Q3 | 35,3925  | 1967,25 |2141,25 |
| Median | 31,19 | 998 | 1423 |
| Mean | 32,785625 | 2031,625  | 3077,875 |


## Merkmale

Liste je 2-3 Gemeinden mit kleine,, durschschnittlichem und großem Zahlenwert auf.

| Merkmal | Klein | Durchschnitt | Groß |
|---------|-------|--------------|------|
| spoe_rel | Kammern | Trofaiach, Proleb | Vordernberg  |
| abgegeben_abs | Wald/ Schoberpass | Eisenerz & St. Michael  | Leoben |
| wahlberechtigt_abs | Wald/ Schoberpass  | St. Michael & Eisenerz  | Leoben |

## Boxplot

| Eigenschaft | spoe_rel | abgegeben_abs | wahlberechtigt_abs |
|-------------|---------|---------|---------|
| Symmetrie | symetrisch | Box zieht etwas nach unten | Box zieht etwas nach unten – ähnlich wie bei abgegebenen|
| Box:Range | Verhältnis normal – 1/3 etwa  | 1/2  | 1/2 |
| Outlier | einen oberen Outliner  | Zwei obere Outliner – d.h. dass es zwei überdurchschnittlich große Gemeinden gibt | Zwei obere Outliner – d.h. dass es bei den größeren Städten auch absolut gesehen die meisten Nichtwähler gab |

