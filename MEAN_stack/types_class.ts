const mynum: number = 5;
const myString: string = "Hello Universe";
const myArr: number[] = [1,2,3,4];

let myObj: { [key: string]: (string | number)} = {name: 'Bill'};

let anythingVariable: any = 25;
anythingVariable = 'Hey';

var arrayOne: boolean[] = [true,false,true,true];
var arrayTwo: (number| string | boolean)[] = [1,'abc',true, 2];

myObj = {x:5, y:10};

class MyNode {
    val: number
    constructor(val: number){
        this.val = val;
    }
    _priv: number
    doSomething(){
        this._priv = 10;
    }
}
let myNodeInstance = new MyNode(1);
console.log(myNodeInstance.val);

function myFunction(val: string): void {
    console.log(val);
    return;
}

function sendingErrors(message: string): never{
	throw new Error('Error message');
}