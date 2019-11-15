// ES5
var name = 'ssafy'
name = 'ssafy2'

var NAME = '' // 파이썬은 따로 상수가 없어서 대문자로 구별

for (var i=0; i < 10 ; i++) {

}
console.log(i) // 10이 나옴


/* ---- scope 참조 가능 범위---- */
// ES6+
let a = 1
a = 1

const coffee = 'latte'
coffe = 'hi' // 다시 할당하려하면 에러남

// const와 let은 중괄호 안에서만 자신의 생명주기를 가지고 있다.

for (let i = 0; i < 10; i ++) {

}
console.log(i) // 이건 에러난다!

const a = [1, 2, 3]
a.push(4) // ok
// No: a = [1, 2, 3, 4]