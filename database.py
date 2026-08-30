import sqlite3


def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS drivers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            license TEXT NOT NULL,
            plate TEXT NOT NULL,
            vehicle_type TEXT NOT NULL,
            capacity INTEGER NOT NULL,
            route TEXT NOT NULL,
            experience TEXT NOT NULL,
            verified INTEGER DEFAULT 0
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS schedules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            driver_id INTEGER,
            route TEXT NOT NULL,
            date TEXT NOT NULL,
            hour INTEGER NOT NULL,
            seats INTEGER NOT NULL,
            FOREIGN KEY (driver_id) REFERENCES drivers(id)
        )
    """)

    conn.commit()
    conn.close()

    print("GUZO PLUS database initialized successfully!")


if __name__ == "__main__":
    init_db()
