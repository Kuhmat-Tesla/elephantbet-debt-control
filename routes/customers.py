from flask import Blueprint, redirect, url_for, request, jsonify
from database import get_bd_connection

customers_bp = Blueprint("customers", __name__, url_prefix="/customers")

@customers_bp.route("/")
def customers_list():
    with get_bd_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT 
                customers.id,
                customers.name,
                customers.phone,
                (SELECT SUM(debts.value) FROM debts WHERE debts.customer_id = customers.id) as total_debts,
                (SELECT SUM(payments.amount) FROM payments WHERE payments.customer_id = customers.id) as total_paid
            FROM customers
        """)
        rows = cursor.fetchall()
        data = [dict(row) for row in rows]
        return jsonify(data)

@customers_bp.route("/create", methods=["POST"])
def customer_create():
    phone = request.form.get("phone")
    name = request.form["name"]
    if not name:
        return "Nome obrigatório", 400
    with get_bd_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO customers (name, phone) VALUES (?,?)
        """, (name, phone))
        return redirect(url_for("customers.customers_list"))

@customers_bp.route("/update/<id>", methods=["POST"])
def customer_update(id):
    name = request.form["name"]
    phone = request.form.get("phone")
    if not name:
        return "Nome obrigatório", 400
    with get_bd_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""UPDATE customers SET name = ?, phone = ? WHERE id = ?""", (name, phone, id))
        return jsonify({"success":True}), 200

@customers_bp.route("/delete/<id>", methods=["DELETE"])
def customer_delete(id):
    with get_bd_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""DELETE FROM customers WHERE id = ?""", (id,))
        return redirect(url_for("customers.customers_list"))
