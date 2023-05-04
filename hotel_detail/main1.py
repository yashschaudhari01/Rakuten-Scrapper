import requests
from bs4 import BeautifulSoup
import json
import time
import os
import pandas as pd

start_time = time.time()

df = pd.read_excel('hotel_ids.xlsx')

for i in df['id']:
    hotel_id = str(i)

    directory = hotel_id
    with open('scrapping log.txt' , 'a') as of:
        of.write(hotel_id+'\n') 
        of.write(str(start_time))
    # Parent Directories 
    try:
        parent_dir = "D:\python\Rakuten scrapper\hotel_detail\All data"
            
        path = os.path.join(parent_dir, directory) 
        os.makedirs(path) 
        print("Directory '% s' created" % directory)
        
    except Exception as ex:
        print(ex)

    try:
        url1 = 'https://travel.rakuten.co.jp/HOTEL/%s/%s.html?' %(hotel_id,hotel_id)
        req1 = requests.get(url1)
        soup1 = BeautifulSoup(req1.content,'html.parser')
        print('Scrapping started...')
        # facilities_title = soup1.find_all('div',{'id':'hotellife'})
        # facilities_title = facilities_title[0].find_all('p',{'class':'alt'})
        # facilities_title = facilities_title[1].text
        facilities = soup1.find_all('table',{'class':'kannai'})
        facilities = facilities[0].find_all('td')
        facilities_d = {}
        for i in range(0,len(facilities),2):
            facilities_d[facilities[i].text] = facilities[i+1].text.strip()
        # with open(hotel_id+"_top_page_table.json", "wb") as of:
        #     of.write(json.dumps(facilities_d,ensure_ascii=False,indent=4).encode('utf8'))
        with open(os.path.join(path, hotel_id + '_top_page_table.json'),'wb') as fp:
                    fp.write(json.dumps(facilities_d,ensure_ascii=False,indent=4).encode('utf8'))
    except Exception as ex:
        with open('scrapping log.txt' , 'a') as of:
            of.write('Top table not present\n')
            of.write('error - '+str(ex)+'\n\n')


    try:
        url = 'https://travel.rakuten.co.jp/HOTEL/%s/%s_std.html' %(hotel_id,hotel_id)
        req = requests.get(url)
        soup = BeautifulSoup(req.content,'html.parser')
        # hotel_id = soup.find_all('a',{'id':'RM_DP_PLAN'})
        # hotel_id = hotel_id[0].get('hotel_no')
        other_info_d ={}
        hotel_name = soup.find('a',{'class': 'rtconds fn'})
        hotel_name = hotel_name.text
        other_info_d['hotel_name'] = hotel_name
        with open(os.path.join(path, hotel_id + 'other_info.json'),'wb') as fp:
            fp.write(json.dumps(other_info_d,ensure_ascii=False,indent=4).encode('utf8'))
        imgs = soup.find_all('ul',{'class':'std-photo-video-thumbnail'})
        imgs = imgs[0].find_all('img')
        imgs_l = []
        c = 1
        for i in imgs:
            img_url = i.get('src')
            if 'jpg' in img_url:
                imgs_l.append(img_url)
                img_req  = requests.get(img_url)
                # open(hotel_id + '_' + str(c) +'.jpg', 'wb').write(img_req.content)
                with open(os.path.join(path, hotel_id + '_' + str(c) +'.jpg'),'wb') as fp:
                    fp.write(img_req.content)
            c+=1
        
    # with open(os.path.join(path, hotel_id+'_final_html.html'), 'wb') as fp:
    #     fp.write(final_html.encode('utf8'))

        info_titles = soup.find_all('h2',{'class':'dtlTblTtl'})
        info_titles_l = []
        for i in info_titles:
            info_titles_l.append(i.text)

        info_titles_l = info_titles_l[1:]
        # print(info_titles_l)

        basic_info = soup.find_all('ul',{'class':'dtlTbl'})
        d_basic_info_l = []
        for i in basic_info:
            d_basic_info_l.append(i.text)

        # Basic information section formatting

        i1 = d_basic_info_l[0]
        i1 = i1.split('\n\n\n\n')
        i1_l =[]

        for j in i1:
            j = j.split('\n')
            i1_l.append(j)

        for i in range(len(i1_l)):
            temp =[]
            for j in i1_l[i]:
                if j != '':
                    temp.append(j) 
            i1_l[i] = temp
        
        for i in range(len(i1_l)):
            i1_l[i] = (' '.join(i1_l[i]))


        for i in range(len(i1_l)):
            i1_l[i] = i1_l[i].split(' ')

        d_basic_info={}
        for i in i1_l:
            if len(i)>1:
                d_basic_info[i[0]] = i[1:]

        for i in d_basic_info:
            d_basic_info[i] = ' '.join(d_basic_info[i])
        print("Writing data of table 1 to json...")
        with open(os.path.join(path,hotel_id+"_table_1.json"), "wb") as of:
            of.write(json.dumps(d_basic_info,ensure_ascii=False,indent=4).encode('utf8'))
    # with open(os.path.join(path, hotel_id+'_final_html.html'), 'wb') as fp:
    #     fp.write(final_html.encode('utf8'))
        i2 = d_basic_info_l[1]
        i2_l = i2.split('\n\n\n\n\n')
        for i in  range(len(i2_l)):
            i2_l[i] = i2_l[i].split('\n')
            temp =[]
            for j in i2_l[i]:
                if j != '':
                    temp.append(j)
            i2_l[i] = temp

        for i in i2_l:
            if len(i) == 0:
                i2_l.remove(i)
        d_i2 = {}
        for i in i2_l:
            d_i2[i[0]] = i[1:]
        for i in d_i2:
            d_i2[i] = ' '.join(d_i2[i])
        print('Writing data of table2 to json...')
        with open(os.path.join(path,hotel_id+"_table_2.json"), "wb") as of:
            of.write(json.dumps(d_i2,ensure_ascii=False,indent=4).encode('utf8'))

        # covid_table = soup.find_all('ul',{'class':'covid_meatures'})
        # c_t_title = soup.find_all('h2',{'id':'id_dtlTblTtl'})

        # for i in range(len(covid_table)):
        #     dd = covid_table[i].find_all('dd')
        #     sub_table_title = covid_table[i].find_all('dt')
        # # sub_table_title = sub_table_title[:2]
        #     print()


        with open('scrapping log.txt' , 'a') as of:
            of.write('scrapping of table 1,2 and images done\n\n')
        # print('Writing data of top page table to json...')
        
    except Exception as ex:
        print(ex)
        with open('scrapping log.txt' , 'a') as of:
            of.write('Error in scrapping table 1 or 2 or images\n')
            of.write('error - '+str(ex)+'\n\n')
    
print('Program execution time :' ,end = ' ')
print("--- %s seconds ---" % (time.time() - start_time))


