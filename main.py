from parse_section import get_sections_list, get_products_list
from parse_page import get_data
from save_file import save_json


section_list = get_sections_list('https://catalog.onliner.by')

for section in section_list:
    products_urls = get_products_list(section)
    for product_url in products_urls:
        product_info = get_data(product_url)
        save_json(product_url, product_info)
