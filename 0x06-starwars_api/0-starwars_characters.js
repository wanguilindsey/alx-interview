#!/usr/bin/node

// Import 'request' library
const request = require('request');

// Star Wars API base URL
const API_URL = 'https://swapi-api.alx-tools.com/api';

// Check if a film ID is provided
if (process.argv.length > 2) {
  // Request film data by film ID
  request(`${API_URL}/films/${process.argv[2]}/`, (err, _, body) => {
    // Log error if request fails
    if (err) {
      console.log(err);
    }
    // Extract character URLs from film data
    const charactersURL = JSON.parse(body).characters;

    // Fetch character names from their URLs
    const charactersName = charactersURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseErr, __, charactersReqBody) => {
          if (promiseErr) {
            reject(promiseErr);
          }
          // Resolve with character name
          resolve(JSON.parse(charactersReqBody).name);
        });
      }));

    // Log all character names
    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}
