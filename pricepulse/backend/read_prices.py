import sqlite3

def read_prices():
    conn = sqlite3.connect("prices.db")
    c = conn.cursor()
    c.execute("SELECT * FROM product_prices")
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.close()

if __name__ == "__main__":
    read_prices()
