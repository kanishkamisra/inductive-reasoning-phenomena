"""Cleans data made available by Bhatia, 2022."""
import json
from collections import defaultdict
import pandas as pd

import config

raw_stimuli = pd.read_excel(
    "data/raw/data - empirical regularities.xlsx", sheet_name=None
)


def get_induction_data(df):
    relevant_idx = df.columns.intersection(config.useful_cols)
    df_dict = df[relevant_idx].to_dict("index")

    phenomena = []

    for idx, mapping in df_dict.items():
        obj = defaultdict(list)
        obj["idx"] = idx + 1

        for k, v in mapping.items():
            if "PREMISE" in k and v != -99.0:
                obj["premise"].append(v.lower())
            elif v != -99.0:
                if isinstance(v, str):
                    obj[config.col2field[k]] = v.lower()
                else:
                    obj[config.col2field[k]] = v

        phenomena.append(dict(obj))

    return phenomena


for k, v in raw_stimuli.items():
    phenomena_name = "_".join(k.lower().split())
    phenomena_data = get_induction_data(v)

    with open(f"data/phenomena/{phenomena_name}.jsonl", "w") as f:
        for entry in phenomena_data:
            f.write(json.dumps(entry) + "\n")
