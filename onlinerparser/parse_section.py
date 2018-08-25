import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import requests
from bs4 import BeautifulSoup


def get_sections_list(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    products = soup.find_all('a', {'class': 'catalog-navigation-list__dropdown-item'})
    section_list = []
    for product in products:
        url = product['href'].split("?", 1)[0]
        section_list.append(url)
    return section_list

#  bad
def check_exists_by_xpath(driver):
    try:
        driver.find_element_by_xpath('//a[@class="schema-pagination__main schema-pagination__main_disabled"]')
    except NoSuchElementException:
        return False
    return True


def get_products_list(section_url):
    products_urls = []
    driver = webdriver.Chrome()
    driver.get(section_url)
    while not check_exists_by_xpath(driver):
        time.sleep(2)
        products = driver\
            .find_element_by_xpath('//div[@class="schema-products"]')\
            .find_elements_by_xpath('//div[@class="schema-product__title"]//a[@data-bind="attr: {href: product.html_url}"]')
        for product in products:
            product_url = product.get_attribute('href')
            products_urls.append(product_url)
        driver.find_element_by_xpath('//div[@class="schema-pagination schema-pagination_visible"]').click()
    return products_urls
