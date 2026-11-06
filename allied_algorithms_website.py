"""A standalone Python version of the Allied Algorithms website.
Run with: python allied_algorithms_website.py
Then open: http://localhost:8000
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from html import escape

HOST = "0.0.0.0"
PORT = 8000


def page():
    return """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Allied Algorithms | A.I.M.</title>
<style>
:root { --green:#245c45; --light:#eef5ef; --cream:#fbfaf4; --dark:#18352a; --accent:#d7a84c; }
* { box-sizing:border-box; }
body { margin:0; font-family:Arial, sans-serif; color:var(--dark); background:var(--cream); line-height:1.6; }
header { position:sticky; top:0; z-index:5; background:white; border-bottom:1px solid #dfe8df; }
.nav { max-width:1100px; margin:auto; padding:16px 24px; display:flex; align-items:center; justify-content:space-between; gap:20px; }
.logo { font-weight:800; letter-spacing:.06em; color:var(--green); }
nav a { color:var(--dark); text-decoration:none; margin-left:18px; font-weight:600; }
.btn { display:inline-block; background:var(--green); color:white; padding:12px 20px; border-radius:8px; text-decoration:none; border:0; cursor:pointer; font-weight:700; }
.hero { min-height:480px; display:grid; place-items:center; text-align:center; padding:90px 24px; background:linear-gradient(135deg,#dcecdf,#f8f2dc); }
.hero h1 { font-size:clamp(2.4rem,6vw,5rem); margin:0 0 16px; color:var(--green); }
.hero p { font-size:1.2rem; max-width:680px; margin:0 auto 28px; }
section { padding:72px 24px; }
.wrap { max-width:1100px; margin:auto; }
.intro { text-align:center; max-width:760px; margin:auto; }
h2 { color:var(--green); font-size:2rem; margin-top:0; }
.steps { display:grid; grid-template-columns:repeat(4,1fr); gap:22px; margin-top:32px; }
.card { background:white; border:1px solid #dfe8df; border-radius:12px; padding:24px; box-shadow:0 4px 14px #18352a12; }
.number { font-size:2rem; font-weight:800; color:var(--accent); }
.stats { background:var(--light); }
.stats-grid { display:grid; grid-template-columns:repeat(2,1fr); gap:24px; text-align:center; }
.stat { font-size:3rem; font-weight:800; color:var(--green); }
.dashboard { display:grid; grid-template-columns:1.3fr 1fr; gap:30px; align-items:center; }
.map { min-height:300px; border-radius:12px; background:#cfe1ce; display:grid; place-items:center; color:var(--green); font-weight:700; border:2px dashed #7ca889; }
form { display:grid; gap:14px; max-width:650px; margin:24px auto 0; }
input, textarea { width:100%; padding:13px; border:1px solid #b9cbbd; border-radius:7px; font:inherit; }
textarea { min-height:120px; }
footer { background:var(--dark); color:white; padding:36px 24px; text-align:center; }
footer a { color:white; }
@media (max-width:760px) { .nav { flex-direction:column; } nav a { margin:0 8px; } .steps,.dashboard,.stats-grid { grid-template-columns:1fr; } }
</style>
</head>
<body>
<header><div class="nav"><div class="logo">ALLIED ALGORITHMS</div><nav>
<a href="#about">About</a><a href="#how">How to Use</a><a href="#dashboard">Dashboard</a><a class="btn" href="#report">Submit a Sighting</a>
</nav></div></header>

<main>
<section class="hero"><div><h1>A.I.M.</h1><p>Allied Invasive Mapping</p><p>Help make it easier for people to recognize, locate, and report Multiflora Rose plants.</p><a class="btn" href="#report">Submit a Sighting</a></div></section>

<section id="about"><div class="wrap intro"><h2>Our goal</h2><p>Our goal is to make it easier for people to recognize and report invasive plants. Use this site to identify Multiflora Rose, locate a plant, submit observations, and verify the data.</p></div></section>

<section id="how" style="background:#f1f6f1"><div class="wrap"><h2>How to Use</h2><div class="steps">
<div class="card"><div class="number">01</div><h3>Identify the Plant</h3><p>Locate a Multiflora Rose plant by its distinctive features.</p></div>
<div class="card"><div class="number">02</div><h3>Map the Location</h3><p>Use the interactive map to record where the plant was found.</p></div>
<div class="card"><div class="number">03</div><h3>Submit the Report</h3><p>Fill out the form with the site name, date, observations, and other details.</p></div>
<div class="card"><div class="number">04</div><h3>Verify the Data</h3><p>Review submitted details and confirm the report.</p></div>
</div></div></section>

<section class="stats"><div class="wrap"><div class="stats-grid"><div class="card"><div class="stat">10</div><div>Total Reported</div></div><div class="card"><div class="stat">10</div><div>Map Markers</div></div></div></div></section>

<section id="dashboard"><div class="wrap dashboard"><div><h2>Location Dashboard</h2><p>Explore reported Multiflora Rose locations and help build a clearer picture of invasive plant activity.</p><div class="map">Interactive map area</div></div><div class="card"><div class="stat">10</div><p>Total reported sightings</p></div></div></section>

<section id="report" style="background:#f1f6f1"><div class="wrap intro"><h2>Report a Sighting</h2><p>Submit your observations of Multiflora Rose or invasive plants in your area.</p><form method="post"><input name="site_name" placeholder="Site name" required><input name="date" type="date" required><textarea name="observations" placeholder="Observations" required></textarea><button class="btn" type="submit">Submit Report</button></form></div></section>
</main>

<footer><p>123 Eco-Trail, Green Valley, CA 90210</p><p><a href="mailto:hello@multiflora-rose.org">hello@multiflora-rose.org</a></p><p>© 2026 ALLIED ALGORITHMS. ALL RIGHTS RESERVED.</p></footer>
</body>
</html>"""


class SiteHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path.startswith("/?"):
            body = page().encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_error(404)

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length).decode("utf-8")
        data = parse_qs(raw)
        name = escape(data.get("site_name", [""])[0])
        response = f"<h1>Thank you</h1><p>Your sighting for {name or 'the selected site'} was received.</p><p><a href='/'>Return to the website</a></p>"
        body = response.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    print(f"Serving Allied Algorithms at http://localhost:{PORT}")
    HTTPServer((HOST, PORT), SiteHandler).serve_forever()
