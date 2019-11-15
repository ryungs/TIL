function sleep_3s() {
    // 실행되자 마자 Invoke뜨고
    console.log('Invoke');
    setTimeout(() => {
        console.log('Wake up!')
    }, 3000)
}

console.log('Start Sleeping');
sleep_3s();
console.log('End of Program');
