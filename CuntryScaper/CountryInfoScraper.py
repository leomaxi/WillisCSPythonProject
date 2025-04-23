# import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd


# function that takes URL as an argument
def get_country_data(url):
    response = requests.get(url)
    countries = []
    #parse data using beautifulsoup
    data = BeautifulSoup(response.text, "html.parser")

    # Each country is inside a div with class "country"
    for country in data.find_all("div", class_="country"):
        #scan through the page data for related info
        name = country.find("h3", class_="country-name").get_text(strip=True)
        capital = country.find("span", class_="country-capital").get_text(strip=True)
        population = country.find("span", class_="country-population").get_text(strip=True).replace(",", "")
        area = country.find("span", class_="country-area").get_text(strip=True).replace(",", "")
        #Add each entry to the countries lists
        countries.append({
            "Name": name,
            "Capital": capital,
            "Population": int(population),
            "Area (km²)": float(area)
        })

    return countries

#Create a function and use panda to save the data to a csv file named countries.csv
def export_to_csv(data, filename="countries.csv"):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data exported to {filename}")

url = "https://www.scrapethissite.com/pages/simple/"
country_info = get_country_data(url)

# Display the first few entries
for entry in country_info[:5]:
    print(entry)

# Export to file
export_to_csv(country_info)
