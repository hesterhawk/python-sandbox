from collections import OrderedDict

def transform(legacy_data):
    final = {}

    for key, items in legacy_data.items():
        {final.update({x.lower():key}) for x in items}

    return OrderedDict(sorted(final.items(), key=lambda x: x))