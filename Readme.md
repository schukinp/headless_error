# Precondition

* [Python 3+](https://www.python.org/) and built in manager pip3
* Browser [Chrome](https://www.google.com/chrome/)
* [ChromeDriver](https://chromedriver.storage.googleapis.com/index.html) for Chrome


# Installation

Install dependencies `pip install -r requirements.txt`

# Start tests

```
$ pytest test_foo.py
```

# Execution Traceback
```
============================= test session starts ==============================
platform darwin -- Python 3.6.8, pytest-6.1.2, py-1.9.0, pluggy-0.13.1 -- /Users/apple/PycharmProjects/headless_error/venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/apple/PycharmProjects/headless_error
collecting ... collected 2 items

test_foo.py::TestFoo::test_one 
test_foo.py::TestFoo::test_two 

============================== 2 passed in 5.94s ===============================

Process finished with exit code 0
PASSED                                    [ 50%] 
[WDM] - Current google-chrome version is 86.0.4240
[WDM] - Get LATEST driver version for 86.0.4240
[WDM] - Driver [/Users/apple/.wdm/drivers/chromedriver/mac64/86.0.4240.22/chromedriver] found in cache
PASSED                                    [100%]
```