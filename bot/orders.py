from binance.exceptions import BinanceAPIException
from bot.logging_config import logger


def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logger.info(
            f"Request: symbol={symbol}, side={side}, "
            f"type={order_type}, qty={quantity}, price={price}"
        )

        params = {
            "symbol": symbol.upper(),
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        response = client.futures_create_order(**params)

        logger.info(response)

        return response

    except BinanceAPIException as e:
        logger.error(e.message)
        raise

    except Exception as e:
        logger.exception(e)
        raise