from flask import Flask
import pandas as pd

app =  Flask(__name__)
df = pd.read_csv("data-dictionary/dictionary.csv")

@app.route("/api/v1/<word>")
def api(word):
    definition = df.loc[df['word'] == word]['definition'].squeeze()
    return {
        "definition": definition,
        "word": word
    }

if __name__ == "__main__":
    app.run(debug=True, port=5001)