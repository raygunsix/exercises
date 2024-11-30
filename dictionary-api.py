from flask import Flask

app =  Flask(__name__)

@app.route("/api/v1/<word>")
def api(word):
    definition = word.upper()
    return {
        "definition": definition,
        "word": word
    }

app.run(debug=True, port=5001)