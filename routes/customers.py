from flask import Blueprint, redirect, url_for, request, jsonify
from database import get_bd_connection

customers_bp = Blueprint("customers", __name__, url_prefix="/customers")

@customers_bp.route("/")
def customers_list():
    with get_bd_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM customers
        """)
        rows = cursor.fetchall()
        data = [dict(row) for row in rows]
        return jsonify(data)

@customers_bp.route("/create", methods=["POST"])
def customer_create():
    phone = request.form["phone"]
    name = request.form["name"]
    if not name:
        return "Nome obrigatório", 400
    with get_bd_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO customers (name, phone) VALUES (?,?)
        """, (name, phone))
        return redirect(url_for("customers.customers_list"))

@customers_bp.route("/update/<id>")
def customer_update(id):
    return "Customer update"

@customers_bp.route("/delete/<id>")
def customer_delete(id):
    return "Delete customer"

