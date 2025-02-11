// Import Algolia search library and InstantSearch.js library
import algoliasearch from 'https://cdn.jsdelivr.net/npm/algoliasearch@4.10.3/dist/algoliasearch.umd.min.js';
import instantsearch from 'https://cdnjs.cloudflare.com/ajax/libs/instantsearch.js/4.75.5/instantsearch.production.min.js';

// Algolia App ID, Search Key, and Index Name
const ALGOLIA_APP_ID = '905371AINN';
const ALGOLIA_SEARCH_KEY = '556c7871a4d6b955893e20a4ab1b3c4e';
const ALGOLIA_INDEX_NAME = 'oh_c_pages';

// Initialize the Algolia search client
const searchClient = algoliasearch(ALGOLIA_APP_ID, ALGOLIA_SEARCH_KEY);

// Initialize InstantSearch.js with the search client
const search = instantsearch({
  searchClient: searchClient, // Providing the search client
  indexName: ALGOLIA_INDEX_NAME,
  routing: true, // Optional: Enables URL-based routing for search queries
});

// SearchBox widget for capturing user input
search.addWidget(
  instantsearch.widgets.searchBox({
    container: '#search-box', // This links to the search-box div in your HTML
    placeholder: 'Search...', // Customizable placeholder text
    showReset: true, // Optional: Show a reset button to clear the query
    showSubmit: true,
   
    cssClasses: {
      input: 'input is-rounded is-inline', // Use Bulma's input class
      reset: 'icon is-medium is-inline', // Use Bulma's reset icon class
      submit: 'icon is-medium is-inline', // Use Bulma's submit icon class
      
    },

    // Using onInput to check for empty queries
    onInput(event) {
      const query = event.target.value.trim(); // Get trimmed input value

      // Check if the query is non-empty before triggering the search
      if (query.length > 0) {
        // Set the query in the search helper and trigger search
        search.helper.setQuery(query).search();
      }
    }  // onInput

  })
);


// Hits widget for displaying search results
search.addWidget(
  instantsearch.widgets.hits({
    container: '#hits',
    templates: {
      empty: 'No results found',
      
      item(hit, { html, components }) {
   
        // Check if the depth attribute is greater than 1
        // Only because we don't want to include the forwarding page in the search results
          const highlightedTitle = components.Highlight({ hit, attribute: 'title' });
          const highlightedDescription = components.Highlight({ hit, attribute: 'description' });
          return html`
              <a href="${hit.url}" target="_blank">
                  <strong>${highlightedTitle}</strong>
              </a>
              <p>${highlightedDescription}</p> 
             
          `;
          
      }
    },
  })
);

// Start the search instance
function startSearch() {
  search.start();
}

// Expose the startSearch function so that it can be called from the main page
window.startSearch = startSearch;

// Function to open the dropdown
function openDropdown(ctl){
  ctl.classList.remove('is-hidden')
}

// Function to close the dropdown
function closeDropdown(ctl){
  ctl.classList.add('is-hidden')
  
}

// Function to initialize the dropdown functionality
function initializeDropdown() {

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

// Initialize components once the DOM is ready
document.addEventListener('DOMContentLoaded', function() {
  // Initialize dropdown from search.js
  initializeDropdown();

