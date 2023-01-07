# s = 'In {0}, someone paid {1} {2} for two pizzas.'
# print(s.format('2010', '10k', 'Bitcoin'))

# «In 2010, someone paid 10k Bitcoin for two pizzas.» (без кавычек).


year = 2010
amount = '10K'
currency = 'Bitcoin'

print(f'In {year}, someone paid {amount} {currency} for two pizzas.')