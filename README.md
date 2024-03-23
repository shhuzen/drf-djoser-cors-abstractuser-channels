<!-- ![Maintenance](https://img.shields.io/maintenance/no/2?label=Maintained%3F&style=for-the-badge) -->

# Disclaimer

this git for fast start backend on python

## DJANGO REST-FRAMEWORK DJOSER CORS ABSTRACTUSER CHANNELS

## Stack

- [DJANGO](https://www.djangoproject.com/)
- [DJOSER - FOR AUTH](https://djoser.readthedocs.io/en/latest/getting_started.html)
- [CHANNELS - LIVETIME MESSAGES GROUP](https://channels.readthedocs.io/en/latest/)
- [DRF - API](https://www.django-rest-framework.org/)
- [PILLOW - IMG](https://pypi.org/project/pillow/)
- [django-cleanup - CLEANER STATIC](https://pypi.org/project/django-cleanup/)

## Install

```
git clone https://github.com/shhuzen/drf-djoser-cors-abstractuser-channels.git
cd drf-djoser-cors-abstractuser-channels
python3.11 -m venv env  # or python
source env/bin/Activate or  source env/Scripts/activate
pip install -r requirements.txt
```

## Migrate / User

```
cd main
python3.11 manage.py migrate
python3.11 manage.py createsuperuser
```

## Run / Develop

```
python manage.py runserver
```

## URL API

```
/admin/
/api/v1/users/

/api/v1/users/me/

/api/v1/users/confirm/

/api/v1/users/resend_activation/

/api/v1/users/set_password/

/api/v1/users/reset_password/

/api/v1/users/reset_password_confirm/

/api/v1/users/set_username/

/api/v1/users/reset_username/

/api/v1/users/reset_username_confirm/

/api/v1/token/login/ (Token Based Authentication)

/api/v1/token/logout/ (Token Based Authentication)

/api/v1/jwt/create/ (JSON Web Token Authentication)

/api/v1/jwt/refresh/ (JSON Web Token Authentication)

/api/v1/jwt/verify/ (JSON Web Token Authentication)

/api/v1/user-detail/

/api/v1/user-detail/<id>

/api/v1/user-detail/




```
