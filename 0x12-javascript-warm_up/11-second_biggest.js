#!/usr/bin/node
const argv = process.argv;
if (argv.length === 2 || argv.length === 3) {
  console.log(0);
} else {
  let biggest = parseInt(argv[3]);
  let second = parseInt(argv[2]);
  if (biggest < second) {
    second = biggest;
    biggest = parseInt(argv[2]);
  }

  for (let i = 4; i < argv.length; i++) {
    const num = parseInt(argv[i]);
    if (num > biggest) {
      second = biggest;
      biggest = num;
    } else if (num > second && num !== biggest) {
      second = num;
    }
  }
  console.log(second);
}
