with open('cities.txt', 'r', encoding='utf-8') as f:
    cities = f.read().splitlines()

def add_cities_from(filename, country):
    with open(filename, 'r', encoding='utf-8') as f:
        local_cities = f.read().splitlines()

    for city in local_cities:
        if city == '':
            continue
        newrow = f'{country},{city}'
        if newrow not in cities:
            cities.append(newrow)

    with open('cities.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(sorted(cities)))
