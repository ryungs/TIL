typeof 1 // number

typeof (typeof 1) // string (항상)

typeof (() => {}) // function

typeof (funtion(){}) // function

typeof(NaN) // number NaN = Not a Number 이지만 number 나온다

'a' / 100 // 치면 NaN 나온다, 숫자 연산자에 해야하는 수식들 하면 NaN

'a' + 100 // "100a" 더하기만 문자열 + 숫자 된다 (특이)

'123' + 1 // '1231' 알아서 문자열 + 숫자로 잡고

'123' * 1 // '123' 여기서는 다시 숫자 * 숫자로 잡는다

100 / 0 // Infinity,  뻗어버리기 때문에 Infinity 라는 타입을 따로 만들었다

typeof (100/ 0) // number
typeof Infinity // number

const aa = {a: 1, b: 2};
aa.c // undefined

typeof undefined // undefined 는 undefined 라는 자기만의 type 을 가지고 있다

null //은 비어있는다는 뜻이다

typeof null // object

typeof {} // object

typeof [] // object

