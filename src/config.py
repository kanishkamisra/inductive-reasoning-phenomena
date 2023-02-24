premise_cols = [f"PREMISE CATEGORY {n}" for n in range(1, 5)]
useful_cols = premise_cols + [
    "CONCLUSION CATEGORY",
    "SUPERORDINATE CATEGORY",
    "PROPERTY",
    "DATA",
    "GROUP",
    "NAME",
]

col2field = {
    "CONCLUSION CATEGORY": "conclusion",
    "SUPERORDINATE CATEGORY": "superordinate",
    "DATA": "strength",
    "GROUP": "group",
    "NAME": "phenomena_name",
    "PROPERTY": "property",
}
