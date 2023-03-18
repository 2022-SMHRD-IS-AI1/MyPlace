$(function(){

    let $menu = $('.menu-item');

    $menu.on('click', function(event){
       
        // event.preventDefault();

        console.log(event.target.textContent);

        //조건문 이용해서 메뉴에 해당하는 상품 요청하기
        //1.ajax로 카테고리(침대,의자 등)값을 쿼리값으로 서버에 전송
        //2.flask 서버에서는 상품정보(이름,이미지주소,가격)을 리턴(JSON형태)
        //3.응답받은 데이터를 화면에 출력


        let resultHTML="";

        //템플릿문자열(백틱)
        //책상
        if(event.target.textContent == ""){
            for(var i=0; i<5; i++){
                resultHTML += `
                <a href=${"#"} class="product">
                    <img src=${"https://bakey-api.codeit.kr/files/629/images/sunglasses.jpg"} width="225">
                    <div class="product-name">
                        ${s[i]}
                    </div>
                    <div class="product-price">
                        ${49,000}          
                    </div>
                </a>
                `;
            }
    
            $('div.product-list').html(resultHTML);
        }
        // 의자
        else if(event.target.textContent == ""){
            for(var i=0; i<5; i++){
                resultHTML += `
                <a href=${"#"} class="product">
                    <img src=${"https://bakey-api.codeit.kr/files/629/images/sunglasses.jpg"} width="225">
                    <div class="product-name">
                        ${s[i]}
                    </div>
                    <div class="product-price">
                        ${49,000}          
                    </div>
                </a>
                `;
            }
    
            $('div.product-list').html(resultHTML);
        }
        // 테이블
        else if(event.target.textContent == ""){
            for(var i=0; i<5; i++){
                resultHTML += `
                <a href=${"#"} class="product">
                    <img src=${"https://bakey-api.codeit.kr/files/629/images/sunglasses.jpg"} width="225">
                    <div class="product-name">
                        ${s[i]}
                    </div>
                    <div class="product-price">
                        ${49,000}          
                    </div>
                </a>
                `;
            }
    
            $('div.product-list').html(resultHTML);
        }
        // 침대
        else if(event.target.textContent == ""){
            for(var i=0; i<5; i++){
                resultHTML += `
                <a href=${"#"} class="product">
                    <img src=${"https://bakey-api.codeit.kr/files/629/images/sunglasses.jpg"} width="225">
                    <div class="product-name">
                        ${s[i]}
                    </div>
                    <div class="product-price">
                        ${49,000}          
                    </div>
                </a>
                `;
            }
    
            $('div.product-list').html(resultHTML);
        }
        // 수납장
        else if(event.target.textContent == ""){
            for(var i=0; i<5; i++){
                resultHTML += `
                <a href=${"#"} class="product">
                    <img src=${"https://bakey-api.codeit.kr/files/629/images/sunglasses.jpg"} width="225">
                    <div class="product-name">
                        ${s[i]}
                    </div>
                    <div class="product-price">
                        ${49,000}          
                    </div>
                </a>
                `;
            }
    
            $('div.product-list').html(resultHTML);
        }
    });

});