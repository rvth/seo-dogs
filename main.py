from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/crawling-and-indexing")
def crawling():
    return render_template("crawling-and-indexing.html")

@app.route("/site-structure")
def structure():
    return render_template("site-structure.html")

@app.route("/on-page")
def onpage():
    return render_template("on-page.html")

@app.route("/user-experience")
def users():
    return render_template("user-experience.html")

@app.route("/links")
def links():
    return render_template("links.html")

@app.route("/international-seo")
def international():
    return render_template("international-seo.html")

@app.route("/crawling")
def crawl():
    return render_template("crawling.html")

@app.route("/rendering")
def rendering():
    return render_template("rendering.html")

@app.route("/indexing")
def indexing():
    return render_template("indexing.html")

@app.route("/robotstxt")
def robots():
    return render_template("robotstxt.html")

@app.route("/noindex-and-nofollow")
def noindex():
    return render_template("noindex-and-nofollow.html")

@app.route("/canonicals")
def canonicals():
    return render_template("canonicals.html")

@app.route("/heading-tags")
def headings():
    return render_template("/heading-tags.html")

@app.route("/meta-data")
def metadata():
    return render_template("meta-data.html")

@app.route("/page-titles")
def titles():
    return render_template("page-titles.html")

@app.route("/meta-descriptions")
def descriptions():
    return render_template("meta-descriptions.html")

@app.route("/alt-text")
def alttext():
    return render_template("alt-text.html")

if __name__ == "__main__":
    app.run(debug=True)