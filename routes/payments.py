from flask import Blueprint, request, jsonify
from database import get_bd_connection

payments_bp = Blueprint("payments", __name__, url_prefix="/payments")

@payments_bp.route("/create/<debt_id>")
def create(debt_id):
    amount = request.form["amount"]
    note = request.form("amount")
    if not amount:
        return jsonify({"success": False, "error": "Campos vazios"}), 200
    with get_bd_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO payments (amount, note, debt_id) VALUES (?, ?, ?)""", (amount, note, debt_id)
        )
    return jsonify({"sucess": True}), 200

@payments_bp.route("/<debt_id>")
def get_payments(debt_id):
    return "Get payment"

@payments_bp.route("/delete/<id>")
def delete_payments(id):
    return "Delete payment"