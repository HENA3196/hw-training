import requests
import json
from parsel import Selector

class Carbon38:
    
    def clothing(self):
        
        self.page_no=1
        
        while True:
            url = f'https://api.fastsimon.com/categories_navigation?q=&page_num={self.page_no}&UUID=fd545484-70c2-4982-b5b5-0f2473719b1d&store_id=57860915389&sort_by=relevency&facets_required=0&with_product_attributes=1&category_id=289864155325&category_url=%2Fcollections%2Ftops'
            response = requests.get(url)
            data = json.loads(response.text)
            category_name = data.get("category_name")
            if ((data.get("items") == [])):
                break
            else:
                len_items = len(data.get("items"))

                for item in range(len_items):  
                        sku = ((data.get("items")[item])["sku"])
                        p_id = ((data.get("items")[item])["id"])
                        image_url = ("https://carbon38.com" + (data.get("items")[item])["u"])
                        product_dict={"p_id":p_id,
                                       "url":image_url,
                                       "sku":sku 

                                    }
                        productdata=(self.product_details(product_dict))
               
                self.page_no+=1

    def product_details(self, dict):
        self.p_id=dict.get('url')
        self.sku=dict.get('sku')
        self.img_url=dict.get('url')
        response = requests.get(self.img_url)
        selector=Selector(text=response.text)
        product=selector.xpath('//h1/text()').get()
        vendor=selector.xpath('//h2[contains(@class, "ProductMeta__Vendor")]/a/text()').get()
        price=selector.xpath('//div[contains(@class, "ProductMeta_PriceList")]//span[contains(@class, "ProductMeta_Price")]/text()').get()
        review=selector.xpath('//div[contains(@class, "ProductMeta__Rating")]//div[contains(@class, "okeReviews-reviewsSummary-ratingCount")]/text()').get()
        color=selector.xpath('//span[@class="ProductForm__SelectedValue "]/text()').get()
        size_list=selector.xpath('//li[@class="HorizontalList__Item"]/label/text()').getall()
        size = [size.strip() for size in size_list if size.strip() != '']
        description=selector.xpath('//div[@class="Faq_ItemWrapper"][1]//div[@class="Faq_Answer Rte"]/span/text()').get()
        img_urls=selector.xpath('//div[@class="AspectRatio AspectRatio--withFallback"]/img/@data-original-src').getall()
        img_urls=['https:'+ url for url in img_urls]

        dict={
            "p_id":self.p_id,
            "img_url":self.img_url,
            "sku":self.sku,
            "title":product,
            "vendor":vendor,
            "price":price,
            "review":review,
            "colour":color,
            "size":size,
            "img_urls":img_urls,
            "description":description

        }
        print(dict)
       
carbon38_obj = Carbon38()
product_data = carbon38_obj.clothing()

