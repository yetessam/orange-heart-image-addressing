Running from VS Code/Terminal

Pre-requisites

Python 3.12 version or greater.


Install dependencies

python -m venv venv
          source venv/bin/activate
          pip install -r python/requirements.txt


Create src folder if it doesn't exist (to do - maybe Python should do this)
          mkdir -p ./src
          
Activate the environment and then run the main script 
    source venv/bin/activate
    python python/main_script.py --out_dir $(pwd)/out --src_dir $(pwd)/src --res_dir $(pwd)/python/resources
