# django-book-keeper

## Installation
cd into the ```django-book-keeper``` directory

activate the virtual environment 
```bash
source env/bin/activate
```

install the libraries for the project
```bash
pip install -r requirements.txt
```

cd back into the ```django-book-keeper``` directory 

cd into to the ```djforms``` directory

create an super user account (an account with admin controls)
```bash
python3 manage.py createsuperuser
```
and fill out the details that the program asks you for such as the username and etc!
YOU WILL NEED TO REMEMBER WHAT YOU ENTERED OR ELSE YOU WILL NEED TO REPEAT THE PROCESS OF CREATING A SUPER USER AGAIN 🙃

Start the server
```bash
python3 manage.py runserver
```

Now the server has started, but it will give you an error, so simply add ```/2/``` after the url

the ```/2/``` is the directory url for the books for james, you can add more books by going into the admin panel. 
To access the admin panel, go to ```http://127.0.0.1:8000/admin``` and sign in with your credentials that you enter for super user and once logged in, go to
author's link and click on add author, give that author an name, and it should have number generated in the url, so once you save the author,
and then go back to ```http://127.0.0.1:8000``` and enter the number for example ```http://127.0.0.1:8000/4/```, then whatever author you created that has the directory 
number of 4 should load up! 
