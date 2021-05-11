# cognetiks

### Get started
- Install Python3.9
- Clone this repository
- Create a .env file (use `.env.example` as guide)

- Create and activate virtualenv
```bash
virtualenv env --python=python3.9
source env/bin/activate #unix only
```
- Install the dependencies
```bash
pip install -r requirements.txt
```

- Format the code after changes to maintain style
```bash
black $(find . -name '*.py')
```

- Run the test suite
```bash
pytest -ssv
```