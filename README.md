# OeML Volltextsuche-Demo

## Central Fulltext Search (cfts)
* bereits exisitierende Volltextsuche u.a. über das OeML -> https://csae8092.github.io/cfts-search-client/
* sehr allgemeines Datenmodel (Faceten)
* generische Sucheroberfläche


## OeML Demo Volltextsuche
* [DEMO](https://acdh-oeaw.github.io/oeml_index_play/)
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
* [Differenzierung: suche in Titel, Haupttext, Anhang ...]


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
* gute Erfahrungen am Institut mit statischen Seiten zur Publikation von "textlastigen" Daten (digitale Editionen)
  * [Hanslick-Online](https://hanslick.acdh.oeaw.ac.at/)
  * [Schnitzler-Briefe](https://schnitzler-briefe.acdh.oeaw.ac.at/)|[Tagebuch](https://schnitzler-tagebuch.acdh.oeaw.ac.at/)|...
  * [Thun-Korrespondenz](https://thun-korrespondenz.acdh.oeaw.ac.at/)
  * [Auden-Musulin-Papers](https://amp.acdh.oeaw.ac.at/)
  * alle zukünftig hinzukommenden Editions-Projekte

# Workflow & Archivierung
* automatisches Konvertierung von OeML-XML nach TEI
* Archivierung der TEIs in ARCHE
* wie werden die OeML-XMLs aktuell erstellt? / Oxygen Framework [WizKit](https://github.com/acdh-oeaw/WizKit)
* GIT?
* Bauen des Index (und ggf. bauen einer Statischen Seite kann über e.g. GitLab automatisiert werden)