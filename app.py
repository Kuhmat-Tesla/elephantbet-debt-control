from flask import Flask, render_template
import database
from routes.customers import customers_bp
from routes.debts import debts_bp
from routes.payments import payments_bp

app = Flask(__name__)
app.register_blueprint(customers_bp)
app.register_blueprint(debts_bp)
app.register_blueprint(payments_bp)

with app.app_context():
    database.create_tables()

@app.route('/')
def index():
    return render_template('base.html')

    

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
