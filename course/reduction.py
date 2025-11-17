# Remise de chacun de ces prix de 15%

def reduce(value):
  prices_discounted = []
  reduction = 0.85
  for price in value :
    price_without_euro = price[:-1]
    price_with_dot = price_without_euro.replace(',', '.')
    price_float = float(price_with_dot)
    prices_discounted.append(round(price_float * 0.85, 2))
  return prices_discounted


prices = ['24,99€', '12,75€', '9,99€']
print(reduce(prices))