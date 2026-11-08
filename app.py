from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/",methods=["POST","GET"])
def home():
    message = request.form.get ("message","")
    if "http" in message:
        return render_template(
            "index.html",
            warning="Do not press the link . it is was flaged by customers and people"
        )
    else:
         return render_template("index.html") 
if __name__ == "__main__":
     app.run(debug=True)