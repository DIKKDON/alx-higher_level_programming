#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${movieId}/`, async (err, res, body) => {
  if (err) console.log(err);

  const movie = JSON.parse(body);
  for (const url of movie.characters) {
    const myPromise = await new Promise((resolve, reject) => {
      request(url, (err, res, body) => {
        if (err) console.log(err);

        const character = JSON.parse(body);
        resolve(character.name);
      });
    });
    console.log(myPromise);
  }
});
