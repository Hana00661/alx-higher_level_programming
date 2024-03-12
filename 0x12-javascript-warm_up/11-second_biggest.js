#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  const tab = [];
  for (let i = 2; i < process.argv.length; i++) {
    tab.push(parseInt(process.argv[i]));
  }
  tab.sort();
  console.log(tab[tab.length - 2]);
}
