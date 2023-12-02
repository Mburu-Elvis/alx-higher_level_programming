#!/usr/bin/node
const argv = process.argv;
const num = parseInt(argv[2]);
function factorial (n) {
  let fact = 1;
  while (n > 0) {
    fact = fact * n;
    n--;
  }
  console.log(fact);
}
factorial(num);
