#!/usr/bin/node
/*  prints the number of movies where the character “Wedge Antilles” is present */

const request = require('request');

if (process.argv.length >= 3) {
  const filmApi = process.argv[2];
  let movieCount = 0;

  request(filmApi, (err, response, body) => {
    if (err == null) {
      body = JSON.parse(body);
      const results = body.results;

      for (const result in results) {
        const charactersApi = results[result].characters;

        for (const character in charactersApi) {
          if (charactersApi[character].search('18') > 0) {
            movieCount++;
            continue;
          }
        }
      }
      console.log(movieCount);
    }
  });
}
