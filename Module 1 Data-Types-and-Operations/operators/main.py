# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line

# 1. Comparisson "The language spoken the most in Switzerland is the same as in Spain."
spain_language = 'Spanish'
switzerland_language = 'German'

print(spain_language == switzerland_language)

# 2. Comparison "The most prevalent religion in Switzerland is the same as in Spain."
spain_religion = 'Roman Catolic'
switzerland_religion = 'Roman Catolic'

print(spain_religion == switzerland_religion)

# 3. Comparison "The name length of Spain's capital does not equal that of Switzerland."
spain_capital = 'Madrid'
switzerland_capital = 'Bern'

print(len(spain_capital) != len(switzerland_capital))

# 4. Comparison "Switzerland's GDP is greater than Spain's GDP."
spain_gdp = 731502000000000
switzerland_gdp = 1393351000000

print(switzerland_gdp > spain_gdp)

# 5. Comparison "The population growth is less than 1% in Switzerland and Spain."
spain_population_growth = 0.0012
switzerland_population_growth = 0.0064

print((spain_population_growth and switzerland_population_growth) < 0.01)

# 6. Comparison "At least one of the two countries has a population count of over 10 million."
spain_population_count = 47222613
switzerland_population_count = 8563760

print((spain_population_count or switzerland_population_count) > 10000000)

# 7. Comparison "Exactly one of the two countries has a population count of over 10 million."
print( ( spain_population_count > 10000000) ^ (switzerland_population_count > 10000000))