# revolut

This repo contain both programming tasks.

#### Run REST service

`python api.py`

username: `admin` and password:`admin`

application in running on Port 5000

endpoint is `/api` with query string `keys` to pass keys to create nested dict

example curl: 

```curl -X post -H "Content-Type: application/json" --user admin:admin -d "@input.json" http://localhost:5000/api?keys=currency,country,city```
