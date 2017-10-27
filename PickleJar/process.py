import importlib


INSTALLED_PICKLES = [
    "gen_convo",
    "date_time",
    "notes",
    "tweet",
    "rvce_results"
]


def process(s):
    input_set = s.lower().split()
    stopwords = ['what', 'who', 'is', 'at', 'is', 'he', 'for',
                 'is', 'ourselves', 'hers', 'between', 'yourself',
                 'but', 'again', 'there', 'about', 'once', 'during',
                 'out', 'very', 'having', 'with', 'they', 'own',
                 'an', 'be', 'some', 'for', 'do', 'its', 'yours',
                 'such', 'into', 'of', 'most', 'itself', 'other',
                 'off', 'is' , 's', 'am', 'or', 'who', 'as', 'from',
                 'him', 'each', 'the', 'themselves', 'until', 'below',
                 'are', 'we', 'these', 'your', 'his', 'through',
                 'don', 'nor', 'me', 'were', 'her', 'more', 'himself',
                 'this', 'down', 'should', 'our', 'their', 'while',
                 'above', 'both', 'up', 'to', 'ours', 'had', 'she',
                 'all', 'no', 'when', 'at', 'any', 'before', 'them',
                 'same', 'and', 'been', 'have', 'in', 'will', 'on',
                 'does', 'yourselves', 'then', 'that', 'because',
                 'what', 'over', 'why', 'so', 'can', 'did', 'not',
                 'now', 'under', 'he', 'you', 'herself', 'has',
                 'just', 'where', 'too', 'only', 'myself', 'which',
                 'those', 'i', 'after', 'few', 'whom', 't', 'being',
                 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing',
                 'it', 'how', 'further', 'was', 'here', 'than']

    result_words = [word for word in input_set if word.lower() not in stopwords]
    result = ' '.join(result_words)

    input_set = set(result.split())

    print("input set is")
    print(input_set)

    for ip in INSTALLED_PICKLES:
        pickle_module = importlib.import_module("pickles."+ip)
        for t in pickle_module.triggers:
            for phrase in pickle_module.triggers[t]:
                print(set(phrase))
                if input_set.issubset(set(phrase)):
                    return getattr(pickle_module, t)(s)
    return None
