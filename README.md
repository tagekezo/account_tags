## Instructions

#### Create virtual environment
```
python3 -m venv venv
```

#### Activate virtual environment
```
source venv/bin/activate
```

#### Install requirements
```
pip install -r requirements.txt
```

#### update aws access key id and secret access key (Org management account required)
```
client = boto3.client('organizations',aws_access_key_id='your_access_key_id',aws_secret_access_key='your_secret_access_key')
```

#### Run script
```
python main.py
```

Results are returned in account_tags.csv

Example
```
id,key,value
45019839422,env,dev
459189739432,type,spoke
869647985359,env,dev
849677982359,type,hub
514692819321,env,dev
413692849321,type,spoke
```
