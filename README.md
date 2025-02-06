# orange-heart-image-addressing
Exploring various forms of addressing (real world and web based) for an orange heart stencilled image using Web 1 and DWeb technologies. 

## Github Actions for the current repo 

Checking into dita branch runs the following jobs: 
  - Generate html5 with latest DITA Open Toolkit, commits the out folder to the dita branch
  - Switch to dev branch and run a Python job to prep the HTML, copy over prepped HTML to the src folder and commit to dev


## Python HTML Cleanup
Uses Beautiful Soup to add custom CSS classes
[python](https://github.com/yetessam/orange-heart-image-addressing/blob/dev/python/modify_files.py)

