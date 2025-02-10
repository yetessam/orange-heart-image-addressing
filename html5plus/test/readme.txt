


1  Check environment 

a Verify that loguru is installed: 

pip show loguru 

b  Make sure tests can get to the html5plus objects

python -m html5plus.test.test_import


Run in a terminal: 
python -m unittest test_nav_plugin.py

Run all: 

python -m unittest discover test
