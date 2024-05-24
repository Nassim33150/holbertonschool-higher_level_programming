document.addEventListener('DOMContentLoaded', () => {
  const listMovies = document.querySelector('#list_movies');

  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
      const films = data.results;
      films.forEach(film => {
        const listItem = document.createElement('li');
        listItem.textContent = film.title;
