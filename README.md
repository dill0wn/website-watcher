# Watch Dom Elements #

A little project that periodically fetches a site and does a text comparison against a css selector on the site.


## Running ##

Activate the py3 env:
```
# for macos
source env/bin/activate
```

Install Dependencies/Prerequisites:
```
pip install -r requirements.text
```


Run the script:
```
python ....
```

## Developing ##
Make sure to `pip install pip-tools`. If adding/modifying a dependency, modify the requirements.in and run: 
```
# update the locked,hashed versions
pip-compile --generate-hashes

# install precise versions
pip install -r requirements.text
```
