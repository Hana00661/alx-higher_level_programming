#!/usr/bin/node

function factoriel (a) {
  if (isNaN(a) || a === 0) {
    return 1;
  } else {
    return a * factoriel(a - 1);
  }
}
console.log(factoriel(process.argv[2]));
