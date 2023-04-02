# Django Query Profiler

Django Query Profiler is a utility that profiles SQL queries made by Django ORM, providing insights into their performance and suggesting optimizations. This package is particularly useful for developers who want to improve the efficiency of their database interactions, focusing on the Django admin interface.

## Features

- Automatically profiles SQL queries made in the Django admin section
- Saves query profiles to a database table with execution time and timestamp
- Provides an admin interface for viewing, searching, and analyzing query profiles

## Installation

To install Django Query Profiler, simply run:


pip install django-query-profiler


## Usage

    Update your Django project's settings.py file to include the QueryProfilerMiddleware and register the django_query_profiler app.

Add the middleware to the MIDDLEWARE setting:


MIDDLEWARE = [
    ...
    'django_query_profiler.middleware.QueryProfilerMiddleware',
    ...
]

Include 'django_query_profiler' in the INSTALLED_APPS setting:


INSTALLED_APPS = [
    ...
    'django_query_profiler',
    ...
]

    Run the following commands in your project's root directory to create the necessary QueryProfile table in the database:


python manage.py makemigrations django_query_profiler
python manage.py migrate

Once the package is installed and configured, the Django Query Profiler will automatically start profiling SQL queries made in the admin section. Each query will be stored as a QueryProfile record in the database, including the SQL query, execution time, and timestamp.

Access the query profiles in the Django admin interface by navigating to /admin/django_query_profiler/queryprofile/. From there, you can view, search, and analyze the query profiles to identify performance bottlenecks and potential optimizations.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.