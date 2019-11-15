const DOMAIN = 'https://jsonplaceholder.typicode.com/';
const RESOURCE = 'posts';
const QUERY_STRING = '';

const URL = DOMAIN + RESOURCE + QUERY_STRING;
// req 대리인 XHR 객체 생성
const XHR = new XMLHttpRequest();

// 요청을 만들고, 정보를 담고, 보내고, 기다리고, 처리한다. XHR 요청 발사 준비 (method ,url)
XHR.open('POST', URL);

XHR.setRequestHeader(

    'Content-Type',
    'application/json;charset=UTF-8'
);
// XHR 요청 발사! JSON(string)으로  보내야 한다
XHR.send( //serializing
    JSON.stringify({ "title": "NewPost", "body": "This is New Post", "userId": 1 })
);

XHR.addEventListener('load', e => {
    const parseData = JSON.parse(e.target.response);
    console.log(parseData);
});


