function myFunc() {
    return n => n + 1;
    // return function (n) { 위에 한줄과 밑에 함수가 같다
    //     return n + 1
    // }
}
const num_101 = myFunc()(100);
console.log(num_101);
   // 101이 되도록 하세요

// 숫자로 이루어진 배열의 요소들을 각각 [???] 한다. [???]는 알아서 해라
const numbersEach = (numbers, callback) => {
    let acc; // JS 에서는 변수에 값을 할당하지 않고 선언만 할 수 있다.
    for (const num of numbers) {
        acc = callback(num, acc);
    }
    return acc;
};

console.log(numbersEach([1,2,3,4,5], (number, sum=0) => sum += number)); // 15 my_array=[1,2,3,4,5]; numbersEach(my_array, adder);
console.log(numbersEach([1,2,3,4], (number, acc=1) => acc *= number)); // 24

const muler = (number, mul=1) => {
    return mul * number;
};

console.log(numbersEach([1,2,3,4,5], muler)); // 120

const adder = (number, sum=0) => {
    return sum + number;
};

console.log(numbersEach([1,2,3,4,5], adder)); // 15

// 인자로 배열을 받는다. 해당 배열의 모든 요소를 더한 숫자를 return
const numbersEachAdd = numbers => {
  let sum = 0;
  for (const number of numbers) {
      sum += number;
  }
  return sum;
};

console.log(numbersEachAdd([1,2,3,4,5]));

// 인자로 배열을 받는다. 해당 배열의 모든 요소를 뺀 숫자를 return
const numbersEachSub = numbers => {
    let acc = 0;
    for (const number of numbers) {
        acc -= number;
    }
    return acc;
};

console.log(numbersEachSub([1,2,3,4,5]));

// 인자로 배열을 받는다. 해당 배열의 모든 요소를 곱한 숫자를 return
const numbersEachMul = numbers => {
    let acc = 1;
    for (const number of numbers) {
        acc *= number;
    }
    return acc;
};

console.log(numbersEachMul([1,2,3]));

