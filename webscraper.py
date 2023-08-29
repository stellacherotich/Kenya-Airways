import requests
from bs4 import BeautifulSoup

url = "https://www.airlinequality.com/airline-reviews/kenya-airways/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find and print all review titles
review_titles = soup.find_all("h2", class_="text_header")
for title in review_titles:
    print(title.get_text())
