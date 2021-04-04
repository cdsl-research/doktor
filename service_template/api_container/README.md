# api_container

## Setup for dev

Setup python environment

```
python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
```
 
Run app

```
python web/main.py
```

Access `http://localhost:5000/` by Web Browser.

## Container support

Build image

```
docker build -t api_container .
```

Run container

```
docker run -it --rm -p 5000:5000 api_container

curl http://localhost:5000/healthz
```
