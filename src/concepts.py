"""How many unique concepts do the phenomena cover?"""
import json
import os
from ordered_set import OrderedSet

PHENOMENA_PATH = "data/phenomena/"
PHENOMENA_FILES = os.listdir(PHENOMENA_PATH)

# unique concepts
concepts = OrderedSet()

for file in PHENOMENA_FILES:
    with open(f"{PHENOMENA_PATH}/{file}", "r") as f:
        for line in f:
            entry = json.loads(line)
            for premise in entry["premise"]:
                concepts.add(premise.strip())
            concepts.add(entry["conclusion"].strip())

concepts = list(concepts)

with open("data/concepts.txt", "w") as f:
    [f.write(c + "\n") for c in concepts]
