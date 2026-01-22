import requests
def basic_weather(city):
    api_key="YOUR_API_KEY"
    base_url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response =requests.get(base_url, timeout=5)
        response.raise_for_status()
        return response.json() 
    except requests.exceptions.RequestException:
        return None
    
    
city=str(input("Enter city name:"))
data=basic_weather(city)
# print(data)

if data is None:
    print("No data received from API")
elif data['cod'] != 200: #str(data.get('cod'))
    print("City not found...API error")
else:
    city_name=data['name']
    temp =data['main'] ['temp'] 
    humidity = data ['main'] ['humidity']   
    description = data['weather'][0]['description'] 
    wind_speed = data['wind']['speed']     
       

    print("----- Weather Report -----")
    print(f" City: {city_name} ")
    print(f" Tempreture :{temp} °C ")
    print(f" Humidity : {humidity}  ")
    print(f" Description : {description} ")
    print(f" Wind Speed : {wind_speed} m/s ")

    
