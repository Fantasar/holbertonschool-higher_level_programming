#!/usr/bin/node
const args = process.argv.slice(2).map(Number);

if (args.length < 2) {
  console.log(0);
} else {
  const max = Math.max(...args);
  let secondMax = Number.NEGATIVE_INFINITY;

  for (const n of args) {
    if (n !== max && n > secondMax) {
      secondMax = n;
    }
  }
  console.log(secondMax);
}
