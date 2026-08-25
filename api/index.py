from flask import Flask, render_template, url_for

app = Flask(__name__,
            static_url_path="",
            static_folder='public',
            template_folder='templates'
            )

@app.route("/")
def home():
    return  render_template("index.html")

@app.route("/about")
def about():
    return  render_template("about.html")

@app.route("/my-projects")
def my_projects():
    return  render_template("my-projects.html")

if __name__ == "__main__":
    app.run(debug=True)