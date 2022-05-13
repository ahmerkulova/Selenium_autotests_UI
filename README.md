## Final project of the course [Test automation via Selenium and Python](https://stepik.org/course/575) (Stepik)

Packages to run tests are in requirements.txt

- To run negative checks:
```
pytest -rxs -vm negative test_product_page.py
```
- To run review tests:
```
pytest -rxs -vm need_review test_product_page.py
```
- To run test with parametrization:
1. Uncomment the line for the method test_guest_can_add_product_to_basket (test_product_page.py)
2. Add parameter 'link' to method
3.
```
pytest -sv test_product_page.py::test_guest_can_add_product_to_basket
```
