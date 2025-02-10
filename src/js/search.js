// search.js

function openDropdown(ctl){
  ctl.classList.remove('is-hidden')
}

function closeDropdown(ctl){
  ctl.classList.add('is-hidden')
  
}

// Function to initialize the dropdown functionality
function initializeDropdown() {
  debugger;
  const searchBox = document.getElementById('search-box');
  const dropdownContainer = document.getElementById('dropdown-container');
  const dropdownContent = document.getElementById('dropdown-content');
  const closeIcon = document.getElementById('close-results');

  // Open dropdown when the user types or pastes content
  searchBox.addEventListener('input', () => openDropdown(dropdownContainer));
  searchBox.addEventListener('focus', () => openDropdown(dropdownContainer));

    
  // Add 'is-scrollable' class for vertical scroll in the dropdown
  dropdownContent.classList.add('is-scrollable');

  // Close dropdown when the close button is clicked
  closeIcon.addEventListener('click', () => closeDropdown(dropdownContainer));
  // Close dropdown when clicking outside of the dropdown
  document.addEventListener('click', (e) => {
    //if (!dropdownContainer.contains(e.target) && e.target !== searchBox) dropdownContent.classList.remove('is-active');
    if (!dropdownContainer.contains(e.target) && e.target !== searchBox) closeDropdown(dropdownContainer);
  });

  // Prevent closing the dropdown when clicking inside
  dropdownContent.addEventListener('click', e => e.stopPropagation());
}

// Expose the initializeDropdown function for external calls
window.initializeDropdown = initializeDropdown;
