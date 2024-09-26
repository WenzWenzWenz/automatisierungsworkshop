"""
Author: Lukas Wenz
Date: 26. Sep 2024
Version: 1.0
Description: This script was created to learn the basics of the WebDriver part of the Selenium toolbox during Dr. Felix
  Boes' workshop on automation.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def wait_and_find_element(driver, by, value, timeout=0.5):
    """
    Wait for an element to be present on the website and return a Selenium link to it. Raises an exception on timeout.
    :param driver: the WebDriver object to use
    :param by: the By object by which the HTML structural element gets located (e.g. By.ID, By.CLASS_NAME, By.XPATH)
    :param value: the value of the HTML structural element to locate
    :param timeout: the number of seconds to wait for the element to be present; o/w raise an exception
    :return: a link to the element if it is present
    """
    WebDriverWait(driver, timeout).until(
        expected_conditions.presence_of_element_located((by, value)))
    return driver.find_element(by, value)

def main():
    """
    This script opens a Chrome browser session, searches for "Cookie Clicker" on DuckDuckGo, clicks on the first link,
    accepts the cookie consent, selects the English language, and farms cookies automatically. The script could in
    future be upgraded by using different threads to farm cookies faster. Note that the function does not return on its
    own.
    """
    # open a Chrome browser session
    driver = webdriver.Chrome()

    # open the website (use sleep to wait for the page to load and see the result)
    driver.get("https://duckduckgo.com/")

    # wait for the search box to load; on timeout, raise an exception; grab link to the element
    # read: the first of any element, whose ID attribute is equal to "searchbox_input"
    search_box_element = wait_and_find_element(driver, By.XPATH, '//*[@id="searchbox_input"]', timeout=3)

    # put some string into the search box and press ENTER key to initialize the search query
    search_box_element.send_keys("Cookie Clicker" + Keys.ENTER)

    # wait for the search results to load, on timeout, raise an exception; grab link to the element
    # read: the first link element (a stands for link), whose data-testid attribute is equal to "result-title-a"
    # we found this attribute in the browser console, so we use it (because Chrome's copied XPATH is not ideal)
    first_link_element = wait_and_find_element(driver, By.XPATH, '//a[@data-testid="result-title-a"]')

    # click on the first link of the search query to reach the Website
    first_link_element.click()

    # wait for the cookie consent button to load, if duration is timeout, raise an exception
    consent_button_element = wait_and_find_element(driver, By.CLASS_NAME, 'fc-cta-consent', timeout=2)

    # click on the cookie consent button to get rid of that pop-up
    consent_button_element.click()

    # wait for the language selection to load, on timeout, raise an exception; grab link to the element
    language_button_element = wait_and_find_element(driver, By.XPATH, '//*[@id="langSelect-EN"]', timeout=2)

    # click on the language selection (english)
    language_button_element.click()

    # wait for the big cookie to load, on timeouted, raise an exception; grab link to the element
    big_cookie_element = wait_and_find_element(driver, By.ID, 'bigCookie', timeout=4)

    # farm cookies automatically :)
    while True:
        big_cookie_element.click()


if __name__ == '__main__':
    main()
