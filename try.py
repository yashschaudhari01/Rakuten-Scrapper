import requests

url ='https://bam.nr-data.net/jserrors/1/7763a18cec?a=755343931&sa=1&v=1177.96a4d39&t=Unnamed%20Transaction&rst=1324101&ck=1&ref=https://travel.rakuten.com/usa/en-us/hotel_info_item/cnt_japan/sub_tokyo/cty_chuo_ward/10123456874075/&xhr=%5B%7B%22params%22:%7B%22method%22:%22POST%22,%22host%22:%22rat.rakuten.co.jp:443%22,%22pathname%22:%22/%22,%22status%22:200%7D,%22metrics%22:%7B%22count%22:1,%22txSize%22:%7B%22t%22:1602%7D,%22duration%22:%7B%22t%22:9896%7D,%22cbTime%22:%7B%22t%22:0%7D,%22time%22:%7B%22t%22:1298994%7D%7D%7D%5D'
myobj = {'somekey': 'somevalue'}

pay="""a=755343931&sa=1&v=1177.96a4d39&t=Unnamed%20Transaction&rst=1324101&ck=1&ref=https://travel.rakuten.com/usa/en-us/hotel_info_item/cnt_japan/sub_tokyo/cty_chuo_ward/10123456874075/&xhr=%5B%7B%22params%22:%7B%22method%22:%22POST%22,%22host%22:%22rat.rakuten.co.jp:443%22,%22pathname%22:%22/%22,%22status%22:200%7D,%22metrics%22:%7B%22count%22:1,%22txSize%22:%7B%22t%22:1602%7D,%22duration%22:%7B%22t%22:9896%7D,%22cbTime%22:%7B%22t%22:0%7D,%22time%22:%7B%22t%22:1298994%7D%7D%7D%5D"""

payload = pay.split("&")

x = requests.post(url, json = myobj)

