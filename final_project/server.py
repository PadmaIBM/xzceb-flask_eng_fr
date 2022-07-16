import machinetranslation
from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")



@app.route("/english_to_french")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    french_text = english_to_french(textToTranslate)
    return french_text

@app.route("/french_to_english")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    english_text = french_to_english(textToTranslate)
    return english_text

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
