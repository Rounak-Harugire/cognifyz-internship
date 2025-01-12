import requests
from bs4 import BeautifulSoup

def fetch_data(url):
    try:
        print(f"Attempting to fetch data from: {url}")
        response = requests.get(url, timeout=10)
        response.raise_for_status() 
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the title
        title = soup.title.string if soup.title else 'No title found'

        # Extract all links
        links = [a['href'] for a in soup.find_all('a', href=True)]

        # Extract all headings (h1, h2, h3)
        headings = {
            'h1': [h1.text.strip() for h1 in soup.find_all('h1')],
            'h2': [h2.text.strip() for h2 in soup.find_all('h2')],
            'h3': [h3.text.strip() for h3 in soup.find_all('h3')],
        }

        # Extract structured data (tables)
        structured_data = []
        tables = soup.find_all('table')
        for table in tables:
            rows = table.find_all('tr')
            table_data = []
            for row in rows:
                cols = row.find_all(['td', 'th'])
                table_data.append([col.text.strip() for col in cols])
            structured_data.append(table_data)

        return {
            'title': title,
            'links': links,
            'headings': headings,
            'structured_data': structured_data,
        }

    except requests.exceptions.Timeout:
        print(f"Timeout occurred while trying to access {url}")
    except requests.exceptions.ConnectionError:
        print(f"Connection error occurred for {url}")
    except requests.exceptions.RequestException as e:
        print(f"General error for {url}: {e}")

    return None

def fetch_paginated_data(base_url, page_param, max_pages):
    all_data = []
    for page in range(1, max_pages + 1):
        url = f"{base_url}?{page_param}={page}"
        print(f"Fetching data from: {url}")
        data = fetch_data(url)
        if data:
            all_data.append(data)
    return all_data

if __name__ == "__main__":
    url = "https://example.com"  # Replace with the actual URL

    data = fetch_data(url)
    if data:
        print("Title of the webpage:", data['title'])
        print("\nLinks:")
        for link in data['links']:
            print(link)

        print("\nHeadings:")
        for level, texts in data['headings'].items():
            print(f"{level.upper()}:")
            for text in texts:
                print(f"  - {text}")

        print("\nStructured Data:")
        for table in data['structured_data']:
            for row in table:
                print(row)

    print("\nFetching paginated data:")
    base_url = "https://example.com/page"  # Example base URL for pagination
    paginated_data = fetch_paginated_data(base_url, "page", 3)  # Fetch data from 3 pages
    for page_data in paginated_data:
        print("Title of the webpage:", page_data['title'])
