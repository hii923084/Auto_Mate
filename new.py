import requests

# Your Vulners API key
api_key = "MOJ1SQ4E60TGO11BWWCBXSJT5OK78S4VAZJ7RJIGA0LY0W9ZOM9QZI0E78OHP0QD"

def search_vulnerabilities(product_name, product_version, max_results=10):
    url = "https://vulners.com/api/v3/search/lucene/"

    # Constructing the search query
    query = f'"{product_name}" AND "{product_version}"'
    params = {
        "query": query,
        "apiKey": api_key,
        "size": max_results
    }

    # Sending the request to the Vulners API
    response = requests.get(url, params=params)
    if response.status_code == 200:
        results = response.json()
        
        if results['result'] == 'OK' and 'data' in results and 'search' in results['data']:
            vulnerabilities = results['data']['search'][:max_results]  # Limiting to top results

            print(f"Top {max_results} vulnerabilities for {product_name} version {product_version}:\n")
            for i, vuln in enumerate(vulnerabilities, start=1):
                title = vuln['_source'].get('title', 'No Title')
                description = vuln['_source'].get('description', 'No description available.')
                cvss_score = vuln['_source'].get('cvss', {}).get('score', 'N/A')
                severity = vuln['_source'].get('cvss', {}).get('severity', 'N/A')
                published_date = vuln['_source'].get('published', 'N/A')
                vuln_url = vuln['_source'].get('href', 'N/A')

                print(f"{i}. Title: {title}")
                print(f"   Description: {description}")
                print(f"   CVSS Score: {cvss_score}")
                print(f"   Severity: {severity}")
                print(f"   Published Date: {published_date}")
                print(f"   URL: {vuln_url}")
                print("-" * 80)
        else:
            print("No vulnerabilities found for the specified product and version.")
    else:
        print(f"Error: Unable to retrieve data (status code {response.status_code})")

# Main function to take user input and search vulnerabilities
if __name__ == "__main__":
    product_name = input("Enter the product name: ")
    product_version = input("Enter the product version: ")
    search_vulnerabilities(product_name, product_version)
