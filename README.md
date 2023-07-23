# Guild Wars 2 API

## Introduction

The Guild Wars forum is a place for people who love the Guild Wars franchise. Users can post their reviews to the community, follow other users, like posts, favorite posts, comment on posts, and contact the admin. 

This repository holds the Django Rest Framework (DRF) API database for the ReactJS frontend part of the project. 

- [Deployed Front End Site]

- [Repository for Front End Site]

- [Deployed API Site]

- [Repository for API Site]


***

## Validator Testing

All python files passed through the PEP8 validator with no issues

Contact:

- [PP8 Contacts] - Models

- [PP8 Contacts] - Serializer

- [PP8 Contacts] - Views

Likes:

- [PP8 Likes] - Models

- [PP8 Likes] - Serializer

- [PP8 Likes] - Views

Profiles:

- [PP8 Profiles] - Models

- [PP8 Profiles] - Serializer

- [PP8 Profiles] - Views

Favourites:

- [PP8 Favourites] - Models

- [PP8 Favourites] - Serializer

- [PP8 Favourites] - Views

Contact:

- [PP8 Contact] - Models

- [PP8 Contact] - Serializer

- [PP8 Contact] - Views

Posts:

- [PP8 Posts] - Models

- [PP8 Posts] - Serializer

- [PP8 Posts] - Views

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

***