#!/usr/bin/node

const axios = require('axios');
axios.get(process.argv[2])
  .then(res => {
    let num = 0;
    const numFilms = res.data.results.length;
    for (let i = 0; i < numFilms; i++) {
      const numChar = res.data.results[i].characters.length;
      for (let j = 0; j < numChar; j++) {
        const str = res.data.results[i].characters[j];
        if (str.includes('18')) {
          num++;
        }
      }
    } console.log(num);
  })
  .catch(err => {
    console.log(err);
  });
