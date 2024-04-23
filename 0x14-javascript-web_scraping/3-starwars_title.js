#!/usr/bin/node

const axios = require('axios');
axios.get(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`)
  .then(res => {
    console.log(res.data.title);
  })
  .catch(err => {
    console.log(err);
  });
