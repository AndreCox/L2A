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

Optionally test for gpu support

## GPU Support 🖥️

You may have an issue relating to CUDA if you checked for GPU support in the last step.
To fix this you have to install the [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads?target_os=windows&target_arch=x86_64&target_version=11&target_type=exe_network)

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
