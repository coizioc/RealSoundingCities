cities = {}
with open('cities.txt', 'r', encoding='utf-8') as f:
    rows = f.read().splitlines()
    for row in rows:
        country, city = row.split(',')
        if country not in cities.keys():
            cities[country] = 0
        cities[country] += 1

i = 1
for country, num_cities in sorted(cities.items(), key=lambda x:(x[1],x[0]), reverse=True):
    print('%3d) %4d %s' % (i, num_cities, country))
    i += 1