# L2A

Monorepo for APSC 258

## Setup

Install python 3
`winget install Python3`

Install git
`winget install git`

Clone repository
`git clone https://github.com/AndreCox/L2A.git`

Open repository
`cd L2A`

Install dependencies
`pip install -r requirements.txt`
If you are doing development install the dev_requirements
`pip install -r dev_requirements.txt`

If you have just installed you can check if everything is working properly (you need to install dev requirements first)
`pytest -v`

## Running Code
`python3 main.py`
