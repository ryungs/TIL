function hi() {

}

const bye = () => {

};

const me = {
    name: 'dr',
    phone:'01012345678',
    email: 'drdr@abc.com',
    intro : function () {
        return `Hi my name is ${this.name}.`
    }
};
console.log(me.intro());

const you = {
    name: 'dg',
    phone:'01012345678',
    email: 'drdr@abc.com',
    intro : () => {
        return `Hi my name is ${this.name}.`
    },
    wait: function () {
        setTimeout(() => {
            console.log(this.email);
        }, 1000)
    }
};
console.log(you.intro());
console.log(you.wait());

