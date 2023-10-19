"""
Маркування тестів
"""

import pytest
from selenium.webdriver.common.by import By

link = "https://casenik.com.ua/"


class TestPage1():

    @pytest.mark.smoke
    def test_is_button_search(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, "//button[@class = 'header_search_button trans_300']")

    @pytest.mark.regression
    def test_is_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, "//a[@href = 'cart/show']")
        print("Шукаємо лінк на корзину")

    @pytest.mark.chrome_117
    @pytest.mark.regression
    def test_is_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, "//div[@class = 'top_bar_user']/a[@href = 'user/login']")


class MathMethod():

    @pytest.mark.math
    def test_2(self):
        assert 4 * 3 == 12

    @pytest.mark.math
    def test_3(self):
        assert 5 * 3 == 15

    @pytest.mark.xfail(reason='Фіксимо')
    # @pytest.mark.math
    def test_5(self):
        assert 5 * 6 == 30

    @pytest.mark.skip
    # @pytest.mark.wrong
    def test_4(self):
        assert 4 + 3 == 12


# pytest -s -v test_19102023.py
# pytest -s -v --browser_mode="gui" test_19102023.py
# pytest -s -v --browser_mode="gui" --browser_name="firefox" test_19102023.py
# pytest -s -v -m "mark" test_19102023.py
# -m mark "smoke" "regression" "chrome_117"
# -m mark "not smoke" "not regression"


