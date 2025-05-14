import os
from flask import Flask, render_template, request, flash
from bot import BasicBot
import logging

app = Flask(__name__)
app.secret_key = os.urandom(24)

bot = BasicBot()

logging.basicConfig(level=logging.INFO)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/order", methods=["POST"])
def place_order():
    symbol = request.form.get("symbol", "").upper()
    side = request.form.get("side", "").upper()
    order_type = request.form.get("order_type", "").upper()
    quantity = request.form.get("quantity", "")
    price = request.form.get("price", "")
    stop_price = request.form.get("stop_price", "")

    response_message = None
    try:
        quantity = float(quantity)
        price = float(price) if price else None
        stop_price = float(stop_price) if stop_price else None

        order = bot.place_order(symbol, side, order_type, quantity, price, stop_price)
        app.logger.info(f"Order placed: {order}")
        response_message = f"Order placed successfully. {order}"

    except Exception as e:
        response_message = f"Error placing order: {str(e)}"
        app.logger.error(response_message)

    return render_template("index.html", response_message=response_message)

if __name__ == "__main__":
    app.run(debug=True)