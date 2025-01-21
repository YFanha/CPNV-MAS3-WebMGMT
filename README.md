# CPNV-MAS3-WebMGMT
# Requirements
- Python=>3.9.5
- Flask=>3.1.0

# Usage

## Docker
Update the ```data.json``` source file with your ```terraform.tfvars.json``` file.
```docker
docker-compose up -d
```
## Host
### pipenv
```PowerShell
pip install pipenv
cd src
pipenv install

python3 run.py
```
