import json

def load_class_names(path_to_json_map):
    with open(path_to_json_map) as f:
        flower_labels = json.load(f)

    flower_labels_new = dict()
    for key in flower_labels:
        flower_labels_new[str(int(key))] = flower_labels[key]

    return flower_labels_new
