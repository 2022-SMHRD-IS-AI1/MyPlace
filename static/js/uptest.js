 // API Server
    // API : 데이터를 반환해주는 서버 or 프로그램
    // 비동기 통신( ajax );
    // http://35.78.206.254:8080/MyPlace_Image/FileUpload
    function request(){
        var inputFile = $('#myFileInput')[0].files[0];
        print('inputFile :',inputFile)
        var formData = new FormData();
        formData.append('file', inputFile);
        $.ajax({
          url : 'http://35.78.206.254:8080/MyPlace_Image/FileUpload',// 어디로?
          data : formData,
          processData: false,
          contentType: false,
          type : "post",
          success : function(res){
            // 성공하면?
            console.log("요청 성공");
            window.location.href="http://127.0.0.1:5500/analyze?file_path="+response.url;
  
            // 페이지 이동
            // window.location.href="http://www.naver.com/";
            // +data : get방식(쿼리스트링)
          },
          error : function(xhr, status, e){
            // 실패하면
            console.log(e)
          }
  
        });
  
      }
      //const uploadButton = document.getElementById("uploadButton");
      //const fileUpload = document.getElementById("myFileUpload");
  
      //uploadButton.addEventListener("click", () => {
      //  const file = fileUpload.files[0];
      //  const formData = new FormData();
      //  formData.append("image", file);
  
      //  const xhr = new XMLHttpRequest();
      //  xhr.open("POST", "/upload");
      //  xhr.onload = function() {
      //    if (xhr.status === 200) {
      //      const response = JSON.parse(xhr.responseText);
      //      if (response.status === 'success') {
      //        window.open(response.url, '_blank');
      //      } else {
      //        console.error("Upload failed.");
      //      }
      //    } else {
      //     console.error("Upload failed.");
      //    }
      //  };
      //  xhr.send(formData);
      // }); -->