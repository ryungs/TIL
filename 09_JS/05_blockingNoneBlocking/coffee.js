function makeCoffee(order) {
    let cup; //빈 컵
    // Coffee 기계 밑에서 걸리는 시간
    setTimeout(() => {
        cup = order;
    }, 2000);
    return cup;
}

console.log(makeCoffee('latte'));



function makeCoffee(order, serve) {
    let cup; //빈 컵
    // Coffee 기계 밑에서 걸리는 시간
    setTimeout(() => {
        cup = order;
        serve(cup);
    }, 2000);
    return cup;
}

const myCoffee = makeCoffee('latte', console.log);