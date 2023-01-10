from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('efa4a360775bcd5d7c95159628bb7799', config_dict)
mgr = owm.weather_manager()

from colorama import init
from  colorama  import  Fore ,  Back ,  Style

print(Back.MAGENTA)

place = input('В каком городе/стране хотите узнать погоду?: ')

observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius')['temp']

print('Температура сейчас в районе ' + str(temp))

if temp < 10:
    print('Холодно, без термобелья не выходи!')
elif temp < 20:
    print('Прохладно, все равно куртка нужна.')
else:
    print('Тепло, можно в шортах.')

input()