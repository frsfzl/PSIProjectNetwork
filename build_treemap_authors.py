"""Builds treemaps_authors.json: authors per (topic, subtopic cluster) for each treemaps.html tab.

pub_id in the doc_topics files is the row index of publications_with_newBuckets_labels0.80Named.csv.
Also exports the NC State author keys (same rule as index.html's buildNCSSet) so treemaps.html
doesn't have to load the full publications CSV.
"""
import csv
import json
import re

csv.field_size_limit(10**9)
PUBS = "publications_with_newBuckets_labels0.80Named.csv"
MODELS = {"specter2": "topics_PSI/topics/doc_topics_specter2_auto.csv",
          "gtrt5": "topics_PSI/topics/doc_topics_gtr_t5_auto.csv"}

pubs = list(csv.DictReader(open(PUBS, newline="")))

ncs_keys = set()
for row in pubs:
    for person in (row.get("nc_state_people") or "").split(";"):
        person = re.sub(r"\s*\([^)]*\)", "", person).strip()
        parts = person.split()
        if len(parts) >= 2:
            ncs_keys.add(parts[-1].lower() + ", " + parts[0].lower())

out = {"ncsKeys": sorted(ncs_keys)}
for model, path in MODELS.items():
    groups = {}
    for r in csv.DictReader(open(path, newline="")):
        authors = [a.strip() for a in (pubs[int(r["pub_id"])]["authors"] or "").split(";") if a.strip()]
        groups.setdefault(r["topic_label"] + "||" + r["subtopic"], set()).update(authors)
    out[model] = {k: sorted(v) for k, v in groups.items()}
    print(model, len(groups), "clusters")

with open("treemaps_authors.json", "w") as f:
    json.dump(out, f, separators=(",", ":"))
