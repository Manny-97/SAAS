# Saas-monitor
A saas backend application that tracks and monitors website(s) up and down times.

# Development
===========

After cloning the repository, create a virtualenv environment and install
the prerequisites:

<pre><code>
    $ python3 -m venv .venv
    $ source .venv/bin/activate
    $ pip install -r requirements.txt or pip install -r requirements_dev.txt 

</code></pre>

<pre><code>
    $ source .env

</code></pre>

It remains to create and the database with required objects.

    $ python manage.py Makemigrations
    $ python manage.py migrate 
    $ python manage.py createsuperuser


If all is well then, you are ready to run the server and browse the testsite.

    $ python manage.py runserver

    # Browse http://localhost:8000/