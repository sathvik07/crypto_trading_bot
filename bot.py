from binance.client import Client
from binance.exceptions import BinanceAPIException
from config import API_KEY, API_SECRET, BASE_URL
from logger import logger

class BasicBot:
    def __init__(self):
        self.client = Client(API_KEY, API_SECRET, testnet=True)
        self.client.FUTURES_URL = BASE_URL
        self.client.API_URL = BASE_URL
        logger.info("Initialized Binance Futures client")

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        try:
            order_type = order_type.upper()
            params = {
                "symbol": symbol,
                "side": side.upper(),
                "type": order_type,
                "quantity": quantity
            }

            if order_type == "MARKET":
                pass

            elif order_type == "LIMIT":
                if price is None:
                    raise ValueError("Price is required for LIMIT orders.")
                params["price"] = f"{price:.2f}"
                params["timeInForce"] = "GTC"

            else:
                raise ValueError(f"Unsupported order type: {order_type}")

            logger.info(f"Sending order with params: {params}")
            order = self.client.futures_create_order(**params)
            logger.info(f"Order response: {order}")
            return order

        except BinanceAPIException as e:
            logger.error(f"Binance API error: {e}")
            return {"error": str(e)}

        except Exception as e:
            logger.exception("Unexpected error occurred during order placement")
            return {"error": str(e)}
