## Regex Tests
This repository contains the following tests to validate regex patterns inside classifier.json file:
1. Json formatting;
2. Regex compiling;
3. Unescaped chars in regexes;
4. Regexes that can classify an unclassifiable text.

### Requirements
- Git
- Python

### Execution
- Clone the project in desired path:  
`git clone https://github.com/lorenapnmarcon/regex-tests.git`
- Install a virtual environment:  
`python -m venv env`
- Activate your venv:   
`env\Scripts\activate.bat` (Windows)  
`source env/bin/activate` (MacOS)
- Install dependencies  
`pip install -r requirements.txt`
- Alter [classifier.json](classifier.json) file and run tests  
`pytest test.py`
- Deactivate your venv  
`deactivate`

### Authors
- [**Lorena Marçon**](https://github.com/lorenapnmarcon)