const me = {
    name: 'dr',
    'phone number': '01012341234', // 띄워쓰기가 있으면 'key'로 쓴다
    appleProducts: {
        ipad: '2018pro',
        iphone: '6s+',
        macbook: '2018 pro',
    }
};

me.name; // 'dr'
me['name']; // 'dr'
me['phone number']; // '01012341234' 띄워쓰기 있으면 me.phonenumber 안됨
me.appleProducts; // {ipad: '2018pro', iphone: '6s+', macbook: '2018 pro',}
me.appleProducts.ipad; //'2018pro'
