import requests

api_endpoint = "https://api.open-meteo.com/v1/forecast"

def validate_coordinates(latitude, longitude):
    try:
        latitude = float(latitude)
        longitude = float(longitude)

        if not -90 <= latitude <= 90:
            print("Latitude must be between -90 and 90.")
            return None

        if not -180 <= longitude <= 180:
            print("Longitude must be between -180 and 180.")
            return None

        return latitude, longitude

    except ValueError:
        print("Latitude and longitude must be numbers.")
        return None

def get_request(url,latitude,longitude):
    try:
        api = f'{url}?latitude={latitude}&longitude={longitude}&current=temperature_2m'
        data = requests.get(api)
    except requests.exceptions.RequestException:
        print("Something went wrong.")
    if data.status_code == 200:
        temperature = data.json()['current']['temperature_2m']
        return temperature
    else:
        print("Failed to fetch data from the API.")

def api_integration(url):
    print("Welcome to our find temperature program:")
    latitude = input("latitude: ")
    longitude = input("longitude: ")
    coordinates = validate_coordinates(latitude, longitude)
    
    if coordinates is not None:
        latitude, longitude = coordinates
        temperature = get_request(url,latitude,longitude)
        if temperature is not None:
            print(f"Temperature = {temperature}")

api_integration(api_endpoint)