import glob
import os
from typesense.api_call import ObjectNotFound
from acdh_cfts_pyutils import TYPESENSE_CLIENT as client
from acdh_tei_pyutils.tei import TeiReader


files = sorted(glob.glob("./data/editions/*.xml"))
resolver_url = "https://www.musiklexikon.ac.at/ml/musik_"
ts_col_name = "oeml-play"

try:
    client.collections[ts_col_name].delete()
except ObjectNotFound:
    pass


current_schema = {
    "name": ts_col_name,
    "fields": [
        {"name": "id", "type": "string"},
        {"name": "resolver", "type": "string"},
        {"name": "title", "type": "string"},  # .//Schlagwort//text()
        {"name": "full_text", "type": "string"},
        {"name": "first_letter", "type": "string", "facet": True},
        {"name": "category", "type": "string", "facet": True},
        {"name": "authors", "type": "string[]", "facet": True},
        {"name": "places", "type": "string[]", "facet": True, "optional": True  },  # .//Geographischer_Begriff
        {"name": "birth_year", "type": "int32", "facet": True, "optional": True},  # .//Geburt[@Metadatum]
        {"name": "death_year", "type": "int32", "facet": True, "optional": True},  # .//Tod[@Metadatum]
        {"name": "jobs", "type": "string[]", "facet": True, "optional": True},  # .//Berufsgruppe split(", ") remove "."
    ],
}

client.collections.create(current_schema)


records = []
counter = 0

for x in files:
    item = {}
    doc = TeiReader(x)
    doc_id = os.path.split(x)[-1].replace(".xml", "")
    first_letter = doc_id[0]
    schlagwort = doc.any_xpath(".//Schlagwort[1]")[0]
    title = " ".join("".join(schlagwort.itertext()).split())
    full_text = ""
    for t in doc.any_xpath(".//Haupttext"):
        full_text += " ".join("".join(t.itertext()).split())
    for t in doc.any_xpath(".//Lexikonartikel"):
        full_text += " ".join("".join(t.itertext()).split())
    for t in doc.any_xpath(".//Teilartikel"):
        full_text += " ".join("".join(t.itertext()).split())
    authors = []
    for a in doc.any_xpath(".//Autor"):
        authors.append(a.text)
    try:
        jobs = doc.any_xpath(".//Berufsgruppe/text()")[0]
    except IndexError:
        jobs = False
    if jobs:
        item["jobs"] = [x.replace(".", "") for x in jobs.split(", ")]
    item["id"] = doc_id
    item["resolver"] = f"{resolver_url}{first_letter}/{doc_id}.xml"
    item["title"] = title
    item["full_text"] = full_text
    item["first_letter"] = first_letter
    item["category"] = doc.any_xpath(".//Lexikonartikel[1]/@type")[0]
    item["authors"] = authors
    item["places"] = [x.text for x in doc.any_xpath(".//Geographischer_Begriff")]        
    records.append(item)
make_index = client.collections[ts_col_name].documents.import_(records)
print(make_index)
print(f"done with indexing {ts_col_name}")