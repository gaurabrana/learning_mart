// script.js — dark mode using Bootstrap's color modes (data-bs-theme on <html>), persisted.

document.addEventListener('DOMContentLoaded', () => {
  const root  = document.documentElement;
  const saved = localStorage.getItem('theme') || 'light';
  root.setAttribute('data-bs-theme', saved);

  const toggle = document.getElementById('darkModeToggle');
  toggle?.addEventListener('click', () => {
    const next = root.getAttribute('data-bs-theme') === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-bs-theme', next);
    localStorage.setItem('theme', next);
  });
});
