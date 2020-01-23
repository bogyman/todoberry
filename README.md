# todoberry

Test project

## Installation
To run the project you need to have docker-compose installed (https://docs.docker.com/compose/install/)

Run containers:

`docker-compose up`

It creates 2 containers: 
1. db(mongoDB). Exposed port 27017
2. todoberry(uvicorn). Exposed port 7000

## Run locally
Install pip packages:

`pip3 install -r requirements.txt`

run api process:

`TODOBERRY_MONGO_HOST=localhost unicorn todoberry.app.app`

Possible env variables:
- TODOBERRY_MONGO_HOST
- TODOBERRY_MONGO_DB
- TODOBERRY_MONGO_MONGO_ITEM_COLLECTION
- TODOBERRY_MONGO_MONGO_LIST_COLLECTION

## Testing
To run functional test:
`pytest todoberry/tests/tests*
`
