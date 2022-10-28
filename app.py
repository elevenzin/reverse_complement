import os
from flask import Flask, render_template, request
from rcomplement import get_dna_reverse_complement, process_fasta

app = Flask(__name__)


@app.route("/")
def form():
    return render_template("form.html")


@app.route("/data", methods=["POST", "GET"])
def data():
    if request.method == "GET":
        return f"The URL /data is accessed directly. Try going to 'localhost:1234' to submit form"
    if request.method == "POST":
        form_data = request.form
        try:
            if form_data["raw_input"].startswith(">"):
                output = dict(process_fasta(form_data["raw_input"]))
            else:
                output = {
                    "Sequence": get_dna_reverse_complement(form_data["raw_input"])
                }
            return render_template("data.html", form_data=output)
        except BaseException as e:
            return f"Got Error: {e}"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 1234))
    app.run(debug=True, host="0.0.0.0", port=port)
