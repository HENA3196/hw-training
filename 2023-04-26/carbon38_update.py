import requests
import json


product = []

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
                    title = ((data.get("items")[item])["l"])
                    title, seperator, color = title.rpartition(" - ")
                    image_url = ("https://carbon38.com" + (data.get("items")[item])["u"])
                    price = ((data.get("items")[item])["p"])
                    description = ((data.get("items")[item])["d"])
                    description=description.replace('\u00a0', '').replace('\u00e9', '').replace('\n', '').replace('\n\n', '').replace('\u2019','')
                    sku = ((data.get("items")[item])["sku"])
                    p_id = ((data.get("items")[item])["id"])
                    vendor = ((data.get("items")[item])["v"])

                    size_list = []
                    skus = ((data.get("items")[item])["skus"])
                    skus_len = len(skus)
                    if skus_len==1:
                        size=skus[0]
                        x, seperator, size = size.rpartition("-")
                        size_list.append(size)                        
                    else:
                        for sizes in range(skus_len // 2):
                            size = skus[sizes]
                            x, seperator, size = size.rpartition("-")
                            size_list.append(size)

                    product_dict = {
                        "product_title": title,
                        "product_url": image_url,
                        "vendor": vendor,                                                
                        "price": price,
                        "colour": color,
                        "sizes": size_list,
                        "description": description,
                        "product_id": p_id,
                        "sku": sku,
                    }

                    product.append(product_dict)
                
            self.page_no += 1
        
        return product
carbon38_obj = Carbon38()
product_data = carbon38_obj.clothing()

with open("products_data.json", "w") as f:
    for p in product_data:
        json.dump(p, f)
        f.write('\n')
