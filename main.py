import re
import os
import time
import undetected_chromedriver.v2 as uc

from utils.func import *
from tensorflow.python.keras.utils.generic_utils import default

# keyword from model
default_keyword = {
	"boat": ["yawl", "catamaran", "pirate", "speedboat", "liner", "schooner"],
	"plane": ["airliner"],
	"bus": ["trolleybus", "minibus", "passenger_car"],
	"train": ["steam_locomotive", "crane", "electric_locomotive", "freight_car"]
}

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

options = uc.ChromeOptions()
# options.add_argument("--headless")
options.add_argument("--window-size=1500,1200")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--log-level=3")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--incognito")
driver = uc.Chrome(service_log_path="NUL", options=options)
# driver.manage().deleteAllCookies()
driver.get('https://google.com')
p = driver.current_window_handle
driver.execute_script('''window.open("https://typeracer.com","_blank");''')
driver.close()
driver.switch_to.window(driver.window_handles[0])

time.sleep(3)

# Initial
iframe = driver.find_element_by_xpath('//*[@title="widget containing checkbox for hCaptcha security challenge"]')
driver.switch_to.frame(iframe)

time.sleep(3)
pageSource = driver.page_source
check = driver.find_element_by_id("checkbox")
driver.execute_script("arguments[0].click();",check)
time.sleep(3)


# After click captcha
driver.switch_to.default_content()
iframe = driver.find_element_by_xpath('//*[@title="Main content of the hCaptcha challenge"]')
driver.switch_to.frame(iframe)
pageSource = driver.page_source

# regx_target = r'<div class="prompt-text" style="font-size: 15px; width: 200px; color: rgb\(255, 255, 255\); vertical-align: top; display: table-cell; position: absolute; z-index: 5; transition: opacity 0.3s cubic-bezier\(0.65, 0, 0\.35, 1\) 0s;">(.*?)</div>'
# result_regx_target = re.findall(regx_target, pageSource, flags=re.MULTILINE)
# print(result_regx_target)
# print(pageSource)

target_element = driver.find_element_by_css_selector('.prompt-text')
target = target_element.text.split()[-1]
target_array = default_keyword[target]
print("Found: " + target)

# regx = "^background: url\(&quot;(.+)quot;\)$"
regx_img_element = r'<div class="image" style=\(.*?background: url\(&quot;https://imgs.hcaptcha.com/.*?&quot;\) 50% 50% / 96.6667px 96.6667px no-repeat;"\)></div>'

regx_img = r"background: url\(&quot;(https://imgs.hcaptcha.com/.*?)&quot;\)"
result_regx_img = re.findall(regx_img, pageSource, flags=re.MULTILINE)
firstCapt = result_regx_img[3:]

correct, test_case = checkIMG(firstCapt, './images-1/', target_array)

print('CORRECT URL: {}'.format('\n\n'.join(correct)))
print('KEYWORD: {}'.format(target))
print('RESULT: {}'.format(test_case))
print('TOTAL: {}'.format(len(correct)))

time.sleep(3)
for crct in correct:
    for no, url in enumerate(firstCapt):
        if crct == url:
            # images = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@aria-label='Challenge Image {}']//div[1]//div[1]".format(no))))
            images = driver.find_element_by_xpath("//*[@aria-label='Challenge Image {}']//div[1]//div[1]".format(no+1))
            driver.execute_script("arguments[0].click();", images)

time.sleep(1)
driver.find_element_by_css_selector('.button-submit.button').click()

driver.switch_to.default_content()

time.sleep(2)



# Stage 2
iframe = driver.find_element_by_xpath('//*[@title="Main content of the hCaptcha challenge"]')
driver.switch_to.frame(iframe)
pageSource = driver.page_source

# regx_target = r'<div class="prompt-text" style="font-size: 15px; width: 200px; color: rgb\(255, 255, 255\); vertical-align: top; display: table-cell; position: absolute; z-index: 5; transition: opacity 0.3s cubic-bezier\(0.65, 0, 0\.35, 1\) 0s;">(.*?)</div>'
# result_regx_target = re.findall(regx_target, pageSource, flags=re.MULTILINE)
# print(result_regx_target)
# print(pageSource)

target_element = driver.find_element_by_css_selector('.prompt-text')
target = target_element.text.split()[-1]
target_array = default_keyword[target]
print("Found: " + target)

# regx = "^background: url\(&quot;(.+)quot;\)$"
regx_img_element = r'<div class="image" style=\(.*?background: url\(&quot;https://imgs.hcaptcha.com/.*?&quot;\) 50% 50% / 96.6667px 96.6667px no-repeat;"\)></div>'

regx_img = r"background: url\(&quot;(https://imgs.hcaptcha.com/.*?)&quot;\)"
result_regx_img = re.findall(regx_img, pageSource, flags=re.MULTILINE)
secondCapt = result_regx_img[3:]

correct, test_case = checkIMG(secondCapt, './images-2/', target_array)

print('CORRECT URL: {}'.format('\n\n'.join(correct)))
print('KEYWORD: {}'.format(target))
print('RESULT: {}'.format(test_case))
print('TOTAL: {}'.format(len(correct)))

time.sleep(3)
for crct in correct:
    for no, url in enumerate(secondCapt):
        if crct == url:
            images = driver.find_element_by_xpath("//*[@aria-label='Challenge Image {}']//div[1]//div[1]".format(no+1))
            # images = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@aria-label='Challenge Image {}']//div[1]//div[1]".format(no))))
            driver.execute_script("arguments[0].click();", images)

time.sleep(1)
driver.find_element_by_css_selector('.button-submit.button').click()

time.sleep(5)
