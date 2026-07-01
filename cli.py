import argparse
from bot.client import get_client
from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)
def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    side = validate_side(args.side)
    order_type = validate_order_type(args.type)
    quantity = validate_quantity(args.quantity)

    if order_type == "LIMIT":
        if args.price is None:
            raise ValueError("Price required for LIMIT order")
        price = validate_price(args.price)
    else:
        price = None

    print("\n========== ORDER REQUEST ==========")
    print(f"Symbol     : {args.symbol}")
    print(f"Side       : {side}")
    print(f"Type       : {order_type}")
    print(f"Quantity   : {quantity}")

    if price:
        print(f"Price      : {price}")

    client = get_client()

    response = place_order(
        client,
        args.symbol,
        side,
        order_type,
        quantity,
        price,
    )

    print("\n========== RESPONSE ==========")
    print("Order ID      :", response.get("orderId"))
    print("Status        :", response.get("status"))
    print("Executed Qty  :", response.get("executedQty"))
    print("Avg Price     :", response.get("avgPrice"))
    print("\n✅ Order placed successfully")


if __name__ == "__main__":
    main()