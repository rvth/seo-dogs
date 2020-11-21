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

@app.route("/crawling-and-indexing/crawling")
def crawl():
    return render_template("crawling.html")

@app.route("/crawling-and-indexing/rendering")
def rendering():
    return render_template("rendering.html")

@app.route("/crawling-and-indexing/indexing")
def indexing():
    return render_template("indexing.html")

@app.route("/crawling-and-indexing/robotstxt")
def robots():
    return render_template("robotstxt.html")

@app.route("/crawling-and-indexing/noindex-and-nofollow")
def noindex():
    return render_template("noindex-and-nofollow.html")

@app.route("/crawling-and-indexing/canonicals")
def canonicals():
    return render_template("canonicals.html")

@app.route("/on-page/heading-tags")
def headings():
    return render_template("/heading-tags.html")

@app.route("/on-page/meta-data")
def metadata():
    return render_template("meta-data.html")

@app.route("/on-page/page-titles")
def titles():
    return render_template("page-titles.html")

@app.route("/on-page/meta-descriptions")
def descriptions():
    return render_template("meta-descriptions.html")

@app.route("/on-page/alt-text")
def alttext():
    return render_template("alt-text.html")

@app.route("/site-structure/site-architecture")
def architecture():
    return render_template("site-architecture.html")

@app.route("/site-structure/sitemap")
def sitemap():
    return render_template("sitemaps.html")

@app.route("/site-structure/urls")
def urls():
    return render_template("urls.html")

@app.route("/site-structure/https")
def https():
    return render_template("HTTPs.html")

@app.route("/user-experience/site-speed")
def speed():
    return render_template("site-speed.html")

@app.route("/user-experience/accessibility")
def accessibility():
    return render_template("accessibility.html")

if __name__ == "__main__":
    app.run(debug=True)