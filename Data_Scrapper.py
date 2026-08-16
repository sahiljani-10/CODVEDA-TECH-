import csv
import requests
from bs4 import BeautifulSoup
# URL to scrape (Using a safe, public web scraping sandbox site)
URL = "http://quotes.toscrape.com/"

# Custom headers to mimic a real browser request
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def scrape_data():
    try:
        print(f"Fetching web page: {URL}...")
        response = requests.get(URL, headers=HEADERS)
        
        # Check if HTTP request was successful
        response.raise_for_status()

        # Parse HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all quote blocks on the page
        quote_elements = soup.find_all("div", class_="quote")
        
        scraped_data = []

        # Loop through elements and extract details
        for element in quote_elements:
            quote_text = element.find("span", class_="text").get_text(strip=True)
            author = element.find("small", class_="author").get_text(strip=True)
            
            scraped_data.append({
                "Quote": quote_text,
                "Author": author
            })

        print(f"Successfully scraped {len(scraped_data)} items!")
        return scraped_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return []

def save_to_csv(data, filename="scraped_data.csv"):
    if not data:
        print("No data available to save.")
        return

    # Define CSV column headers
    fieldnames = ["Quote", "Author"]

    # Open file in write mode with utf-8 encoding
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # Write headers row
        writer.writeheader()
        
        # Write extracted data rows
        writer.writerows(data)

    print(f"Data successfully saved to '{filename}' bro!")

if __name__ == "__main__":
    extracted_data = scrape_data()
    save_to_csv(extracted_data)