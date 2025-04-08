import requests
import os
import json
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
load_dotenv()

def fetch_brand_data(domain):
    """Fetch brand data for the given domain."""
    api_key = os.getenv('BRANDFETCH_API_KEY')
    if not api_key:
        print("Error: BRANDFETCH_API_KEY not found in environment variables")
        return
        
    headers = {
        'Authorization': f'Bearer {api_key}'
    }
    
    base_url = os.getenv('BRANDFETCH_URL', "https://api.brandfetch.io/v2/brands/")
    url = f"{base_url}{domain}"
    
    print(f"\nFetching brand data for: {domain}")
    print("-" * 50)
    
    try:
        response = requests.get(url, headers=headers)
        print(f"Status code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            # Pretty print the JSON response
            print("\nAPI Response:")
            print("-" * 50)
            print(json.dumps(data, indent=2))
            
            # Create output directory if it doesn't exist
            output_dir = Path('output')
            output_dir.mkdir(exist_ok=True)
            
            # Save the JSON response to a file
            output_file = output_dir / f"{domain.replace('.', '_')}_brand_data.json"
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            print(f"\nData saved to: {output_file}")
            return data
        else:
            print(f"Error: {response.status_code}")
            print(f"Response: {response.text}")
            return None
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return None

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python brand_fetch.py <domain>")
        print("Example: python brand_fetch.py google.com")
        sys.exit(1)
        
    domain = sys.argv[1]
    fetch_brand_data(domain)