@ -1,93 +0,0 @@
# Orange Heart Content Addressing Design Document

## Overview

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
- Find and simply link in an existing grid layout CSS.
- Responsiveness: Utilize CSS Grid for layout structure and uses Implement media queries for responsive design across devices.
- Accessibility: Ensure all my HTML pages are accessible. Use tags like `<menu>`, `<nav>`, `<form>`, and `<main>` that don’t need not use ARIA landmarks, as their purpose is already established with their names. Review that the content has enough metadata and includes ARIA roles and labels where necessary.

## Captain's Log

### TBD 

🔲 Seek out a volunteer where we are putting in hearts to intentionally hide  identifying metadata. 
🔲 Upload 3 orange heart images to IPFS and get the CIDs
🔲 Insert references in ipfs.html file to use those IPFS URLs
🔲 Test updated HTML locally to ensure that the images load correctly from IPFS

### Friday June 20th, 2024

Prepping with Krylon matte transparent fixative on two 5 x 7 birchwood panels. Made in Canada. 



### Wed June 19th, 2024

Create mockups for physical layout for gallery wall space.    Took first draft photographs of the art pieces and then loaded them into a new Miro board to create a 2D diagram of the physical gallery space.   Scaling the images down to onto the Miro grid to result in a maximum wall width of 3 feet.  Will need to pad everything by several inches to accommodate frames. 

Design branch on Git holds the current set of draft images.   

### Tuesday June 18th, 2024
Updates to design doc. 

### Monday June 17th, 2024

Today’s decisions: start with Fleek, don’t recreate the wheel when it comes to CSS, and start with RDF/xml. Stick some images into IPFS and then sign up for Fleek as my IPFS Gateway. Should I use RDF vs Property DBs? Asked Chat GPT for a series of options for hosting. Fleek is Web 3 friendly and I can also store my content on Github and publish that way, which opens up the content to multiple contributors.

✅ Created a Github Repo https://github.com/yetessam/orange-heart-image-addressing
