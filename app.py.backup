
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


# ==========================================
# DATABASE CONNECTION
# ==========================================

def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def home():
    return render_template("index.html")
@app.route('/vehicle')
def vehicle():
    return render_template('vehicle.html')

# ==========================================
# DRIVER PAGE
# ==========================================

@app.route("/driver", methods=["GET", "POST"])
def driver():

    conn = get_db_connection()

    if request.method == "POST":

        name = request.form["name"]
        phone = request.form["phone"]
        license_number = request.form["license"]
        plate = request.form["plate"]
        vehicle_type = request.form["vehicle_type"]
        capacity = request.form["capacity"]
        route = request.form["route"]
        experience = request.form["experience"]

        conn.execute("""
            INSERT INTO drivers
            (name, phone, license, plate, vehicle_type, capacity, route, experience)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            name,
            phone,
            license_number,
            plate,
            vehicle_type,
            capacity,
            route,
            experience
        ))

        conn.commit()
        conn.close()

        return redirect(url_for("driver"))

    drivers = conn.execute(
        "SELECT * FROM drivers ORDER BY id DESC"
    ).fetchall()

    conn.close()

    return render_template(
        "driver.html",
        drivers=drivers
    )


# ==========================================
# DRIVER MANAGEMENT
# ==========================================

@app.route("/driver-management")
def driver_management():
    return redirect(url_for("driver"))


# ==========================================
# SCHEDULE PAGE
# ==========================================

@app.route("/schedule")
def schedule():
    return render_template("schedule.html")


# ==========================================
# SMART DASHBOARD
# ==========================================

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# ==========================================
# AI TRAFFIC PREDICTION
# ==========================================

@app.route("/traffic")
def traffic():
    return render_template("traffic.html")


# ==========================================
# SMART ETA
# ==========================================

@app.route("/eta")
def eta():
    return render_template("eta.html")


# ==========================================
# SMART SCHEDULING
# ==========================================

@app.route("/smart-schedule")
def smart_schedule():
    return render_template("schedule.html")


# ==========================================
# ACCIDENT DETECTION
# ==========================================

@app.route("/accident")
def accident():
    return render_template("accident.html")


# ==========================================
# PASSENGER DEMAND
# ==========================================

@app.route("/demand")
def demand():
    return render_template("demand.html")


# ==========================================
# SMART ROUTE MANAGEMENT
# ==========================================

@app.route("/routes")
def routes():
    return render_template("routes.html")


# ==========================================
# PASSENGER PAGE
# ==========================================

@app.route("/passenger")
def passenger():
    return render_template("passenger.html")


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)

