PRICE_PER_LITRE = 10
transactions = []
seen_ids = set()
 
def is_valid_id(tid):
    return isinstance(tid, str) and tid.startswith('W') and len(tid) >= 4
 
def is_valid_customer(c):
    return isinstance(c, str) and c.startswith('C') and len(c) >= 4
 
def is_valid_point(p):
    return isinstance(p, str) and p.startswith('KLA') and len(p) >= 5
 
def register_transaction(tid, customer, point, quantity):
    if not is_valid_id(tid):
        return False, 'Invalid transaction ID'
    if tid in seen_ids:
        return False, 'Duplicate transaction ID'
    if not is_valid_customer(customer):
        return False, 'Invalid customer reference'
    if not is_valid_point(point):
        return False, 'Invalid supply point'
    try:
        qty = float(quantity)
    except (TypeError, ValueError):
        return False, 'Quantity must be numeric'
    if qty <= 0:
        return False, 'Quantity must be positive'
    amount = qty * PRICE_PER_LITRE
    record = {
        'id': tid,
        'customer': customer,
        'point': point,
        'quantity': qty,
        'amount': amount
    }
    transactions.append(record)
    seen_ids.add(tid)
    return True, 'Registered successfully'
 
def display_all():
    for r in transactions:
        print(r)
 
def search_by_customer(customer):
    return [r for r in transactions if r['customer'] == customer]
 
def total_quantity():
    return sum(r['quantity'] for r in transactions)
 
def total_revenue():
    return sum(r['amount'] for r in transactions)
 
def customer_highest_quantity():
    from collections import defaultdict
    cum = defaultdict(float)
    for r in transactions:
        cum[r['customer']] += r['quantity']
    if not cum:
        return None, 0
    best = max(cum, key=cum.get)
    return best, cum[best]
