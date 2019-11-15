// JSON은 표기 법
// {'a': 'A'}

const myObject = {
    coffee: 'Americano',
    iceCream: 'Hush',
};
console.log(typeof myObject); // object 따라서 myObject.coffee 됨!

const jsonData = JSON.stringify(myObject); // object를 json 언어로 바꾸는거
console.log(typeof jsonData); // string 따라서 jsonData.coffee 안됨!

const parseData = JSON.parse(jsonData); // json을 object로 바꿔주는거
console.log(typeof parseData); // object 따라서 parseData.coffee 됨!