# NBA Finder - 
This project connects to NBA data to find various data

## Documentation

- [pytest](http://pytest.org)
- [requests](https://docs.python-requests.org/en/master/)


## Installation

### pytest

```pip install pytest``` and ```pip install requests```


## Run tests

```
pytest                           // runs all tests in all folders recursively
pytest -v                        // verbose output

pytest -k test_add               // specific test
pytest tests                     // specific test package
pytest tests/test_nba_finder.py  // specific test module

pytest --duration=3              // profiling of 3 slowest (test) functions
pytest --doctest-modules         // run doctests
```