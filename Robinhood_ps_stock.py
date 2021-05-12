import heapq


class OrderType:
    BUY = "buy"
    SELL = "sell"


class Order:
    def __init__(self, type, price, quantity):
        self.type = type
        self.price = price
        self.quantity = quantity

    def __lt__(self, other_order):
        return self.price < other_order.price if other_order.type == OrderType.SELL else self.price >= other_order.price

    def __gt__(self, other_order):
        return self.price > other_order.price if other_order.type == OrderType.SELL else self.price <= other_order.price

    def __eq__(self, other_order):
        return self.price == other_order.price


class Order_Book:
    def __init__(self):
        self.buy_order_book = []
        self.sell_order_book = []

    def order_matching(self, orders):
        ans = 0
        for i, (price, quantity, type) in enumerate(orders):
            curr_order = Order(type, int(price), int(quantity))
            if type == OrderType.BUY:
                while curr_order.quantity and self.sell_order_book and self.sell_order_book[0].price < curr_order.price:
                    sell_order = heapq.heappop(self.sell_order_book)
                    ans += min(curr_order.quantity, sell_order.quantity)
                    if sell_order.quantity > curr_order.quantity:
                        sell_order.quantity -= curr_order.quantity
                        heapq.heappush(self.sell_order_book, sell_order)
                    curr_order.quantity = max(curr_order.quantity - sell_order.quantity, 0)

                if curr_order.quantity:
                    heapq.heappush(self.buy_order_book, curr_order)
            elif type == OrderType.SELL:
                while curr_order.quantity and self.buy_order_book and self.buy_order_book[0].price > curr_order.price:
                    buy_order = heapq.heappop(self.buy_order_book)
                    ans += min(curr_order.quantity, buy_order.quantity)
                    if buy_order.quantity > curr_order.quantity:
                        buy_order.quantity -= curr_order.quantity
                        heapq.heappush(self.buy_order_book, buy_order)
                        curr_order.quantity = max(curr_order.quantity - buy_order.quantity, 0)

                if curr_order.quantity:
                    heapq.heappush(self.sell_order_book, curr_order)

        return ans


if __name__ == "__main__":
    order_book = Order_Book()
    orders = [['150', '5', 'buy'], ['190', '1', 'sell'],
              ['200', '1', 'sell'], ['100', '9', 'buy'],
              ['140', '8', 'sell'], ['210', '4', 'buy']]
    print(order_book.order_matching(orders))
