const ServerURL = "http://18.182.31.43:8080/MyPlace_Image/";
// API Server
// API : 데이터를 반환해주는 서버 or 프로그램
// 비동기 통신( ajax );
// http://35.78.206.254:8080/MyPlace_Image/FileUpload

const myFileInput = $("#myFileInput")

function request() {
  var inputFile = $("#myFileInput")[0].files[0];
  console.log("inputFile :", inputFile);
  var formData = new FormData();
  formData.append("myFileInput", inputFile);

  console.log(formData);
  $.ajax({
    url: ServerURL + "FileUpload", // 어디로?
    processData: false,
    contentType: false,
    data: formData,
    type: "post",
    success: function (res) {
      // 성공하면?
      console.log(res);
      window.location.href =
        "http://127.0.0.1:5500/analyze?file_path=" + ServerURL + res;

      // 페이지 이동
      // window.location.href="http://www.naver.com/";
      // +data : get방식(쿼리스트링)
    },
    error: function (xhr, status, e) {
      // 실패하면
      console.log(e);
    }
  });
}
