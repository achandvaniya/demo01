Steps to configure the projects.

1. Take pull of the code base.
2. Create a virtual environment and install packages from the requirement.txt
2. Create databases and update the username, password and database name in settings.py file.
3. Run the migrations using below commands.
./manage.py makemigrations
./manage.py migrate
4. Create django superuser.
5. Start the server.
5. Login into the Django admin panel and add some cities, cleaner and CityCleanerMap(Which cleaner is working in which company)
6. On Home page you are able to create bookings.