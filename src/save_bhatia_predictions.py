"""Cleans data made available by Bhatia, 2022."""
import json
from collections import defaultdict
import pandas as pd

import config

def get_induction_data(df):
    relevant_idx = df.columns.intersection(config.useful_pred_cols)
    df_dict = df[relevant_idx].to_dict("index")

    phenomena = []

    for idx, mapping in df_dict.items():
        obj = defaultdict(list)
        obj["idx"] = idx + 1

        for k, v in mapping.items():
            if "PREMISE" in k and v != -99.0:
                obj["premise"].append(v.lower().strip())
            elif v != -99.0:
                if isinstance(v, str):
                    obj[config.col2field[k]] = v.lower().strip()
                else:
                    obj[config.col2field[k]] = v

        phenomena.append(dict(obj))

    return phenomena

raw_stimuli_other = pd.read_excel(
    "data/raw/data - predictive accuracy.xlsx", sheet_name=None
)

# print(raw_stimuli_other['New - Exp 1'].columns)

for k, v in raw_stimuli_other.items():
    phenomena_name = config.exp_dict[k]
    phenomena_data = get_induction_data(v)

    with open(f"data/phenomena/{phenomena_name}_predictions.jsonl", "w") as f:
        for entry in phenomena_data:
            f.write(json.dumps(entry) + "\n")