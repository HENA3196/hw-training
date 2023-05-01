from parsel import Selector

# HTML,XML USES CSS/ XPATH


html_text = "<html><body><h1>Hello, Parsel!</h1></body></html>"
html_selector = Selector(html_text)
print(html_selector.css('h1'))    #css
print(html_selector.xpath('//h1'))  # XPath



# JSON USES JMESPATH
# NOT WORKING
# json_text = '{"title":"Hello, Parsel!"}'
# json_selector = Selector(text=json_text)
# print(json_selector.jmespath('title'))

