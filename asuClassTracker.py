from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from winotify import Notification, audio

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-logging")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--log-level=3')
driver = webdriver.Chrome(options=chrome_options)


# class_code = '76320'

while True:
    class_code = input("Enter 5 digit class number: ")
    if int(class_code) not in range(9999,100000):
        print("Sorry, invalid class code.")
        continue
    else:
        #we're happy with the value given.
        #we're ready to exit the loop.
        break
    
def get_data(ccode):
    url = rf"https://catalog.apps.asu.edu/catalog/classes/classlist?keywords={ccode}&searchType=all&term=2237&collapse=Y"
    driver.get(url)
    sleep(2)
    try:
        noresults = driver.find_element(By.CLASS_NAME,"search-title")
        if noresults.text=="No classes found":
            return -1
    except:
        noresults=None

    if noresults is not None:
        try:
            found = driver.find_elements(By.CLASS_NAME,"seats")
            res_text = (found[1].text)
        except:
            return -1
        available, total = res_text.split(" of ")
        available, total = int(available), int(total)
        return available, total

seats_not_open = True
data = get_data(class_code)
if data==-1:
    print("There are no results for this class code.")

else:
    print("Got it! Now Tracking...")
    print("Auto Refreshing Every ~3 seconds...")
    print("You will be notified if any seat opens up")
    print("*****************************************")
    while True:
        available, total = get_data(class_code)
        print(f"Current status: {available}/{total} seats")
        print("-------------------------------------")
        if(available>0):
            toast = Notification(app_id="ASU Class Tracker",
                     title="Seats are Available!",
                     msg=f"{available}/{total} seats available!",
                     )
            toast.set_audio(audio.Mail, loop=False)
            toast.show()
    
driver.close()