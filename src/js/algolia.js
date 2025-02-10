// scripts/algolia.js

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
  debugger;
  search.start();
}

// Expose the startSearch function so that it can be called from the main page
window.startSearch = startSearch;
