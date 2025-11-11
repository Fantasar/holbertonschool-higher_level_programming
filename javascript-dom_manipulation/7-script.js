document.addEventListener('DOMContentLoaded', function () {
  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
      console.log(data.results);
      const listMovies = document.getElementById('listMovies');
      data.results.forEach(movie => {
        const li = document.createElement('li');
        li.innerText = movie.title;
        listMovies.appendChild(li);
      });
    })
    .catch(error => console.error('Erreur:', error));
});
