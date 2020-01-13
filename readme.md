# Q-CTRL Back-end Engineering Challenge

## Details
See [Challenge Details](https://github.com/qctrl/back-end-challenge)

## Requirements
This project is developed on __Python 3.8__ Environment with __Django 3__ Framework. Django Rest Framework is used to handle Rest API. All required packages can be found in Pipfile.

## Usage
Run server: `python manage.py runserver`

Before running the server, please make sure to configure Database setting.

## APIs
|Method|Url|Description|
|--|--|--|
|`GET`|`/controls`|List all controls (Five per page)
|`POST`|`/controls/`|Create a new control
|`GET`|`/controls/:id`|Get a specific control
|`PUT`|`/controls/:id/`|Update a specific control
|`DELETE`|`/controls/:id/`|Delete a specific control
|`POST`|`/controls/bulk`|Bulk upload controls in CSV format
|`GET`|`/controls/download`|Download controls in CSV format
