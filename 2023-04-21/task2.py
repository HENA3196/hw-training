import requests
from parsel import Selector
import json

response = requests.get("https://carbon38.com/collections/shop-all?")
selector = Selector(text=response.text)
print(selector)

product = []

for selector in selector.xpath('//ul[@id="isp_search_results_container"]//li'):
	
	product_title= selector.css('div.isp_product_title::text').get()
	color = product_title.split(' - ')[-1]
	product_title = product_title.replace(f" - {color}", "")
	vendor=selector.css('div.isp_product_vendor::text').get()
	price="$"+selector.css('span.isp_product_price::text').get()
	img = selector.css('a.isp_product_image_href img.isp_product_image')
	img_src = 'https:'+img.xpath('@src').get()
	p_id=selector.xpath("@product_id").get()
	 
	product_dict={
    	"product_name": product_title,
    	"img_src": img_src,
    	"Brand": vendor,
    	"color": color,
      	"price": price,
     	"pid":p_id,
       	}
	
	product.append(product_dict)
with open("products.json","w") as f:
#     json.dump(product,f)
