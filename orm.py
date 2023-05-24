



from django.db import connection
from django.http import request

username = request.POST['username']
password = request.POST['password']

query = "SELECT * FROM users WHERE username = %s AND password = %s;"
params = [username, password]

with connection.cursor() as cursor:
    cursor.execute(query, params)
    result = cursor.fetchone()
