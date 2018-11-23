# DRF Tutorial

## Test Environment Setting

### Install pipenv
> This project using pipenv so, if you want to run, you have to install pipenv before run
* using pip
```bash
$ pip install pipenv
```

* using homebrew (in mac)
```bash
$ brew install pipenv
```

* using apt (in ubuntu)
```bash
$ sudo apt install software-properties-common python-software-properties
$ sudo add-apt-repository ppa:pypa/ppa
$ sudo apt update
$ sudo apt install pipenv
```

### Install Packages for Production Environment
```bash
$ pipenv install
``` 
Then, pipenv install packages:
* django
* djangorestframework
* pygments
* djangorestframework-jwt

### Install Packages for Development Environment
```bash
$ pipenv install --dev
``` 
Then, pipenv install packages:
* [production packages]
* httpie

If you want to run examples in README, you have to install packages for dev env.


## JWT Authentication

### Obtain JWT Token
* Request
```bash
$ http -f POST http://localhost:8000/auth/ username='username' password='password'
```
* Response
```
HTTP/1.1 200 OK
Allow: POST, OPTIONS
Content-Length: 193
Content-Type: application/json
Date: Fri, 23 Nov 2018 02:12:44 GMT
Server: WSGIServer/0.2 CPython/3.7.0
Vary: Accept
X-Frame-Options: SAMEORIGIN

{
    "token": "<token>"
}
```

### Request w/ JWT Token
* Request

Send request with `Authorization` header 

```bash
$ http http://localhost:8000/ 'Authorization: JWT <token>'
```

* Response
```
HTTP/1.1 200 OK
Allow: GET, HEAD, OPTIONS
Content-Length: 85
Content-Type: application/json
Date: Fri, 23 Nov 2018 02:21:46 GMT
Server: WSGIServer/0.2 CPython/3.7.0
Vary: Accept
X-Frame-Options: SAMEORIGIN

{
    "snippets": "http://localhost:8000/snippets/",
    "users": "http://localhost:8000/users/"
}
```

* If wrong token
```
HTTP/1.1 401 Unauthorized
Allow: GET, HEAD, OPTIONS
Content-Length: 38
Content-Type: application/json
Date: Fri, 23 Nov 2018 02:20:59 GMT
Server: WSGIServer/0.2 CPython/3.7.0
Vary: Accept
WWW-Authenticate: JWT realm="api"
X-Frame-Options: SAMEORIGIN

{
    "detail": "Error decoding signature."
}
```

* If signature was expired
```
HTTP/1.1 401 Unauthorized
Allow: GET, HEAD, OPTIONS
Content-Length: 35
Content-Type: application/json
Date: Fri, 23 Nov 2018 02:21:14 GMT
Server: WSGIServer/0.2 CPython/3.7.0
Vary: Accept
WWW-Authenticate: JWT realm="api"
X-Frame-Options: SAMEORIGIN

{
    "detail": "Signature has expired."
}
```

### Refresh Token
* Request
```
$ http -j POST http://localhost:8000/auth/refresh/ token=<token>
```

* Response
```
HTTP/1.1 200 OK
Allow: POST, OPTIONS
Content-Length: 223
Content-Type: application/json
Date: Fri, 23 Nov 2018 02:46:38 GMT
Server: WSGIServer/0.2 CPython/3.7.0
Vary: Accept
X-Frame-Options: SAMEORIGIN

{
    "token": "<new token>"
}
```

### Verify Token
* Request
```
$ http -j POST http://localhost:8000/auth/verify/ token=<token>
```

* Response
```
HTTP/1.1 200 OK
Allow: POST, OPTIONS
Content-Length: 223
Content-Type: application/json
Date: Fri, 23 Nov 2018 02:47:03 GMT
Server: WSGIServer/0.2 CPython/3.7.0
Vary: Accept
X-Frame-Options: SAMEORIGIN

{
    "token": "<token>"
}
```

## References
* Base codes: [http://raccoonyy.github.io/drf3-tutorial-1.html](http://raccoonyy.github.io/drf3-tutorial-1.html)
* DRF Reference: [https://www.django-rest-framework.org/api-guide/pagination/](https://www.django-rest-framework.org/api-guide/pagination/)
* JWT Authentication: [https://getblimp.github.io/django-rest-framework-jwt/](https://getblimp.github.io/django-rest-framework-jwt/)