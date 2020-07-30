import json

def getSurah():
    data = []
    for a in range(1, 115):
        o = open("surah/" + str(a) + ".json").read()
        j = json.loads(o)
        data.append(j)
    return data