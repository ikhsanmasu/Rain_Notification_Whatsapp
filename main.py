import requests
from twilio.rest import Client
import os

lat = -0.947083
lon = 100.417183
API_key = {open weather api key}
OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"

weather_param = {
    "lat": lat,
    "lon": lon,
    "appid": API_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_param)
response.raise_for_status()

weather_data = response.json()

will_rain = False
for hour_data in weather_data["hourly"][:12]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
        break

account_sid = os.environ.get("sid")
auth_token = os.environ.get("token")
client = Client(account_sid, auth_token)

if will_rain:
    message = client.messages.create(
                                  body='Hari ini akan hujan, bawalah payung!',
                                  from_='whatsapp:{your twilio phone number}',
                                  to='whatsapp:{Number you want to send the message}'
                              )
    print(message.status)

