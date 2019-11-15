const arr = [1, 2, 3]

// return 값 : X
arr.forEach((num) => {
    console.log(num)
}) // return값 없음


// 위 표현방법과 같은 방법 이거 구별하는 법 알아야함
arr.forEach(function (num) {
    console.log(num)
})

// return 값 : callback함수 안에서 return 된 값들의 배열
arr.map((num) => {
    return num
}) // [1, 2, 3]이 return, return num * 2 하면 [2, 4, 6]이 된다.

// return 값 : callback함수 안에서 return true인 요소들의 배열
arr.filter((num) => {
    return num > 1
}) // arr의 요소 1, 2, 3 중 2, 3만 만족하므로 새로 만들어지는 return 배열에 들어간다.
// [2, 3]이 return


// return 값 : callback안에서 처음 return true인 요소
arr.find((num) => {
    return num > 1
}) // 만족하는 요소 하나 선착순으로 리턴하고 끝!
// 2