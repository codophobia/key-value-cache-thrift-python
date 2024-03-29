[![build-test](https://github.com/codophobia/key-value-cache-thrift-python/actions/workflows/build-test.yaml/badge.svg)](https://github.com/codophobia/key-value-cache-thrift-python/actions/workflows/build-test.yaml) [![lint](https://github.com/codophobia/key-value-cache-thrift-python/actions/workflows/lint.yaml/badge.svg)](https://github.com/codophobia/key-value-cache-thrift-python/actions/workflows/lint.yaml) [![release](https://github.com/codophobia/key-value-cache-thrift-python/actions/workflows/release.yaml/badge.svg)](https://github.com/codophobia/key-value-cache-thrift-python/actions/workflows/release.yaml) ![GitHub License](https://img.shields.io/github/license/codophobia/key-value-cache-thrift-python) ![PyPI - Version](https://img.shields.io/pypi/v/thriftcacheserver)

## key-value-cache-thrift-python
Implement a simple key value cache using thrift and Python

## Set up virtual environment
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Start the cache server
```
python3 -m cache run-server
```

## Run the client
```
python3 -m cache run-client
```

## Run tests
```
pytest cache
```

## Run flake
```
flake8 cache --exclude gen
```