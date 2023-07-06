countries = input().split(', ')
capitals = input().split(', ')
c_n_c = list(zip(countries, capitals))

country_data = {country: capital for (country, capital) in c_n_c}

for country, capital in country_data.items():
    print(country, '->', capital)