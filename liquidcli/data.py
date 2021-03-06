from dataclasses import dataclass
from typing import List


@dataclass
class Execution:
    id: int = ''
    quantity: float = 0
    price: float = 0
    taker_side: str = ''
    created_at: int = 0


@dataclass
class FiatAccount:
    id: int = 0
    currency: str = ''
    currency_symbol: str = ''
    balance: float = 0
    reserved_balance: float = 0
    pusher_channel: str = ''
    lowest_offer_interest_rate: float = 0
    highest_offer_interest_rate: float = 0
    exchange_rate: float = 0
    currency_type: str = ''


@dataclass
class AccountDetail:
    id: int = 0
    currency: str = ''
    balance: float = 0
    free_balance: float = 0
    reserved_balance: float = 0
    pnl: float = 0
    margin: float = 0
    maintenance_margin: float = 0


@dataclass
class CryptoAccount:
    id: int = 0
    balance: float = 0
    reserved_balance: float = 0
    address: str = ''
    currency: str = ''
    currency_symbol: str = ''
    pusher_channel: str = ''
    minimum_withdraw: float = 0
    lowest_offer_interest_rate: float = 0
    highest_offer_interest_rate: float = 0
    currency_type: str = ''


@dataclass
class ReservedBalance:
    object_type: str = ''
    object_id: int = -1
    amount: float = -1


@dataclass
class Page:
    current_page: int
    total_pages: int
    models: List[object]


@dataclass
class Order:
    id: int = 0
    order_type: str = ''
    margin_type: str = ''
    quantity: float = 0
    disc_quantity: float = ''
    iceberg_total_quantity: float = 0
    side: str = ''
    filled_quantity: float = 0
    price: float = 0
    updated_at: int = 0
    created_at: int = 0
    status: str = ''
    product_id: int = 0
    product_code: str = ''
    funding_currency: str = ''
    currency_pair_code: str = ''
    order_fee: float = 0
    client_order_id: str = ''
    executions: List[Execution] = None
