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


### Assumptions and limitations
Due to the assignment specifically being small and meant to act as a signal how my fundamental skills are, I am well aware that some functions are not up to par with production ready fintech code yet.

Rounding is applied once at the final output to avoid errors mid-calculations. In production, I assume there are hard set rules as to how it should be handled, which is one of the things I'd want to get a deep understanding of. 

The API also lacks authentication and rate limiting amongst other things. I've attempted to cover the most important edge cases in the tests, mostly around invalid inputs, but a production fintech product would need significantly more coverage.

#### Final thoughts
I'm extremely excited about the opportunity to build real fintech products and learn from a strong team. I can learn quickly, I have very high ambitions and extremely high-set goals for myself.