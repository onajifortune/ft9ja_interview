import decimal
from bson.decimal128 import Decimal128, create_decimal128_context

def data_convert(current_balance, profit_loss):
    d3 = current_balance + float(profit_loss)
    return d3