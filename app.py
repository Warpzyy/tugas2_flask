from flask import Flask, render_template, request

app = Flask(__name__)

data_list = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nama = request.form.get("nama")
        pesan = request.form.get("pesan")

        data_list.append({
            "nama": nama,
            "pesan": pesan
        })

    return render_template("index.html", data=data_list)

if __name__ == "__main__":
    app.run(debug=True)