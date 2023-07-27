# Guild Wars 2 API

## Introduction

The Guild Wars forum is a place for people who love the Guild Wars franchise. Users can post their reviews to the community, follow other users, like posts, favorite posts, comment on posts, and contact the admin. 

This repository holds the Django Rest Framework (DRF) API database for the ReactJS frontend part of the project. 

![Image showing the website's responsiveness on different screens](docs/am-i-reponsive-image.png)

- [Deployed Front End Site](https://gw2-forum-3bb633979161.herokuapp.com/)

- [Repository for Front End Site](https://github.com/NatBat92/guild-wars-2-forum)

- [Deployed API Site](https://gw2forumapi-7625ca6fa938.herokuapp.com/)

- [Repository for API Site](https://github.com/NatBat92/drf-apih)


***

## Validator Testing

All python files passed through the PEP8 validator with no issues

Contact:

- [PP8 Contact](docs/python-linter-contact-models.png) - Models

- [PP8 Contact](docs/python-linter-contact-serializers.png) - Serializer

- [PP8 Contact](docs/python-linter-contact-views.png) - Views

Likes:

- [PP8 Likes](docs/python-linter-likes-models.png) - Models

- [PP8 Likes](docs/python-linter-likes-serializers.png) - Serializer

- [PP8 Likes](docs/python-linter-likes-views.png) - Views

Profiles:

- [PP8 Profiles](docs/python-linter-profiles-models.png) - Models

- [PP8 Profiles](docs/python-linter-profiles-serializers.png) - Serializer

- [PP8 Profiles](docs/python-linter-profiles-views.png) - Views

Favourites:

- [PP8 Favourites](docs/python-linter-favourites-models.png) - Models

- [PP8 Favourites](docs/python-linter-favourites-serializers.png) - Serializer

- [PP8 Favourites](docs/python-linter-favourites-views.png) - Views

Comments:

- [PP8 Contact](docs/python-linter-comments-models.png) - Models

- [PP8 Contact](docs/python-linter-comment-serializers.png) - Serializer

- [PP8 Contact](docs/python-linter-comment-views.png) - Views

Posts:

- [PP8 Posts](docs/python-linter-post-models.png) - Models

- [PP8 Posts](docs/python-linter-post-serializers.png) - Serializer

- [PP8 Posts](docs/python-linter-post-views.png) - Views

***
## Testing

Backend Manual Testing

|Area|Test|Result|
|---|---|----|
|Deployed site|Home shows message and no errors|PASS|
||/profiles/ shows all profiles|PASS|
||/profiles/:id shows single profile|PASS|
||/posts/ shows all posts|PASS|
||/posts/:id shows single post|PASS|
||/comments/shows all comments|PASS|
||/comments/:id shows single comment|PASS|
||/favourites/shows all favourites|PASS|
||/likes/shows all likes|PASS|
||/admin/ allows superuser to login|PASS|
||/admin/ basic admin view and functions|PASS|
|Dev site|/posts/ show pagination|PASS|
||/posts/ show text search by user__username|PASS|
||/admin/ shows login for Superuser and then loads admin panel|PASS|


### Manual testing of user stories

- As an admin, I want to be able to create, edit and delete the users, posts, comments and likes, so that I can have a control over the content of the application and remove any potential inappropriate content

**Test** | **Action** | **Expected Result** | **Actual Result**
-------- | ------------------- | ------------------- | -----------------
User | Create, update & delete user | A user can be created, edited or deleted | Works as expected
User | Change permissions | User permissions can be updated | Works as expected
Profile | Create, update & delete | User profile can be created, edited or deleted | Works as expected
Post | Create, update & delete | A post can be created, edited or deleted | Works as expected
Comment | Create, update & delete | A comment can be created, edited or deleted | Works as expected
Like | Create & delete | A like can be created or deleted (like / unlike post) | Works as expected
Follower | Create & delete | Follow or unfollow user | Works as expected
Favourite | Create & delete | Favourite or Unfavourite post | Works as expected

***
## Bugs

### Unfixed

None identified

***

## Technologies Used

### Languages and Frameworks Used

- [Python](https://www.python.org/)
- [Django](https://pypi.org/project/Django/3.2.14/)
- [Django-REST-framework](https://www.django-rest-framework.org/) - Toolkit for building web API's with Django.

### Python Modules Used

- Built-in Packages/Modules
  - [os](https://docs.python.org/3/library/os.html) - This module provides a portable way of using operating system dependent functionality.

### Packages Used

- External Python Packages
  - [cloudinary](https://pypi.org/project/cloudinary/) - Cloudinary intergration.
  - [django-cloudinary-storage](https://pypi.org/project/django-cloudinary-storage/) - Cloudinary intergration.
  - [dj-database-url](https://pypi.org/project/dj-database-url/) - Allows the use of 'DATABASE_URL' environmental variable in the Django project settings file to connect to a PostgreSQL database.
  - [django-allauth](https://pypi.org/project/django-allauth/) - Set of Django application used for account registration, management and authentication.
  - [dj-rest-auth](https://pypi.org/project/dj-rest-auth/) - API endpoints for handling authentication in Django Rest Framework.
  - [django-filter](https://pypi.org/project/django-filter/) - Application that allows dynamic QuerySet filtering from URL parameters.
  - [djangorestframework-simplejwt](https://pypi.org/project/djangorestframework-simplejwt/) - JSON Web Token authentication backend for the Django REST Framework.
  - [django-cors-headers](https://pypi.org/project/django-cors-headers/) - Django App that adds CORS headers to responses.
  - [gunicorn](https://pypi.org/project/gunicorn/) - Python WSGI HTTP Server.
  - [psycopg2](https://pypi.org/project/psycopg2) - Python PostgreSQL database adapter.


### Programs and Tools Used

- [GitPod](https://www.gitpod.io/)
- [GitHub](https://github.com/)
- [Heroku](https://heroku.com/)


<hr>

## Deployment
### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on
our GitHub account to view and/or make changes without affecting the original
repository by using the following steps...

1. Log in to GitHub and locate the [GitHub
   Repository](https://github.com/NatBat92/drf-api)
1. At the top of the Repository (not top of page) just above the "Settings"
   Button on the menu, locate the "Fork" Button.
1. Click the button (not the number to the right) and you should now have a copy
   of the original repository in your GitHub account.

### Making a Local Clone

**NOTE**: It is a requirement of the project that you have Python version 3.8 or higher installed locally.

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/NatBat92/drf-api).
1. Under the repository name, click "Code".
1. To clone the repository using HTTPS, under "HTTPS", copy the link.
1. Open your local terminal with git installed
1. Change the current working directory to the location where you want the cloned directory to be created.
1. Type `git clone`, and then paste the URL you copied in Step 3.

    ```console
    ~$ git clone https://github.com/NatBat92/drf-api
    ```

1. Press Enter. Your local clone will be created.

    ```console
    $ git clone https://github.com/NatBat92/drf-api
    > Cloning into `test-dir`...
    > remote: Counting objects: 10, done.
    > remote: Compressing objects: 100% (8/8), done.
    > remove: Total 10 (delta 1), reused 10 (delta 1)
    > Unpacking objects: 100% (10/10), done.
    ```

    [Click here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) for a more detailed explanation of the process above with pictures.

1. Change the current working directory to the cloned project folder (this will be a child directory in the location you cloned the project).

1. It is recommended to use a virtual environment during development ([learn more about virtual environments](https://realpython.com/python-virtual-environments-a-primer/)). If you would prefer not to use one please skip the following steps:
    1. Create a virtual environment in the projects working directory by entering the following command in the same terminal window used for the steps above `python3 -m venv .venv`.
    1. Before use, the virtual environment will need to be activated using the command `source .venv/bin/activate` in the same terminal window used previously.
1. Packages required by the project can now using the command `pip install -r requirements.txt`
1. In the cloned directory, rename the file `.env-example` to `.env` and populate it with the information required.
1. Make Django migrations using the command `./manage.py migrate`.

### Deploying with Heroku

**NOTE**: It is a prerequisite of deployment to Heroku that you already have access to the following:

- A Cloudinary account, create one for free at [https://cloudinary.com](https://cloudinary.com).

**NOTE**: It is assumed you have followed all deployment instructions listed in this readme starting with the section titled 'Forking the GitHub Repository'.

1. Log in to [Heroku](https://www.heroku.com/) and if not taken there automatically, navigate to your personal app dashboard.
1. At the top of the page locate the 'New' drop down, click it and then select 'Create new app'.
1. Give your application a unique name, select a region appropriate to your location and click the 'Create app' button.
1. Your app should now be created, so from the menu towards the top of the page select the 'Resources' section.
1. Search for 'Heroku Postgres' under the Add-ons section and add it.
1. From the menu towards the top of the page select the 'Settings' section and lick 'Reveal Config Vars' in the Config vars section. Enter the following key / value pairings:
    1. Key as `ALLOWED_HOSTS` and the value as the name of you project with '.herokuapp.com' appended to the end e.g.  `example-app.herokuapp.com`. Click the Add button.
    1. Key as `CLOUDINARY_URL` and the value as your cloudinary API Environment variable e.g. `cloudinary://**************:**************@*********`. Click the Add button.
    1. Key as `SECRET_KEY` and the value as a complex string which will be used to provide cryptographic signing. Click the Add button.
    1. Ensure the key `DATABASE_URL` is already populated. This should have been created automatically by Heroku.
    1. The `DATABASE_URL` should be copied into your local `.env`, created during the cloning process.(Add the address to your ElephantSQL respository)
    1. To make authenticated requests to this API (e.g. from a fontend application) you are required to add the key `CLIENT_ORIGIN` with the value set as the URL you will be sending the authentication request from.
    1. Additionally, a `CLIENT_ORIGIN_DEV` key can be set with the value of a development server (IP or URL) for use during local development.
1. Open the `.env` file in the project directory and delete the key / value pair `DEV_ENVIRONMENT_DATABASE = True` before saving the file. This can be added back after the next step to ensure local development changes will not alter the remote database.
1. Navigate to the 'Deploy' page using the menu towards the top of the page.
1. Select 'GitHub' from the 'Deployment method' section and you will be prompted to 'Connect to GitHub'.
1. Once connected to your GitHub account you will be able to search for your repository which contains the forked 'property-direct-backend' repository.
1. Once the repository is found click 'Connect'.
1. At the bottom of the page find the section named 'Manual deploy', select the 'main' branch in the drop down and click the 'Deploy' button.
1. Once deployment is complete, click the 'View' button to load the URL of the deployed application.

***

## Credits

- Code Institute's Moments project was used to lay the foundations of this project and was adapted on to create a unique project.  

- My fiance Emma for testing my code and giving me that push and confidence to get this over the line

- My Mentor Gareth for going through my project and letting me know what I can do to improve things/ provide desireable features for my users.

***