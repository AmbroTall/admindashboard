# admindashboard

git clone https://github.com/AmbroTall/admindashboard/new/master
cd https://github.com/AmbroTall/admindashboard/new/master
virtualenv -p python3.9 venv
source ./Scripts/activate
pip install django 
cd admindashboard
python manage.py migrate
python manage.py runserver
