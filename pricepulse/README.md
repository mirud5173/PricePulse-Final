# 📉 PricePulse

**PricePulse** is a FastAPI-based web application that tracks e-commerce product prices, visualizes their history in real-time, and sends email alerts when target prices are met.

---

## 🚀 Features

- 📊 Real-time price tracking with Chart.js dashboard
- 🔁 Automatic scraping every 30 minutes
- ✅ User authentication system
- ✉️ Email alerts when products reach target price
- 🗑️ Delete products and their history from dashboard
- 🕒 Timezone-aware price history (IST)

---

## 🛠️ Installation

### 1. Clone the Repository

```
git clone https://github.com/<your-username>/pricepulse.git
cd pricepulse
```
2. Create Virtual Environment & Install Dependencies
```
pip install fastapi uvicorn sqlalchemy jinja2 aiosqlite apscheduler python-dotenv playwright
playwright install
```
3. Set Up Environment Variables
Create a .env file in the root directory with the following:

```
EMAIL_USER=your-email@gmail.com
EMAIL_PASS=your-password
```
4. Run the App
```
uvicorn backend.main:app --reload
```
Visit http://127.0.0.1:8000 in your browser.

📁 Project Structure
```
pricepulse/
├── backend/
│   ├── auth.py
│   ├── database.py
│   ├── email_utils.py
│   ├── main.py
│   ├── models.py
│   ├── scheduler.py
│   ├── schemas.py
│   ├── scraper.py
│   └── routers/
│       ├── alerts.py
│       ├── prices.py
│       ├── products.py
│       ├── scrape.py
│       └── users.py
├── frontend/
│   ├── dashboard.html
│   ├── login.html
│   └── styles.css
├── .env
├── prices.db
└── README.md
```
### 🧑‍💻 Author

Developed by Mirudhula. Contributions and feedback are welcome!
