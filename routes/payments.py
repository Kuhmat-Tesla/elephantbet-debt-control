from flask import Blueprint

payments_bp = Blueprint("payments", __name__, url_prefix="/payments")

@payments_bp.route("/create")
def create():
    return "Paymemt create"

@payments_bp.route("/<id>")
def get_payments(id):
    return "Get payment"

@payments_bp.route("/delete/<id>")
def delete_payments(id):
    return "Delete payment"