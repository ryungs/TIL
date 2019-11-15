// function addAll (number=[]) {
//     let sum = 0;
//     numbers.forEach(number => sum += numbers);
//     return sum;
// }

module.exports = {
    // key value 가 같으면 하나는 삭제해도 된다
    // addAll: addAll,
    // subAll: subAll,
    // mulAll: mulAll

    // function 따로 정의 하지 않고 안에 바로 적어줘도 된다
    addAll(numbers=[]) {
        let sum = 0;
        numbers.forEach(number => sum += number);
        return sum;
    },
    subAll() {

    },
    mulAll() {

    },
    name: 'dr',
};

// 새로운 인자 추가하는 방법
phoneNumber = '01012345678';
module.exports.phoneNumber = phoneNumber;