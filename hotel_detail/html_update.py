import json
import time
import os
import pandas as pd
start_time = time.time()


df = pd.read_excel('hotel_ids.xlsx')

for i in df['id']:
    hotel_id = str(i)
    directory = hotel_id  
    parent_dir = "C:/Users/HP/Desktop/Image scrapper/hotel_detail/All data"
    
    path = os.path.join(parent_dir, directory) 
    with open('html_update log.txt' , 'a') as of:
        of.write(hotel_id+'\n')
        of.write(start_time)
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

            # with open(hotel_id+'_top_table.txt','wb') as of:
            #     of.write(main.encode('utf8'))
        except Exception as ex:
            print(ex)
            with open('html_update log.txt' , 'a') as of:
                of.write('Top page table not present.\n')

        print('Program execution time :' ,end = ' ')
        print("--- %s seconds ---" % (time.time() - start_time))





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
                    <h2 class="mb-3">Hokkaido</h2>
                    <h1 class="mb-4">Akan Country Club</h1>
                    </div>
                    <div class="col-12 col-sm-12 col-md-4">
                    <!-- <div class="wishlist2 float-md-end">
                        <a href="#">
                        <svg viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="presentation"
                            focusable="false">
                            <path
                            d="m16 28c7-4.733 14-10 14-17 0-1.792-.683-3.583-2.05-4.95-1.367-1.366-3.158-2.05-4.95-2.05-1.791 0-3.583.684-4.949 2.05l-2.051 2.051-2.05-2.051c-1.367-1.366-3.158-2.05-4.95-2.05-1.791 0-3.583.684-4.949 2.05-1.367 1.367-2.051 3.158-2.051 4.95 0 7 7 12.267 14 17z">
                            </path>
                        </svg> お気に入り</a>
                    </div> -->
                    </div>
                </div>
                <ul class="list-unstyled mt-4 mt-sm-4 mt-md-0" style="margin-left: -16px;">
                    <!-- <li>
                    <div class="rating2">
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <span>3/5</span>
                    </div>
                    </li> -->
                    <li class="ms-4"><i class="fa-solid fa-location-dot me-2"></i> 14 Tongue, Akan-cho, Kushiro-shi, Hokkaido
                    </li>
                </ul>
                </div>
            </div>
            <div class="row gy-4">
                <div class="col-md-8 detail-box position-relative">
                <a href="#" data-bs-toggle="modal" data-bs-target="#layoutgallery">
                    <img src="images/bann3.jpg" alt="" class="img-fluid w-100">
                    <h4 class="p-3">Layout Gallery</h4>
                </a>
                </div>
                <div class="col-md-4">
                <div class="detail-box position-relative">
                    <a href="#" data-bs-toggle="modal" data-bs-target="#photogallery">
                    <img src="images/bann3.jpg" alt="" class="img-fluid w-100">
                    <h4 class="p-3">Photo Gallery</h4>
                    </a>
                </div>
                <div class="detail-box position-relative mt-3">
                    <a href="#" data-bs-toggle="modal" data-bs-target="#dronegallery">
                    <img src="images/bann3.jpg" alt="" class="img-fluid w-100">
                    <h4 class="p-3">Drone Gallery</h4>
                    </a>
                </div>
                </div>
            </div>
            <div class="row mt-4">
                <div class="col-md-12 tags">
                <button class="btn btn-secondary px-4 py-2">トーナメント開催</button>
                <button class="btn btn-secondary px-4 py-2">合宿・キャンプ</button>
                <button class="btn btn-secondary px-4 py-2">宿泊</button>
                <button class="btn btn-secondary px-4 py-2">多⾔語</button>
                <button class="btn btn-secondary px-4 py-2">送迎</button>
                <!-- <button class="btn btn-secondary px-4 py-2">コース紹介</button>
                <button class="btn btn-secondary px-4 py-2">コース紹介</button>
                <button class="btn btn-secondary px-4 py-2">コース紹介</button>
                <button class="btn btn-secondary px-4 py-2">コース紹介</button> -->
                </div>
            </div>
            <div class="row topspace2">
                <div class="col-md-7">
                <h3 class="headnew mb-4">コース紹介</h3>
                <p>
                    20 minutes by car from Kushiro Airport, the gateway to eastern Hokkaido. There is a red-crowned crane nature
                    park on the way, and you can also see the red-crowned crane, which is a special natural monument.
                    Said to be the masterpiece of the master craftsman Seizo Tomizawa, the strategic design that makes use of
                    the natural forest is a layout that makes you want to try again and again.
                    It is a forest course where you can see Mt.</p>
                <p></p>
                ≪Access≫<br>
                ◆ Doto Expressway Akan IC opened (March 2016): about 8 minutes<br>
                ◆ Kushiro Station: about 45 minutes<br>
                ◆ Kushiro Airport: about 20 minutes<br>
                ◆ Lake Akan Onsen: about 40 minutes<br>
                </p>
                </div>
                <div class="col-md-5">
                <div class="detail-con p-3 p-sm-3 p-md-5">
                    <h5><i class="fa-solid fa-phone me-2"></i>TEL: 0297-72-0727 / FAX: 0297-72-0795</h5>
                    <button class="btn btn-secondary mt-2">楽天GORA電話予約センター[8:00〜23:00]</button>
                    <h5 class="mt-4"><i class="fa-solid fa-car me-2"></i>常磐自動車道・谷和原 10km以内</h5>
                </div>
                <div class="detail-con cus-color p-3 p-sm-4 p-md-5 mt-4">
                    <h5>Total Cost</h5>
                    <p>谷和原 10km以内</p>
                    <h5 class="mt-4">Stay Cost</h5>
                    <p>谷和原 10km以内</p>
                </div>
                </div>
            </div>
            <div class="row topspace2 gy-5">
                <div class="col-md-12">
                <h3 class="headnew mb-3">コース紹介</h3>
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
            </div>
            <div class="row">
                <div class="col-md-12 ">
                <div class="tour-news p-5">
                    <h3 class="mb-4">Tournament News</h3>
                    <p>We are holding Golf Tournament in the Year 2023. Players from all over the world will come to participate
                    in this event. You are requested to come and enjoy Golf Playing with watching Tournament. Date will be
                    annoused later. Kindly Get in touch before you come or book in advance to secure your seat for the event.
                    We are looking forward to welcome you.
                    Thank You.
                    </p>
                    <p>We are holding Golf Tournament in the Year 2023. Players from all over the world will come to participate
                    in this event. You are requested to come and enjoy Golf Playing with watching Tournament. Date will be
                    annoused later. Kindly Get in touch before you come or book in advance to secure your seat for the event.
                    We are looking forward to welcome you.
                    Thank You.
                    </p>
                    <p>We are holding Golf Tournament in the Year 2023. Players from all over the world will come to participate
                    in this event. You are requested to come and enjoy Golf Playing with watching Tournament. Date will be
                    annoused later. Kindly Get in touch before you come or book in advance to secure your seat for the event.
                    We are looking forward to welcome you.
                    Thank You.
                    </p>
                    <p>We are holding Golf Tournament in the Year 2023. Players from all over the world will come to participate
                    in this event. You are requested to come and enjoy Golf Playing with watching Tournament. Date will be
                    annoused later. Kindly Get in touch before you come or book in advance to secure your seat for the event.
                    We are looking forward to welcome you.
                    Thank You.
                    </p>
                    <p>We are holding Golf Tournament in the Year 2023. Players from all over the world will come to participate
                    in this event. You are requested to come and enjoy Golf Playing with watching Tournament. Date will be
                    annoused later. Kindly Get in touch before you come or book in advance to secure your seat for the event.
                    We are looking forward to welcome you.
                    Thank You.
                    </p>
                </div>
                </div>
            </div>
            <!-- Yardage Table Start -->
            <div class="row topspace2">
                <div class="col-md-12">
                <h2 class="headnew mb-4">Yardage</h2>
                <h4 class="headnew1 mb-4">Marimo Course</h4>
                <button class="btn btn-danger px-5">Bent</button>
                <table class="table  table-bordered mt-3 text-center">
                    <thead>
                    <th>HOLE</th>
                    <th>1</th>
                    <th>2</th>
                    <th>3</th>
                    <th>4</th>
                    <th>5</th>
                    <th>6</th>
                    <th>7</th>
                    <th>8</th>
                    <th>9</th>
                    <th>計</th>
                    </thead>
                    <!-- <button type="button" class="btn btn-secondary ms-1" data-bs-toggle="tooltip"
                            data-bs-placement="bottom" title="Tooltip on bottom">
                            D
                        </button> -->
                    <tbody>
                    <tr class="bg-grey">
                        <td>PAR</td>
                        <td>4 </td>
                        <td>3</td>
                        <td>5</td>
                        <td>4</td>
                        <td>3</td>
                        <td>4</td>
                        <td>5</td>
                        <td>4</td>
                        <td>4</td>
                        <td>36</td>
                    </tr>
                    <tr>
                        <td>Back</td>
                        <td>4</td>
                        <td>3</td>
                        <td>5</td>
                        <td>4</td>
                        <td>3</td>
                        <td>4</td>
                        <td>5</td>
                        <td>4</td>
                        <td>4</td>
                        <td>36</td>
                    </tr>
                    <tr>
                        <td>Regular</td>
                        <td>4</td>
                        <td>3</td>
                        <td>5</td>
                        <td>4</td>
                        <td>3</td>
                        <td>4</td>
                        <td>5</td>
                        <td>4</td>
                        <td>4</td>
                        <td>36</td>
                    </tr>
                    <tr>
                        <td>Front</td>
                        <td>4</td>
                        <td>3</td>
                        <td>5</td>
                        <td>4</td>
                        <td>3</td>
                        <td>4</td>
                        <td>5</td>
                        <td>4</td>
                        <td>4</td>
                        <td>36</td>
                    </tr>
                    <tr class="bg-grey">
                        <td>HDCP</td>
                        <td>4</td>
                        <td>3</td>
                        <td>5</td>
                        <td>4</td>
                        <td>3</td>
                        <td>4</td>
                        <td>5</td>
                        <td>4</td>
                        <td>4</td>
                        <td>36</td>
                    </tr>
                    </tbody>
                </table>
                <h4>単位：Y</h4>
                </div>
            </div>
            <!-- Yardage Table End -->
            <!-- Yardage Table Start -->
            <div class="row topspace2">
                <div class="col-md-12">
                <h4 class="headnew1 mb-4">Tancho Course</h4>
                <button class="btn btn-danger px-5">Bent</button>
                <table class="table  table-bordered mt-3 text-center">
                    <thead>
                    <th>HOLE</th>
                    <th>1</th>
                    <th>2</th>
                    <th>3</th>
                    <th>4</th>
                    <th>5</th>
                    <th>6</th>
                    <th>7</th>
                    <th>8</th>
                    <th>9</th>
                    <th>計</th>
                    </thead>
                    <!-- <button type="button" class="btn btn-secondary ms-1" data-bs-toggle="tooltip"
                            data-bs-placement="bottom" title="Tooltip on bottom">
                            D
                        </button> -->
                    <tbody>
                    <tr class="bg-grey">
                        <td>PAR</td>
                        <td>4 </td>
                        <td>3</td>
                        <td>5</td>
                        <td>4</td>
                        <td>3</td>
                        <td>4</td>
                        <td>5</td>
                        <td>4</td>
                        <td>4</td>
                        <td>36</td>
                    </tr>
                    <tr>
                        <td>Back</td>
                        <td>4</td>
                        <td>3</td>
                        <td>5</td>
                        <td>4</td>
                        <td>3</td>
                        <td>4</td>
                        <td>5</td>
                        <td>4</td>
                        <td>4</td>
                        <td>36</td>
                    </tr>
                    <tr>
                        <td>Regular</td>
                        <td>4</td>
                        <td>3</td>
                        <td>5</td>
                        <td>4</td>
                        <td>3</td>
                        <td>4</td>
                        <td>5</td>
                        <td>4</td>
                        <td>4</td>
                        <td>36</td>
                    </tr>
                    <tr>
                        <td>Front</td>
                        <td>4</td>
                        <td>3</td>
                        <td>5</td>
                        <td>4</td>
                        <td>3</td>
                        <td>4</td>
                        <td>5</td>
                        <td>4</td>
                        <td>4</td>
                        <td>36</td>
                    </tr>
                    <tr class="bg-grey">
                        <td>HDCP</td>
                        <td>4</td>
                        <td>3</td>
                        <td>5</td>
                        <td>4</td>
                        <td>3</td>
                        <td>4</td>
                        <td>5</td>
                        <td>4</td>
                        <td>4</td>
                        <td>36</td>
                    </tr>
                    </tbody>
                </table>
                <h4>単位：Y</h4>
                </div>
            </div>
            <!-- Yardage Table End -->
            <!-- Yardage Table Start -->
            <div class="row topspace2">
                <div class="col-md-12">
                <h4 class="headnew1 mb-4">Pirika Course</h4>
                <button class="btn btn-danger px-5">Bent</button>
                <table class="table  table-bordered mt-3 text-center">
                    <thead>
                    <th>HOLE</th>
                    <th>1</th>
                    <th>2</th>
                    <th>3</th>
                    <th>4</th>
                    <th>5</th>
                    <th>6</th>
                    <th>7</th>
                    <th>8</th>
                    <th>9</th>
                    <th>計</th>
                    </thead>
                    <!-- <button type="button" class="btn btn-secondary ms-1" data-bs-toggle="tooltip"
                            data-bs-placement="bottom" title="Tooltip on bottom">
                            D
                        </button> -->
                    <tbody>
                    <tr class="bg-grey">
                        <td>PAR</td>
                        <td>4 </td>
                        <td>3</td>
                        <td>5</td>
                        <td>4</td>
                        <td>3</td>
                        <td>4</td>
                        <td>5</td>
                        <td>4</td>
                        <td>4</td>
                        <td>36</td>
                    </tr>
                    <tr>
                        <td>Back</td>
                        <td>4</td>
                        <td>3</td>
                        <td>5</td>
                        <td>4</td>
                        <td>3</td>
                        <td>4</td>
                        <td>5</td>
                        <td>4</td>
                        <td>4</td>
                        <td>36</td>
                    </tr>
                    <tr>
                        <td>Regular</td>
                        <td>4</td>
                        <td>3</td>
                        <td>5</td>
                        <td>4</td>
                        <td>3</td>
                        <td>4</td>
                        <td>5</td>
                        <td>4</td>
                        <td>4</td>
                        <td>36</td>
                    </tr>
                    <tr>
                        <td>Front</td>
                        <td>4</td>
                        <td>3</td>
                        <td>5</td>
                        <td>4</td>
                        <td>3</td>
                        <td>4</td>
                        <td>5</td>
                        <td>4</td>
                        <td>4</td>
                        <td>36</td>
                    </tr>
                    <tr class="bg-grey">
                        <td>HDCP</td>
                        <td>4</td>
                        <td>3</td>
                        <td>5</td>
                        <td>4</td>
                        <td>3</td>
                        <td>4</td>
                        <td>5</td>
                        <td>4</td>
                        <td>4</td>
                        <td>36</td>
                    </tr>
                    </tbody>
                </table>
                <h4>単位：Y</h4>
                </div>
            </div>
            <!-- Yardage Table End -->
            <!-- Course Rate Table1 Start -->
            <div class="row topspace2 male-female">
                <div class="col-md-12 col-lg-6">
                <h3 class="headnew mb-4">Course Rate</h3>
                <ul class="nav nav-pills mb-3" id="pills-tab" role="tablist">
                    <li class="nav-item" role="presentation">
                    <button class="nav-link active  btn-danger px-5" id="male-tab1" data-bs-toggle="pill"
                        data-bs-target="#male1" type="button" role="tab" aria-controls="male1"
                        aria-selected="true">Male</button>
                    </li>
                    <li class="nav-item ms-3" role="presentation">
                    <button class="nav-link px-5" id="female-tab1" data-bs-toggle="pill" data-bs-target="#female1"
                        type="button" role="tab" aria-controls="female1" aria-selected="false">Female</button>
                    </li>
                </ul>
                <h3 class="headnew mb-4">Combination : Marimo x Tancho</h3>

                <div class="tab-content" id="pills-tabContent">
                    <div class="tab-pane fade show active" id="male1" role="tabpanel" aria-labelledby="male-tab1">
                    <table class="table  table-bordered mt-3 text-center" id="table1_show">
                        <thead>
                        <th>Green</th>
                        <th>Tee</th>
                        <th>Course Rating</th>
                        <th>Yards</th>
                        </thead>
                        <tbody>
                        <tr>
                            <td rowspan="4">Bent</td>
                            <td>Back</td>
                            <td>3</td>
                            <td>5</td>
                        </tr>
                        <tr>
                            <td>Regular</td>
                            <td>3</td>
                            <td>5</td>
                        </tr>
                        <tr>
                            <td>Front</td>
                            <td>3</td>
                            <td>5</td>
                        </tr>
                        <tr>
                            <td>Gold Ladies</td>
                            <td>3</td>
                            <td>5</td>
                        </tr>
                        </tbody>
                    </table>
                    </div>
                    <div class="tab-pane fade" id="female1" role="tabpanel" aria-labelledby="female-tab1">
                    <table class="table  table-bordered mt-3 text-center" id="table2_show">
                        <thead>
                        <th>Green</th>
                        <th>Tee</th>
                        <th>Course Rating</th>
                        <th>Yards</th>
                        </thead>
                        <tbody>
                        <tr>
                            <td rowspan="4">Bent</td>
                            <td>Back</td>
                            <td>4</td>
                            <td>7</td>
                        </tr>
                        <tr>
                            <td>Regular</td>
                            <td>5</td>
                            <td>2</td>
                        </tr>
                        <tr>
                            <td>Front</td>
                            <td>3</td>
                            <td>5</td>
                        </tr>
                        <tr>
                            <td>Gold Ladies</td>
                            <td>7</td>
                            <td>9</td>
                        </tr>
                        </tbody>
                    </table>
                    </div>
                </div>
                </div>
            </div>
            <!-- Course Rate Table1 End -->
            <!-- Course Rate Table2 Start -->
            <div class="row topspace2 male-female">
                <div class="col-md-12 col-lg-6">
                <h3 class="headnew mb-4">Course Rate</h3>
                <ul class="nav nav-pills mb-3" id="pills-tab" role="tablist">
                    <li class="nav-item" role="presentation">
                    <button class="nav-link active  btn-danger px-5" id="male-tab2" data-bs-toggle="pill"
                        data-bs-target="#male2" type="button" role="tab" aria-controls="male2"
                        aria-selected="true">Male</button>
                    </li>
                    <li class="nav-item ms-3" role="presentation">
                    <button class="nav-link px-5" id="female-tab2" data-bs-toggle="pill" data-bs-target="#female2"
                        type="button" role="tab" aria-controls="female2" aria-selected="false">Female</button>
                    </li>
                </ul>
                <h3 class="headnew mb-4">Combination : Tancho x Pirika</h3>

                <div class="tab-content" id="pills-tabContent">
                    <div class="tab-pane fade show active" id="male2" role="tabpanel" aria-labelledby="male-tab2">
                    <table class="table  table-bordered mt-3 text-center" id="table1_show">
                        <thead>
                        <th>Green</th>
                        <th>Tee</th>
                        <th>Course Rating</th>
                        <th>Yards</th>
                        </thead>
                        <tbody>
                        <tr>
                            <td rowspan="4">Bent</td>
                            <td>Back</td>
                            <td>3</td>
                            <td>5</td>
                        </tr>
                        <tr>
                            <td>Regular</td>
                            <td>3</td>
                            <td>5</td>
                        </tr>
                        <tr>
                            <td>Front</td>
                            <td>3</td>
                            <td>5</td>
                        </tr>
                        <tr>
                            <td>Gold Ladies</td>
                            <td>3</td>
                            <td>5</td>
                        </tr>
                        </tbody>
                    </table>
                    </div>
                    <div class="tab-pane fade" id="female2" role="tabpanel" aria-labelledby="female-tab2">
                    <table class="table  table-bordered mt-3 text-center" id="table2_show">
                        <thead>
                        <th>Green</th>
                        <th>Tee</th>
                        <th>Course Rating</th>
                        <th>Yards</th>
                        </thead>
                        <tbody>
                        <tr>
                            <td rowspan="4">Bent</td>
                            <td>Back</td>
                            <td>4</td>
                            <td>7</td>
                        </tr>
                        <tr>
                            <td>Regular</td>
                            <td>5</td>
                            <td>2</td>
                        </tr>
                        <tr>
                            <td>Front</td>
                            <td>3</td>
                            <td>5</td>
                        </tr>
                        <tr>
                            <td>Gold Ladies</td>
                            <td>7</td>
                            <td>9</td>
                        </tr>
                        </tbody>
                    </table>
                    </div>
                </div>
                </div>
            </div>
            <!-- Course Rate Table2 End -->
            <!-- Course Rate Table2 Start -->
            <div class="row topspace2 male-female">
                <div class="col-md-12 col-lg-6">
                <h3 class="headnew mb-4">Course Rate</h3>
                <ul class="nav nav-pills mb-3" id="pills-tab" role="tablist">
                    <li class="nav-item" role="presentation">
                    <button class="nav-link active  btn-danger px-5" id="male-tab3" data-bs-toggle="pill"
                        data-bs-target="#male3" type="button" role="tab" aria-controls="male3"
                        aria-selected="true">Male</button>
                    </li>
                    <li class="nav-item ms-3" role="presentation">
                    <button class="nav-link px-5" id="female-tab3" data-bs-toggle="pill" data-bs-target="#female3"
                        type="button" role="tab" aria-controls="female3" aria-selected="false">Female</button>
                    </li>
                </ul>
                <h3 class="headnew mb-4">Combination : Marimo x Pirika</h3>

                <div class="tab-content" id="pills-tabContent">
                    <div class="tab-pane fade show active" id="male3" role="tabpanel" aria-labelledby="male-tab3">
                    <table class="table  table-bordered mt-3 text-center" id="table1_show">
                        <thead>
                        <th>Green</th>
                        <th>Tee</th>
                        <th>Course Rating</th>
                        <th>Yards</th>
                        </thead>
                        <tbody>
                        <tr>
                            <td rowspan="4">Bent</td>
                            <td>Back</td>
                            <td>3</td>
                            <td>5</td>
                        </tr>
                        <tr>
                            <td>Regular</td>
                            <td>3</td>
                            <td>5</td>
                        </tr>
                        <tr>
                            <td>Front</td>
                            <td>3</td>
                            <td>5</td>
                        </tr>
                        <tr>
                            <td>Gold Ladies</td>
                            <td>3</td>
                            <td>5</td>
                        </tr>
                        </tbody>
                    </table>
                    </div>
                    <div class="tab-pane fade" id="female3" role="tabpanel" aria-labelledby="female-tab3">
                    <table class="table  table-bordered mt-3 text-center" id="table2_show">
                        <thead>
                        <th>Green</th>
                        <th>Tee</th>
                        <th>Course Rating</th>
                        <th>Yards</th>
                        </thead>
                        <tbody>
                        <tr>
                            <td rowspan="4">Bent</td>
                            <td>Back</td>
                            <td>4</td>
                            <td>7</td>
                        </tr>
                        <tr>
                            <td>Regular</td>
                            <td>5</td>
                            <td>2</td>
                        </tr>
                        <tr>
                            <td>Front</td>
                            <td>3</td>
                            <td>5</td>
                        </tr>
                        <tr>
                            <td>Gold Ladies</td>
                            <td>7</td>
                            <td>9</td>
                        </tr>
                        </tbody>
                    </table>
                    </div>
                </div>
                </div>
            </div>
            <!-- Course Rate Table2 End -->

            <div class="row my-5">
                <div class="col-md-12 notice">
                <h3>Notice</h3>
                <p>We hold many open competitions during the season (mid-April to late November).
                    Please join us.
                    You can enter from one person.
                </p>
                </div>
            </div>
            <div class="row gy-4 topspace2 mt">
                <div class="col-md-12">
                <h3 class="headnew mb-4">Facilities</h3>
                </div>
                <div class="col-md-3">
                <div class="detail-icon text-center pt-4">
                    <img src="images/hockey.png" width="70">
                    <h4 class="mt-4">Facility1※</h4>
                    <h3 class="p-2 py-3 mb-0">Facility1※</h3>
                </div>
                </div>
                <div class="col-md-3">
                <div class="detail-icon text-center pt-4">
                    <img src="images/hockey.png" width="70">
                    <h4 class="mt-4">Facility2※</h4>
                    <h3 class="p-2 py-3 mb-0">Facility2※</h3>
                </div>
                </div>
                <div class="col-md-3">
                <div class="detail-icon text-center pt-4">
                    <img src="images/hockey.png" width="70">
                    <h4 class="mt-4">Facility3※</h4>
                    <h3 class="p-2 py-3 mb-0">Facility3※</h3>
                </div>
                </div>
                <div class="col-md-3">
                <div class="detail-icon text-center pt-4">
                    <img src="images/hockey.png" width="70">
                    <h4 class="mt-4">Facility4※</h4>
                    <h3 class="p-2 py-3 mb-0">Facility4※</h3>
                </div>
                </div>
            </div>
            <!-- <button class="btn btn-default mt-5 px-4 py-2">ゴルフ場周辺の練習場を探す <i class="fa-solid fa-angles-right"></i></button> -->
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
                <img src="images/bann1.jpg" alt="Banner" class="img-fluid w-100">
                </div>
            </div>
            <div class="row topspace2">
                <div class="col-md-12 table2">
                <h3 class="headnew mb-4">Various access methods</h3>
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
            </div>'''

        

        final_html_2 = '''
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
                        <button class="nav-link active" id="nav-course1lay-tab" data-bs-toggle="tab" data-bs-target="#nav-course1lay"
                            type="button" role="tab" aria-controls="nav-course1lay" aria-selected="false">[[Course1]]</button>
                        <!--  Course1 Header End-->
                        </div>
                    </nav>
                    <!--  Sub Tab Header End-->
                    <!--  Sub Tab Content Start-->
                    <div class="tab-content numbertab" id="nav-tabsubContent">
                        <!--  Course1 Content Start-->
                        <div class="tab-pane fade show active" id="nav-course1lay" role="tabpanel" aria-labelledby="nav-course1lay-tab">
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
                                <div id="c11h1"><img src="images/bann1.jpg" alt="Banner" class="img-fluid w-100">
                                    <h4 class="banhead mb-0">[[HOLE 1  PAR4  Regular309Y   HDCP17]]</h4>
                                </div>
                                <!-- Add additional images as required in given section -->
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
                                <!-- Add images here as requried for that section -->'''
                                
        final_html_3 ='''
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


        <!-- Drone Gallery Slider - Start -->
        <div class="modal fade" id="dronegallery" tabindex="-1" aria-labelledby="dronegallerylabel" aria-hidden="true">
            <div class="modal-dialog modal-lg">
            <div class="modal-content">
                <div class="modal-header"><!-- Write Golf Place Name here -->
                <h5 class="modal-title" id="dronegallerylabel">'ホテルルートイン常滑駅前'</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body modal-slider mt-3">
                <!--  Main Tab Headers Start -->
                <ul class="nav nav-pills mb-3" id="pills-tabmaindr" role="tablist">
                    <li class="nav-item" role="presentation">
                    <button class="nav-link active" id="pills-homemaindr-tab" data-bs-toggle="pill"
                        data-bs-target="#pills-homemaindr" type="button" role="tab" aria-controls="pills-homemaindr"
                        aria-selected="true">Photo Gallery</button><!-- Fixed Name -->
                    </li>
                </ul>
                <!-- Main Tab Headers End -->
                <!--  Main Tab Content Start-->
                <div class="tab-content" id="pills-tabmaindrContent">
                    <div class="tab-pane fade show active" id="pills-homemaindr" role="tabpanel"
                    aria-labelledby="pills-homemaindr-tab">
                    <!--  Sub Tab Header Start--><!--  Remove respective TAB and Content if you do not want to show -->
                    <nav class="mt-5">
                        <div class="nav nav-tabs" id="nav-tabsub" role="tablist">
                        <!--  CourseInfo Header Start-->
                        <button class="nav-link active" id="nav-courseinfodr-tab" data-bs-toggle="tab"
                            data-bs-target="#nav-courseinfodr" type="button" role="tab" aria-controls="nav-courseinfodr"
                            aria-selected="true">CourseInfo</button>
                        <!--  CourseInfo Header End-->
                        <!--  Course1 Header Start-->
                        <button class="nav-link" id="nav-course1dr-tab" data-bs-toggle="tab" data-bs-target="#nav-course1dr"
                            type="button" role="tab" aria-controls="nav-course1dr" aria-selected="false">[[Course1]]</button>
                        <!--  Course1 Header End-->
                        </div>
                    </nav>
                    <!--  Sub Tab Header End-->
                    <!--  Sub Tab Content Start-->
                    <div class="tab-content numbertab" id="nav-tabsubContent">
                        <!--  CourseInfo Content Start-->
                        <div class="tab-pane fade show active" id="nav-courseinfodr" role="tabpanel"
                        aria-labelledby="nav-courseinfodr-tab">
                        <div class="mt-4">
                            <ul class="nav nav-pills mb-3" id="pills-tabcinfo" role="tablist">
                            <!--  CourseInfo Tab Header 1H Start-->
                            <li class="nav-item" role="presentation">
                                <button class="nav-link active" id="numbercinfodr1h-tab" data-bs-toggle="pill"
                                data-bs-target="#numbercinfodr1h" type="button" role="tab" aria-controls="numbercinfodr1h"
                                aria-selected="true"></button>
                            </li>
                            <!--  CourseInfo Tab Header 1H End-->
                            </ul>
        
                            <div class="tab-content" id="pills-tabcinfoContent">
                            <!--  CourseInfo Tab Content 1H Start-->
                            <div class="tab-pane fade show active" id="numbercinfodr1h" role="tabpanel"
                                aria-labelledby="numbercinfodr1h-tab">
                                <div class="owl-carousel">
                                <!-- Add images here as requried for that section -->
                                <div id="cinfodr1h1"><img src="images/bann1.jpg" alt="Banner" class="img-fluid w-100">
                                    <h4 class="banhead mb-0">[[1st Image in Slider]]</h4>
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
                        <div class="tab-pane fade" id="nav-course1dr" role="tabpanel" aria-labelledby="nav-course1dr-tab">
                        <div class="mt-4">
                            <ul class="nav nav-pills mb-3" id="pills-tabc1" role="tablist">
                            <!--  course1dr Tab Header 1H Start-->
                            <li class="nav-item" role="presentation">
                                <button class="nav-link active" id="numberc1dr1h-tab" data-bs-toggle="pill"
                                data-bs-target="#numberc1dr1h" type="button" role="tab" aria-controls="numberc1dr1h"
                                aria-selected="true">[[1H]]</button>
                            </li>
                            <!--  course1dr Tab Header 1H End-->
                            </ul>
        
                            <div class="tab-content" id="pills-tabc1Content">
                            <!--  course1 Tab Content 1H Start-->
                            <div class="tab-pane fade show active" id="numberc1dr1h" role="tabpanel"
                                aria-labelledby="numberc1dr1h-tab">
                                <div class="owl-carousel">
                                <!-- Add additional images as required in given section -->
                                <div id="c1dr1h1"><video class="w-100" autoplay loop muted>
                                    <source src="http://localhost/golfdev/htmlv7/video/GolfDemo.mp4" type="video/mp4" />
                                </video>
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
        <!-- Drone Gallery Slider - End -->

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
        img_div =''
        flag = True
        c = 1
        for images in os.listdir(path):
        
            # check if the image ends with png
            if (images.endswith(".jpg")):
                # print(c)
                s = '''<div id="c11h%s"><img src= '%s' alt="Banner" class="img-fluid w-100">
                            <h4 class="banhead mb-0">[[HOLE 1  PAR4  Regular309Y   HDCP17]]</h4>
                        </div>''' %(str(c),'All data/'+hotel_id+'/'+images)
                img_div+=s+'\n'
                # print(images)
                c+=1
            final_html = ''

        final_html +=final_html_1+'\n'
        try:
            if main != '':
                final_html +=main +'\n'
        except:
            pass
        if c_text_1 != '':
            final_html+= c_text_1 +'\n'
        if c_text_2 != '':
            final_html += c_text_2 +'\n'
        final_html+=final_html_2
        if img_div != '':
            final_html += img_div
        final_html += final_html_3

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
        print()
    except Exception as ex:
        with open('html_update log.txt' , 'a') as of:
            of.write(str(ex) +'\n\n')