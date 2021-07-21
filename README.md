# NBA Finder - 
This project connects to NBA data to find various data

## Documentation

- [pytest](http://pytest.org)
- [requests](https://docs.python-requests.org/en/master/)


## Installation
I strongly recommend to use a Virtual Environment for this project.

### pytest and requests

```pip install pytest``` and ```pip install requests```

## Run in console

```python nba/nba_finder.py _height_```

where height must be written in inches.


Example: ```python nba/nba_finder.py 177```

With the current data, the tallest players are at 177 Inches, and the Shortest players are at 139 Inches


## Run tests

```
pytest                           // runs all tests in all folders recursively
pytest -v                        // verbose output

pytest tests                     // specific test package
pytest tests/test_nba_finder.py  // specific test module

pytest --duration=3              // profiling of 3 slowest (test) functions
pytest --doctest-modules         // run doctests
```