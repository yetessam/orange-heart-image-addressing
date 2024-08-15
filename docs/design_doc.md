# Orange Heart Project

## Content Addressing Design Document

### Overview

**Project Name:** Orange Heart Image Addressing

**Purpose:** Themewise, I’m using an orange heart to explore and present different forms of addressing (physical and digital). As a proof of concept, I want to easily use and incorporate various Web 3 technologies into this exercise.

**Target Audience:** Art enthusiasts, information architects, people interested in web technologies.

## Description

Content addressing interests me. Moving from art that's got a physical location such as a street corner or an address to the digital addressing for digital representations of an orange heart whose original stencils get reused over and over again. I'd like to do a piece of work that looks at this one image and then its different forms of addressing, whether the art is moving through the postal service using mailing addresses, intersection, local landmark, or online hosting with Web 3 providers such as Fleek using IPFS.

## Website Content Structure

### Overall Structure
- Home
- Orange Heart
- Gallery Page
  - 1 to n subpages
- Captain's Log

### Website Content Diagram
- **Home**
- **Orange Heart**
  - Describe the significance of the orange heart. Comfort, care, and serenity. The orange heart emoticon is also commonly used to show love, admiration, and support. Emergency orange esp with regard to the continuing situation in Gaza, support for Truth and Reconciliation around Indigenous Residential School survivors in Canada.
- **Gallery Page**
  - Links to 3-5 HTML pages that have similar but different photos of orange hearts with titles and descriptions for each. Assuming here that we should be using a separate page is simpler. That might be an incorrect assumption.
  - Include examples of physical addressing, hearts that exist on streets or on landmarks. Street art has ambient findability and immediacy.
- **Captain’s Log**
  - Blog about the process and document decision.

## Technical Description

### Building Blocks

#### Images

Selected PNG.  

See the optimal-device-dimensions.csv for optimal image dimensions for varying devices. 
Consider automating image generation so that we can switch to SVG easily. 
Consider using DITA keys from day one for image addressing so that if we switch to SVG from PNG, its super easy.


#### Technologies
- HTML5, CSS3, JavaScript, Knowledge Graphs support (RDF? RDFa for embedding RDF, Property Graph databases?)

#### Hosting
- Fleek https://fleek.co/ and deployment strategy. See https://docs.fleek.co/

#### IPFS Gateway
- Use https://ipfs.io/ipfs which results in the following sample URL
  - https://ipfs.io/ipfs/QmExampleCID

#### Github Source
- https://github.com/yetessam/orange-heart-image-addressing

### SEO
- Implement SEO best practices for better search engine visibility (consider dropping out of scope?).

### Linked Data/Knowledge Graphs
- At this point, I’m still not sure whether I want to get into Linked Data. And if so, do I just create RDF XML files which are easy (for me) to create or Property-based knowledge graph.
- RDF Schema: Define RDF for the orange heart images, including creator, location, digital address.
- Property KGs: Create property knowledge graphs to illustrate relationships between physical and digital addresses.

### Responsive CSS
- Link in an existing grid layout CSS: https://bulma.io/
- Responsive
- Uses CSS variable, Flexbox and Grid
- Uses media queries for responsive design across devices

### Accessibility
- Accessibility: Ensure all my HTML pages are accessible. Use tags like `<menu>`, `<nav>`, `<form>`, and `<main>` that don’t need not use ARIA landmarks, as their purpose is already established with their names. Review that the content has enough metadata and includes ARIA roles and labels where necessary.  
- Bulma uses a lot of divs, that's one concern 


### DWeb Tech to Investigate, Consider Out of Scope
- Nextcloud which is decentralized Google Drive

###  Source Content
- Using DITA XML for source
