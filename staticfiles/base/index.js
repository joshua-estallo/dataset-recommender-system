// NAVIGATION BAR - SEARCH INPUT
document.addEventListener('DOMContentLoaded', function() {
  var searchInput = document.getElementById('searchInput');

  searchInput.addEventListener('focus', function() {
      this.removeAttribute('placeholder');
  });

  searchInput.addEventListener('blur', function() {
      this.setAttribute('placeholder', 'Search a dataset...');
  });
});

