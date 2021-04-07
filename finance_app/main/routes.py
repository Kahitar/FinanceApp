from flask import render_template, url_for, redirect, request, Blueprint
from finance_app.main.forms import SearchForm
from finance_app.models import Transaction


main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template("dashboard.html", assets=[])


@main.route("/transactions")
def transactions():
    return render_template('transactions.html')


@main.route("/dividends")
def dividends():
    return render_template('dividends.html')
