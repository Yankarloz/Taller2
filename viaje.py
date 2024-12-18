from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

#Google chrome driver
service = Service('driver/chromedriver.exe')
bot = webdriver.Chrome(service=service)
bot.maximize_window()
time.sleep(2)

#Page on which you are going to work
bot.get('https://www.viajesexito.com')
time.sleep(10)
bot.refresh()

#Select viaje+hotel
travel_hotel = bot.find_element(By.XPATH, '//*[@id="paquetesTooltips"]/a/span')
time.sleep(2)
travel_hotel.click()
time.sleep(2)

#Section origin of the trip
origin = bot.find_element(By.XPATH, '//*[@id="airhotel"]/div/div[1]/div/div[1]/div')
time.sleep(2)
origin.click()
time.sleep(2)
origin_search = bot.find_element(By.XPATH, '//*[@id="popUpCityPredictiveFrom_netactica_airhotel"]')
origin_search.send_keys('jose maria cordova')
origin_search.send_keys(Keys.RETURN)
time.sleep(2)

#Select travel destination
input = "Aeropuerto internacional de cancun"
destination = bot.find_element(By.XPATH, '//*[@id="CityPredictiveTo_netactica_airhotel"]')
time.sleep(2)
destination.click()
time.sleep(2)
destination_search = bot.find_element(By.XPATH, '//*[@id="popUpCityPredictiveTo_netactica_airhotel"]')
time.sleep(2)
destination_search.send_keys(input)
time.sleep(2)
destination_search.send_keys(Keys.ARROW_DOWN)
destination_search.send_keys(Keys.RETURN)
time.sleep(2)

#Select the departure and arrival date box, and select the dates on the calendar
date_exit = bot.find_element(By.XPATH, '//*[@id="airhotel"]/div/div[2]')
date_exit.click()
time.sleep(2)
date_initial = bot.find_element(By.XPATH, '//*[@id="Body"]/div[9]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[5]/div[7]')
date_initial.click()
time.sleep(2)
date_final = bot.find_element(By.XPATH, '//*[@id="Body"]/div[9]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[3]/div/div[2]/div[4]')
date_final.click()
time.sleep(2)
date_accept = bot.find_element(By.XPATH, '//*[@id="Body"]/div[9]/div[2]/div[2]/div[2]/button[2]')
date_accept.click()
time.sleep(2)

#Select the number of rooms and the number of people occupying them
room = bot.find_element(By.XPATH, '//*[@id="txtNumHabitacionesAirHotel"]')
time.sleep(2)
room.click()
room_add = bot.find_element(By.XPATH, '//*[@id="popUpHabitacionesAirHotel"]/div[2]/div[1]')
room_add.click()
time.sleep(2)
adult_add = bot.find_element(By.XPATH, '//*[@id="roomtwopaquetes"]/div/div[3]/div/div[2]/div/span[2]/button')
adult_add.click()
adult_add.click()
time.sleep(2)
Accept_rooms = bot.find_element(By.XPATH, '//*[@id="popUpHabitacionesAirHotel"]/div[2]/div[2]')
Accept_rooms.click()
time.sleep(5)

#Look for the options that the page offers us by opening a new tab
search = bot.find_element(By.XPATH, '//*[@id="airhotel"]/div/div[4]')
search.click()
time.sleep(15)

# Handling the new tab
original_window = bot.current_window_handle
time.sleep(2)

# Wait until a new tab opens
while len(bot.window_handles) == 1:
    time.sleep(1)

new_window = [window for window in bot.window_handles if window != original_window][0]
bot.switch_to.window(new_window)

# Actions in the new tab
time.sleep(5)
print("New window: ", bot.title)
time.sleep(2)

# Brings hotel price information
description = bot.find_element(By.XPATH, '//*[@id="divRightColumn"]').text
print("")
print(input.upper)
print("")
print("elemnts: " + description)
print("")
time.sleep(2)

# select advanced options and choose an airline
airline = bot.find_element(By.XPATH, '//*[@id="ulNewSearch"]/div[6]')
time.sleep(2)
airline.click()
time.sleep(2)
airline_search = bot.find_element(By.XPATH, '//*[@id="txtAirlineCode"]')
time.sleep(2)
airline_search.send_keys('avianca')
time.sleep(2)
airline_search.send_keys(Keys.RETURN)
time.sleep(2)
seacrh_avianca = bot.find_element(By.XPATH, '//*[@id="ulNewSearch"]/div[8]')
seacrh_avianca.click()
time.sleep(15)

# Scroll down to the bottom
bot.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

#Open the whatsapp link
whattsapp = bot.find_element(By.XPATH, '//*[@id="lineas-contacto"]/p[1]/a')
whattsapp.click()
time.sleep(2)

#Finish the bot
bot.quit()
