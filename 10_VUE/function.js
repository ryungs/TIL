/*

    1급객체란 무엇인가?
        1. 변수에 저장(바인드) 됨.
        2. 함수 인자로 들어감
        3. return 값으로 뱉어짐
*/

// WHAT 다음에 들어갈 수 있으면 ([], '', 1, {}, 함수) 모두 1급 객체
const WHAT = function () {
    return 'hihi'
}
let number = WHAT
console.log(WHAT)
function no () {
    return WHAT;
}


function myFunc() {
    return n => n + 1;
}