import json
import time
import os
import pandas as pd
start_time = time.time()


df = pd.read_excel('hotel_ids.xlsx')

for i in df['id']:
    hotel_id = str(i)
    directory = hotel_id  
    parent_dir = "D:\python\Rakuten scrapper\hotel_detail\All data"
    
    path = os.path.join(parent_dir, directory) 
    with open('html_update log.txt' , 'a') as of:
        of.write(hotel_id+'\n')
        of.write(str(start_time))
    # with open(os.path.join(path, hotel_id+'_final_html.html'), 'wb') as fp:
    #     fp.write(final_html.encode('utf8'))
    try:
        temp_table_1_1 = '''<div class="row gy-5 basicinfo">
                <h3 class="headnew mb-4">基本情報</h3>
                '''
        temp_table_1_3 = '''
            </div>'''

        table_1 = open(os.path.join(path,hotel_id+'_table_1.json'),'r',encoding='utf-8')
        table_1 = json.loads(table_1.read())
        temp_table_1_2 = ''
        for i in table_1:
            info_div = ('''<div class="col-md-6">
                    <h3>%s</h3>
                    <hr>
                    <h5>%s</h5>
                    </div>
                    ''' %(i , ' '.join(table_1[i])))
            temp_table_1_2+=info_div

        c_text_1 = temp_table_1_1+temp_table_1_2+temp_table_1_3

        with open(os.path.join(path, hotel_id+'_table_1.txt'), 'wb') as fp:
            fp.write(c_text_1.encode('utf8'))

        try:
            other_info = open(os.path.join(path,hotel_id+'other_info.json'),'r',encoding='utf-8')
            other_info = json.loads(other_info.read())
            hotel_name = other_info['hotel_name']
        except :
            pass

        # with open(hotel_id+'_table_1.txt','wb') as of:
        #     of.write(c_text_1.encode('utf8'))
        # print(temp_table_1_1+temp_table_1_2+temp_table_1_3)



        temp_table_2_1 = '''<div class="row gy-5 basicinfo">
                <h3 class="headnew mb-4">その他設備・サービス</h3>
                '''
        temp_table_2_3 = '''
            </div>'''
        table_2 = open(os.path.join(path,hotel_id+'_table_2.json'),'r',encoding='utf-8')
        table_2 = json.loads(table_2.read())
        temp_table_2_2 = ''
        for i in table_2:
            info_div_2 = ('''<div class="col-md-6">
                    <h3>%s</h3>
                    <hr>
                    <h5>%s</h5>
                    </div>''' %(i , ' '.join(table_2[i])))
            temp_table_2_2+=info_div_2
            # print(info_div_1)
        c_text_2 = temp_table_2_1+temp_table_2_2+temp_table_2_3

        with open(os.path.join(path, hotel_id+'_table_2.txt'), 'wb') as fp:
            fp.write(c_text_2.encode('utf8'))

        # with open(hotel_id+'_table_2.txt','wb') as of:
        #     of.write(c_text_2.encode('utf8'))

        try :
            top_page_table1 = '''<div class="row topspace2">
                    <div class="col-md-12 table2">
                    <h3 class="headnew mb-4">≫館内のご案内</h3>
                    <table class="table  table-bordered mt-3 ">
                        <tbody>
                        '''
                        
            top_page_table3 ='''</tbody>
                    </table>
                    </div>
                </div>'''
            temp_str = ''''''
            top_page_table = open(os.path.join(path,hotel_id+'_top_page_table.json'),'r',encoding='utf-8')
            top_page_table = json.loads(top_page_table.read())
            for i in top_page_table:
                tr = ('''<tr>
                            <td class="w-25 color-td">%s</td>
                            <td>%s</td>
                        </tr>
                        ''' %(i , ' '.join(top_page_table[i])))
                temp_str+=tr
            main = top_page_table1 +temp_str+top_page_table3

            with open(os.path.join(path, hotel_id+'_top_table.txt'), 'wb') as fp:
                fp.write(main.encode('utf8'))
            tt_flag = True
            # with open(hotel_id+'_top_table.txt','wb') as of:
            #     of.write(main.encode('utf8'))
        except Exception as ex:
            print(ex)
            tt_flag = False
            with open('html_update log.txt' , 'a') as of:
                of.write('Top page table not present.\n')
        img_div =''
        flag = True
        c = 1
        for images in os.listdir(path):
        
            # check if the image ends with png
            # if (images.endswith(".jpg")):
            #     # print(c)
            #     s = '''<div id="c11h%s"><img src= '%s' alt="Banner" class="img-fluid w-100">
            #             </div>''' %(str(c),'/storage/uploads/HotelMaster/'+hotel_id+'/'+images)
            #     img_div+=s+'\n'
            #     # print(images)
            #     c+=1
            if (images.endswith(".jpg")):
                # print(c)
                s = '''<div id="c11h%s"><img src= '%s' alt="Banner" class="img-fluid w-100">
                        </div>''' %(str(c),'D:\python\Rakuten scrapper\hotel_detail\All data/'+hotel_id+'/'+images)
                img_div+=s+'\n'
                # print(images)
                c+=1





        final_html_1 = '''<!doctype html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="">
  <meta name="author" content="">
  <meta name="generator" content="">
  <title>Golf</title>
  <!-- CSS -->
  <link href="css/bootstrap.min.css" rel="stylesheet">
  <!-- Favicons -->
  <link rel="icon" href="images/favicon.png" type="image/png">
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700;900&display=swap" rel="stylesheet">
  <link href="css/style.css" rel="stylesheet">
  <link rel="stylesheet" href="css/owl.carousel.min.css">
  <link rel="stylesheet" href="css/owl.theme.default.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.2/css/all.min.css">
</head>

<body>
  <header>
    <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
      <div class="container">
        <a class="navbar-brand" href="#" title="Samurai Golf Tours">
          <img src="images/logo.svg" alt="Samurai Golf Tours" />
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse"
          aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
          <i class="fa-solid fa-bars"></i>
        </button>
        <div class="collapse navbar-collapse" id="navbarCollapse">
          <ul class="navbar-nav ms-auto mb-2 mb-md-0">
            <li class="nav-item">
              <a class="nav-link" href="#" title="Guest Register">Guest Register</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#" title="Host Register">Host Register</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#" title="Login" data-bs-toggle="modal" data-bs-target="#login">Login</a>
            </li>
            <li class="nav-item dropdown user">
              <a class="nav-link dropdown-toggle" href="#" title="Login" id="dropdownMenuButton1"
                data-bs-toggle="dropdown" aria-expanded="false">User</a>
              <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
                <li><a class="dropdown-item" href="#">Account Info</a></li>
                <li><a class="dropdown-item" href="#">Transaction History</a></li>
                <li><a class="dropdown-item" href="#">Change Password</a></li>
                <li><a class="dropdown-item" href="#">Logout</a></li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
  <section class="main-detailpg">
    <div class="container topspace">
      <div class="row">
        <div class="col-12 col-md-12 detail-txt">
          <div class="row">
            <div class="col-sm-12 col-md-8">
              <!-- Dynamic Update from DB -->
              <h2 class="mb-3">[[Prefecture Name]]</h2>
              <!-- Dynamic Update from DB -->
              <h1 class="mb-4">%s</h1>
            </div>
            <div class="col-12 col-sm-12 col-md-4">
            </div>
          </div>
          <ul class="list-unstyled mt-4 mt-sm-4 mt-md-0" style="margin-left: -16px;">
            <!-- Dynamic Update from DB -->
            <li class="ms-4"><i class="fa-solid fa-location-dot me-2"></i> %s
            </li>
          </ul>
        </div>
      </div>
      <div class="row gy-4">
        <div class="col-md-8 pe-1">
          <!-- Dynamic Update from DB -->
          <img src="images/bann3.jpg" alt="" class="img-fluid w-100">
        </div>
        <div class="col-md-4">
          <div class="detail-box position-relative">           
              <!-- Dynamic Update from DB -->
              <img src="images/bann3.jpg" alt="" class="img-fluid w-100">
          </div>
          <div class="detail-box position-relative mt-3">
            <a href="#" data-bs-toggle="modal" data-bs-target="#layoutgallery">
              <!-- Dynamic Update from DB -->
              <img src="images/bann3.jpg" alt="" class="img-fluid w-100">
              <h4 class="p-3">Photo Gallery</h4>
            </a>
          </div>
        </div>
      </div>
      <div class="row mt-4">
        <div class="col-md-12 tags">
          <!-- Dynamic Update from DB -->
          <button class="btn btn-secondary px-4 py-2">トーナメント開催</button>
          <button class="btn btn-secondary px-4 py-2">合宿・キャンプ</button>
          <button class="btn btn-secondary px-4 py-2">宿泊</button>
          <button class="btn btn-secondary px-4 py-2">多⾔語</button>
          <button class="btn btn-secondary px-4 py-2">送迎</button>
        </div>
      </div>
      <div class="row topspace2">
        <div class="col-md-7">
          <h3 class="headnew mb-4">Introduction</h3>
          <!-- Message when DB content is blank -->
          <p>This Hotel is situated in City Name of SOME Prefecture </p>
          <!-- Dynamic Update from DB Course Introducton HTML Format ( Scraping Data ) -->
        </div>
        <div class="col-md-5">
          <div class="detail-con p-3 p-sm-3 p-md-5">
            <h5 style="text-align: center;margin-top: 5px;"><i class="fa-solid fa-phone me-2"></i>TEL: 0000-00-0000 /
              FAX: 0000-00-0000</h5>
            <h5 style="text-align: center;padding-top: 10px;"><button class="btn btn-secondary mt-2"
                style="text-align: center;">Samurai Golf Tourism [8:00〜23:00]</button></h5>
            <h5 style="text-align: center;"><a href="[[url('/')]]/book-now" target="_blank" class="btn btn-primary mt-4"
                style="font-size: 4rem;">Book Now </a></h5>
          </div>
          <!-- Dynamic Update from DB -->
          <div class="detail-con cus-color p-3 p-sm-4 p-md-5 mt-4">
            <!-- Dynamic Update from DB HTML format -->
            <!-- Message when DB content is blank -->
          <p>No Special Price Information is available. </p>
          </div>
        </div>
      </div>
      <!-- Dynamic Update from DB Course Detail HTML Format ( Scraping Data ) -->
      <!-- <div class="row topspace2 gy-5">
        <div class="col-md-12">
          <h3 class="headnew mb-3">Basic Information</h3>
        </div>
        <div class="col-6 col-sm-4 col-md-2">
          <h3>ホール数</h3>
          <hr>
          <h5>27ホール</h5>
        </div>
        <div class="col-6 col-sm-4 col-md-2">
          <h3>距離</h3>
          <hr>
          <h5>10,619Y</h5>
        </div>
        <div class="col-6 col-sm-4 col-md-2">
          <h3>パー</h3>
          <hr>
          <h5>108</h5>
        </div>
        <div class="col-6 col-sm-4 col-md-2">
          <h3>種別</h3>
          <hr>
          <h5>林間</h5>
        </div>
        <div class="col-6 col-sm-4 col-md-2">
          <h3>グリーン数</h3>
          <hr>
          <h5>1グリーン</h5>
        </div>
        <div class="col-6 col-sm-4 col-md-2">
          <h3>グリーン</h3>
          <hr>
          <h5>ベント</h5>
        </div>
        <div class="col-6 col-sm-4 col-md-2">
          <h3>コース高低差</h3>
          <hr>
          <h5>適度なアップダウン</h5>
        </div>
        <div class="col-6 col-sm-4 col-md-2">
          <h3>面積</h3>
          <hr>
          <h5>170万m2</h5>
        </div>
        <div class="col-6 col-sm-4 col-md-2">
          <h3>コース</h3>
          <hr>
          <h5>まりもコース,<br>丹頂コース,<br>ピリカコース</h5>
        </div>
        <div class="col-6 col-sm-4 col-md-2">
          <h3>設計者</h3>
          <hr>
          <h5>富澤誠造, <br>土肥勇</h5>
        </div>
        <div class="col-6 col-sm-4 col-md-2">
          <h3>ドラコン推奨</h3>
          <hr>
          <h5>まりもコース: 9番<br>丹頂コース: 5番<br>ピリカコース: 3番</h5>
        </div>
        <div class="col-6 col-sm-4 col-md-2">
          <h3>ニアピン推奨</h3>
          <hr>
          <h5>まりもコース: 3番<br>丹頂コース: 4番<br>ピリカコース: 4番</h5>
        </div>
      </div> -->
      <!-- Dynamic Update from DB HTML format -->
      <div class="row">
        <div class="col-md-12 ">
          <div class="tour-news p-5 notice">
            <h3 class="mb-4">Cancel Policy</h3>
            <!-- Message when DB content is blank -->
            <p>No Cancel Policy information available.</p>
          </div>
        </div>
      </div>
      <div class="col-md-12">
        <div class="detail-con p-3 p-sm-3 p-md-5">
          <h5 style="text-align: center;margin-top: 5px;"><i class="fa-solid fa-phone me-2"></i>TEL: 0000-00-0000 / FAX:
            0000-00-0000</h5>
          <h5 style="text-align: center;padding-top: 10px;"><button class="btn btn-secondary mt-2"
              style="text-align: center;">Samurai Golf Tourism [8:00〜23:00]</button></h5>
          <h5 style="text-align: center;"><a href="[[url('/')]]/book-now" target="_blank" class="btn btn-primary mt-4"
              style="font-size: 4rem;">Book Now </a></h5>
        </div>
      </div>
      <div class="row my-5">
        <div class="tour-news p-5 notice">
          <h3>Hotel Special Annoucements / Notice</h3>
          <!-- Message when DB content is blank -->
          <p>No Annoucements / Notice Information is available.</p>
        </div>
      </div>

      <div class="col-md-12">
        <div class="detail-con p-3 p-sm-3 p-md-5">
          <h5 style="text-align: center;margin-top: 5px;"><i class="fa-solid fa-phone me-2"></i>TEL: 0000-00-0000 / FAX:
            0000-00-0000</h5>
          <h5 style="text-align: center;padding-top: 10px;"><button class="btn btn-secondary mt-2"
              style="text-align: center;">Samurai Golf Tourism [8:00〜23:00]</button></h5>
          <h5 style="text-align: center;"><a href="[[url('/')]]/book-now" target="_blank" class="btn btn-primary mt-4"
              style="font-size: 4rem;">Book Now </a></h5>
        </div>
      </div>
      
      <!-- Facility details, show only when DB data exists. -->
      <div class="row mt-4 gy-5">
        <div class="col-md-4">
          <h3>Competition Room</h3>
          <hr>
          <h5>Maximum capacity 90 people</h5>
        </div>
        <div class="col-md-4">
          <h3>Home Delivery</h3>
          <hr>
          <h5>Yamato</h5>
        </div>
        <div class="col-md-4">
          <h3>Competition Room</h3>
          <hr>
          <h5>Maximum capacity 90 people</h5>
        </div>
        <div class="col-md-4">
          <h3>Home Delivery</h3>
          <hr>
          <h5>Yamato</h5>
        </div>
        <div class="col-md-4">
          <h3>Competition Room</h3>
          <hr>
          <h5>Maximum capacity 90 people</h5>
        </div>
        <div class="col-md-4">
          <h3>Home Delivery</h3>
          <hr>
          <h5>Yamato</h5>
        </div>
      </div>
      <div class="row map3">
        <div class="col-md-12">
          <div class="mapboxgl-map" id="mapnew"></div>
        </div>
      </div>
      <!-- Facility details, show only when DB data exists. -->
      <!-- <div class="row topspace2">
        <div class="col-md-12 table2">
          <h3 class="headnew mb-4">Various Additional Information</h3>
          <table class="table  table-bordered mt-3 ">
            <tbody>
              <tr>
                <td class="w-25 color-td">Address</td>
                <td>14 Todishara, Akancho, Kushiro City, Hokkaido 085-0220</td>
              </tr>
              <tr>
                <td class="w-25 color-td">Car</td>
                <td>Doto Expressway [Akan] Within 5km Doto Expressway Akan IC opened (March 2016) 5km, about 8 minutes.
                  ; 31 km from Kushiro Station, about 45 minutes. ;About 20 minutes from Kushiro Airport. ;About 40
                  minutes from Akanko Onsen. ;Take Route 38 from Kushiro. At Tairakuge, take National Route 240, which
                  is known as the Marimo National Route, and pass Kushiro Airport, Tsuru Park, etc., and turn right
                  following the sign on the right after passing through Akan city.</td>
              </tr>
              <tr>
                <td class="w-25 color-td">Train</td>
                <td>31 km from Kushiro Station, about 45 minutes.</td>
              </tr>
              <tr>
                <td class="w-25 color-td">Club bus</td>
                <td>No club bus transfer</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div> -->
      <div class="row gy-5 basicinfo">''' % ( other_info['hotel_name'] , table_1['住所'])
        
        final_html_2 =     '''
    </div>

    </div>

    <div class="col-md-12">
      <div class="detail-con p-3 p-sm-3 p-md-5">
        <h5 style="text-align: center;margin-top: 5px;"><i class="fa-solid fa-phone me-2"></i>TEL: 0000-00-0000 / FAX:
          0000-00-0000</h5>
        <h5 style="text-align: center;padding-top: 10px;"><button class="btn btn-secondary mt-2"
            style="text-align: center;">Samurai Golf Tourism [8:00〜23:00]</button></h5>
        <h5 style="text-align: center;"><a href="[[url('/')]]/book-now" target="_blank" class="btn btn-primary mt-4"
            style="font-size: 4rem;">Book Now </a></h5>
      </div>
    </div>
  </section>
  <footer class="text-center mt-5">
    <div class="container">
      <div class="row">
        <div class="col-md-12">
          <a href="#" title="Samurai Golf Tourism">
            <img src="images/footer-logo.png" alt="Samurai Golf Tourism">
          </a>
          <ul class="list-unstyled mt-5">
            <li><a href="#" title="About Us">About Us</a></li>
            <li><a href="#" title="Host Registration Guide">Host Registration Guide</a></li>
            <li><a href="#" title="Terms and Conditions">Terms and Conditions</a></li>
            <li><a href="#" title="Privacy Policy">Privacy Policy</a></li>
            <li><a href="#" title="Travel Agent Guide">Travel Agent Guide</a></li>
            <li><a href="#" title="Contact Us">Contact Us</a></li>
            <li><a href="#" title="Company Information">Company Information</a></li>
            <li><a href="#" title="Cancel Policy">Cancel Policy</a></li>
          </ul>
          <p class="copyright mb-0">Copyright &copy; Samurai Golf Tourism. All rights reserved.</p>
        </div>
      </div>
    </div>
  </footer>
  <a href="#" title="Back To Top" class="back-to-top d-flex align-items-center justify-content-center">
    <i class="fa-solid fa-angle-up"></i></a>

  <!-- Layout Gallery Slider - Start -->
  <div class="modal fade" id="layoutgallery" tabindex="-1" aria-labelledby="layoutgallerylabel" aria-hidden="true">
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header"><!-- Write Golf Place Name here -->
          <h5 class="modal-title" id="layoutgallerylabel">[[Name of Golf Place]]</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body modal-slider mt-3">
          <!--  Main Tab Headers Start -->
          <ul class="nav nav-pills mb-3" id="pills-tabmainlay" role="tablist">
            <li class="nav-item" role="presentation">
              <button class="nav-link active" id="pills-layoutmain-tab" data-bs-toggle="pill"
                data-bs-target="#pills-layoutmain" type="button" role="tab" aria-controls="pills-layoutmain"
                aria-selected="true">Layout Gallery</button><!-- Fixed Name -->
            </li>
          </ul>
          <!-- Main Tab Headers End -->
          <!--  Main Tab Content Start-->
          <div class="tab-content" id="pills-tabmainlayContent">
            <div class="tab-pane fade show active" id="pills-layoutmain" role="tabpanel"
              aria-labelledby="pills-layoutmain-tab">
              <!--  Sub Tab Header Start--><!--  Remove respective TAB and Content if you do not want to show -->
              <nav class="mt-5">
                <div class="nav nav-tabs" id="nav-tabsub" role="tablist">
                  <!--  Course1 Header Start-->
                  <button class="nav-link active" id="nav-course1lay-tab" data-bs-toggle="tab"
                    data-bs-target="#nav-course1lay" type="button" role="tab" aria-controls="nav-course1lay"
                    aria-selected="false">[[Course1]]</button>
                  <!--  Course1 Header End-->
                </div>
              </nav>
              <!--  Sub Tab Header End-->
              <!--  Sub Tab Content Start-->
              <div class="tab-content numbertab" id="nav-tabsubContent">
                <!--  Course1 Content Start-->
                <div class="tab-pane fade show active" id="nav-course1lay" role="tabpanel"
                  aria-labelledby="nav-course1lay-tab">
                  <div class="mt-4">
                    <ul class="nav nav-pills mb-3" id="pills-tabc1" role="tablist">
                      <!--  course1lay Tab Header 1H Start-->
                      <li class="nav-item" role="presentation">
                        <button class="nav-link active" id="numberc11h-tab" data-bs-toggle="pill"
                          data-bs-target="#numberc11h" type="button" role="tab" aria-controls="numberc11h"
                          aria-selected="true">[[1H]]</button>
                      </li>
                      <!--  course1lay Tab Header 1H End-->
                    </ul>

                    <div class="tab-content" id="pills-tabc1Content">
                      <!--  course1lay Tab Content 1H Start-->
                      <div class="tab-pane fade show active" id="numberc11h" role="tabpanel"
                        aria-labelledby="numberc11h-tab">
                        <div class="owl-carousel">
                          <!-- Add additional images as required in given section -->
                          
                          ''' 

        final_html_3 = '''
        </div>
                      </div>
                      <!--  course1lay Tab Content 1H End-->
                    </div>
                  </div>
                </div>
                <!--  Course1 Content End-->

              </div>
              <!--  Sub Tab Content End-->
            </div>
          </div>
          <!--  Main Tab Content End-->
        </div>
      </div>
    </div>
  </div>
  <!-- Layout Gallery Slider - End -->


  <!-- Photo Gallery Slider - Start -->
  <div class="modal fade" id="photogallery" tabindex="-1" aria-labelledby="photogallerylabel" aria-hidden="true">
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header"><!-- Write Golf Place Name here -->
          <h5 class="modal-title" id="photogallerylabel">[[Name of Golf Place]]</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body modal-slider mt-3">
          <!--  Main Tab Headers Start -->
          <ul class="nav nav-pills mb-3" id="pills-tabmain" role="tablist">
            <li class="nav-item" role="presentation">
              <button class="nav-link active" id="pills-homemain-tab" data-bs-toggle="pill"
                data-bs-target="#pills-homemain" type="button" role="tab" aria-controls="pills-homemain"
                aria-selected="true">Photo Gallery</button><!-- Fixed Name -->
            </li>
          </ul>
          <!-- Main Tab Headers End -->
          <!--  Main Tab Content Start-->
          <div class="tab-content" id="pills-tabmainContent">
            <div class="tab-pane fade show active" id="pills-homemain" role="tabpanel"
              aria-labelledby="pills-homemain-tab">
              <!--  Sub Tab Header Start--><!--  Remove respective TAB and Content if you do not want to show -->
              <nav class="mt-5">
                <div class="nav nav-tabs" id="nav-tabsub" role="tablist">
                  <!--  CourseInfo Header Start-->
                  <button class="nav-link active" id="nav-courseinfo-tab" data-bs-toggle="tab"
                    data-bs-target="#nav-courseinfo" type="button" role="tab" aria-controls="nav-courseinfo"
                    aria-selected="true">CourseInfo</button>
                  <!--  CourseInfo Header End-->
                  <!--  Course1 Header Start-->
                  <button class="nav-link" id="nav-course1-tab" data-bs-toggle="tab" data-bs-target="#nav-course1"
                    type="button" role="tab" aria-controls="nav-course1" aria-selected="false">[[Course1]]</button>
                  <!--  Course1 Header End-->
                </div>
              </nav>
              <!--  Sub Tab Header End-->
              <!--  Sub Tab Content Start-->
              <div class="tab-content numbertab" id="nav-tabsubContent">
                <!--  CourseInfo Content Start-->
                <div class="tab-pane fade show active" id="nav-courseinfo" role="tabpanel"
                  aria-labelledby="nav-courseinfo-tab">
                  <div class="mt-4">
                    <ul class="nav nav-pills mb-3" id="pills-tabcinfo" role="tablist">
                      <!--  CourseInfo Tab Header 1H Start-->
                      <li class="nav-item" role="presentation">
                        <button class="nav-link active" id="numbercinfo1h-tab" data-bs-toggle="pill"
                          data-bs-target="#numbercinfo1h" type="button" role="tab" aria-controls="numbercinfo1h"
                          aria-selected="true"></button>
                      </li>
                      <!--  CourseInfo Tab Header 1H End-->
                    </ul>

                    <div class="tab-content" id="pills-tabcinfoContent">
                      <!--  CourseInfo Tab Content 1H Start-->
                      <div class="tab-pane fade show active" id="numbercinfo1h" role="tabpanel"
                        aria-labelledby="numbercinfo1h-tab">
                        <div class="owl-carousel">
                          <!-- Add images here as requried for that section -->
                          <div id="cinfo1h1"><img src="images/bann1.jpg" alt="Banner" class="img-fluid w-100">
                            <h4 class="banhead mb-0">[[1st Image in Slider]]</h4>
                          </div>
                          <div id="cinfo1h2"><img src="images/bann1.jpg" alt="Banner" class="img-fluid w-100">
                            <h4 class="banhead mb-0">[[2nd Image in Slider]]</h4>
                          </div>
                          <!-- Add images here as requried for that section -->
                        </div>
                      </div>
                      <!--  CourseInfo Tab Content 1H End-->
                    </div>
                  </div>
                </div>
                <!--  CourseInfo Content End-->
                <!--  Course1 Content Start-->
                <div class="tab-pane fade" id="nav-course1" role="tabpanel" aria-labelledby="nav-course1-tab">
                  <div class="mt-4">
                    <ul class="nav nav-pills mb-3" id="pills-tabc1" role="tablist">
                      <!--  course1 Tab Header 1H Start-->
                      <li class="nav-item" role="presentation">
                        <button class="nav-link active" id="numberc11h-tab" data-bs-toggle="pill"
                          data-bs-target="#numberc11h" type="button" role="tab" aria-controls="numberc11h"
                          aria-selected="true">[[1H]]</button>
                      </li>
                      <!--  course1 Tab Header 1H End-->
                    </ul>

                    <div class="tab-content" id="pills-tabc1Content">
                      <!--  course1 Tab Content 1H Start-->
                      <div class="tab-pane fade show active" id="numberc11h" role="tabpanel"
                        aria-labelledby="numberc11h-tab">
                        <div class="owl-carousel">
                          <!-- Add additional images as required in given section -->
                          <div id="c11h1"><img src="images/bann1.jpg" alt="Banner" class="img-fluid w-100">
                            <h4 class="banhead mb-0">[[1st Image in Slider]]</h4>
                          </div>
                          <!-- Add additional images as required in given section -->
                        </div>
                      </div>
                      <!--  course1 Tab Content 1H End-->
                    </div>
                  </div>
                </div>
                <!--  Course1 Content End-->

              </div>
              <!--  Sub Tab Content End-->
            </div>
          </div>
          <!--  Main Tab Content End-->
        </div>
      </div>
    </div>
  </div>
  <!-- Photo Gallery Slider - End -->

  <!-- javascript -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="js/bootstrap.bundle.min.js"></script>
  <script src="js/owl.carousel.js"></script>
  <script src="js/main.js"></script>
  <script src="js/smoothscroll.min.js"></script>
  <script src="https://api.tiles.mapbox.com/mapbox-gl-js/v1.6.0/mapbox-gl.js"></script>
  <script>
    mapboxgl.accessToken =
      'pk.eyJ1IjoibGxveWRsd2VlbmRvIiwiYSI6ImNrNzVjbGUzMjBlNDUzZXNicnhycnpraGwifQ.ZlURI2KWF1ihr57-LNmj8g';
    var map = new mapboxgl.Map({
      container: 'mapnew',
      style: 'mapbox://styles/mapbox/streets-v11',
      center: [-79.4512, 43.6568],
      zoom: 13
    });
    // document.getElementById('geocoder').appendChild(geocoder.onAdd(map));
  </script>
  <script>
    $(document).ready(function () {
      $('.owl-carousel').owlCarousel({
        loop: true,
        margin: 0,
        nav: true,
        dots: true,
        autoplay: false,
        autoplayHoverPause: true,
        autoplayTimeout: 4000,
        stopOnHover: false,
        touchDrag: true,
        mouseDrag: true,
        navText: ['<i class="fa-solid fa-angle-left"></i>', '<i class="fa-solid fa-angle-right"></i>'],
        smartSpeed: 1000,
        responsive: {
          0: {
            items: 1,
            touchDrag: false,
            mouseDrag: false,
          },
          600: {
            items: 1,
          },
          1000: {
            items: 1
          }
        }
      })
    })
  </script>
  <script>
    $("#table3").click(function () {
      $("#table3_show").show();
      $("#table1_show").hide();
      $("#table2_show").hide();
      $("#table4_show").hide();
      $("#table5_show").hide();
    });
    $("#male-tab").click(function () {
      $("#table1_show").show();
      $("#table3_show").hide();
      $("#table4_show").hide();
      $("#table5_show").hide();
    });
    $("#female-tab").click(function () {
      $("#table2_show").show();
      $("#table3_show").hide();
      $("#table4_show").hide();
      $("#table5_show").hide();
    });
    $("#table4").click(function () {
      $("#table4_show").show();
      $("#table3_show").hide();
      $("#table1_show").hide();
      $("#table2_show").hide();
      $("#table5_show").hide();
    });
    $("#table5").click(function () {
      $("#table5_show").show();
      $("#table1_show").hide();
      $("#table2_show").hide();
      $("#table3_show").hide();
      $("#table4_show").hide();
    });
  </script>
</body>

</html>'''
        
        
        final_html_4 = '''
        <!-- Photo Gallery Slider - Start -->
  <div class="modal fade" id="photogallery" tabindex="-1" aria-labelledby="photogallerylabel" aria-hidden="true">
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header"><!-- Write Golf Place Name here -->
          <h5 class="modal-title" id="photogallerylabel">[[Name of Golf Place]]</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body modal-slider mt-3">
          <!--  Main Tab Headers Start -->
          <ul class="nav nav-pills mb-3" id="pills-tabmain" role="tablist">
            <li class="nav-item" role="presentation">
              <button class="nav-link active" id="pills-homemain-tab" data-bs-toggle="pill"
                data-bs-target="#pills-homemain" type="button" role="tab" aria-controls="pills-homemain"
                aria-selected="true">Photo Gallery</button><!-- Fixed Name -->
            </li>
          </ul>
          <!-- Main Tab Headers End -->
          <!--  Main Tab Content Start-->
          <div class="tab-content" id="pills-tabmainContent">
            <div class="tab-pane fade show active" id="pills-homemain" role="tabpanel"
              aria-labelledby="pills-homemain-tab">
              <!--  Sub Tab Header Start--><!--  Remove respective TAB and Content if you do not want to show -->
              <nav class="mt-5">
                <div class="nav nav-tabs" id="nav-tabsub" role="tablist">
                  <!--  CourseInfo Header Start-->
                  <button class="nav-link active" id="nav-courseinfo-tab" data-bs-toggle="tab"
                    data-bs-target="#nav-courseinfo" type="button" role="tab" aria-controls="nav-courseinfo"
                    aria-selected="true">CourseInfo</button>
                  <!--  CourseInfo Header End-->
                  <!--  Course1 Header Start-->
                  <button class="nav-link" id="nav-course1-tab" data-bs-toggle="tab" data-bs-target="#nav-course1"
                    type="button" role="tab" aria-controls="nav-course1" aria-selected="false">[[Course1]]</button>
                  <!--  Course1 Header End-->
                </div>
              </nav>
              <!--  Sub Tab Header End-->
              <!--  Sub Tab Content Start-->
              <div class="tab-content numbertab" id="nav-tabsubContent">
                <!--  CourseInfo Content Start-->
                <div class="tab-pane fade show active" id="nav-courseinfo" role="tabpanel"
                  aria-labelledby="nav-courseinfo-tab">
                  <div class="mt-4">
                    <ul class="nav nav-pills mb-3" id="pills-tabcinfo" role="tablist">
                      <!--  CourseInfo Tab Header 1H Start-->
                      <li class="nav-item" role="presentation">
                        <button class="nav-link active" id="numbercinfo1h-tab" data-bs-toggle="pill"
                          data-bs-target="#numbercinfo1h" type="button" role="tab" aria-controls="numbercinfo1h"
                          aria-selected="true"></button>
                      </li>
                      <!--  CourseInfo Tab Header 1H End-->
                    </ul>

                    <div class="tab-content" id="pills-tabcinfoContent">
                      <!--  CourseInfo Tab Content 1H Start-->
                      <div class="tab-pane fade show active" id="numbercinfo1h" role="tabpanel"
                        aria-labelledby="numbercinfo1h-tab">
                        <div class="owl-carousel">
                          <!-- Add images here as requried for that section -->
                          <div id="cinfo1h1"><img src="images/bann1.jpg" alt="Banner" class="img-fluid w-100">
                            <h4 class="banhead mb-0">[[1st Image in Slider]]</h4>
                          </div>
                          <div id="cinfo1h2"><img src="images/bann1.jpg" alt="Banner" class="img-fluid w-100">
                            <h4 class="banhead mb-0">[[2nd Image in Slider]]</h4>
                          </div>
                          <!-- Add images here as requried for that section -->
                        </div>
                      </div>
                      <!--  CourseInfo Tab Content 1H End-->
                    </div>
                  </div>
                </div>
                <!--  CourseInfo Content End-->
                <!--  Course1 Content Start-->
                <div class="tab-pane fade" id="nav-course1" role="tabpanel" aria-labelledby="nav-course1-tab">
                  <div class="mt-4">
                    <ul class="nav nav-pills mb-3" id="pills-tabc1" role="tablist">
                      <!--  course1 Tab Header 1H Start-->
                      <li class="nav-item" role="presentation">
                        <button class="nav-link active" id="numberc11h-tab" data-bs-toggle="pill"
                          data-bs-target="#numberc11h" type="button" role="tab" aria-controls="numberc11h"
                          aria-selected="true">[[1H]]</button>
                      </li>
                      <!--  course1 Tab Header 1H End-->
                    </ul>

                    <div class="tab-content" id="pills-tabc1Content">
                      <!--  course1 Tab Content 1H Start-->
                      <div class="tab-pane fade show active" id="numberc11h" role="tabpanel"
                        aria-labelledby="numberc11h-tab">
                        <div class="owl-carousel">
                          <!-- Add additional images as required in given section -->
                          <div id="c11h1"><img src="images/bann1.jpg" alt="Banner" class="img-fluid w-100">
                            <h4 class="banhead mb-0">[[1st Image in Slider]]</h4>
                          </div>
                          <!-- Add additional images as required in given section -->
                        </div>
                      </div>
                      <!--  course1 Tab Content 1H End-->
                    </div>
                  </div>
                </div>
                <!--  Course1 Content End-->

              </div>
              <!--  Sub Tab Content End-->
            </div>
          </div>
          <!--  Main Tab Content End-->
        </div>
      </div>
    </div>
  </div>
  <!-- Photo Gallery Slider - End -->

  <!-- javascript -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="js/bootstrap.bundle.min.js"></script>
  <script src="js/owl.carousel.js"></script>
  <script src="js/main.js"></script>
  <script src="js/smoothscroll.min.js"></script>
  <script src="https://api.tiles.mapbox.com/mapbox-gl-js/v1.6.0/mapbox-gl.js"></script>
  <script>
    mapboxgl.accessToken =
      'pk.eyJ1IjoibGxveWRsd2VlbmRvIiwiYSI6ImNrNzVjbGUzMjBlNDUzZXNicnhycnpraGwifQ.ZlURI2KWF1ihr57-LNmj8g';
    var map = new mapboxgl.Map({
      container: 'mapnew',
      style: 'mapbox://styles/mapbox/streets-v11',
      center: [-79.4512, 43.6568],
      zoom: 13
    });
    // document.getElementById('geocoder').appendChild(geocoder.onAdd(map));
  </script>
  <script>
    $(document).ready(function () {
      $('.owl-carousel').owlCarousel({
        loop: true,
        margin: 0,
        nav: true,
        dots: true,
        autoplay: false,
        autoplayHoverPause: true,
        autoplayTimeout: 4000,
        stopOnHover: false,
        touchDrag: true,
        mouseDrag: true,
        navText: ['<i class="fa-solid fa-angle-left"></i>', '<i class="fa-solid fa-angle-right"></i>'],
        smartSpeed: 1000,
        responsive: {
          0: {
            items: 1,
            touchDrag: false,
            mouseDrag: false,
          },
          600: {
            items: 1,
          },
          1000: {
            items: 1
          }
        }
      })
    })
  </script>
  <script>
    $("#table3").click(function () {
      $("#table3_show").show();
      $("#table1_show").hide();
      $("#table2_show").hide();
      $("#table4_show").hide();
      $("#table5_show").hide();
    });
    $("#male-tab").click(function () {
      $("#table1_show").show();
      $("#table3_show").hide();
      $("#table4_show").hide();
      $("#table5_show").hide();
    });
    $("#female-tab").click(function () {
      $("#table2_show").show();
      $("#table3_show").hide();
      $("#table4_show").hide();
      $("#table5_show").hide();
    });
    $("#table4").click(function () {
      $("#table4_show").show();
      $("#table3_show").hide();
      $("#table1_show").hide();
      $("#table2_show").hide();
      $("#table5_show").hide();
    });
    $("#table5").click(function () {
      $("#table5_show").show();
      $("#table1_show").hide();
      $("#table2_show").hide();
      $("#table3_show").hide();
      $("#table4_show").hide();
    });
  </script>
</body>

</html>'''


        img_chunk = '''<!-- Photo Gallery Slider - Start -->
<div class="modal fade" id="photogallery" tabindex="-1" aria-labelledby="photogallerylabel" aria-hidden="true">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <div class="modal-header"><!-- Write Golf Place Name here -->
        <h5 class="modal-title" id="photogallerylabel">%s</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body modal-slider mt-3">
        <!--  Main Tab Headers Start -->
        <ul class="nav nav-pills mb-3" id="pills-tabmain" role="tablist">
          <li class="nav-item" role="presentation">
            <button class="nav-link active" id="pills-homemain-tab" data-bs-toggle="pill"
              data-bs-target="#pills-homemain" type="button" role="tab" aria-controls="pills-homemain"
              aria-selected="true">Photo Gallery</button><!-- Fixed Name -->
          </li>
        </ul>
        <!-- Main Tab Headers End -->
        <!--  Main Tab Content Start-->
        <div class="tab-content" id="pills-tabmainContent">
          <div class="tab-pane fade show active" id="pills-homemain" role="tabpanel"
            aria-labelledby="pills-homemain-tab">
            <!--  Sub Tab Header Start--><!--  Remove respective TAB and Content if you do not want to show -->
            <nav class="mt-5">
              <div class="nav nav-tabs" id="nav-tabsub" role="tablist">
                <!--  CourseInfo Header Start-->
                <button class="nav-link active" id="nav-courseinfo-tab" data-bs-toggle="tab"
                  data-bs-target="#nav-courseinfo" type="button" role="tab" aria-controls="nav-courseinfo"
                  aria-selected="true">Introduction</button>
                <!--  CourseInfo Header End-->
              </div>
            </nav>
            <!--  Sub Tab Header End-->
            <!--  Sub Tab Content Start-->
            <div class="tab-content numbertab" id="nav-tabsubContent">
              <!--  CourseInfo Content Start-->
              <div class="tab-pane fade show active" id="nav-courseinfo" role="tabpanel"
                aria-labelledby="nav-courseinfo-tab">
                <div class="mt-4">
                  <ul class="nav nav-pills mb-3" id="pills-tabcinfo" role="tablist">
                    <!--  CourseInfo Tab Header 1H Start-->
                    <li class="nav-item" role="presentation">
                      <button class="nav-link active" id="numbercinfo1h-tab" data-bs-toggle="pill"
                        data-bs-target="#numbercinfo1h" type="button" role="tab" aria-controls="numbercinfo1h"
                        aria-selected="true"></button>
                    </li>
                    <!--  CourseInfo Tab Header 1H End-->
                  </ul>

                  <div class="tab-content" id="pills-tabcinfoContent">
                    <!--  CourseInfo Tab Content 1H Start-->
                    <div class="tab-pane fade show active" id="numbercinfo1h" role="tabpanel"
                      aria-labelledby="numbercinfo1h-tab">
                      <div class="owl-carousel">
                        <!-- Add images here as requried for that section -->
                          
                          %s


        </div>
                      </div>
                      <!--  course1lay Tab Content 1H End-->
                    </div>
                  </div>
                </div>
                <!--  Course1 Content End-->

              </div>
              <!--  Sub Tab Content End-->
            </div>
          </div>
          <!--  Main Tab Content End-->
        </div>
      </div>
    </div>
  </div>
  <!-- Photo Gallery Slider - End -->'''%(other_info['hotel_name'] , img_div)
        


        with open(os.path.join(path, hotel_id+'img_chunk.txt'), 'wb') as fp:
            fp.write(img_chunk.encode('utf8'))
        
        final_html = ''

        final_html +=final_html_1+'\n'
        
        if tt_flag == True:
            final_html +=main +'\n'
        
        if c_text_1 != '':
            final_html+= c_text_1 +'\n'
        if c_text_2 != '':
            final_html += c_text_2 +'\n'
        
        final_html += final_html_2
        final_html += img_div + '\n'
        final_html+=final_html_3
        
        final_html += final_html_4

        # print(final_html_1 )
        # print(main)
        # print(c_text_1)
        # print(c_text_2)
        # print(final_html_2)
        # print(final_html)





        with open(hotel_id+'_final_html.html','wb') as of:
            of.write(final_html.encode('utf8'))
        with open(os.path.join(path, hotel_id+'_final_html.html'), 'wb') as fp:
            fp.write(final_html.encode('utf8'))
        with open('html_update log.txt' , 'a') as of:
                of.write('Final html page generated..\n\n')
        print('Final html page generated..')
    except Exception as ex:
        with open('html_update log.txt' , 'a') as of:
            of.write(str(ex) +'\n\n')
            of.write('Final html page not generated.')

    
print('Program execution time :' ,end = ' ')
print("--- %s seconds ---" % (time.time() - start_time))