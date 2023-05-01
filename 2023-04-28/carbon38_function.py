import requests
import json
from parsel import Selector


product_list = []


def page(page_no):
    page_no+=1
    return page_no

def get_product_details(dict):
    p_id = dict.get('p_id')
    sku = dict.get('sku')
    img_url = dict.get('url')
    response = requests.get(img_url)
    selector = Selector(text=response.text)
    product = selector.xpath('//h1/text()').get()
    vendor = selector.xpath('//h2[contains(@class, "ProductMeta__Vendor")]/a/text()').get()
    price = selector.xpath('//div[contains(@class, "ProductMeta__PriceList")]//span[contains(@class, "ProductMeta__Price")]/text()').get()
    price = price.replace('$', '').replace('USD', '')
    review = selector.xpath('//div[contains(@class, "ProductMeta__Rating")]//div[contains(@class, "okeReviews-reviewsSummary-ratingCount")]/text()').get()
    color = selector.xpath('//span[@class="ProductForm__SelectedValue "]/text()').get()
    size_list = selector.xpath('//fieldset[@class="ProductForm__Fieldset"]//li[@class="HorizontalList__Item"]/label/text()').getall()
    size_list = [size.strip() for size in size_list if size.strip() != '']
    description = selector.xpath('normalize-space(//div[@class="Faq__Answer Rte"])').get()
    img_urls = selector.xpath('//div[@class="AspectRatio AspectRatio--withFallback"]/img/@data-original-src').getall()
    img_urls = ['https:' + url for url in img_urls]

    product_dict = {
        "title": product,
        "product_url": img_url,
        "size": size_list,
        "colour": color,
        "vendor": vendor,
        "price": price,
        "img_urls": img_urls,
        "p_id": p_id,
        "review": review,            
        "sku": sku,
        "description": description
    }
    return product_dict


def get_products(page_no): 
    print(page_no)   
    global product_list
    url = f'https://api.fastsimon.com/categories_navigation?q=&page_num={page_no}&UUID=fd545484-70c2-4982-b5b5-0f2473719b1d&store_id=57860915389&sort_by=relevency&facets_required=0&with_product_attributes=1&category_id=289864155325&category_url=%2Fcollections%2Ftops'
    response = requests.get(url)
    data = json.loads(response.text)
    if ((data.get("items") == [])):
        with open("products_functions.json", "w") as f:
            for p in product_list:
                json.dump(p, f)
                f.write('\n')

        return(product_list)
    else:
        len_items = len(data.get("items"))

        for item in range(len_items):  
                sku = ((data.get("items")[item])["sku"])
                p_id = ((data.get("items")[item])["id"])
                image_url = ("https://carbon38.com" + (data.get("items")[item])["u"])
                product_dict = {
                    "p_id": p_id,
                    "url": image_url,
                    "sku": sku 
                }
                product_data = get_product_details(product_dict)
                product_list.append(product_data)
        get_products(page(page_no))

page_no=1  
get_products(page_no)
