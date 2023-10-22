#!/usr/bin/env python3
import cgi
import cgitb
import os

cgitb.enable()

def get_cookie_value(cookie_name):
    cookie_string = os.environ.get('HTTP_COOKIE', '')
    cookies = cookie_string.split('; ')
    for cookie in cookies:
        name_value_pair = cookie.split('=')
        name = name_value_pair[0]
        value = '='.join(name_value_pair[1:])
        if name == cookie_name:
            return value
    return None

def set_cookie(cookie_name, cookie_value):
    print("Set-Cookie: {}={}; Path=/".format(cookie_name, cookie_value))

def delete_cookie(cookie_name):
    print("Set-Cookie: {}=0; Path=/; Expires=Thu, 01 Jan 1970 00:00:00 GMT".format(cookie_name))

counter_cookie = get_cookie_value('form_counter')

if counter_cookie is None:
    counter = 1
else:
    counter = int(counter_cookie) + 1

set_cookie('form_counter', str(counter))

form = cgi.FieldStorage()
language = form.getvalue("language")
experience = form.getvalue("experience")
preferences = form.getlist("preferences[]")
selected_radio = form.getvalue("radio")

delete_cookie_button = form.getvalue("delete_cookie_button")
if delete_cookie_button:
    delete_cookie('form_counter')
    counter = 0

print("Content-type: text/html\n")
print("<html>")
print("<head>")
print("<title>Результат обробки форми</title>")
print("<meta charset='UTF-8'>")

print("<style>")
print("body { font-family: 'Arial', sans-serif; background-color: #f4f4f4; margin: 20px; text-align: center}")
print("h2 { color: #333; }")
print("p { margin-bottom: 10px; }")
print("form { margin-top: 20px; }")
print("input[type='submit'] { background-color: #4caf50; color: white; padding: 10px 15px; cursor: pointer; border: none; }")
print("</style>")

print("<title>Результат обробки форми</title>")
print("<meta charset='UTF-8'>")
print("</head>")
print("<body>")
print("<h2>Ваші введені дані:</h2>")
print("<p><strong>Мова програмування:</strong> {}</p>".format(language))
print("<p><strong>Досвід у програмуванні:</strong> {}</p>".format(experience))
print("<p><strong>Вподобання:</strong> {}</p>".format(", ".join(preferences)))
print("<p><strong>Обрана мова програмування:</strong> {}</p>".format(selected_radio))
print("<p><strong>Лічильник заповнених форм:</strong> {}</p>".format(counter))

print('<form action="" method="post">')
print('<input type="submit" name="delete_cookie_button" value="Видалити cookie">')
print('</form>')

print("</body>")
print("</html>")
