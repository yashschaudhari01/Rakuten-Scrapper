import requests
from bs4 import BeautifulSoup
import json


url = 'https://travel.rakuten.co.jp/HOTEL/27813/27813_std.html'
req = requests.get(url)
soup = BeautifulSoup(req.content,'html.parser')

hotel_title = soup.find('a',{'class': 'rtconds fn'})
hotel_title = hotel_title.text

imgs = soup.find_all('ul',{'class':'std-photo-video-thumbnail'})
imgs = imgs[0].find_all('img')
imgs_l = []
# c = 1
for i in imgs:
    img_url = i.get('src')
    imgs_l.append(img_url)
c = 1
# def generate_img_slider(imgs_l,c):
divs_l = []
for i in range(len(imgs_l)):
    img_div = ('''<div id="c11h%s"><img src="%s" alt="Banner" class="img-fluid w-100">
                    <h4 class="banhead mb-0">[[HOLE 1  PAR4  Regular309Y   HDCP17]]</h4>
                </div>''' %(str(c),imgs_l[i]))
    divs_l.append(img_div)
    c+=1
    # print(img_div)

    # return divs_l

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
    info_div = ('''<div class="col-md-6">
            <h3>%s</h3>
            <hr>
            <h5>%s</h5>
            </div>''' %(i , ' '.join(d_basic_info[i])))
    # print(info_div)
# 976 vr i2 ch takaych ahe


# 2nd info table scrapping

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


for i in d_i2:
    info_div_1 = ('''<div class="col-md-6">
            <h3>%s</h3>
            <hr>
            <h5>%s</h5>
            </div>''' %(i , ' '.join(d_i2[i])))
    print(info_div_1)

print()



# slider = ('''<!-- Layout Gallery Slider - Start -->
#   <div class="modal fade" id="layoutgallery" tabindex="-1" aria-labelledby="layoutgallerylabel" aria-hidden="true">
#     <div class="modal-dialog modal-lg">
#       <div class="modal-content">
#         <div class="modal-header"><!-- Write Golf Place Name here -->
#           <h5 class="modal-title" id="layoutgallerylabel">%s</h5>
#           <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
#         </div>
#         <div class="modal-body modal-slider mt-3">
#           <!--  Main Tab Headers Start -->
#           <ul class="nav nav-pills mb-3" id="pills-tabmainlay" role="tablist">
#             <li class="nav-item" role="presentation">
#               <button class="nav-link active" id="pills-layoutmain-tab" data-bs-toggle="pill"
#                 data-bs-target="#pills-layoutmain" type="button" role="tab" aria-controls="pills-layoutmain"
#                 aria-selected="true">Layout Gallery</button><!-- Fixed Name -->
#             </li>
#           </ul>
#           <!-- Main Tab Headers End -->
#           <!--  Main Tab Content Start-->
#           <div class="tab-content" id="pills-tabmainlayContent">
#             <div class="tab-pane fade show active" id="pills-layoutmain" role="tabpanel"
#               aria-labelledby="pills-layoutmain-tab">
#               <!--  Sub Tab Header Start--><!--  Remove respective TAB and Content if you do not want to show -->
#               <nav class="mt-5">
#                 <div class="nav nav-tabs" id="nav-tabsub" role="tablist">
#                   <!--  Course1 Header Start-->
#                   <button class="nav-link active" id="nav-course1lay-tab" data-bs-toggle="tab" data-bs-target="#nav-course1lay"
#                     type="button" role="tab" aria-controls="nav-course1lay" aria-selected="false">{{Course1}}</button>
#                   <!--  Course1 Header End-->
#                 </div>
#               </nav>
#               <!--  Sub Tab Header End-->
#               <!--  Sub Tab Content Start-->
#               <div class="tab-content numbertab" id="nav-tabsubContent">
#                 <!--  Course1 Content Start-->
#                 <div class="tab-pane fade show active" id="nav-course1lay" role="tabpanel" aria-labelledby="nav-course1lay-tab">
#                   <div class="mt-4">
#                     <ul class="nav nav-pills mb-3" id="pills-tabc1" role="tablist">
#                       <!--  course1lay Tab Header 1H Start-->
#                       <li class="nav-item" role="presentation">
#                         <button class="nav-link active" id="numberc11h-tab" data-bs-toggle="pill"
#                           data-bs-target="#numberc11h" type="button" role="tab" aria-controls="numberc11h"
#                           aria-selected="true">[[1H]]</button>
#                       </li>
#                       <!--  course1lay Tab Header 1H End-->
#                     </ul>
  
#                     <div class="tab-content" id="pills-tabc1Content">
#                       <!--  course1lay Tab Content 1H Start-->
#                       <div class="tab-pane fade show active" id="numberc11h" role="tabpanel"
#                         aria-labelledby="numberc11h-tab">
#                         <div class="owl-carousel">
#                           <!-- Add additional images as required in given section -->
#                           <div id="c11h1"><img src="%s" alt="Banner" class="img-fluid w-100">
#                             <h4 class="banhead mb-0">[[HOLE 1  PAR4  Regular309Y   HDCP17]]</h4>
#                           </div>
#                           <!-- Add additional images as required in given section -->
#                         </div>
#                       </div>
#                       <!--  course1lay Tab Content 1H End-->
#                     </div>
#                   </div>
#                 </div>
#                 <!--  Course1 Content End-->
  
#               </div>
#               <!--  Sub Tab Content End-->
#             </div>
#           </div>
#           <!--  Main Tab Content End-->
#         </div>
#       </div>
#     </div>
#   </div>''' %(hotel_title,url ))


