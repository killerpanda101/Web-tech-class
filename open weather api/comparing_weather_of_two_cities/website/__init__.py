from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '0_w9Ck_XvNFT3tfwO'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///SensorDataDB.db'
data_base = SQLAlchemy(app)




from website import routes


   
