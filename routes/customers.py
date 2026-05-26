from flask import Blueprint

customers_bp = Blueprint("customers", __name__, url_prefix="/customers")

@customers_bp.route("/")
def customers_list():
    return "Customers list"

@customers_bp.route("/create")
def customer_create():
    return "Create customer"

@customers_bp.route("/update/<id>")
def customer_update(id):
    return "Customer update"

@customers_bp.route("/delete/<id>")
def customer_delete(id):
    return "Delete customer"

