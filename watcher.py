import os
from selenium import webdriver
import logging
from urllib import request


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime) %(levelname)-5.5s: %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

url = 'https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3080/'


def is_element_present(driver, selector, wait_time=None):
    driver.find_elements_by_css_selector('selector')


def main():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver_path = '/usr/lib/chromium-browser/chromedriver'
    if not os.path.isfile(driver_path):
        raise FileNotFoundError('Chromedriver not installed')

    driver = webdriver.Chrome(
        executable_path=driver_path, chrome_options=options)
    driver.get(url)
    is_element_present(driver, '.btn.show-out-of-stock', )


if __name__ == '__main__':
    main()
