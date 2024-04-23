#!/usr/bin/node
const axios = require('axios');
axios.get(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`)
  .then(res => {
    for (let i = 0; i < res.data.characters.length; i++) {
      axios.get(res.data.characters[i])
        .then(res => {
          console.log(res.data.name);
        });
    }
  })
  .catch(err => {
    console.log(err);
  });
