import time

import pyautogui

adress = "https://google.com"
useragent = "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
proxy = "proxy.soax.com:10316"
gmail_login = "coffeyvega641255@gmail.com"
gmail_password = "5K4uxRcJHB"
latitude = "55.7545543020341"
longitude = "37.6268005371094"

sessions_manager = pyautogui.locateOnScreen("sessions_manager.png", confidence=0.9)
center_sessions_manager = pyautogui.center(sessions_manager)
x, y = center_sessions_manager
pyautogui.click(x, y)
time.sleep(3)
add_session = pyautogui.locateOnScreen("add_session.png", confidence=0.9)
center_add_session = pyautogui.center(add_session)
x, y = center_add_session
pyautogui.click(x, y)
time.sleep(3)
pyautogui.write(adress)
add = pyautogui.locateOnScreen("add.png", confidence=0.9)
center_add = pyautogui.center(add)
x, y = center_add
pyautogui.click(x, y)
time.sleep(3)
start_page = pyautogui.locateOnScreen("start_page.png", confidence=0.9)
center_start_page = pyautogui.center(start_page)
x, y = center_start_page
pyautogui.click(x, y)
time.sleep(3)
useragents_manager = pyautogui.locateOnScreen("useragents_manager.png", confidence=0.9)
center_useragents_manager = pyautogui.center(useragents_manager)
x, y = center_useragents_manager
pyautogui.click(x, y)
time.sleep(10)
add_useragent = pyautogui.locateOnScreen("add_useragent.png", confidence=0.9)
center_add_useragent = pyautogui.center(add_useragent)
x, y = center_add_useragent
pyautogui.click(x, y)
time.sleep(3)
pyautogui.write(useragent)
add = pyautogui.locateOnScreen("add.png", confidence=0.9)
center_add = pyautogui.center(add)
x, y = center_add
pyautogui.click(x, y)
time.sleep(3)
start_page = pyautogui.locateOnScreen("start_page.png", confidence=0.9)
center_start_page = pyautogui.center(start_page)
x, y = center_start_page
pyautogui.click(x, y)
time.sleep(3)
proxyservers_manager = pyautogui.locateOnScreen("proxyservers_manager.png", confidence=0.9)
center_proxyservers_manager = pyautogui.center(proxyservers_manager)
x, y = center_proxyservers_manager
pyautogui.click(x, y)
time.sleep(3)
add_proxy = pyautogui.locateOnScreen("add_proxy.png", confidence=0.9)
center_add_proxy = pyautogui.center(add_proxy)
x, y = center_add_proxy
pyautogui.click(x, y)
time.sleep(3)
pyautogui.write(proxy)
add = pyautogui.locateOnScreen("add.png", confidence=0.9)
center_add = pyautogui.center(add)
x, y = center_add
pyautogui.click(x, y)
time.sleep(3)
start_page = pyautogui.locateOnScreen("start_page.png", confidence=0.9)
center_start_page = pyautogui.center(start_page)
x, y = center_start_page
pyautogui.click(x, y)
time.sleep(3)
sessions_manager = pyautogui.locateOnScreen("sessions_manager.png", confidence=0.9)
center_sessions_manager = pyautogui.center(sessions_manager)
x, y = center_sessions_manager
pyautogui.click(x, y)
time.sleep(3)
empty_session = pyautogui.locateOnScreen("empty_session.png", confidence=0.9)
center_empty_session = pyautogui.center(empty_session)
x, y = center_empty_session
pyautogui.rightClick(x, y)
time.sleep(3)
for i in range(11):
    pyautogui.press("down")
    time.sleep(0.1)
pyautogui.press("right")
time.sleep(0.1)
pyautogui.press("down")
time.sleep(0.1)
pyautogui.press("down")
time.sleep(0.1)
pyautogui.press("enter")
time.sleep(5)
pyautogui.press("tab")
time.sleep(0.1)
pyautogui.press("enter")
time.sleep(3)
save = pyautogui.locateOnScreen("save.png", confidence=0.9)
center_save = pyautogui.center(save)
x, y = center_save
pyautogui.click(x, y)
time.sleep(3)
for i in range(12):
    pyautogui.press("down")
    time.sleep(0.1)
pyautogui.press("right")
time.sleep(0.1)
pyautogui.press("down")
time.sleep(0.1)
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("down")
pyautogui.press("up")
save = pyautogui.locateOnScreen("save.png", confidence=0.9)
center_save = pyautogui.center(save)
x, y = center_save
pyautogui.click(x, y)
time.sleep(3)
for i in range(12):
    pyautogui.press("down")
    time.sleep(0.1)
pyautogui.press("right")
time.sleep(0.1)
pyautogui.press("down")
time.sleep(0.1)
pyautogui.press("down")
time.sleep(0.1)
pyautogui.press("enter")
time.sleep(5)
pyautogui.rightClick(797, 227)
time.sleep(1)
for i in range(6):
    pyautogui.press("up")
    time.sleep(0.1)
    pyautogui.press("right")
    for i in range(4):
        pyautogui.press("down")
        pyautogui.press("enter")
block_all_requests = pyautogui.locateOnScreen("block_all_requests.png", confidence=0.9)
center_block_all_requests = pyautogui.center(block_all_requests)
x, y = center_block_all_requests
pyautogui.rightClick(x, y)
time.sleep(0.25)
pyautogui.press("down")
pyautogui.press("enter")
time.sleep(1)
pyautogui.click(1688, 452)
time.sleep(0.1)
pyautogui.write(latitude)
time.sleep(0.1)
pyautogui.click(1690, 543)
pyautogui.write(longitude)
time.sleep(3)
save = pyautogui.locateOnScreen("save.png", confidence=0.9)
center_save = pyautogui.center(save)
x, y = center_save
pyautogui.click(x, y)
time.sleep(3)
pyautogui.doubleClick(797, 227)
time.sleep(5)
google_login = pyautogui.locateOnScreen("google_login.png", confidence=0.9)
center_google_login = pyautogui.center(google_login)
x, y = center_google_login
pyautogui.rightClick(x, y)
time.sleep(3)
pyautogui.press("tab")
pyautogui.write(gmail_login)
pyautogui.press("enter")
time.sleep(1)
pyautogui.press(gmail_password)
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(940, 80)
pyautogui.write("tinder.com")
pyautogui.press("enter")
tinder_login = pyautogui.locateOnScreen("tinder_login.png", confidence=0.9)
center_tinder_login = pyautogui.center(tinder_login)
x, y = center_tinder_login
pyautogui.rightClick(x, y)
time.sleep(3)
tinder_login_google = pyautogui.locateOnScreen("tinder_login_google.png", confidence=0.9)
center_tinder_login_google = pyautogui.center(tinder_login_google)
x, y = center_tinder_login_google
pyautogui.rightClick(x, y)
time.sleep(3)
pyautogui.click(920, 465)
time.sleep(5)