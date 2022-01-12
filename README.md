# L2A

Monorepo for APSC 258. This repo includes a setup.py script that will automaticaly install the required dependencies and configure pre install scripts.

### Components
1. ⬆️ pre-commit hooks - automaticaly lint and format code before push.
2. 🧪 pytest - runs the tests located in test folder to check functionality.
3. 🤖 workflows - on push to main branch runs code testing in cloud to check validity before we merge.
4. 📦 dependabot - scan code daily for out of date modules.
5. 📑 black - code formatter; makes sure all of our code is homogenous.
6. 🔬 flake8 - code linter; scans our code for formatting errors before we end up with problems later.

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
