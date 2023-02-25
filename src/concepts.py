"""How many unique concepts do the phenomena cover?"""
import json
import os

PHENOMENA_PATH = "data/phenomena/"
PHENOMENA_FILES = os.listdir(PHENOMENA_PATH)

# unique concepts
concepts = set()

for file in PHENOMENA_FILES:
    with open(f'{PHENOMENA_PATH}/{file}', 'r') as f:
        for line in f:
            entry = json.loads(line)
            concepts.update(entry['premise'])
            # for p in entry['premise']:
            #     concepts.add(p)
            concepts.add(entry['conclusion'])
print(concepts)
# print(len(concepts))
