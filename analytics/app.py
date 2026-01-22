from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
@app.route("/analytics")
def analytics():
    html = """
    <html>
    <head>
        <title>Analytics Dashboard</title>
        <style>
            body {
                font-family: Arial;
                background: linear-gradient(120deg,#1e3c72,#2a5298);
                color: white;
                padding: 40px;
            }
            .card {
                background: white;
                color: #333;
                padding: 20px;
                border-radius: 12px;
                width: 250px;
                display: inline-block;
                margin: 15px;
            }
        </style>
    </head>
    <body>
        <h1>📊 Analytics Dashboard</h1>
        <div class="card">Active Users<br><b>1240</b></div>
        <div class="card">Requests / Min<br><b>342</b></div>
        <div class="card">CPU Usage<br><b>62%</b></div>
        <div class="card">Status<br><b style="color:green;">Healthy</b></div>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

