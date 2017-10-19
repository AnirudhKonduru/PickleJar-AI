import importlib

INSTALLED_PICKLES = [
    "gen_convo",
    "date_time",
    "notes"
]

def process(s):
    input_set = set(s.split())
    print(input_set)
    for ip in INSTALLED_PICKLES:
        pickle_module = importlib.import_module("pickles."+ip)
        for t in pickle_module.triggers:
            for phrase in pickle_module.triggers[t]:
                if input_set.issubset(set(phrase)):
                    return getattr(pickle_module, t)(s)
    return None
