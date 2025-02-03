#Running from VS Code's Terminal

##Pre-requisites

###Update pip

```
pip install --upgrade pip
```

### Use Python 3.12 version or greater.
```
python --version
```
### Install dependencies and activate environment

```
	python -m venv venv
        source venv/bin/activate
        pip install -r python/requirements.txt

```
### Use HTML5 output

Make sure you have an output folder to process.
If you don't already have DITA OT html5 output, go to the Github Actions tab and download a out-html5-archive artifact and unzip it.

For example, your out folder might be /Users/yas/Downloads/out

Check the contents of your out folder
```
	ls -la /Users/yas/Downloads/out

```

It should contain css an index.html as well as css, images and topics folders.

### Prepare the src folder



Empty out existing src folder
```
        rm -rf src/*

```

If there's no src folder, create an empty one.

```
        mkdir -p ./src
```
          
### Run the main script 
    
```
python python/main_script.py --out_dir /Users/yas/Downloads/out --src_dir ./src --res_dir ./python/resources
```
