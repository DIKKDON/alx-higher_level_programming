#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${movieId}/`, (err, res, body) => {
  if (err) console.log(err);

  const movie = JSON.parse(body);
  for (const url of movie.characters) {
    request(url, (err, res, body) => {
      if (err) console.log(err);

      const character = JSON.parse(body);
      console.log(character.name);
    });
  }
});
