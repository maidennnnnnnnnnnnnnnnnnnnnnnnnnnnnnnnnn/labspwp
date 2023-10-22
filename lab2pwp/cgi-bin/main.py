#!/usr/bin/env python3
import cgi

print("Content-type: text/html\n")

form = cgi.FieldStorage()

language = form.getvalue("language")
experience = form.getvalue("experience")
preferences = form.getlist("preferences[]")
selected_radio = form.getvalue("radio")

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
print("</body>")
print("</html>")
