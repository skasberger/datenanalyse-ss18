# Aufgabe 3
Name: NIKOLAUS PICHLER

Partei: FPÖ

Bezirk: Voistberg

## Inspizieren

Struktur: Tabellarisch

Merkmale: relativer Stimmenanteil, 0-14_rel, 15-29_rel

| gkz | Gemeindekennzahl | nominal |
| gemeinde | Gemeindename | nominal |
| wahlberechtigt_abs | Anzahl der Wahlberechtigten in absoluten Zahlen | Verhältnisskala |
| abgegeben_abs | Anzahl der abgegebenen Stimmen in absoluten Zahlen |  Verhältnisskala|
| ungueltig_rel | Anzahl der ungültigen Stimmen in Prozent | Verhältnisskala |
| gueltig_abs | Anzahl der gütligen Stimmen in absoluten Zahlen | Verhältnisskala |
| spoe_rel | Anzahl der Stimmen für die SPÖ in Prozent | Verhältnisskala |
| oevp_abs | Anzahl der Stimmen für die ÖVP in absoluten Zahlen | Verhältnisskala |
| fpoe_rel | Anzahl der Stimmen für die FPÖ in Prozent | Verhältnisskala |
| gruene_rel | Anzahl der Stimmen für die Grünen in Prozent | Verhältnisskala |
| 0_14_rel | Anzahl der 0-14 Jährigen in Prozent | Verhältnisskala |
| 15_29_rel | Anzahl der 15-29 Jährigen in Prozent | Verhältnisskala |
| 30_44_rel | Anzahl der 30-44 Jährigen in Prozent | Verhältnisskala |
| 45_59_rel | Anzahl der 45-59 Jährigen in Prozent | Verhältnisskala |
| 60_74_rel | Anzahl der 60-74 Jährigen in Prozent | Verhältnisskala |
| 75_abs | Anzahl der 75 Jährigen in absoluten Zahlen | Verhältnisskala |
| 1p_rel | Einpersonenaushalt in Prozent | Verhältnisskala |
| 2p_rel | Zweipersonenhaushalt in Prozent | Verhältnisskala |
| 3p_abs | Dreipersonenhaushalt in absoluten Zahlen | Verhältnisskala |
| 4p_rel | Vierpersonenhaushalt in Prozent | Verhältnisskala |
| 5p_rel | Fünfpersonenhaushalt in Prozent | Verhältnisskala |
| oesterreich_abs | Anzahl der österreichischen Staatsbürger in absoluten Zahlen | Verhältnisskala |
| ausland_rel | Anzahl der ausländischen Staatsbürger im Bezirk in Prozent | Verhältnisskala |

Komplett: Nein, weil nicht alle Parteien. Alle Haushalte mit über 5 Personen fehlen ebenfalls.

Korrekt: Ja

## Metriken

Gib die Metriken zu den einzelnen Merkmalen an.

| Metrik | FPÖrel | FPÖ0-14 | FPÖ15_29 |
|--------|---------|---------|---------|
| Min | 33,9 | 8,9  | 14,7 |
| Max | 41,2  | 14,9  | 17,0 |
| Range | 7,3 | 5,9 | 2,2 |
| Q1 | 35,6 | 11,49 | 15,2 |
| Median | 37,8 | 12,9 | 15,4 |
| Q3 | 39,2 | 13,7 | 15,8 |
| Mean | 37,5 | 12,5  | 15,56 |


## Merkmale

Liste je 2-3 Gemeinden mit kleinem, durschschnittlichem und großem Zahlenwert auf.

| Merkmal | Klein | Durchschnitt | Groß |
|---------|-------|--------------|------|
| FPÖrel | Mooskirchen (33,8) | Rosenthal an der Kainach (39,3)  | Stallhofen (41,2) |
| FPÖ0-14 | Hirschegg-Pack (8,9)| Voitsberg 12,2  | Stallhofen (14,9) |
| FPÖ15_29 | Kainach bei Voitsberg (14,8) | Bärnbach (15,4) | Rosenthal an der Kainach (17,0) |

## Boxplot

Gib zu den Eigenschaften Symmetrie, Box-Range Verhältnis und Outlier kurz an, was du gefunden hast.

| Eigenschaft | BOXPLOT | BOXPLOT | BOXPLOT |
|-------------|---------|---------|---------|
| Symmetrie | annähernd symmetrisch | annähernd symmetrisch | nein |
| Box:Range Verhältnis | normal | schmal | schmal |
| Outlier | nein | nein | ja |

