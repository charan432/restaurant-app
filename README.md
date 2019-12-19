# restaurant-app
This is a sample restaurant app (Name: FoodFun) built in Python &amp; Django. users can see list of restaurants and their dishes. Users can book a table for a selected restaurant


Installation Instructions:

1) Clone the repo to your local machine.

2) Go to your project directory and create a new `env` 
        python -m venv env
  
3) After env is created, activate the `env`.
          source ./env/Scripts/activate

4) In order to install the requirements from `requirements.txt` file, run below command:
         pip install -r requirements.txt
         
5) For Database, I am using MySql DB. For migration of db, run below commands:
           python manage.py makemigrations
           python manage.py migrate
           
6) Now, run the server
          python manage.py runserver
          
