
Aufgabenbericht Einheit 3 - Brossmann
Partei: ÖVP
Bezirk: Hartberg-Fürstenfeld
---

## Skalierungsniveaus
- gkz = nominal
- wahlberechtigt= Verhältnis
- abgegebene Stimmen = Verhältnis 
        - gültig = Verhätnis
        -  ungültig = Verhältnis
- Alter = Verhältnis
- Personen/Haushalt = Verhätnis
- Nationalität = Verhältnis
- Anzahl Stimmen / Partei = Verhältnis

## Prüfung auf Korrektheit 
(anhand Überprüfung mit Funktionen im Libre Office) 
- Wahlberechtigte im Bezirk = korrekt
- abgegebene Stimmen = Gesamtzahl weicht von ausgerechneter Summe ab (Gesamtzahl = 61757, ausgerechnete Summe = 54484)
        - gültig = Gesamtzahl weicht von ausgerechneter Summe ab (Gesamtzahl = 61148, ausgerechnete Summe = 53919)
        - ungültig= Gesamtzahl weicht von ausgerechneter Summe ab (Gesamtzahl = 609, ausgerechnete Summe = 565)
- Stimmen pro Partei
        - SPÖ = Gesamtzahl weicht von ausgerechneter Summe ab ( Gesamtzahl = 10178, ausgerechnete Summe = 21520)
        - ÖVP = Gesamtzahl weicht von ausgerechneter Summe ab ( Gesamtzahl = 24319, ausgerechnete Summe = 21520)
        - FPÖ = Gesamtzahl weicht von ausgerechneter Summe ab ( Gesamtzahl = 20766, ausgerechnete Summe = 18792)
        - Grüne = Gesamtzahl weicht von ausgerechneter Summe ab ( Gesamtzahl = 1132, ausgerechnete Summe = 850)
Auffällig ist also, dass bis auf die Zahl der Wahlberechtigten keine der angegebenen Zahlen stimmen. Die angegebenen Gesamtzahlen sowie die ausgerechneten Summen gesamt ergeben aber pro Kategorie den zu erfüllenden Wert (angegebene gültige Stimmen + angegebene ungültige Stimmen = angegebene Gesamtzahl und vice versa).  Das könnte auf die Anzahl von Briefwahlen zurückgeführt werden. 

## Prüfung auf Komplettheit
Hier ist festzuhalten, dass nicht alle antretenden Parteien in den Daten beachtet wurden. Es fehlten: 
NEOS, Pilz, GILT,KPÖ, Weiße, FLÖ, NBZ, ODP, SLP, EUAUS, CPÖ, M

## Metriken-Intepretation  Gesamt-Steiermark
- Wahlberechtigte: Die Metrik min gibt an, wieviel der Minimalwert der Wahlberechtigten in den steirischen Gemeinden ist. Der max-Wert gibt den Höchstwert von Wahlberechtigten an. Die range gibt die Differenz zwischen dem Maximal- und Minimalwert an, also wie groß der Unterschied zwischen der Höchstzahl an Wahlberechtigten einer Gemeinde und der Zahl der Wahlberechtigten jener Gemeinde ist, die am wenigsten Wahlberechtigte aufweist. Das Quartil 1 zeigt an, dass 25 % der Gemeinden weniger oder gleich 1289 Wahlberechtigte haben (das Quartil 3 gibt an, dass 25 % der Gemeinden größer oder gleich 2359 Wahlberechtigte aufweisen). Mean gibt den Mittelwert der Wahlberechtigten pro Gemeinde in der Steiermark. Der Median 1948 zeigt, dass 50% der Gemeinden weniger oder gleich diese Zahl an Wahlberechtigten haben und 50% der Gemeinden mehr oder gleich diese Zahl an Wahlberechtigten.
- Abgegebene Stimmen: Ähnlich wie vorhin zeigt der min an, was der kleinste Wert an abgegebenen Stimmen in einer Gemeinde sowie max die Höchstzahl an abgegebenen Stimmen in der Steiermark (in einer Gemeinde) aufzeigt. Die range zeigt an, wie groß der Unterschied zwischen der Höchstzahl an abgegebenen Stimmen einer Gemeinde und dem niedrigsten Wert an abgegebenen Stimmen in einer Gemeinde ist. Das Quartil 1 zeigt, dass 25% der abgegebenen Stimmen unter oder gleich des Q1-Wertes ist, Q3 zeigt an, dass 25% der abgegebenen Stimmen größer oder gleich des Q3-Wertes sind. Der mean zeigt den Mittelwert der abgegebenen Stimmen pro Gemeinde in der Steiermark an. Der Median zeigt an, dass 50% der Gemeinden weniger oder gleich 1352 abgegebene stimmen aufweisen und 50% der steirischen Gemeinden mehr oder gleich diese Anzahl an Stimmen aufweisen. 
- Gültige/ungültige Stimmen: Für gültige und ungültige Stimmen herrscht das gleiche Prinzip vor. Der min-Wert zeigt den Minimal-Wert an gültigen oder ungültigen Stimmen an, der max-Wert zeigt die Höchstzahl von gültigen oder ungültigen Stimmen für eine Gemeinde als Steiermark-Höchstwert an. Range zeigt die Differenz zwischen dem Maximal-Wert an ungültigen oder gültigen Stimmen und dem Minimal-Wert von ungültigen oder gültigen Stimmen auf. Q1 zeigt an, dass 25% der Werte der ungültigen oder gültigen Stimmen unter oder gleich dem Q1-Wert sind (ungültige: 8, gültige: 914) und Q3 zeigt an, dass 25% der Werte gleich oder größer dem Q3-Wert sind (ungültige: 21; gültige: 2341). Mean zeigt den Durchschnittswert an gültigen oder ungültigen Stimmen einer Gemeinde an. Median von 12 für ungültige Stimmen und 1343 für gültige Stimmen teilt die Werte in untere 50% und obere 50% des Datensatzes. 
- 
... und für die Metriken der verschiedenen Parteien, Altersgruppen, Haushaltszugehörigkeiten und Nationalitäten gelten prinzipiell die selben Regeln. 

## Welche Aussage bezüglich der Wahl kann mit der zugrundeliegenden Datenbasis getroffen werden? 
Man kann aufgrunde des Datensets grundliegende Fragen beantworten, wie eben welche Partei wieviele Stimmen in der Steiermark verzeichnen konnte. Oder aber auch, wie die Wählerschaft altersmäßig aufgeteilt ist. Ein paar Beispiele für Fragen, die beantwortet werden können: 
- Stimmenanzahl/Partei in der Steiermark und in einzelnen Gemeinden
- Anzahl der Wahlberechtigten gesamt und pro Gemeinde
- Anzahl der gültigen und ungültigen Stimmen gesamt und pro Gemeinde
- Alter der Bevölkerung und Verteilung des Alters 
- Anzahl der 1-, 2-, 3-, 4-, 5(+)-Personen-Haushalte gesamt und pro Gemeinde
- Anzahl der österreichischen und ausländischen Bewohnern in der Steiermark und pro Gemeinde (daraus folgend könnte auch der Prozentsatz von ausländischen Bewohnern auf die Gesamtbevölkerung einer Gemeinde ausgerechnet werden)
## Sind alle Daten vorhanden, um das Wahlverhalten in der Steiermark bei der NRW17 zu beschreiben? 
Es sind grundlegende Daten vorhanden, um das Wählerverhalten genauer beschreiben und analysieren zu können fehlen aber Daten rund um das Geschlechterverhältnis, Berufsstand, Bildungsniveau, Einkommen, Anzahl d. Kinder in einer Familie etc. 
## Sind dir irgendwelche Besonderheiten bzgl. des Datensets aufgefallen bzw. gab es etwas für dich Unerwartetes?
Während dem Summenzählen für die abgegebenen/gültigen/ungültigen Stimmen sind Differenzen zwischen angegebener Gesamtzahl sowie den ausgerechneten Summen aufgefallen. Das könnte sich auf die Briefwähler zurückführen lassen. 
## Welche Einstellungen hast du für den Boxplot gewählt und warum? 
Alle Boxplots sind vertikal, weil einem so die Ausreißer gleich ins Auge stechen. Auch die Skalierung ist recht einläuchtend. 
## Ergebnisse der Metriken
#### Parteiergebnisse FPÖ:
- min: 205
- max: 1766
- range: 1561
- mean: 597,8
- Q1:371,5
- median: 486
- Q3: 664,5
#### 2-Personen-Haushalte
- min: 80
- max: 1284
- range: 1204
- mean: 264,33
- Q1: 147
- median: 186,5
- Q3: 272,75

#### Alter 15-29
- min: 169
- max: 1342
- range: 1173
- mean: 418,94
- Q1: 267
- median: 336,5
- Q3: 463
