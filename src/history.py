from dataclasses import dataclass
from order import Order


@dataclass
class SalesHistory:
    orders: list[Order]
