# L2A

Monorepo for APSC 258

## Auto Setup 🤖

Install python 3
`winget install python3 -v 3.9.6150.0`

Install git
`winget install git.git`

Clone repository
`git clone https://github.com/AndreCox/L2A.git`

Open repository
`cd L2A`

Run setup
`python setup.py`

## Manual Setup ⚙️

Install python 3
`winget install Python3 -v 3.9.6150.0`

Install git
`winget install git.git`

Clone repository
`git clone https://github.com/AndreCox/L2A.git`

Open repository
`cd L2A`

Install dependencies
`pip install -r requirements.txt`

Install the dev requirements
`pip install -r requirements-dev.txt`

Add the hooks to your pre-commit
`pre-commit install`

## Testing Code 🧪

`pytest -v`

## Running Code 🚀

`python3 main.py`
