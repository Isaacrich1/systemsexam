vehicles = []
 
def process_vehicles():
    try:
        count = int(input('Number of vehicles: '))
    except ValueError:
        print('Invalid count')
        return
 
    for _ in range(count):
        reg = input('Registration: ').strip()
        try:
            dist = float(input('Distance travelled: '))
            fuel = float(input('Fuel consumed: '))
        except ValueError:
            print('Non-numeric input – rejected')
            continue
        if dist < 0 or fuel <= 0:
            print('Negative or zero values – rejected')
            continue
 
        eff = dist / fuel
        if eff >= 15:
            cls = 'Efficient'
        elif eff >= 10:
            cls = 'Moderate'
        else:
            cls = 'Inefficient'
 
        vehicles.append({
            'reg': reg,
            'distance': dist,
            'fuel': fuel,
            'efficiency': eff,
            'class': cls
        })
