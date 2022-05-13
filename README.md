## Final project of the course [Test automation via Selenium and Python](https://stepik.org/course/575) (Stepik)
###Stack
- Selenium Webdriver 3.14.0
- Python 3.10.2
- Google Chrome 101.0.4951.41
- Pytest 5.1.1 

Recommended to run test from the virtual environment. Packages to run tests are in requirements.txt. To install:
```
pip install -r requirements.txt
```

- To run review tests:
```
pytest -rxs -vm need_review test_product_page.py
```
- To run negative checks:
```
pytest -rxs -vm negative test_product_page.py
```
- To run test with parametrization:
1. Uncomment the line for the method test_guest_can_add_product_to_basket (test_product_page.py)
2. Add parameter 'link' to method
3. Run in command line
```
pytest -sv test_product_page.py::test_guest_can_add_product_to_basket
```
