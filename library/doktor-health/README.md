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
    my_health = health.Health(status=health.HealthStatus.GREEN,
                              description="It works")
    return json.jsonify(my_health.to_dict())
```

## When use in requirements

```
-e git+https://git@github.com/cdsl-research/doktor.git#egg=doktor-health&subdirectory=library/doktor-health  
```
