from flask import Flask, request, render_template_string
import logging
from datetime import datetime


app = Flask(__name__)


# Configure logging
logging.basicConfig(filename="auth.log", level=logging.INFO,
format="%(asctime)s - %(message)s")


# Simple hardcoded credentials
VALID_USERNAME = "admin"
VALID_PASSWORD = "admin123"




login_page = """
<!DOCTYPE html>
<html>
<body>
<h2>Login</h2>
<form method="POST">
Username: <input name="username"/><br><br>
Password: <input type="password" name="password"/><br><br>
<button type="submit">Login</button>
</form>
{% if message %}<p>{{ message }}</p>{% endif %}
</body>
</html>
"""


@app.route('/login', methods=['GET', 'POST'])
def login():
if request.method == 'POST':
username = request.form.get('username')
password = request.form.get('password')


if username == VALID_USERNAME and password == VALID_PASSWORD:
logging.info(f"SUCCESSFUL LOGIN: user={username}")
return "Login successful!"
else:
logging.warning(f"FAILED LOGIN: user={username}, password={password}")
return render_template_string(login_page, message="Invalid credentials")


return render_template_string(login_page, message=None)




app.run(host='0.0.0.0', port=5000)