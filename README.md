[![Build Status](https://travis-ci.org/andela-jmwangi/picfect-api.svg?branch=feature-review)]
(https://travis-ci.org/andela-jmwangi/picfect-api)
[![Coverage Status](https://coveralls.io/repos/github/andela-jmwangi/picfect-api/badge.svg?branch=feature-review)]
(https://coveralls.io/github/andela-jmwangi/picfect-api?branch=feature-review)
[![Code Health](https://landscape.io/github/andela-jmwangi/picfect-api/feature-review/landscape.svg?style=flat)]
(https://landscape.io/github/andela-jmwangi/picfect-api/feature-review)

## Picfect Rest Api

## What is it?

Django Rest Api for [Picfect PhotoEditing Application](http://picfect.herokuapp.com/)

## Features

- Authenticating users via facebook access token
- Uploading photos
- Creating filters for photos uploaded
- Fetching photos and their edited filters


### Available API Endpoints


| Endpoint                              | Functionality                                  |
|---------------------------------------|------------------------------------------------|
| GET /api/register/backend             | Authenticate a user                            |
| GET /api/images/                      | Fetch images                                   |
| POST /api/images/                     | Upload Images and generate filters             |
| GET  /api/images/id/thumbnails        | List all the filtered images of an image       |
| PUT  /api/images/id                   | Update image details                           |

## Setup

1. Run `git clone `
2. `cd` into `picfect-api`
3. Run `pip install -r requirements.txt`
4. In `pgAdmin`, create a db called `picfect` with user `picfect` and password `picfect`
5. Create a .env.yml file in the root of picfect-api with the following settings (shown settings are samples)
    ```
    DB_USER: 'picfect'

    DB_PASSWORD: 'picfect'

    SECRET_KEY: 'lu287vo)fxr+9yptgg-0sd-2%)9!2yghz((e#*ye72nklpv#qq'

    SOCIAL_AUTH_FACEBOOK_SECRET: '6539760368ca1491979f11efc15c7242'
    ```
6. Make migrations with `python picfectapi/manage.py makemigrations --settings=picfectapi.settings.development`
7. Migrate with `python picfectapi/manage.py migrate --settings=picfectapi.settings.development`
8. Run the app with `python picfectapi/manage.py runserver --settings=picfectapi.settings.development`

## Usage

For developers, the API docs can be accessed on [Picfect API Docs](https://picfectapi.herokuapp.com/docs/).

#### Example usage (Note: Examples use [HTTPie](https://github.com/jkbrzt/httpie) to send requests)

Login/Registration:

```
http -f GET picfectapi.herokuapp.com/api/auth/register/facebook/?access_token=<facebook_access_token>

HTTP/1.1 201 Created
Allow: POST, OPTIONS
Connection: keep-alive
Content-Type: application/json
Date: Fri, 15 Apr 2016 09:04:03 GMT
Server: gunicorn/19.4.5
Transfer-Encoding: chunked
Vary: Accept
Via: 1.1 vegur
X-Frame-Options: SAMEORIGIN

```

## Testing

In the project root folder, run command `python picfectapi/manage.py test api --settings=picfectapi.settings.test`

## License

The MIT License

Copyright (c) 2016 Jack Mwangi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.