# Captain's Log


## Tuesday June 25th, 2024


## Monday June 24th, 2024

Directed the contents of the DITA OT logs to the Summary box in Github Actions.
Testing with DITA properites and trying to get the CSS auto-applied to the external CDN. 

## Sunday June 23rd

Github Actions and priming and testing 5x5s.

## Sat June 22, 2024

I've been getting these wooden birchwood boxes to do real-life art.   Having to prime them and pull together supplies.

I've done a few prototypes which didn't work out and then I primed again.  Currently, still concerned that the Krylon matte fixative makes inks bleed including the Sharpie black oil ink.     Went back to 'regular' Sharpie and still need to test the fixative.   Finished the background for the 16 x 20 piece.

Working on Github to source the content in DITA XML so that we can leverage DITA's link management. 
Created a dita branch on Github that takes the XML files, pushes them through the HTML5 transform in the latest version of the DITA Open Toolkit and then checks in the content to the out folder.
 

Seems like its going to be more efficient to generate this HTML here. 

To do:  push the HTML5 to  a dev branch where I could have Beautiful Soup run through and make any other changes that are needed.  Then when that's done, move to staging and then move to prod. 


## Sunday June 16, 2024

Getting a Fleek account.  I chose to authenticate through Ethereum, specifically with Metamask.  Metamask gives you some contextual warning about being careful with Web 3 dapps.

Set up an initial deployment yetessam/orange-heart-image-addressing (branch: prod) and selected src as the Publish directory 
Published at 10:01 AM to https://delicate-glitter-6121.on.fleek.co/

Locally ran  python -m http.server 8000 so that we can verify that the markdown is loaded locally,  checked developer console and made adjustments until we had zero errors in the console.

Pushed changes to design branch.  Currently using javascript to load markdownas unformatted HTML, although I could also use the python code.  

Compare http://localhost:8000/index.html   


🧡🧡🧡🧡

## Friday June 15st, 2024

Prepped with Krylon matte transparent fixative on two 5 x 7 birchwood panels. Made in Canada. 

Selected a Bulma for a modern CSS framework

🧡🧡🧡🧡

## Wed June 13th, 2024

Create mockups for physical layout for gallery wall space.    Took first draft photographs of the art pieces and then loaded them into a new Miro board to create a 2D diagram of the physical gallery space.   Scaling the images down to onto the Miro grid to result in a maximum wall width of 3 feet.  Will need to pad everything by several inches to accommodate frames. 

Design branch on Git holds the current set of draft images.   

🧡🧡🧡🧡

## Tuesday June 12th, 2024
Updates to design doc. 

🧡🧡🧡🧡

## Monday June 11th, 2024

Today’s decisions: start with Fleek, don’t recreate the wheel when it comes to CSS, and start with RDF/xml. Stick some images into IPFS and then sign up for Fleek as my IPFS Gateway. Should I use RDF vs Property DBs? Asked Chat GPT for a series of options for hosting. Fleek is Web 3 friendly and I can also store my content on Github and publish that way, which opens up the content to multiple contributors.

✅ Created a Github Repo https://github.com/yetessam/orange-heart-image-addressing
