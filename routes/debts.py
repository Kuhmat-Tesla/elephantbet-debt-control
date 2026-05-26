from flask import Blueprint

debts_bp = Blueprint("debts", __name__, url_prefix="/debts")

@debts_bp.route("/create")
def debts_create():
    return "Debt cteate"

@debts_bp.route("/<id>")
def debts_get(id):
    return f"Dept get {id}"

@debts_bp.route("/update/<id>")
def debts_update(id):
    return f"Depts update {id}"

@debts_bp.route("/delete/<id>")
def debts_delete(id):
    return f"Depts delete {id}"