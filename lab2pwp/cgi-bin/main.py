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

print("Content-type: text/html\n")
print("<html>")
print("<head>")
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
print("</body>")
print("</html>")
