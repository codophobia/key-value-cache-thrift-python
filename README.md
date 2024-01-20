# key-value-cache-thrift-python
Implement a simple key value cache using thrift and Python

# Set up virtual environment
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

# Start the cache server
```
python3 -m cache run-server
```

# Run the client
```
python3 -m cache run-client
```

# Run tests
```
pytest cache
```

# Run flake
```
flake8 cache --exclude gen
```