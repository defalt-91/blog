// let myarray = [
//     ['arman', 30],
//     ['ayda', 22],
//     ['farah', 26]
// ];
// myarray.push('afsaneh')
// myarray.unshift('armanian')



// function testing(x) {
//     if (x > 4) {
//         return "x is greater than four"
//     } else if (x == 0) {
//         return 'x is zero'
//     } else {
//         return 'x is smaller than four'
//     }
// }

// function testswitch(x) {
//     switch (x) {
//         case 1:
//             return 'x is one'
//         case 2:
//             return 'x is two'
//         case 3:
//             return 'x is three'
//     }
// }


// function switch2(x, y) {
//     switch (x, y) {
//         case 1 || 1:
//             return 'both are one';
//         case 2 || 2:
//             return 'both are two'
//         default:
//             return 'please enter a valid num'
//     }
// }

// var me = {
//     'fname': 'arman',
//     'lname': 'soltanian',
// };
// me.age = 23
// me.mood = 'good'
// delete me.age
// me.fnam = 'ayda'
// function tests(x) {

//     if (me.hasOwnProperty(x)) {
//         console.log('darad')
//     } else {
//         return console.log('nadarad')
//     }
// }
// // tests(mood)
// // console.log(me)


// // console.log(switch2(0, 1))

// // console.log(myarray[0])

// // console.log(testing(0))

// // console.log(testswitch(4))

// var myobj = [
//     { 'name': 'arman', 'age': 23 },
//     { 'lname': 'ayda', 'aage': 20 },
//     num = 23
// ]
// console.log(myobj[2].hasOwnProperty('age'))

// var mynestedobj = {
//     'car': {
//         'inside': {
//             'glove box': 'map',
//             'passenger seat': 'crumbs'
//         },
//         'outside': {
//             'trunk': 'jack'
//         }
//     }
// }
// console.log(mynestedobj.car.inside['passenger seat'])

// var lists = ['arman', 23, ['programmer', 'developer']]
// lists.push('assdh')
// console.log(lists)

// function whiletest(x) {
//     var myvar = [];
//     while (x < 6) {
//         myvar.push(x);
//         x++
//     }
//     return console.log(myvar)
// }
// whiletest(3)

// for (i = 1; i < 20; i += 2) {
//     console.log(i)
// }
// var i = 10
// do {
//     console.log(i)
// } while (i < 5);

// function Ternary(x, y) {
//     return x > y ? console.log('true') : console.log('false')
// } 
// Ternary(1, 0)
// const name = {
//     fname: 'arman',
//     lname: 'soltanian',
// }
// const armanlist = `my name is ${name.fname} and my lastname is ${name.lname}`
// console.log(armanlist)

// let names = ['arman', 'soltanian']

// let abs = `hello my  name is $names[0] and my seconf name is $names[2]`

// class makenum {
//     constructor(num) {
//         this.number = num
//     }
// }

// let var2 = new makenum(23)

// console.log(var2)

// class makefunc {
//     constructor(...arr) {
//         this.x = arr
//     }
// }

// let namee = new makefunc(23, 13, 14)
// console.log(namee.x)

class arman {
    constructor(author) {
        this.author = author
    }
    get writer() {
        return this.author;
    }
    set writer(updatedauthor) {
        this.author = updatedauthor;
    }
}
let armando = new arman('ayda')
armando.writer = 'farah'
console.log(armando.writer, armando.author)


class dildo {
    constructor(x) {
        this.x = x
    }
    set y(Y) {
        this.y = Y
    }
    get y() {
        return this.y
    }
}
const dildi = new dildo(10)
dildi.y = 'arman'
console.log(dildi.y)