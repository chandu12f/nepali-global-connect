import os
from flask import Flask, render_template_string

app = Flask(__name__)

HTML_LAYOUT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nepali Global Connect</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; background-color: #f4f6f9; color: #333; }
        header { background-color: #1a365d; color: white; padding: 2rem; text-align: center; }
        h1 { margin: 0; font-size: 2.5rem; }
        p { font-size: 1.1rem; }
        .container { max-width: 800px; margin: 2rem auto; padding: 2rem; background: white; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: center; }
        .btn { display: inline-block; padding: 10px 20px; background-color: #e53e3e; color: white; text-decoration: none; border-radius: 5px; margin-top: 1rem; font-weight: bold; }
        .btn:hover { background-color: #c53030; }
    </style>
</head>
<body>
    <header>
        <h1>🇳🇵 Nepali Global Connect</h1>
        <p>Connecting Nepalese Community Worldwide</p>
    </header>
    <div class="container">
        <h2>Welcome to Our Platform</h2>
        <p>Your web service is officially live, running, and accessible globally!</p>
        <a href="#" class="btn">Explore Community</a>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_LAYOUT)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
