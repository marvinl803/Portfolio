from flask import Flask, render_template, abort
import os

app = Flask(__name__)

projects = [
    {
        "name": "Real Madrid Zone App",
        "thumb": "img/real-madrid.jpg",
        "hero": "img/real-madrid.jpg",
        "categories": ["python", "web"],
        "slug": "real-madrid-zone",
        "prod": "https://www.realmadridzone.online/",
    },
    {
        "name": "Habit Tracking App",
        "thumb": "img/habit-tracking.jpg",
        "hero": "img/habit-tracking.jpg",
        "categories": ["python", "web"],
        "slug": "habit-tracking",
        "prod": "https://habit-tracker-fmnl.onrender.com/",
    },
    {
        "name": "Microblogging App",
        "thumb": "img/microblogging.jpg",
        "hero": "img/microblogging.jpg",
        "categories": ["Python", "Web"],
        "slug": "microblog",
        "prod": "https://web-microblog-8rdj.onrender.com/",
    },
    {
        "name": "Personal Portfolio App",
        "thumb": "img/portfolio.png",
        "hero": "img/portfolio.png",
        "categories": ["Python", "Web"],
        "slug": "portfolio",
        "prod": "https://web-microblog-8rdj.onrender.com/",
    },
]

slug_to_project = {project["slug"]: project for project in projects}

@app.route("/")
def home():
    return render_template("home.html", projects=projects)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f"project_{slug}.html", project=slug_to_project[slug])

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, port=port)
