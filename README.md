# OeML Volltextsuche-Demo

## Central Fulltext Search (cfts)
* bereits exisitierende Volltextsuche u.a. über das OeML -> https://csae8092.github.io/cfts-search-client/
* sehr allgemeines Datenmodel (Faceten)
* generische Sucheroberfläche


## OeML Demo Volltextsuche
* basierend auf vier Beispieldateien
* zusätzliche Faceten:
  * Kategorie
  * in den Artikel erwähnte Orte
  * AutorInnen (Kürzel)
  * [in den Artikel erwähnte Personen]
  * [referenzierte Artikel]

* v.a. für Personen eine weiterer Facets/Filtermöglichekeiten
  * Berufe
  * Geburts- Sterbedatum


## technische Umsetzung

zwei Arbeitsschritte: 
* "bauen" des Indexes; ein (Python) Skript mit Zugriff auf alle zu indexierenden OeML XMLs
* Suchinterface: HTML + JavaScript
  * kann (vermutlich) in bestehende Applikation integriert werden

# OeML Webiste als Static-Page
* Statisch vs. Dynamisch
  * Static-Page/Static-Site: Webserver + HTML Dateien
    * einfach zu Warten;
    * i.d. Regel sehr schnell
    * potentiell limititierte Funktionalität
  * Dynamische Website: Webserver + **Application Server** zur Generierung der Angeforderten HTML-Seiten
    * muss laufend gewarted (updates) werden
    * tendenziell mehr Möglichkeiten
* gute Erfahrungen am Institut mit Statischen Seiten zur Publikation von "textlastigen" Daten (digitale Editionen)
  * Hanslick-Online
  * Schnitzler-Briefe|Tagebuch|...
  * Thun-Korrespondenz
  * Auden-Musulin-Papers
  (alle neu hinzukommenen Editions-Projekte)