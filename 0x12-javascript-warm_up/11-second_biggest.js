#!/usr/bin/node
const argv = process.argv;
if (argv.length === 2 || argv.length === 3) {
  console.log(0);
} else {
  let biggest = parseInt(argv[3]);
  let second = parseInt(argv[2]);
  if (biggest < second) {
    const temp = second;
    second = biggest;
    biggest = temp;
  }

  for (let i = 4; i < argv.length; i++) {
    let num = parseInt(argv[i]);
    if (num > biggest) {
      let temp2 = biggest;
      biggest = num;
      second = temp2;
    } else if (num > second && num !== biggest) {
      second = num;
    }
  }
  console.log(second);
}
