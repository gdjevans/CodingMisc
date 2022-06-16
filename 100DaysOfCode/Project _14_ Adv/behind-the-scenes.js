const hobbies = ['Sports', 'Cooking']; // a pointer is stored in memory.
const age = 32; // the value itself is stored

hobbies.push('Reading'); // the address of the array doesn't change

// hobbies = ['Coding', 'Sleeping']; // not allowed!

console.log(hobbies);

//Primative values: numbers, strings, booleans and more (undefined)
//Reference value: Objects

const person = {age: 32};

function getAdultYears(p) {
    p.age -= 18;
    return p.age; 
}

console.log(getAdultYears(...person));
console.log(person);