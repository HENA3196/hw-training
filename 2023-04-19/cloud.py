import cloudscraper

scraper = cloudscraper.create_scraper()

response = scraper.get('https://example.com')

print(response.text)
