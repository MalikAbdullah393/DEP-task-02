import requests
from bs4 import BeautifulSoup
import csv
# getting url
url = "https://www.shopify.com"  # Replace with the URL you want to scrape
response = requests.get(url)
#Using a soup as mention in task
soup = BeautifulSoup(response.text, 'html.parser')
headers = soup.find_all('h2')
#open CSV file where data to be store
with open('scraped_data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Header'])  # Write the header
    #here we are writing data
    for header in headers:
        writer.writerow([header.text.strip()])

print("Data scraped and saved to scraped_data.csv")
