from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
import math
import random
from database import init_db

init_db()

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


# ==========================================
# VEHICLE PAGE
# ==========================================

@app.route("/vehicle")
def vehicle():
    return render_template("vehicle.html")


# ==========================================
# DRIVER PAGE
# ==========================================

@app.route("/driver", methods=["GET", "POST"])
def driver():

    conn = get_db_connection()

    if request.method == "POST":

        name = request.form.get("name", "")
        phone = request.form.get("phone", "")
        license_number = request.form.get("license", "")
        plate = request.form.get("plate", "")
        vehicle_type = request.form.get("vehicle_type", "")
        capacity = request.form.get("capacity", 0)
        route = request.form.get("route", "")
        experience = request.form.get("experience", "")

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
# SCHEDULE
# ==========================================

@app.route("/schedule")
def schedule():
    return render_template("schedule.html")


@app.route("/smart-schedule")
def smart_schedule():
    return render_template("schedule.html")


# ==========================================
# DASHBOARD
# ==========================================

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# ==========================================
# TRAFFIC PREDICTION
# ==========================================

@app.route("/traffic")
def traffic():
    return render_template("traffic.html")


# ==========================================
# ETA
# ==========================================

@app.route("/eta")
def eta():
    return render_template("eta.html")


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
# ROUTES
# ==========================================

@app.route("/routes")
def routes():
    return render_template("routes.html")


# ==========================================
# PASSENGER
# ==========================================

@app.route("/passenger")
def passenger():
    return render_template("passenger.html")


# ==========================================
# FAKE GPS VEHICLE DATA
# ==========================================

VEHICLES = [
    {
        "id": "BUS-01",
        "type": "Bus",
        "icon": "🚌",
        "lat": 9.0300,
        "lng": 38.7500,
        "speed": 32,
        "route": "Bole → Mexico",
    },
    {
        "id": "BUS-02",
        "type": "Bus",
        "icon": "🚌",
        "lat": 9.0350,
        "lng": 38.7550,
        "speed": 28,
        "route": "Mexico → Piassa",
    },
    {
        "id": "BUS-03",
        "type": "Bus",
        "icon": "🚌",
        "lat": 9.0400,
        "lng": 38.7600,
        "speed": 35,
        "route": "Piassa → Megenagna",
    },
    {
        "id": "BUS-04",
        "type": "Bus",
        "icon": "🚌",
        "lat": 9.0250,
        "lng": 38.7450,
        "speed": 25,
        "route": "Merkato → Bole",
    },
    {
        "id": "BUS-05",
        "type": "Bus",
        "icon": "🚌",
        "lat": 9.0450,
        "lng": 38.7650,
        "speed": 30,
        "route": "Megenagna → Piassa",
    },
    {
        "id": "BUS-06",
        "type": "Bus",
        "icon": "🚌",
        "lat": 9.0200,
        "lng": 38.7400,
        "speed": 27,
        "route": "Bole → Merkato",
    },
    {
        "id": "BUS-07",
        "type": "Bus",
        "icon": "🚌",
        "lat": 9.0500,
        "lng": 38.7700,
        "speed": 31,
        "route": "Megenagna → Bole",
    },

    {
        "id": "MINI-01",
        "type": "Minibus",
        "icon": "🚐",
        "lat": 9.0320,
        "lng": 38.7520,
        "speed": 38,
        "route": "Bole → Piassa",
    },
    {
        "id": "MINI-02",
        "type": "Minibus",
        "icon": "🚐",
        "lat": 9.0380,
        "lng": 38.7580,
        "speed": 42,
        "route": "Mexico → Bole",
    },
    {
        "id": "MINI-03",
        "type": "Minibus",
        "icon": "🚐",
        "lat": 9.0280,
        "lng": 38.7480,
        "speed": 36,
        "route": "Merkato → Piassa",
    },

    {
        "id": "TRUCK-01",
        "type": "Truck",
        "icon": "🚚",
        "lat": 9.0420,
        "lng": 38.7620,
        "speed": 22,
        "route": "Akaki → Bole",
    },
    {
        "id": "TRUCK-02",
        "type": "Truck",
        "icon": "🚚",
        "lat": 9.0180,
        "lng": 38.7380,
        "speed": 20,
        "route": "Bole → Akaki",
    },

    {
        "id": "MOTO-01",
        "type": "Motorcycle",
        "icon": "🏍️",
        "lat": 9.0340,
        "lng": 38.7540,
        "speed": 48,
        "route": "Bole → Mexico",
    },
    {
        "id": "MOTO-02",
        "type": "Motorcycle",
        "icon": "🏍️",
        "lat": 9.0460,
        "lng": 38.7660,
        "speed": 52,
        "route": "Piassa → Megenagna",
    },
    {
        "id": "MOTO-03",
        "type": "Motorcycle",
        "icon": "🏍️",
        "lat": 9.0220,
        "lng": 38.7420,
        "speed": 45,
        "route": "Merkato → Bole",
    },

    {
        "id": "CAR-01",
        "type": "Private Car",
        "icon": "🚗",
        "lat": 9.0310,
        "lng": 38.7510,
        "speed": 40,
        "route": "Bole → Piassa",
    },
    {
        "id": "CAR-02",
        "type": "Private Car",
        "icon": "🚗",
        "lat": 9.0370,
        "lng": 38.7570,
        "speed": 43,
        "route": "Mexico → Bole",
    },
    {
        "id": "CAR-03",
        "type": "Private Car",
        "icon": "🚗",
        "lat": 9.0430,
        "lng": 38.7630,
        "speed": 37,
        "route": "Piassa → Bole",
    },
    
    {
        "id": "CAR-04",
        "type": "Private Car",
        "icon": "🚗",
        "lat": 9.0240,
        "lng": 38.7440,
        "speed": 39,
        "route": "Merkato → Mexico",
    },

    {
        "id": "AMB-01",
        "type": "Ambulance",
        "icon": "🚑",
        "lat": 9.0260,
        "lng": 38.7460,
        "speed": 60,
        "route": "Merkato → Bole",
        "emergency": True
    },

    {
        "id": "FIRE-01",
        "type": "Fire Truck",
        "icon": "🚒",
        "lat": 9.0340,
        "lng": 38.7540,
        "speed": 55,
        "route": "Mexico → Piassa",
        "emergency": True
    }
]



# ==========================================
# GPS PAGE
# ==========================================

@app.route("/gps")
def gps():
    return render_template("gps.html")


# ==========================================
# GPS API
# ==========================================

@app.route("/api/vehicles")
def api_vehicles():

    # Simulated movement
    for vehicle in VEHICLES:

        vehicle["lat"] += random.uniform(-0.00035, 0.00035)
        vehicle["lng"] += random.uniform(-0.00035, 0.00035)

        # Keep vehicles around Addis Ababa demo area
        vehicle["lat"] = max(8.995, min(9.075, vehicle["lat"]))
        vehicle["lng"] = max(38.710, min(38.800, vehicle["lng"]))

        # Small random speed change
        vehicle["speed"] += random.randint(-2, 2)
        vehicle["speed"] = max(5, min(70, vehicle["speed"]))

    return jsonify({
        "success": True,
        "count": len(VEHICLES),
        "vehicles": VEHICLES
    })


# ==========================================
# GPS VEHICLE SUMMARY
# ==========================================

@app.route("/api/vehicle-summary")
def vehicle_summary():

    summary = {
        "Bus": 0,
        "Minibus": 0,
        "Truck": 0,
        "Motorcycle": 0,
        "Private Car": 0
    }

    for vehicle in VEHICLES:
        summary[vehicle["type"]] += 1

    return jsonify(summary)
# ==========================================
# ACCIDENT DETECTION API
# ==========================================

@app.route("/api/accident-detection")
def accident_detection():

    # Simulated accident location
    incident_lat = 9.0240
    incident_lng = 38.7440

    nearby = []

    for vehicle in VEHICLES:

        # Skip emergency vehicles
        if vehicle.get("emergency"):
            continue

        # Calculate approximate distance
        lat_diff = vehicle["lat"] - incident_lat
        lng_diff = vehicle["lng"] - incident_lng

        distance_km = math.sqrt(
            lat_diff ** 2 + lng_diff ** 2
        ) * 111

        distance_m = distance_km * 1000

        item = dict(vehicle)

        item["distance_m"] = round(distance_m)

        # Simulated AI involvement score
        distance_score = max(
            1,
            100 - (distance_m / 500) * 100
        )

        speed_score = min(
            100,
            (vehicle["speed"] / 70) * 100
        )

        item["involvement_score"] = round(
            distance_score * 0.7 +
            speed_score * 0.3
        )

        nearby.append(item)

    # Sort by highest AI involvement score
    nearby.sort(
        key=lambda x: x["involvement_score"],
        reverse=True
    )

    # Always show the TOP 4 vehicles
    top_four = nearby[:4]

    return jsonify({
        "incident": {
            "detected": True,
            "location": "Bole Road",
            "lat": incident_lat,
            "lng": incident_lng,
            "type": "Vehicle Collision",
            "priority": "HIGH"
        },

        "vehicles": top_four,

        "emergency_vehicles": [
            vehicle
            for vehicle in VEHICLES
            if vehicle.get("emergency")
        ]
    })

# ==========================================
# HEALTH CHECK
# ==========================================

@app.route("/health")
def health():
    return jsonify({
        "status": "online",
        "system": "GUZO PLUS",
        "gps": "simulation",
        "vehicles": len(VEHICLES)
    })


# ==========================================
# RUN
# ==========================================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

