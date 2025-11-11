document.addEventListener('DOMContentLoaded', function () {
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())
    .then(data => {
      console.log(data.hello);
      document.getElementById('hello').innerText = data.hello;
    })
    .catch(error => console.error('Erreur:', error));
});
