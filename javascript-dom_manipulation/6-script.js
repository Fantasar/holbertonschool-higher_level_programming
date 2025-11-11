document.addEventListener('DOMContentLoaded', function () {
  fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => response.json())
    .then(data => {
      console.log(data.name);
      document.getElementById('character').innerText = data.name;
    })
    .catch(error => console.error('Erreur:', error));
});
