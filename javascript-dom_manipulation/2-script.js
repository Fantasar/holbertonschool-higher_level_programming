#!/usr/bin/node
const newclass = document.getElementById('red_header');
const header = document.querySelector('header');
newclass.addEventListener('click', () => {
  header.classList.add('red');
});
