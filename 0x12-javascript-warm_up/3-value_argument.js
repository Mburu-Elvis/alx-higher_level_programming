#!/usr/bin/node
const argv = process.argv;
if (argv[2] === undefined) {
  console.log('No argument');
} else {
  let myStr = [];
  let k = 0;
  for (let i = 2; argv[i] !== undefined; i++) {
    myStr[k] = argv[i];
    k++;
  }
  myStr = myStr.join(' ');
  console.log(myStr);
}
