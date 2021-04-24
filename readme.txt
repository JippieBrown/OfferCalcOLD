Install virtual env 
	& C:/Users/hauke/AppData/Local/Programs/Python/Python39/python.exe -m venv c:/Users/hauke/Documents/OfferCalc/venv
run virtualenv
	PS C:\Users\hauke\Documents\OfferCalc> .\venv\Scripts\activate
	(venv) PS C:\Users\hauke\Documents\OfferCalc> 
run python
	C:\Users\hauke\Documents\OfferCalc\venv\Scripts\python.exe 
upgrade pip
	py -m pip install --upgrade pip
install requirements
	py -m pip install -r requirements.txt
	py -m pip install email_validator
	py -m pip install flask_bcrypt
	py -m pip install flask_login
DB aktivieren
	python
	from OfferGUI.models import db
DB neue Liste hinzufügen
	db.create_all()
DB leeren
	db.drop_all()
	