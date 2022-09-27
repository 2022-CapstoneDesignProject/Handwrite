

// Express 기본 모듈 불러오기
var express = require('express');
var http = require('http');
var path = require('path');
 
// Express의 미들웨어 불러오기
var bodyParser = require('body-parser');
var cookieParser = require('cookie-parser');
var static = require('serve-static');
var errorHandler = require('errorhandler');
 
// 에러 핸들러 모듈 사용
var expressErrorHandler = require('express-error-handler');
 
// Session 미들웨어 불러오기
var expressSession = require('express-session');
 

// 익스프레스 객체 생성
var app = express();
 
//파일 업로드용 미들웨어
var multer = require('multer');
var fs = require('fs');

// 클라이언트에서 ajax로 요청했을 때 CORS(다중 서버 접속) 지원
var cors = require('cors');

// 기본 속성 설정
app.set('port', process.env.PORT || 3000);
 
// body-parser를 이용해 application/x-www-form-urlencoded 파싱
app.use(bodyParser.urlencoded({ extended: false }))
 
// body-parser를 이용해 application/json 파싱
app.use(bodyParser.json())
 
// public 폴더와 upload 폴더 오픈
app.use('/public', express.static(path.join(__dirname, 'public')));
app.use('/uploads', express.static(path.join(__dirname, 'uploads')));


// cookie-parser 설정
app.use(cookieParser());
 
// 세션 설정
app.use(expressSession({
    secret:'my key',
    resave:true,
    saveUninitialized:true
}));
 
// 클라이언트에서 ajax로 요청했을 때 CORS(다중 서버 접속)지원
app.use(cors());

//multer 미들웨어 사용 : 미들웨어 사용 순서 중요 body-parser -> multer -> router
// 파일 제한 : 10개, 1G
var storage = multer.diskStorage({
    destination: function(req, file, callback){
        var dir = './uploads';
        if(!fs.existsSync(dir)) fs.mkdirSync(dir);
        callback(null, './uploads');
    },
    filename: function(req, file, callback){
        callback(null, file.originalname + Date.now())
    }
});
 
var upload = multer({
    storage: storage,
    limits: {
        files: 10,
        fileSize: 1024*1024*1024
    }
});

// 라우터 사용하여 라우팅 함수 등록
var router = express.Router();

app.get('/', function(req, res){
    res.sendFile(__dirname + "/public/index.html");
});

/*
app.post('/', upload.array('photo', 1), function(req, res){
    var response = '<a href="index.html></a>'
    

    
})*/
// 사진 업로드하는 기능 라우팅 함수
/*upload.single 미들웨어를 라우터 콜백함수 전에 끼워 넣었는데 
이것은 폼데이터의 속성명이 img이거나 폼 태그 인풋의 name이 img인 파일 하나를 받겠다는 뜻
이미지를 하나가 아닌 여러 개를 받고 싶다 하면 upload.array('키', 최대파일개수)
*/
//router.get('/', upload.array('photo',1),function(req,res){
router.use('/', upload.array('photo',1),function(req,res){
//router.use('/', upload.single('img'),function(req,res){
//route('/process/photo').    
    try{
        if(req.files && req.files.length > 0){
            var files = req.files;

            console.dir('#==== 업로드된 첫번째 파일 정보 ====#');
            console.dir(req.files[0]);
            console.dir('#=====#');
        
            // 현재의 파일 정보를 저장할 변수 선언
            var originalname = '',
                filename = '',
                mimetype= '',
                size = 0;
        
            if(Array.isArray(files)){
                console.log("배열에 들어있는 파일의 갯수 : %d",files.length);
                for(var index = 0; index < files.length; index++){
                    originalname = files[index].originalname;
                    filename = files[index].filename;
                    mimetype = files[index].mimetype;
                    size = files[index].size;
                }
            }else{
                // 배열에 들어가 있지 않은 경우 (현재 설정에서는 해당 없음)
                console.log('파일 갯수 : 1');
                
                originalname = files[index].originalname;
                filename = files[index].filename;
                mimetype = files[index].mimetype;
                size = files[index].size;
                
            }
            console.log('현재 파일 정보 : ' + originalname + ', ' + filename + ', ' + mimetype + ', ' + size);
        }
                
        //클라이언트에 응답 전송
        //res.writeHead('200', {'Content-Type':'text/html;charset=utf8'});
        //res.write('<h3>파일 업로드 성공</h3>');
        //res.write('<hr/>');
        //res.write('<p>원본 파일 이름 : ' + originalname + '-> 저장 파일명 ' + filename + '</p>');
        //res.write('<p>MIME TYPE : ' + mimetype + '</p>');
        //res.write('<p>파일 크기 : ' + size + '</p>');
        //res.end();
        
    }
    catch(err){
        console.dir(err.stack);
    }
});

/*
// 사진 업로드하는 기능 라우팅 함수
router.route('/process/photo').post(upload.array('photo',1),function(req,res){
    
    try{
        var files = req.files;
        
        console.dir('#==== 업로드된 첫번째 파일 정보 ====#');
        console.dir(req.files[0]);
        console.dir('#=====#');
        
        // 현재의 파일 정보를 저장할 변수 선언
        var originalname = '',
            filename = '',
            mimetype= '',
            size = 0;
        
            if(Array.isArray(files)){
                console.log("배열에 들어있는 파일의 갯수 : %d",files.length);
                for(var index = 0; index < files.length; index++){
                    originalname = files[index].originalname;
                    filename = files[index].filename;
                    mimetype = files[index].mimetype;
                    size = files[index].size;
                }
            }else{
                // 배열에 들어가 있지 않은 경우 (현재 설정에서는 해당 없음)
                console.log('파일 갯수 : 1');
                
                originalname = files[index].originalname;
                filename = files[index].filename;
                mimetype = files[index].mimetype;
                size = files[index].size;
                
            }
        console.log('현재 파일 정보 : ' + originalname + ', ' + filename + ', ' + mimetype + ', ' + size);
        
        //클라이언트에 응답 전송
        res.writeHead('200', {'Content-Type':'text/html;charset=utf8'});
        res.write('<h3>파일 업로드 성공</h3>');
        res.write('<hr/>');
        res.write('<p>원본 파일 이름 : ' + originalname + '-> 저장 파일명 ' + filename + '</p>');
        res.write('<p>MIME TYPE : ' + mimetype + '</p>');
        res.write('<p>파일 크기 : ' + size + '</p>');
        res.end();
        
    }
    catch(err){
        console.dir(err.stack);
    }
});
*/


// 모든 router 처리 끝난 후 404 오류 페이지 처리
var errorHandler = expressErrorHandler({
    static:{
        '404': './public/404.html'
    }
});
 
//app.use(expressErrorHandler.httpError(404));
app.use(errorHandler);

// 라우터 객체를 app 객체에 등록
app.use('/',router); 

// Express 서버 시작
http.createServer(app).listen(app.get('port'), function(){
  console.log('Express server listening on port ' + app.get('port'));
});

