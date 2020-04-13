import random
import math

import pandas as pd

from markov import Markov

df = pd.read_csv('worldcitiespop2.csv')
print('loaded df')

def get_city():
    num_countries = 1
    while random.randint(1, 30) == 1:
        num_countries += 1
    countries = []
    corpus = ""

    with open('countrycodes.csv', 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()
        while len(countries) < num_countries:
            try:
                num_cities = 0
                while num_cities < 100:
                    country_name, rand_country_code = random.choice(lines).split(',')
                    cities = df[df['Country'] == rand_country_code.lower()]
                    num_cities = len(cities)
                corpus += cities.iloc[:,2].str.cat(sep='\n') + '\n'
                countries.append(country_name)
            except Exception:
                pass

    model = Markov(corpus)

    city_name = None
    while not city_name:
        city_name = model.get_word()

    mashup_edition = ''
    if num_countries > 1:
        mashup_edition = 'Special Mashup Edition:\n'
    tweet_str = mashup_edition + city_name + ', ' + '-'.join(countries)
    return tweet_str

if __name__ == '__main__':
    for _ in range(30):
        tweet_str = get_city()
        print(tweet_str)