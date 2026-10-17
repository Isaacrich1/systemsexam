def save_transactions(filename='water_records.txt'):
    with open(filename, 'w') as f:
        for r in transactions:
            f.write(f"{r['id']},{r['customer']},{r['point']},"
                    f"{r['quantity']},{r['amount']}\n")
 
def load_transactions(filename='water_records.txt'):
    global transactions, seen_ids
    transactions = []
    seen_ids = set()
    try:
        with open(filename, 'r') as f:
            for line_no, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                parts = line.split(',')
                if len(parts) != 5:
                    print(f'Skipping bad line {line_no}')
                    continue
                tid, cust, point, qty_str, amt_str = parts
                try:
                    qty = float(qty_str)
                except ValueError:
                    print(f'Skipping line {line_no}: quantity is not a number')
                    continue
                ok, msg = register_transaction(tid, cust, point, qty)
                if not ok:
                    print(f'Skipping line {line_no}: {msg}')
    except FileNotFoundError:
        print('No previous file found – starting with empty list')
