from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Your API key
API_KEY = 'b90d360317633ce482489e6e835ccf23'
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-weather', methods=['POST'])
def get_weather():
    city_name = request.json.get('city', '').strip()
    print(city_name)
    
    if not city_name:
        return jsonify({'error': 'Please enter a city name'}), 400
    
    # API request parameters (same as your React code)
    apiURL = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(apiURL)
        
        if response.status_code == 200:
            data = response.json()
            
            # Format data exactly like your React component
            weather_data = {
                'pressure': data['main']['pressure'],
                'celcius': data['main']['temp'],
                'country': data['sys']['country'],
                'name': data['name'],
                'humidity': data['main']['humidity'],
                'wind': data['wind']['speed'],
                'coLon': data['coord']['lon'],
                'coLat': data['coord']['lat'],
                'visibility': data['visibility'],
                'des': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon']
            }
            return jsonify(weather_data)
        elif response.status_code == 404:
            return jsonify({'error': 'City not found. Please check the spelling.'}), 404
        else:
            return jsonify({'error': 'Unable to fetch weather data'}), response.status_code
            
    except requests.exceptions.RequestException as e:
        return jsonify({'error': 'Network error. Please check your connection.'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)