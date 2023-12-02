#!/usr/bin/node
const argv = process.argv;
let num = parseInt(argv[2]);
let fact = 1;
while (num > 0) {
  fact = fact * num;
  num--;
}
console.log(fact);
