#!/usr/bin/node

function add (a, b) {
  return a + b;
}
const num = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);
console.log(add(num, num2));
