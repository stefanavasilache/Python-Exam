# Proiect-Python
In the project i've installed the next tools in order to scrape data rom 2 online shops, details : 

https://www.anaconda.com/
https://scrapy.org/

In order to create the spiders which are collecting the data i've used the next command:

scrapy genspider name_of_the_spider url_of_the_website
In the URL must be removed the HTTP because this part is going to be added automatically

To be able to create the xml paths for collecting the details needed wnet to scarpy shell, there I've fetched the data with:

fetch("")

To get the titles prices, i've created a var as in the next exemple:

var = response.xpath("//div[@class='produs-price']/span/span/sup/text()")

To retrieve the data :

var.getall()
