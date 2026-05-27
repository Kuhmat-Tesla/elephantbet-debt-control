from flask import Blueprint, request, jsonify
from database import get_bd_connection

payments_bp = Blueprint("payments", __name__, url_prefix="/payments")

@payments_bp.route("/create/<customer_id>", methods=["POST"])
def create(customer_id):
    amount = request.form["amount"]
    note = request.form.get("note")
    if not amount:
        return jsonify({"success": False, "error": "Campos vazios"}), 400
    with get_bd_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO payments (amount, note, customer_id) VALUES (?, ?, ?)""", (amount, note, customer_id)
        )
    return jsonify({"success": True}), 200

@payments_bp.route("/<customer_id>", methods=["GET"])
def get_payments(customer_id):
    with get_bd_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM payments WHERE customer_id = ?""", (customer_id,))
        rows = cursor.fetchall()
        data = jsonify([dict(row) for row in rows])
        return data

@payments_bp.route("/delete/<id>", methods=["DELETE"])
def delete_payments(id):
    with get_bd_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""DELETE FROM payments WHERE id = ?""", (id,))
    return jsonify({"success": True}), 200
