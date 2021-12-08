import re

string = "asdasdasd background: url(&quot;https://imgs.hcaptcha.com/klXm7yKXLk0OizLzRy+8L15WCBa8Lsn8gbqroUgxIFhJ3jK7aUPjkdArJ7eL+Czuf1X7G0MMU8mM1T/0+JsHyu68taHfO+GEt9jkUc8J1STlh/BfWqcZz/1OicZ8H58/LTAohGwCdu+QmqyT3650SGoGdHVcXRP3lwRJvbgvrtc63rU5Eol1X2/L8GUgYZ8Yl+WP&quot;) asdasds background: url(&quot;https://imgs.hcaptcha.com/klXm7yKXLk0OizLzRy+8L15WCBa8Lsn8gbqroUgxIFhJ3jK7aUPjkdArJ7eL+Czuf1X7G0MMU8mM1T/0+JsHyu68taHfO+GEt9jkUc8J1STlh/BfWqcZz/1OicZ8H58/LTAohGwCdu+QmqyT3650SGoGdHVcXRP3lwRJvbgvrtc63rU5Eol1X2/L8GUgYZ8Yl+WP&quot;)"
regx1 = r"background: url\(&quot;(https://imgs.hcaptcha.com/.*?)&quot;\)"

m = re.findall(regx1, string, flags=re.MULTILINE)
# print(m)
# print(m.group(1))
# print(re.findall(string, regx))

string2 = 'asdasdasd <div class="prompt-text" style="font-size: 15px; width: 200px; color: rgb(255, 255, 255); vertical-align: top; display: table-cell; position: absolute; z-index: 5; transition: opacity 0.3s cubic-bezier(0.65, 0, 0.35, 1) 0s;">Please click each image containing a bus</div> asdasdasdasds asdasddas'
regx2 = r'<div class="prompt-text" style="font-size: 15px; width: 200px; color: rgb\(255, 255, 255\); vertical-align: top; display: table-cell; position: absolute; z-index: 5; transition: opacity 0.3s cubic-bezier\(0.65, 0, 0\.35, 1\) 0s;">(.*?)</div>'

m = re.findall(regx2, string2, flags=re.MULTILINE)
# print(m)


string3 = '<div class="image" style="position: absolute; top: 50%; left: 50%; z-index: 5; width: 96.6667px; height: 96.6667px; margin-left: -48.3333px; margin-top: -48.3333px; background: url(&quot;https://imgs.hcaptcha.com/klTbt85zDZxfEk7v5sixpa6H05S5TGUlABAqoBmLmc0FJbWmIZRUo3pBiN3FLjldgZtMtdp+O9dO1KwqFfNjTYgIEe/Q9KSytPVKopDRNvhYztjzb3kjzohDRwFWI1EM9JPCjljaHtGN95ZeO5npWfciseH+sd4pZQEOTOefKV9FRSegKrXn9sRAUw==HVi0xJTiwai98fHq&quot;) 50% 50% / 96.6667px 96.6667px no-repeat;"></div>'
regx_img_element = r'<div class="image" style=.*? background: url\(&quot;https://imgs.hcaptcha.com/.*?\)"\)></div>'

m = re.findall(regx_img_element, string3, flags=re.MULTILINE)
print(m)