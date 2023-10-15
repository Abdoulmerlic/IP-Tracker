import requests

def get_ip_location(ip_address):
    access_key = "02c3790aa70927767b81978f888ebbf1"  # Replace with your actual API key
    url = f"http://api.ipstack.com/{ip_address}?access_key={access_key}"

    try:
        response = requests.get(url)
        data = response.json()
        latitude = data["latitude"]
        longitude = data["longitude"]
        city = data["city"]
        country = data["country_name"]
        print(f"Location for IP {ip_address}: {latitude}, {longitude}")
        print(f"City: {city}, Country: {country}")
    except requests.exceptions.RequestException as e:
        print("Error: ", e)

# Ask the user for an IP address input
ip_address = input("Enter the IP address you want to trace: ")
get_ip_location(ip_address)

