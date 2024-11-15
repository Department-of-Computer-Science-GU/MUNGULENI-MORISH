import requests
from bs4 import BeautifulSoup
from plyer import notification

# Function to get weather details
def get_weather(city):
    try:
        # URL for weather updates (modify based on actual site structure)
        url = f"https://www.weather-forecast.com/locations/{city}/forecasts/latest"
        
        # Make a request to the website
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the relevant data (adjust based on the site's HTML)
        weather_forecast = soup.find('span', class_='phrase').text

        return weather_forecast

    except Exception as e:
        return f"Error retrieving weather data: {e}"

# Function to show desktop notification
def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10  # Duration in seconds
    )

if __name__ == "__main__":
    # Example city (modify as required)
    city = "Kampala"
    
    # Get the weather details
    weather_details = get_weather(city)
    
    # Show weather details in desktop notification
    show_notification(f"Weather Update for {city}", weather_details)
