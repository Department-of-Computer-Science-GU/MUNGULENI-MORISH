import requests
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server

# Function to fetch a random fact from the API
def fetch_random_fact():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors
        data = response.json()
        return data["text"]
    except requests.exceptions.RequestException as e:
        return f"Error fetching fact: {str(e)}"  # Return the error message

# Main function to generate the PyWebio web app
def fun_fact_app():
    # Inject custom HTML and CSS for the layout
    put_html('''
    <div style="font-family: 'Helvetica Neue', sans-serif; max-width: 600px; margin: 50px auto; padding: 30px; background-color: orange; border-radius: 10px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); text-align: center;">
        <h1 style="color: #4a90e2; margin-bottom: 20px;">🎉 Fun Fact Generator 🎉</h1>
        <p style="font-size: 18px; color: #333; margin-bottom: 30px;">Click the button below to learn something new and random!</p>
       
    </div>
    ''')

    # Main loop for the button interaction
    while True:
        # Button that triggers fact generation
        if actions(buttons=['Generate Fun Fact']) == 'Generate Fun Fact':
            # Fetch a random fact and update the content
            fact = fetch_random_fact()
            put_html(f'''
            <div style="background-color: black; padding: 20px; border-radius: 10px; margin-top: 20px; min-height: 100px;">
                <p style="color: #00796b; font-size: 22px;">{fact}</p>
            </div>
            ''')

# Run the PyWebio app
if __name__ == "__main__":
    start_server(fun_fact_app, port=8080)
