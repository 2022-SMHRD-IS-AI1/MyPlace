function upload() {
  
 
    var file = document.getElementById("myFileUpload").files[0];
      var formData = new FormData();
      formData.append("image", file);
      var xhr = new XMLHttpRequest();
      xhr.open("POST", "/upload", true);
      xhr.onload = function() {
        if (xhr.status === 200) {
          // 업로드 성공시 처리할 코드 작성
          console.log("Upload successful!");
        } else {
          // 업로드 실패시 처리할 코드 작성
          console.error("Upload failed.");
        }
      };
      xhr.send(formData);
    }
    