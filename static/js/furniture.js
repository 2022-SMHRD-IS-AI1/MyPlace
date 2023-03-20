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

    $menu.on('click', function(event){
       
        // event.preventDefault();

        console.log(event.target.textContent);
        console.log("bed", bed_price[0].textContent)
        console.log("bed", bed_url[0].textContent)
        console.log("bed", bed_path[0].textContent)

        //조건문 이용해서 메뉴에 해당하는 상품 요청하기
        //1.ajax로 카테고리(침대,의자 등)값을 쿼리값으로 서버에 전송
        //2.flask 서버에서는 상품정보(이름,이미지주소,가격)을 리턴(JSON형태)
        //3.응답받은 데이터를 화면에 출력

        let resultHTML="";

        //템플릿문자열(백틱)

        //책상
        if(event.target.textContent == "desk"){
            for(var i=0; i<5; i++){
                resultHTML += `
                <a href=${desk_url[0].textContent} class="product">
                    <img src="${desk_path[0].textContent}" width="225">
                    <div class="product-name">
                        ${"책상"}
                    </div>
                    <div class="product-price">
                        ${desk_price[0].textContent+'원'}          
                    </div>
                </a>
                `;
            }
    
            $('div.product-list').html(resultHTML);
        }
 
        // 의자
        else if(event.target.textContent == "chair"){
            for(var i=0; i<5; i++){
                resultHTML += `
                <a href=${chair_url[0].textContent} class="product">
                    <img src="${chair_path[0].textContent}" width="225">
                    <div class="product-name">
                        ${"의자"}
                    </div>
                    <div class="product-price">
                        ${chair_price[0].textContent+'원'}          
                    </div>
                </a>
                `;
            }
    
            $('div.product-list').html(resultHTML);
        }

        // 테이블
        else if(event.target.textContent == "table"){
            for(var i=0; i<5; i++){
                resultHTML += `
                <a href=${table_url[0].textContent} class="product">
                    <img src="${table_path[0].textContent}" width="225">
                    <div class="product-name">
                        ${"테이블"}
                    </div>
                    <div class="product-price">
                        ${table_price[0].textContent+'원'}          
                    </div>
                </a>
                `;
            }
    
            $('div.product-list').html(resultHTML);
        }

        // 침대
        else if(event.target.textContent == "bed"){
            for(var i=0; i<5; i++){
                resultHTML += `
                <a href=${bed_url[0].textContent} class="product">
                    <img src="${bed_path[0].textContent}" width="225">
                    <div class="product-name">
                        ${"침대"}
                    </div>
                    <div class="product-price">
                        ${bed_price[0].textContent+'원'}          
                    </div>
                </a>
                `;
            }
    
            $('div.product-list').html(resultHTML);
        }

        // 수납장
        else if(event.target.textContent == "closet"){
            for(var i=0; i<5; i++){
                resultHTML += `
                <a href=${closet_url[0].textContent} class="product">
                    <img src="${closet_path[0].textContent}" width="225">
                    <div class="product-name">
                        ${"수납장"}
                    </div>
                    <div class="product-price">
                        ${closet_price[0].textContent}          
                    </div>
                </a>
                `;
            }
    
            $('div.product-list').html(resultHTML);
        }
    });

});