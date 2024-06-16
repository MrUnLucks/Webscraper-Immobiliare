from flask import Flask, jsonify
import scrape  # Import the module containing your scraping functions

app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug=True)

@app.route("/")
def hello_world():
    return jsonify({"message": "Hello, World!"})

@app.route("/scrape")
def start_scraping():
    try:
        toRet = scrape.scrape_immobiliare()
        return jsonify(toRet)
    except Exception as e:
        return jsonify({"error": str(e)})
      