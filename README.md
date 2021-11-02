# StatusPreasensLogs 
Simple django app for collecting logs.

## Setup 
```bash
$ git clone https://github.com/injirez/StatusPreasens
$ cd SPLogs
```
### Activate venv
```bash
cd SPLogs
source venv/bin/activate
```
### Install the dependencies
```bash
(venv)$ pip3 install -r requirements.txt
```
### Run the app
```bash
(venv)$ pip3 manage.py runserver
```
## Account
### API
* url:  http://127.0.0.1:8000/
  * admin
    * Create superuser:
        * ```bash
          (venv)$ python3 manage.py createsuperuser
          ```
### DB
* host: localhost
* user: user
* password: password
* port: 5432

To change credentials of db look to DATABASES in settings.py.

## REST API
The REST API is described below.

### Pagination
* example: ``http://127.0.0.1:8000/example/?limit=10&offset=1``

### Swagger
Allows you to see all methods and usage of app.
* url: ``http://127.0.0.1:8000/swagger/``



###Get list of Users
####Request
``GET /users/``

```bash 
curl -X GET "http://127.0.0.1:8000/users/" -H  "accept: application/json"
```
#### Filters
* fio
  * ``http://127.0.0.1:8000/users/?search=example``
#### Response
```bash
 allow: GET,POST,HEAD,OPTIONS 
 content-length: 153 
 content-type: application/json 
 date: Tue,02 Nov 2021 14:57:52 GMT 
 referrer-policy: same-origin 
 server: WSGIServer/0.2 CPython/3.8.10 
 vary: Accept,Cookie 
 x-content-type-options: nosniff 
 x-frame-options: DENY 
{
  "count": 0,
  "next": "http://127.0.0.1:8000/users/",
  "previous": null,
  "results": []
}
```
### Create a new User
#### Request
``POST /users/``

```bash 
curl -X POST "http://127.0.0.1:8000/users/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa2\",  \"fio\": \"example\"}"
```

#### Response
```bash
 allow: GET,POST,HEAD,OPTIONS 
 content-length: 61 
 content-type: application/json 
 date: Tue,02 Nov 2021 15:01:19 GMT 
 referrer-policy: same-origin 
 server: WSGIServer/0.2 CPython/3.8.10 
 vary: Accept,Cookie 
 x-content-type-options: nosniff 
 x-frame-options: DENY 
{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa2",
  "fio": "example"
}
```


### Get list of log Files
#### Request
``GET /files/``

```bash 
curl -X GET "http://127.0.0.1:8000/files/" -H  "accept: application/json"
```
#### Filters
* path
  * ``http://127.0.0.1:8000/files/?search=example``
#### Response
```bash
 allow: GET,POST,HEAD,OPTIONS 
 content-length: 178 
 content-type: application/json 
 date: Tue,02 Nov 2021 15:04:54 GMT 
 referrer-policy: same-origin 
 server: WSGIServer/0.2 CPython/3.8.10 
 vary: Accept,Cookie 
 x-content-type-options: nosniff 
 x-frame-options: DENY 
{
  "count": 0,
  "next": "http://127.0.0.1:8000/files/",
  "previous": null,
  "results": []
}
```
### Create a new log File
#### Request
``POST /files/``

```bash 
curl -X POST "http://127.0.0.1:8000/files/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa2\",  \"path\": \"example\"}"
```

#### Response
```bash
 allow: GET,POST,HEAD,OPTIONS 
 content-length: 62 
 content-type: application/json 
 date: Tue,02 Nov 2021 15:06:21 GMT 
 referrer-policy: same-origin 
 server: WSGIServer/0.2 CPython/3.8.10 
 vary: Accept,Cookie 
 x-content-type-options: nosniff 
 x-frame-options: DENY 
{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa2",
  "path": "example"
}
```


### Get list of lk_django logs
#### Request
``GET /lk/``

```bash 
curl -X GET "http://127.0.0.1:8000/lk/" -H  "accept: application/json" 
```
#### Filters
* id
* func_name
* message
* sequent_log
* subsequent_log
* project_name__name
* user_uid__fio
* path_name__path

  * ``http://127.0.0.1:8000/files/?search=example``
#### Response
```bash
 allow: GET,HEAD,OPTIONS 
 content-length: 497 
 content-type: application/json 
 date: Tue,02 Nov 2021 15:27:36 GMT 
 referrer-policy: same-origin 
 server: WSGIServer/0.2 CPython/3.8.10 
 vary: Accept,Cookie 
 x-content-type-options: nosniff 
 x-frame-options: DENY 
{
  "count": 0,
  "next": "http://127.0.0.1:8000/lk/",
  "previous": null,
  "results": []
}
```
### Create a new lk_django log
#### Request
``POST /createLk/``

```bash 
curl -X POST "http://127.0.0.1:8000/createLk/" -H  "accept: application/json" -H  "Content-Type: application/json" -H  "X-CSRFToken: tvNd6asOSmP21dwOZZwiSbQd3eTkWilwextA231MNP8F5yQ7Stu2hp1PrFMbOMlj" -d "{  \"id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa2\",  \"project_name\": \"lk_django\",  \"user_uid\": \"example\",  \"path_name\": \"example\",  \"func_name\": \"example\",  \"message\": \"example\",  \"sequent_log\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",  \"subsequent_log\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\"}"
```

#### Response
```bash
 allow: GET,POST,HEAD,OPTIONS 
 content-length: 266 
 content-type: application/json 
 date: Tue,02 Nov 2021 15:33:38 GMT 
 referrer-policy: same-origin 
 server: WSGIServer/0.2 CPython/3.8.10 
 vary: Accept,Cookie 
 x-content-type-options: nosniff 
 x-frame-options: DENY 
{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa2",
  "project_name": "lk_django",
  "user_uid": "example",
  "path_name": "example",
  "func_name": "example",
  "message": "example",
  "sequent_log": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "subsequent_log": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}
```


### Get list of push_django logs
#### Request
``GET /push/``

```bash 
curl -X GET "http://127.0.0.1:8000/push/" -H  "accept: application/json" 
```
#### Filters
* id
* func_name
* message
* sequent_log
* subsequent_log
* project_name__name
* user_uid__fio
* path_name__path

  * ``http://127.0.0.1:8000/push/?search=example``
#### Response
```bash
 allow: GET,HEAD,OPTIONS 
 content-length: 508 
 content-type: application/json 
 date: Tue,02 Nov 2021 15:37:59 GMT 
 referrer-policy: same-origin 
 server: WSGIServer/0.2 CPython/3.8.10 
 vary: Accept,Cookie 
 x-content-type-options: nosniff 
 x-frame-options: DENY
{
  "count": 0,
  "next": "http://127.0.0.1:8000/push/",
  "previous": null,
  "results": []
}
```
### Create a new push_django log
#### Request
``POST /createPush/``

```bash 
curl -X POST "http://127.0.0.1:8000/createPush/" -H  "accept: application/json" -H  "Content-Type: application/json" -H  "X-CSRFToken: tvNd6asOSmP21dwOZZwiSbQd3eTkWilwextA231MNP8F5yQ7Stu2hp1PrFMbOMlj" -d "{  \"id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa2\",  \"project_name\": \"push_django\",  \"user_uid\": \"example\",  \"path_name\": \"example\",  \"func_name\": \"example\",  \"message\": \"example\",  \"sequent_log\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",  \"subsequent_log\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\"}"
```

#### Response
```bash
 allow: GET,POST,HEAD,OPTIONS 
 content-length: 266 
 content-type: application/json 
 date: Tue,02 Nov 2021 15:33:38 GMT 
 referrer-policy: same-origin 
 server: WSGIServer/0.2 CPython/3.8.10 
 vary: Accept,Cookie 
 x-content-type-options: nosniff 
 x-frame-options: DENY 
{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa2",
  "project_name": "push_django",
  "user_uid": "example",
  "path_name": "example",
  "func_name": "example",
  "message": "example",
  "sequent_log": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "subsequent_log": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}
```

### Get list of sms_django logs
#### Request
``GET /sms/``

```bash 
curl -X GET "http://127.0.0.1:8000/sms/" -H  "accept: application/json" 
```
#### Filters
* id
* func_name
* message
* sequent_log
* subsequent_log
* project_name__name
* user_uid__fio
* path_name__path

  * ``http://127.0.0.1:8000/sms/?search=example``
#### Response
```bash
 allow: GET,HEAD,OPTIONS 
 content-length: 478 
 content-type: application/json 
 date: Tue,02 Nov 2021 15:43:13 GMT 
 referrer-policy: same-origin 
 server: WSGIServer/0.2 CPython/3.8.10 
 vary: Accept,Cookie 
 x-content-type-options: nosniff 
 x-frame-options: DENY
{
  "count": 0,
  "next": "http://127.0.0.1:8000/sms/",
  "previous": null,
  "results": []
}
```
### Create a new push_django log
#### Request
``POST /createSms/``

```bash 
curl -X POST "http://127.0.0.1:8000/createSms/" -H  "accept: application/json" -H  "Content-Type: application/json" -H  "X-CSRFToken: tvNd6asOSmP21dwOZZwiSbQd3eTkWilwextA231MNP8F5yQ7Stu2hp1PrFMbOMlj" -d "{  \"id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa2\",  \"project_name\": \"sms_django\",  \"user_uid\": \"example\",  \"path_name\": \"example\",  \"func_name\": \"example\",  \"message\": \"example\",  \"sequent_log\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",  \"subsequent_log\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\"}"
```

#### Response
```bash
 allow: GET,POST,HEAD,OPTIONS 
 content-length: 263 
 content-type: application/json 
 date: Tue,02 Nov 2021 15:44:31 GMT 
 referrer-policy: same-origin 
 server: WSGIServer/0.2 CPython/3.8.10 
 vary: Accept,Cookie 
 x-content-type-options: nosniff 
 x-frame-options: DENY 
{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa2",
  "project_name": "sms_django",
  "user_uid": "example",
  "path_name": "example",
  "func_name": "example",
  "message": "example",
  "sequent_log": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "subsequent_log": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}
```


### Get list of spnavigator_django logs
#### Request
``GET /spnavigator/``

```bash 
curl -X GET "http://127.0.0.1:8000/spnavigator/" -H  "accept: application/json" 
```
#### Filters
* id
* func_name
* message
* sequent_log
* subsequent_log
* project_name__name
* user_uid__fio
* path_name__path

  * ``http://127.0.0.1:8000/spnavigator/?search=example``
#### Response
```bash
 allow: GET,HEAD,OPTIONS 
 content-length: 508 
 content-type: application/json 
 date: Tue,02 Nov 2021 15:45:59 GMT 
 referrer-policy: same-origin 
 server: WSGIServer/0.2 CPython/3.8.10 
 vary: Accept,Cookie 
 x-content-type-options: nosniff 
 x-frame-options: DENY
{
  "count": 0,
  "next": "http://127.0.0.1:8000/spnavigator/",
  "previous": null,
  "results": []
}
```
### Create a new spnavigator_django log
#### Request
``POST /createSpn/``

```bash 
curl -X POST "http://127.0.0.1:8000/createSpn/" -H  "accept: application/json" -H  "Content-Type: application/json" -H  "X-CSRFToken: tvNd6asOSmP21dwOZZwiSbQd3eTkWilwextA231MNP8F5yQ7Stu2hp1PrFMbOMlj" -d "{  \"id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa2\",  \"project_name\": \"spnavigator_django\",  \"user_uid\": \"example\",  \"path_name\": \"example\",  \"func_name\": \"example\",  \"message\": \"example\",  \"sequent_log\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",  \"subsequent_log\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\"}"
```

#### Response
```bash
 allow: GET,POST,HEAD,OPTIONS 
 content-length: 274 
 content-type: application/json 
 date: Tue,02 Nov 2021 15:47:38 GMT 
 referrer-policy: same-origin 
 server: WSGIServer/0.2 CPython/3.8.10 
 vary: Accept,Cookie 
 x-content-type-options: nosniff 
 x-frame-options: DENY 
{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa2",
  "project_name": "spnavigator_django",
  "user_uid": "example",
  "path_name": "example",
  "func_name": "example",
  "message": "example",
  "sequent_log": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "subsequent_log": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}
```
