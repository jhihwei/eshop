from orders.models import OrderItem

def get_product_string(order_item:OrderItem):
  products =   [i.product.name+"#" for i in order_item]
  return "".join(products)