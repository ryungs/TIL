const numbers = [1, 2, 3, 4];

numbers[0]; // 1
numbers[-1]; //undifined
numbers.length; // 4

/* 원본이 달리지는 methods */
numbers.reverse(); // [4, 3, 2, 1]
numbers; // [4, 3, 2, 1]
numbers.reverse(); // [1, 2, 3, 4]

//stack 개념
numbers.push('a'); // 5 new length
numbers; // [1, 2, 3, 4, 'a']
numbers.pop();
numbers; // [1, 2, 3, 4]

//큐 개념
console.log(numbers.unshift('a')); // 5 new length
numbers; // ['a', 1, 2, 3, 4]
numbers.shift(); // 'a'
numbers; // [1, 2, 3, 4]

/* Copy 혹은 다른 결과 return (원본유지) methods */
// 이 숫자가 있냐 없냐
numbers.includes(1); //True
numbers.includes(0); //False

numbers.push('a', 'a'); // test 용으로 적은거
numbers; // [1, 2, 3, 4, 'a', 'a']
numbers.indexOf('a'); // 4 제일 처음 나오는 애의 인덱스 값만 리턴
numbers.indexOf('b'); // -1 없다는 뜻

numbers; // [1, 2, 3, 4, 'a', 'a']
numbers.join('-'); // '1-2-3-4-a-a'
numbers.join(''); // '1234aa'
numbers.join(); // '1,2,3,4,a,a'



