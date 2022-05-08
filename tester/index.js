/*var http = require('http');
var fs = require('fs');
 
// 웹 서버 객체를 만든다.
var server = http.createServer();
 
// 웹 서버를 시작하여 3000번 포트에서 대기하도록 설정한다.
var port = 3000;
server.listen(port, function(){
    console.log('웹 서버가 시작되었습니다. : %d',port);
});
 
// 클라이언트 연결 이벤트 처리
server.on('connection', function(socket){
    var addr = socket.address();
    console.log('클라이언트가 접속했습니다. : %s, %d',addr.address, addr.port);
});
 
// 클라이언트 요청 이벤트 처리
server.on('request', function(req,res){
    console.log('클라이언트 요청이 들어왔습니다.');
    console.dir(req);
});

// 클라이언트 요청 이벤트 처리
server.on('request', function(req,res){
  console.log('클라이언트 요청이 들어왔습니다.');
  
  var filename = "cat.png";
    fs.readFile(filename, function(err, data){
        if(err) throw err;
        
        res.writeHead(200, {"Content-Type":"image/png"});
        res.write(data);
        res.end();
    });
  
});

// 서버 종료 이벤트 처리
server.on('close', function(){
    console.log('서버가 종료됩니다.');
});
*/

var submit = document.getElementById('submitButton');
submit.addEventListener('click', showImage);     //Submit 버튼 클릭시 이미지 보여주기

function showImage() {
    var newImage = document.getElementById('image-show').lastElementChild;
    newImage.style.visibility = "visible";
    
    document.getElementById('image-upload').style.visibility = 'hidden';

    document.getElementById('fileName').textContent = null;     //기존 파일 이름 지우기
}


function loadFile(input) {
    var file = input.files[0];

    var name = document.getElementById('fileName');
    name.textContent = file.name;

    var newImage = document.createElement("img");
    newImage.setAttribute("class", 'img');

    newImage.src = URL.createObjectURL(file);   

    newImage.style.width = "70%";
    newImage.style.height = "70%";
    newImage.style.visibility = "hidden";   //버튼을 누르기 전까지는 이미지 숨기기
    newImage.style.objectFit = "contain";

    var container = document.getElementById('image-show');
    container.appendChild(newImage);
    
};
