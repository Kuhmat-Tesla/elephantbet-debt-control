from flask import Blueprint, request, jsonify
from database import get_bd_connection

debts_bp = Blueprint("debts", __name__, url_prefix="/debts")

@debts_bp.route("/create/<customer_id>", methods=["POST"])
def debts_create(customer_id):
    ticket_ref = request.form["ticket_ref"]
    value = request.form["value"]
    description = request.form.get("description")
    if not ticket_ref or not value:
        return jsonify({"success": False, "error": "Campos vazios"}), 400
    with get_bd_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM debts WHERE ticket_ref = ?""", (ticket_ref,)
        )
        if cursor.fetchone() is not None:
            return jsonify({"success": False, "error": "Ticket já existe"}), 400
        cursor.execute("""INSERT INTO debts (ticket_ref, value, customer_id, description) VALUES (?, ?, ?, ?)""", (ticket_ref, value, customer_id, description)
        )
        return jsonify({"success": True}), 200

@debts_bp.route("/<customer_id>", methods=["GET"])
def debts_get(customer_id):
    with get_bd_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM debts WHERE customer_id = ?""", (customer_id,))
        rows = cursor.fetchall()
        data = jsonify([dict(row) for row in rows])
        return data

@debts_bp.route("/update/<id>", methods=["POST"])
def debts_update(id):
    ticket_ref = request.form["ticket_ref"]
    value = request.form["value"]
    description = request.form.get("description")
    if not ticket_ref or not value:
        return jsonify({"success": False, "error": "Campos vazios"}), 400
    with get_bd_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""UPDATE debts SET ticket_ref = ?, value = ?, description =? WHERE id = ? """, (ticket_ref, value, description, id))
    return jsonify({"success": True}), 200

@debts_bp.route("/delete/<id>", methods=["DELETE"])
def debts_delete(id):
    with get_bd_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""DELETE FROM debts WHERE id = ?""", (id,))
    return jsonify({"success": True}), 200
