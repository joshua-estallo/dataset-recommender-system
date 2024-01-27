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

// CITATION POP-UP
const openModalButtons = document.querySelectorAll("[data-modal-target]")
const closeModalButtons = document.querySelectorAll("[data-close-button]")
const overlay = document.getElementById("overlay")

openModalButtons.forEach(button => {
  button.addEventListener("click", () => {
    const modal = document.querySelector(button.dataset.modalTarget)
    openModal(modal)
  })
})

closeModalButtons.forEach(button => {
  button.addEventListener("click", () => {
    const modal = button.closest(".modal")
    closeModal(modal)
  })
})

overlay.addEventListener("click", () => {
  const modals = document.querySelectorAll(".modal.active")
  modals.forEach(modal => {
    closeModal(modal)
  })
})
function openModal(modal) {
  if (modal == null) return
  modal.classList.add("active")
  overlay.classList.add("active")
}

function closeModal(modal) {
  modal.classList.remove("active")
  overlay.classList.remove("active")
}



// copy citation
const copyCite = document.getElementById('copyCite');
  const citeBodyText = document.querySelector('.cite-body').innerText;

  copyCite.addEventListener('click', () => {
    navigator.clipboard.writeText(citeBodyText)
  });

// copy bibtex
const copyBibtex = document.getElementById('copyBibtex');
  const bibtexBodyText = document.querySelector('.bibtex-body').innerText;

  copyBibtex.addEventListener('click', () => {
    navigator.clipboard.writeText(bibtexBodyText)
  });