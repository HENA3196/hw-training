import requests
import json


product = []

class Carbon38:

    def clothing(self):
        
        self.page_no=0
        
        while True:
            url = f'https://api.fastsimon.com/categories_navigation?q=&page_num={self.page_no}&UUID=fd545484-70c2-4982-b5b5-0f2473719b1d&store_id=57860915389&sort_by=relevency&facets_required=0&with_product_attributes=1&category_id=289864155325&category_url=%2Fcollections%2Ftops'
            response = requests.get(url)
            data = json.loads(response.text)
            category_name = data.get("category_name")
            if ((data.get("items") == [])):
                break
            else:
                len_items = len(data.get("items"))

                for i in range(len_items):        
                    title = ((data.get("items")[i])["l"])
                    title, seperator, color = title.rpartition(" - ")
                    image_url = ("https://carbon38.com" + (data.get("items")[i])["u"])
                    price = ("$" + (data.get("items")[i])["p"] + " USD")
                    description = ((data.get("items")[i])["d"])
                    description=description.replace('\u00a0', '').replace('\u00e9', '').replace('\n', '').replace('\n\n', '')
                    sku = ((data.get("items")[i])["sku"])
                    p_id = ((data.get("items")[i])["id"])
                    vendor = ((data.get("items")[i])["v"])

                    size_list = []
                    skus = ((data.get("items")[i])["skus"])
                    skus_len = len(skus)
                    for i in range(skus_len // 2):
                        size = skus[i]
                        x, seperator, size = size.rpartition("-")
                        size_list.append(size)

                    product_dict = {
                        "product_name": title,
                        "img_src": image_url,
                        "Brand": vendor,
                        "color": color,
                        "price": price,
                        "size": size_list,
                        "pid": p_id,
                        "sku": sku,
                        "description": description
                    }

                    product.append(product_dict)

                
            self.page_no += 1

        
        return product
carbon38_obj = Carbon38()
product_data = carbon38_obj.clothing()

with open("product_data.json", "w") as f:
    json.dump(product_data, f, indent=2)
