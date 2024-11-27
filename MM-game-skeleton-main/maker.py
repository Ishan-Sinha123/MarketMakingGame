from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Tuple, Literal

@dataclass
class OrderType:
    """
    Data class to represent the order type, which can be either "limit" or "market"
    """
    type: Literal["limit", "market"]
    from_time: int
    to_time: int

    def __init__ (self, type: Literal["limit", "market"], from_time: int, to_time: int):
        self.type = type
        self.from_time = from_time
        self.to_time = to_time

    def __str__(self):
        return f"OrderType(type={self.type}, from_time={self.from_time}, to_time={self.to_time})"
    
    def new_limit_order(from_time: int, to_time: int):
        """
        Create a new limit order with the given from_time and to_time
        """
        return OrderType("limit", from_time, to_time)
    
    def new_market_order(timestamp: int):
        """
        Create a new market order with the given timestamp
        """
        return OrderType("market", timestamp, timestamp)

class MarketMaker(ABC):
    """
    Abstract class for market maker, where each player will use previous interval data to make decisions
    to buy or sell stocks. The market maker will return the bid and ask prices, and the volume to buy and sell.
    The bid price represents the highest amount a buyer is willing to pay for a stock, 
    while the ask price describes the lowest level at which a seller is willing to sell their shares
    """
    @abstractmethod
    def update(self, prev_bid_price, prev_ask_price, holding, money, timestamp) -> Tuple[float, int, float, int, OrderType]:
        """
        Update the market maker with the previous bid and ask prices, and the timestamp of the current interval,
        and return the new bid and ask prices, and the volume to buy and sell

        There are two type of order you can make each time interval: market order and limit order.

        Market order: an order to buy or sell a stock at the current market price. The buy and sell price
        is determined by the market (not you). Market order doesn't have a time frame. If you are setting the
        next bid price and next ask price for a market order, it will be defaulted to the market bid and ask price.

        Limit order: an order to buy or sell a stock at a specific price or better. 
        A buy limit order can only be executed at the limit price or lower (compare to market ask/sell price), 
        and a sell limit order can only be executed at the limit price or higher (compare to market bid/buy price). 
        Limit order have a time frame, from_time and to_time, which specifies the time interval in which the
        order is valid.

        Market order have higher priority than limit order. If you are setting both market order and limit order
        in a given time interval, the market order will be executed first.

        :param prev_bid_price: the previous bid price
        :param prev_ask_price: the previous ask price
        :param holding: the number of stocks you are holding from previous interval
        :param money: the amount of money you have from previous interval
        :param timestamp: the timestamp of the current (not previous) interval

        :return: a tuple containing the new bid price limit, the volume to buy, the new ask price limit, 
        the volume to sell, and the order type as OrderType object
        """
        pass

class SimpleMarketMaker(MarketMaker):
        """
        An example on how to implement a market maker.
        """
        def __init__(self):
             pass
        
        # TODO: Replace this example with your strategy
        def update(self, prev_bid_price, prev_ask_price, holding, money, timestamp) -> Tuple[float, int, float, int, OrderType]:
            """
            Example on how to implement the update method for the market maker.

            This example will return the previous bid price and ask price, and the volume to buy and sell
            as 100, and a new limit order with the timestamp and timestamp + 100.

            To return a market order, you can use OrderType.new_market_order(timestamp)
            ```
            return prev_bid_price, 100, prev_ask_price, 100, OrderType.new_market_order(timestamp)
            ```
            For market order, the limit price will be defaulted to the market bid and ask price.

            Note that the volume to buy and sell can be any integer value, including 0. If the volume is negative,
            it will be set to 0. If the volume to sell is more than the holding, it will be set to the holding.

            :param prev_bid_price: the previous bid price
            :param prev_ask_price: the previous ask price
            :param holding: the number of stocks you are holding from previous interval
            :param money: the amount of money you have from previous interval
            :param timestamp: the timestamp of the current (not previous) interval

            :return: a tuple containing the new bid price limit, the volume to buy, the new ask price limit,
            the volume to sell, and the order type as OrderType object

            """
            return prev_bid_price, 100, prev_ask_price, 100, OrderType.new_limit_order(timestamp, timestamp + 100)
