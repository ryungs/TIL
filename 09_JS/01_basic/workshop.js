// This is Comment

// 1.
const concat = function (str1, str2) {
    return `${str1}-${str2}`;
};

const concat = (str1, str2) => `${str1}-${str2}`;

// 2.
const checkLongStr =  string => {
    if (string.length > 10) {
        return true;
    } else {
        return false;
    }
};

if (checkLongStr(concat('Happy', 'Hacking'))) {
    console.log('LONG STRING');
} else {
    console.log('SHORT STRING');
}

// 위에꺼 줄이기

console.log(
    checkLongStr(concat('Happy', 'Hacking')) ? 'LONG STRING': 'SHORT STRING'
);


