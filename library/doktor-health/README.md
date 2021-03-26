# Doktor-health
This library is used to monitor the state of the doktor microservice, a thesis search service.
Doktor:
https://github.com/cdsl-research/doktor

# Usage
## Install
Install with
```
pip install "git+ssh://git@github.com/cdsl-research/doktor.git#egg=doktor-health&subdirectory=library/doktor-health"
```

## Import
```
import doktor_health
```
or  
```
from doktor_health import health
```

## When use in requirements
```text
-e git+https://git@github.com/cdsl-research/doktor.git#egg=doktor-health&subdirectory=library/doktor-health  
```
