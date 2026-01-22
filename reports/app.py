from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
@app.route("/reports")
def reports():
    html = """
    <html>
    <head>
        <title>Reports Dashboard</title>
        <style>
            body {
                font-family: Arial;
                background: linear-gradient(120deg,#42275a,#734b6d);
                color: white;
                padding: 40px;
            }
            table {
                background: white;
                color: #333;
                border-radius: 12px;
                padding: 20px;
            }
            td {
                padding: 10px 20px;
            }
        </style>
    </head>
    <body>
        <h1>📄 Reports</h1>
        <table>
            <tr><td>Monthly Revenue</td><td><b>$82,000</b></td></tr>
            <tr><td>User Growth</td><td><b>18%</b></td></tr>
            <tr><td>System Status</td><td><b>Operational</b></td></tr>
        </table>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

