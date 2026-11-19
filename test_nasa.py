import requests

from config import require_firms_key

MAP_KEY = require_firms_key()
test_url = f"https://firms.modaps.eosdis.nasa.gov/api/country/csv/{MAP_KEY}/VIIRS_SNPP_NRT/GBR/1"

print("Testing connection to NASA FIRMS...")
response = requests.get(test_url)

print(f"Status Code: {response.status_code}")
print("Response Text from NASA:")
print(response.text)