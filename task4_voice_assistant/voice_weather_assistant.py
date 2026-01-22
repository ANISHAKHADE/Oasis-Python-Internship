import speech_recognition as sr
def stt():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for background noise...")
        r.adjust_for_ambient_noise(source, duration=1)
        print("Speak something now...")
        audio= r.listen(source, timeout=5, phrase_time_limit=5)

    print("Audio captured successfully...")

    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Could not understand audio") 
    except sr.RequestError as e:
        print("API error:", e)    

 

import requests
def basic_weather(city):
    api_key="YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    base_url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response =requests.get(base_url, timeout=5)
        response.raise_for_status()
        return response.json() 
    except requests.exceptions.RequestException:
        return None













text=stt()
print("Recognized :" , text)
if "weather" in text:
    print("Weather command recognized ")
    if "in" in text:
        city = str(text.split("in")[1].strip())
        data=basic_weather(city)

        
        if data is None:
            print("No data received from API")
        elif data['cod'] != 200: 
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
    else:
        print("Please say: weather in <city>") 
        city=None

    
elif "exit"in text or "quit" in text:
    print("Exiting...")
else:
    print("Command not recognized ")


    
