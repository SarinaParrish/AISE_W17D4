# REPRO

## Setup

python3 -m venv .venv  
source .venv/bin/activate  

pip install numpy==1.26.4  
pip install torch==2.2.2 torchvision==0.17.2 --index-url https://download.pytorch.org/whl/cpu  
pip install transformers==4.41.2 pillow accelerate  

## Run

python main.py

## Notes

- First run downloads model (~300MB)
- Requires Python 3.11