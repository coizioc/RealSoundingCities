import random
import math

from markov import Markov

def get_city():
    cities = {}
    with open('cities.txt', 'r', encoding='utf-8') as f:
        rows = f.read().splitlines()
        for row in rows:
            country, city = row.split(',')
            if country not in cities.keys():
                cities[country] = ''
            cities[country] += city + '\n'

    def combine(*args):
        def roundup(x):
            return int(math.ceil(x / 100.0)) * 100

        def lcm(numlist):
            lcm = numlist[0]
            for i in numlist[1:]:
                lcm = lcm * i / math.gcd(int(lcm), i)
            return lcm

        country_lens = []
        country_texts = []
        for arg in args:
            country_lens.append(roundup(len(cities[arg].splitlines())))
        lcm = lcm(country_lens)
        for i in range(len(country_lens)):
            country_cities = cities[args[i]]
            num_multiply = int(lcm / country_lens[i])
            for _ in range(num_multiply - 1):
                country_cities += cities[args[i]]
            country_texts.append(country_cities)
        return '\n'.join(country_texts)

    def select_countries():
        countries = []

        def select_country():
            while True:
                curr_country = random.choice(list(cities.keys()))
                if len(cities[curr_country].splitlines()) > 100 and curr_country not in countries:
                    countries.append(curr_country)
                    break

        select_country()
        num_cities = 1

        while random.randint(1, 30) == 1:
            num_cities += 1
            select_country()

        return countries

    rand_countries = select_countries()
    corpus = combine(*rand_countries)

    model = Markov(corpus)
    city_name = None
    while not city_name:
        city_name = model.get_word()

    mashup_edition = ''
    if len(rand_countries) > 1:
        mashup_edition = 'Special Mashup Edition:\n'
    tweet_str = f"{mashup_edition}{city_name}, {'-'.join(rand_countries)}"
    return tweet_str


# model_1 = Markov(corpus, 1)
# model_2 = Markov(corpus, 2)
# model_3 = Markov(corpus, 3)
#
# output_format = "%30s %30s %30s"
# print(f"Country: {', '.join(rand_countries)} ({sum([len(cities[x].splitlines()) for x in rand_countries])} cities)")
# print(output_format % ("State len: " + str(model_1.state_len),
#                 "State len: " + str(model_2.state_len),
#                 "State len: " + str(model_3.state_len)))
# for _ in range(20):
#     print(output_format % (model_1.get_word(), model_2.get_word(), model_3.get_word()))