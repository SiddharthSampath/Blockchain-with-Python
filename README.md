**Creating and activating a virtual env**
```
python -m venv blockchain-env
source blockchain-env/Scripts/activate
```

**Installing requirements**
```
pip3 install -r requirements.txt
```

**Running tests with pytest**

Activate the virtual environment

```
python -m pytest backend/tests
```