# Code By Billal Fauzan
# Credits:
# - Quran Json from https://github.com/rioastamal/quran-json

# Copyright (c) 2020 Billal Fauzan, All right reserved.
from flask import Flask, render_template
from module import getSurah
import os

app = Flask(__name__)
data = getSurah()

@app.errorhandler(404)
def not_found(e):
    return render_template("error.html")

@app.route("/surah/<ayat>")
def surah(ayat):
    if ayat.isdigit():
        ayat = int(ayat) - 1
        if ayat > len(data):
            return render_template("error.html")
        else:
            text = data[ayat][str(ayat + 1)]["text"]
            name_surah = data[ayat][str(ayat + 1)]["name_latin"]
            trans = data[ayat][str(ayat + 1)]["translations"]["id"]["text"]
            arab = []
            id = []
            for a in text:
                arab.append(text[a])
            for b in trans:
                id.append(trans[b])
            return render_template("surah.html", value=zip(arab, id), nama=name_surah)
    else:
        return render_template("error.html")

@app.route('/')
def index():
    ayat = []
    name_latin = []
    num = 0
    for surah in data:
        num += 1
        ayat.append(surah[str(num)]["number"])
        name_latin.append(surah[str(num)]["name_latin"])
    return render_template("index.html",name=enumerate(name_latin))
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)