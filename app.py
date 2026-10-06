import os
from flask import Flask, render_template_string

app = Flask(__name__)

PAGE = """
<!doctype html>
<html>
<head>
  <title>Jenkins + Docker App</title>
  <style>
    body { font-family: Arial, sans-serif; background:#0f172a; color:#e2e8f0;
           display:flex; justify-content:center; align-items:center; height:100vh; margin:0; }
    .card { background:#1e293b; padding:40px 60px; border-radius:12px; text-align:center; }
    h1 { color:#38bdf8; }
    .tag { background:#334155; padding:4px 12px; border-radius:20px; }
  </style>
</head>
<body>
  <div class="card">
    <h1>{{ message }}</h1>
    <p>Environment: <span class="tag">{{ env }}</span></p>
    <p>Build number: <span class="tag">#{{ build }}</span></p>
    <p>Secret configured: <span class="tag">{{ secret }}</span></p>
  </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(
        PAGE,
        message=os.getenv("APP_MESSAGE", "No message set"),
        env=os.getenv("APP_ENV", "unknown"),
        build=os.getenv("BUILD_NUMBER", "local"),
        secret="Yes" if os.getenv("API_KEY") else "No",
    )

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)