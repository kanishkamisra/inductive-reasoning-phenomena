premise_cols = [f"PREMISE CATEGORY {n}" for n in range(1, 5)]
useful_cols = premise_cols + [
    "CONCLUSION CATEGORY",
    "SUPERORDINATE CATEGORY",
    "PROPERTY",
    "DATA",
    "GROUP",
    "NAME",
]

useful_pred_cols = useful_cols + [
    "Feature Overlap",
    "DeBERTa - MNLI",
    "GPT3 - DaVinci",
    "Feature Overlap - Logit",
    "BART - MNLI",
    "RoBERTa - MNLI",
    "GPT3 - Babbage",
]

col2field = {
    "CONCLUSION CATEGORY": "conclusion",
    "SUPERORDINATE CATEGORY": "superordinate",
    "DATA": "strength",
    "GROUP": "group",
    "NAME": "phenomena_name",
    "PROPERTY": "property",
    "Feature Overlap": "feature_overlap",
    "DeBERTa - MNLI": "deberta-mnli",
    "GPT3 - DaVinci": "gpt3_davinci",
    "Feature Overlap - Logit": "feature_overlap_logit",
    "BART - MNLI": "bart-mnli",
    "RoBERTa - MNLI": "roberta-mnli",
    "GPT3 - Babbage": "gpt3_babbage",
}

exp_dict = {
    "Old - Rips": "rips",
    "Old - Osherson E2": "osherson_e2",
    "Old - Osherson E4": "osherson_e4",
    "New - Exp 1": "bhatia_e1",
    "New - Exp 2": "bhatia_e2",
    "New - Exp 3": "bhatia_e3",
    "New - Exp 4": "bhatia_e4",
}
