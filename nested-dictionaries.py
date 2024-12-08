countries = {
    "France": {
        "capital": "Paris",
        "language": "French"
    },
    "Japan": {
        "capital": "Tokyo",
        "language": "Japanese"
    },
    "Spain": {
        "capital": "Madrid",
        "language": "Spanish"
    },
    "USA": {
        "capital": "Washington DC",
        "language": "English"
    }
}

#to get info from one of the dictionaries, you'd write this:
#print(countries["USA"]["language"])

for country_name, country_info in countries.items():
    #print(country_name)
    #print(country_info)
    #print(country_info["capital"])
    print(f"The capital of {country_name} is {country_info['capital']} and they speak {country_info['language']}")
    
#another way (advanced apparently)
for country_name, country_info in countries.items():
    capital_city = country_info['capital']
    langauge = country_info['language']
    print(f"The capital of {country_name} is {capital_city} and they speak {langauge}")