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

@app.route("/links/internal-links")
def internallinks():
    return render_template("internal-links.html")

@app.route("/links/backlinks")
def backlinks():
    return render_template("backlinks.html")

@app.route("/links/redirects")
def redirects():
    return render_template("redirects.html")

@app.route("/international-seo/hreflang")
def hreflang():
    return render_template("hreflang.html")

@app.route("/international-seo/tld-and-cctld")
def tld_cctld():
    return render_template("tld-and-cctld.html")

@app.route("/cls-test")
def cls_test():
    return render_template("cls-test.html")

@app.route("/cls-test-2")
def cls_test_2():
    return render_template("cls-test-2.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/blog/technical-seo")
def technicalseo():
    return render_template("technicalseo.html")

@app.route("/blog/python")
def pythonblog():
    return render_template("pythonblog.html")

@app.route("/blog/personal-development")
def personaldevelopment():
    return render_template("personaldevelopment.html")

@app.route("/blog/tech-ethics")
def techethics():
    return render_template("techethics.html")

@app.route("/blog/machine-learning")
def machinelearning():
    return render_template("machinelearningblog.html")

@app.route("/blog/dogs")
def dogs():
    return render_template("dogs.html")

if __name__ == "__main__":
    app.run(debug=True)