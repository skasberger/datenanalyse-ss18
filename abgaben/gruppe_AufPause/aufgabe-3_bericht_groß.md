# Aufgabe 3

Name: Angelika Groß

Partei: SPÖ

Bezirk: Voitsberg

## Inspizieren

Struktur: Tabelle

Merkmale: spoe_rel, 0-14_rel und ausland_rel

| Merkmal | Inhalt | Skalierung |
|---------|---------|----------------|
gkz | Gemeindekennzahl | nominal
gemeinde | Gemeindename | nominal
wahlberechtigt_abs | Anzahl der Wahlberechtigten in absoluten Zahlen | Verhältnisskala
abgegeben_abs | Anzahl der abgegebenen Stimmen in absoluten Zahlen | Verhältnisskala
ungueltig_rel | Anzahl der ungültigen Stimmen in Prozent | Verhältnisskala
gueltig_abs | Anzahl der gütligen Stimmen in absoluten Zahlen | Verhältnisskala
spoe_rel | Anzahl der Stimmen für die SPÖ in Prozent | Verhältnisskala
oevp_abs | Anzahl der Stimmen für die ÖVP in absoluten Zahlen | Verhältnisskala
fpoe_rel | Anzahl der Stimmen für die FPÖ in Prozent | Verhältnisskala
gruene_rel | Anzahl der Stimmen für die Grünen in Prozent | Verhältnisskala
0_14_rel | Anzahl der 0-14 Jährigen in Prozent | Verhältnisskala
15_29_rel | Anzahl der 15-29 Jährigen in Prozent | Verhältnisskala
30_44_rel | Anzahl der 30-44 Jährigen in Prozent | Verhältnisskala
45_59_rel | Anzahl der 45-59 Jährigen in Prozent | Verhältnisskala
60_74_rel | Anzahl der 60-74 Jährigen in Prozent | Verhältnisskala
75_abs | Anzahl der 75 Jährigen in absoluten Zahlen | Verhältnisskala
1p_rel | Einpersonenaushalt in Prozent | Verhältnisskala
2p_rel | Zweipersonenhaushalt in Prozent | Verhältnisskala
3p_abs | Dreipersonenhaushalt in absoluten Zahlen | Verhältnisskala
4p_rel | Vierpersonenhaushalt in Prozent | Verhältnisskala
5p_rel | Fünfpersonenhaushalt in Prozent | Verhältnisskala
oesterreich_abs | Anzahl der österreichischen Staatsbürger in absoluten Zahlen | Verhältnisskala
ausland_rel | Anzahl der ausländischen Staatsbürger im Bezirk in Prozent | Verhältnisskala

Komplett: Nein, da nicht alle Parteien angeführt werden. Außerdem fehlen alle Haushalte mit über 5 Personen.

Korrekt: Ja

## Metriken

Gib die Metriken zu den einzelnen Merkmalen an.

| Metrik | spoe_rel | 0-14_rel | ausland_rel |
|--------|---------|---------|---------|
| Min | 14,08 | 8,97 | 1,15 |
| Max | 36,36 | 14,92 | 6,32 |
| Range | 22,28 | 5,95 | 5,17 |
| Q1 | 18,485 | 11,485 | 2,48 |
| Median | 21,19 | 12,9 | 3,08 |
| Q3 | 29,225 | 13,72 | 5,235 |
| Mean | 23,4946 | 12,5206 | 3,7426 |


## Merkmale

Liste je 2-3 Gemeinden mit kleinem, durschschnittlichem und großem Zahlenwert auf.

| Merkmal | Klein | Durchschnitt | Groß |
|---------|-------|--------------|------|
| spoe_rel | Hirschegg-Pack | Geistthal-Södingberg | Rosental an der Kainach |
| 0-14_rel | Hirschegg-Pack | Voitsberg | Stallhofen |
| ausland_rel | Sankt Martin am Wöllmißberg | Edelschrott | Köflach |

## Boxplot

Gib zu den Eigenschaften Symmetrie, Box-Range Verhältnis und Outlier kurz an, was du gefunden hast.

| Eigenschaft | BOXPLOT | BOXPLOT | BOXPLOT |
|-------------|---------|---------|---------|
| Symmetrie | Nein | Nein | Nein |
| Box:Range Verhältnis | Breit | Schmal | Schmal |
| Outlier | Nein | Nein | Nein |

