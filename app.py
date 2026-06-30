from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/difference", methods=["POST"])
def difference():
    date1 = request.form.get("date1", "").strip()
    date2 = request.form.get("date2", "").strip()

    # Convert to datetime objects
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")

    # Calculate difference
    diff_days = abs((d2 - d1).days)

    return render_template(
        "index.html",
        date1=date1,
        date2=date2,
        diff_days=diff_days
    )

if __name__ == "__main__":
    app.run(debug=True)
