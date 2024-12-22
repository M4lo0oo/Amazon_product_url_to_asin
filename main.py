import re

def extract_asin(url):
    match = re.search(r"/dp/([A-Z0-9]{10})", url)
    if match:
        return match.group(1)
    return None

url = input("Enter the product url : ")
asin = extract_asin(url)
print(f"The ASIN is : {asin}")