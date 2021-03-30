# Doktor-health

This library is used to monitor the state of the doktor microservice, a thesis search service.

# Usage

## Install

Install with

```
pip install "git+ssh://git@github.com/cdsl-research/doktor.git#egg=doktor-health&subdirectory=library/doktor-health"
```

## Example code

```
from doktor_health import health

@app.route("/healthz")
def healthz():
    my_health = health.Health()
    return json.jsonify(my_health)

@app.route("/healthz")
def healthz():
    my_health = health.Health(
        health.HealthStatus.RED,
        "Database connection error"
    )
    return json.jsonify(my_health)
```

## When use in requirements

```
-e git+https://git@github.com/cdsl-research/doktor.git#egg=doktor-health&subdirectory=library/doktor-health  
```
