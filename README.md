# Ikano Assignment

### Clone the repo
```
git clone https://github.com/augustsletto/ikano2.git
cd ikano
```

### Install dependencies
```
uv sync
# or 
pip install -r requirements.txt
```

### Run the FastAPI server
```
uv run fastapi dev

# or

uvicorn main:app --host 0.0.0.0 --port 8000

# or with docker

docker compose up --build

```
http://localhost:8000/docs for the API docs


### Run tests
```
uv run pytest tests/ -v

# or 

python -m pytest tests/ -v
```

### API Endpoints

```
# fibonacci example API call

curl -X 'POST' \
  'http://localhost:8000/fibonacci/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"n": 10}'

# response body
{
  "fibonacci_int": "55"
}
```

```
# factorial example API call

curl -X 'POST' \
  'http://localhost:8000/factorial/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"n": 52}'


# response body
{
  "factorial_int": "80658175170943878571660636856403766975289505440883277824000000000000"
}
```



```
# loan example API call

curl -X 'POST' \
  'http://localhost:8000/loan/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "principal": 100000,
  "annual_rate": 0.05,
  "months": 48
}'

# response body
{
    "monthly_repayment":"2302.93"
}
```

