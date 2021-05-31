import requests
import luigi
from bs4 import BeautifulSoup
import json


class brands(luigi.Task):

    store_num = luigi.IntParameter()

    def run(self):
        url = "https://stores.shoppersdrugmart.ca/en/store/" + str(self.store_num)

        html = requests.get(url).content
        
        data = BeautifulSoup(html, 'html.parser')
        
        parent = data.find("body").find_all("ul", class_ = "shoppers-list" )
        
        info = parent[1].text
        print(info)

        with open('brands.txt', 'a') as f:
            f.write("store Number:" + str(self.store_num))
            f.write('\n')
            f.write(str(info))
            f.write('\n')

if __name__ == '__main__':
    luigi.build([brands(500),brands(534),brands(561),brands(571)], workers=5, local_scheduler=True)


        