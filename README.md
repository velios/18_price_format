# Price Formatter

Script takes unformatted price and format it.<br>
Program have two interfaces:
* API - for use in site
* command line - for use from command line

### How to Use


##### Use from command line
```bash
$ python3 format_price.py -p 1234567.00
1 234 567.00
$ python3 tests.py # Test application with unittest
OK
Ran 3 tests in 0.0000s 
```

##### Use like API
```python
from format_price import format_price
# now you may use function format_price in your app
```

### Behaviour

If value can not be formatted return `None`


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
