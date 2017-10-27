import sys
import yaml


def init():
    with open("config.yaml") as stream:
        config = yaml.safe_load(stream)

    if config is None:
        config = {}
    # set default values
    config["input"] = "text"
    config["output"] = "text"


    for i in range(1, len(sys.argv)-1):
        if (sys.argv[i] == "-i" or "--input") and (sys.argv[i+1] == "text" or "speech"):
            config["input"] = sys.argv[i+1]
        if (sys.argv[i] == "-o" or "--output") and (sys.argv[i+1] == "text" or "speech"):
            config["input"] = sys.argv[i+1]

    with open("config.yaml", "w") as stream:
        yaml.dump(config, stream)
