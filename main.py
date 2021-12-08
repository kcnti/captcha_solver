import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import re
import urllib.request
from utils.recog import solve
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

driver = webdriver.Chrome()
driver.get('https://beta.exitus.me')
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
print("Found: " + target)

# regx = "^background: url\(&quot;(.+)quot;\)$"
regx_img_element = r'<div class="image" style=\(.*?background: url\(&quot;https://imgs.hcaptcha.com/.*?&quot;\) 50% 50% / 96.6667px 96.6667px no-repeat;"\)></div>'

regx_img = r"background: url\(&quot;(https://imgs.hcaptcha.com/.*?)&quot;\)"
result_regx_img = re.findall(regx_img, pageSource, flags=re.MULTILINE)
firstCapt = result_regx_img[3:]

correct = []
test_case = []

for n, url_image in enumerate(firstCapt):
    path = './images-1/'+str(n)+'.png'
    dl = urllib.request.urlretrieve(url_image, path)

    result = solve(path)
    for name in result:
        if target.lower() in name.lower():
            correct.append(url_image)
            test_case.append(name)
            break

print('CORRECT URL: {}'.format('\n\n'.join(correct)))
print('KEYWORD: {}'.format(target))
print('RESULT: {}'.format(test_case))
print('TOTAL: {}'.format(len(correct)))

for crct in correct:
    for no, url in enumerate(firstCapt):
        if crct == url:
            images = driver.find_element_by_xpath("//*[@aria-label='Challenge Image {}']//div[1]//div[1]".format(no))
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
print("Found: " + target)

# regx = "^background: url\(&quot;(.+)quot;\)$"
regx_img_element = r'<div class="image" style=\(.*?background: url\(&quot;https://imgs.hcaptcha.com/.*?&quot;\) 50% 50% / 96.6667px 96.6667px no-repeat;"\)></div>'

regx_img = r"background: url\(&quot;(https://imgs.hcaptcha.com/.*?)&quot;\)"
result_regx_img = re.findall(regx_img, pageSource, flags=re.MULTILINE)
secondCapt = result_regx_img[3:]

correct = []
test_case = []

for n, url_image in enumerate(secondCapt):
    path = './images-2/'+str(n)+'.png'
    dl = urllib.request.urlretrieve(url_image, path)

    result = solve(path)
    for name in result:
        if target.lower() in name.lower():
            correct.append(url_image)
            test_case.append(name)
            break

print('CORRECT URL: {}'.format('\n\n'.join(correct)))
print('KEYWORD: {}'.format(target))
print('RESULT: {}'.format(test_case))
print('TOTAL: {}'.format(len(correct)))

for crct in correct:
    for no, url in enumerate(secondCapt):
        if crct == url:
            images = driver.find_element_by_xpath("//*[@aria-label='Challenge Image {}']//div[1]//div[1]".format(no))
            driver.execute_script("arguments[0].click();", images)

time.sleep(1)
driver.find_element_by_css_selector('.button-submit.button').click()


# for no, url in enumerate(firstCapt):
#     images = driver.find_element_by_xpath("//*[@aria-label='Challenge Image {}']//div[1]//div[1]".format(no))
#     regx_img = r"background: url\(&quot;(https://imgs.hcaptcha.com/.*?)&quot;\)"
#     result_regx_img = re.findall(regx_img, url, flags=re.MULTILINE)

# for url in correct:
#     image_element = driver.find_element_by_id("image")
#     driver.execute_script("arguments[0].click();", image_element)
