import sqlite3
DATABASE = "DATABASE.db"

def get_bd_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    with get_bd_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS customers(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            phone TEXT)
        """)
        cursor.execute("""CREATE TABLE IF NOT EXISTS debts(
            id INTEGER PRIMARY KEY,
            ticket_ref TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            value REAL NOT NULL,
            description TEXT,
            customer_id INTEGER NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customers(id)
        )
        """)
        cursor.execute("""CREATE TABLE IF NOT EXISTS payments(
            id INTEGER PRIMARY KEY,
            paid_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            amount REAL NOT NULL,
            note TEXT,
            debt_id INTEGER NOT NULL,
            FOREIGN KEY (debt_id) REFERENCES debts(id)
        )
        """)
    
