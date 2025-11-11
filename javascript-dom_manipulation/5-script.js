#!/usr/bin/node
document.addEventListener('DOMContentLoaded', function () {
  const addButton = document.getElementById('update_header');
  addButton.addEventListener('click', function () {
    document.querySelector('header').textContent = 'New Header!!!';
  });
});
