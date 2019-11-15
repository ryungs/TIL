// ES5 for loop
// var numbers = [1, 2, 3];
// var doubleNumbers = [];
//
// for (var i = 0; i <numbers.length ; i ++) {
//     doubleNumbers.push((numbers[i] * 2));
// }
// console.log(doubleNumbers);
// ---------------------------------------------------------
// ES6 +
const numbers = [1, 2, 3];

function double(n) {
    return n * 2;
}

const doubleNumbers = numbers.map(double); // map함수는 새로운 함수를 return 한다.
const tripleNumbers = numbers.map(number => {
   return number * 3;
});

console.log(tripleNumbers);

// 인자를 받아서 배열로 만드는 방법
const image = [
    { height: 30, width: 60},
    { height: 10, width: 20},
    { height: 20, width: 20},
];

const imageAreas = image.map(image => {
    return image.height * image.width;
});

console.log(imageAreas);

/*
    아래의 pluck 함수를 완성하세요.
    pluck 함수는 배열(array)고 요소 이름 (ket(

 */

function pluck (array, property) {
    const newArray = array.map(e => {
        if (e[property]) return e[property];
    });
    return newArray
};

const paints = [
    { color: 'red'},
    { color: 'blue'},
    { color: 'green'},
    { smell: 'ushh'},
];

pluck(paints, 'color'); // ['red', 'greed', 'blue']
pluck(paints, 'smell'); // ['ushh']