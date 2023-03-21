$(function(){

    let $menu = $('.menu-item');
    let table_price = $('#table_price');
    let table_url = $('#table_url');
    let table_path = $('#table_path');
    let desk_price = $('#desk_price');
    let desk_url = $('#desk_url');
    let desk_path = $('#desk_path');
    let chair_price = $('#chair_price');
    let chair_url = $('#chair_url');
    let chair_path = $('#chair_path');
    let closet_price = $('#closet_price');
    let closet_url = $('#closet_url');
    let closet_path = $('#closet_path');
    let bed_price = $('#bed_price');
    let bed_url = $('#bed_url');
    let bed_path = $('#bed_path');

    let modern_bed_name_list=["도르미릴렉스 모던 유로탑 침대","포스트모던 레아 서랍형 LED침대","다다미침대"]
    let modern_desk_name_list=["학생 고무 원목 모던 컴퓨터 사무용 서재 책상","모던스틸 1800 책상","텐바이텐 10X10 : 모던 심플 L자형 책상"]
    let modern_closet_name_list=["사이드보드 거실 장식장 TV 서랍장","다이닝 사이드 캐비닛 솔리드 우드 통합 벽 가정용 25cm 모던 심플 거실 보관 와인 캐빈","유니크신발수납장"]
    let modern_bed_photo_list = ["static/images/modern_bed2.jpg", "static/images/modern_bed3.jpg", "static/images/modern_bed4.jpg"]
    let modern_desk_photo_list = ["static/images/modern_desk2.jpg", "static/images/modern_desk3.jpg", "static/images/modern_desk4.jpg"]
    let modern_closet_photo_list = ["static/images/modern_closet2.jpg", "static/images/modern_closet3.jpg", "static/images/modern_closet4.jpg"]
    let modern_bed_price_list = ["510,000", "436,500", "647,780"]
    let modern_desk_price_list = ["192,700", "188,430", "679,000"]
    let modern_closet_price_list = ["178,000", "339,900", "109,000"]

    $menu.on('click', function(event){
       
        // event.preventDefault();

        console.log(event.target.textContent);
        console.log("bed", bed_price[0].textContent);
        console.log("bed", bed_url[0].textContent);
        console.log("bed", bed_path[0].textContent);

        //조건문 이용해서 메뉴에 해당하는 상품 요청하기
        //1.ajax로 카테고리(침대,의자 등)값을 쿼리값으로 서버에 전송
        //2.flask 서버에서는 상품정보(이름,이미지주소,가격)을 리턴(JSON형태)
        //3.응답받은 데이터를 화면에 출력

        let resultHTML="";

        //템플릿문자열(백틱)

        //책상
        if(event.target.textContent == "desk"){
            resultHTML += `
                <a href=${desk_url[0].textContent} class="product">
                    <img src="${desk_path[0].textContent}" width="225">
                    <div class="product-name">
                        ${"순수원목 B테이블라지 접이식 거실테이블"}
                    </div>
                    <div class="product-price">
                        ${desk_price[0].textContent+'원'}
                        <br>
                        <br>   
                    </div>
                </a>
                `;
            for(var i=0; i<3; i++){
                resultHTML += `
                <a href=${"https://www.naver.com/"} class="product">
                    <img src="${modern_desk_photo_list[i]}" width="225">
                    <div class="product-name">
                        ${modern_desk_name_list[i]}
                    </div>
                    <div class="product-price">
                        ${modern_desk_price_list[i]+'원'}          
                        <br>
                        <br>
                    </div>
                </a>
                `;
            }
    
            $('div.product-list').html(resultHTML);
        }
 
        // 의자
        else if(event.target.textContent == "chair"){
            resultHTML += `
                <a href=${chair_url[0].textContent} class="product">
                    <img src="${chair_path[0].textContent}" width="225">
                    <div class="product-name">
                        ${"의자"}
                    </div>
                    <div class="product-price">
                        ${chair_price[0].textContent+'원'}    
                        <br>
                        <br>      
                    </div>
                </a>
                `;
            for(var i=0; i<3; i++){
                resultHTML += `
                <a href=${"https://www.youtube.com/"} class="product">
                    <img src="${"https://bakey-api.codeit.kr/files/629/images/sunglasses.jpg"}" width="225">
                    <div class="product-name">
                        ${"의자"}
                    </div>
                    <div class="product-price">
                        ${"49,000"+'원'}          
                        <br>
                        <br>
                    </div>
                </a>
                `;
            }
    
            $('div.product-list').html(resultHTML);
        }

        // 테이블
        else if(event.target.textContent == "table"){
            resultHTML += `
                <a href=${table_url[0].textContent} class="product">
                    <img src="${table_path[0].textContent}" width="225">
                    <div class="product-name">
                        ${"테이블"}
                    </div>
                    <div class="product-price">
                        ${"49,000"+'원'}
                        <br>
                        <br>       
                    </div>
                </a>
                `;
            for(var i=0; i<3; i++){
                resultHTML += `
                <a href=${"https://www.nexon.com/Home/Game"} class="product">
                    <img src="${"https://bakey-api.codeit.kr/files/629/images/sunglasses.jpg"}" width="225">
                    <div class="product-name">
                        ${"테이블"}
                    </div>
                    <div class="product-price">
                        ${table_price[0].textContent+'원'}
                        <br>
                        <br>
                    </div>
                </a>
                `;
            }
    
            $('div.product-list').html(resultHTML);
        }

        // 침대
        else if(event.target.textContent == "bed"){
            resultHTML += `
                <a href=${bed_url[0].textContent} class="product">
                    <img src="${bed_path[0].textContent}" width="225">
                    <div class="product-name">
                        ${"레스트 좌식 접이식 소파베드"}
                    </div>
                    <div class="product-price">
                        ${bed_price[0].textContent+'원'}    
                        <br>
                        <br>      
                    </div>
                </a>
                `;
            for(var i=0; i<3; i++){
                resultHTML += `
                <a href=${"#"} class="product">
                    <img src="${modern_bed_photo_list[i]}" width="225">
                    <div class="product-name">
                        ${modern_bed_name_list[i]}
                    </div>
                    <div class="product-price">
                        ${modern_bed_price_list[i]+'원'}
                        <br>
                        <br>  
                    </div>
                </a>
                `;
            }
    
            $('div.product-list').html(resultHTML);
        }

        // 수납장
        else if(event.target.textContent == "closet"){
            resultHTML += `
                <a href=${closet_url[0].textContent} class="product">
                    <img src="${closet_path[0].textContent}" width="225">
                    <div class="product-name">
                        ${"디셈버 2단 TV거실장세트"}
                    </div>
                    <div class="product-price">
                        ${closet_price[0].textContent}
                        <br>
                        <br>
                    </div>
                </a>
                `;
            for(var i=0; i<3; i++){
                resultHTML += `
                <a href=${"#"} class="product">
                    <img src="${modern_closet_photo_list[i]}" width="225">
                    <div class="product-name">
                        ${modern_closet_name_list[i]}
                    </div>
                    <div class="product-price">
                        ${modern_closet_price_list[i]}원
                        <br>
                        <br>
                    </div>
                </a>
                `;
            }
    
            $('div.product-list').html(resultHTML);
        }
    });
01
});