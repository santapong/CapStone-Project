# CapStone-Project

## Abstract
This project is a part of Capstone project in Automation Engineering. That has a Goal that to create Automation Gen AI for answer question about subject and knowledge of Automation in KMITL.
## Diagram

![image](/imgs/Workflow.png)

## Setup Project
### Download Project repository
1. Install git bash [Click me](https://git-scm.com/downloads) !!
2. Git clone repository
```
git clone https://github.com/santapong/CapStone-Project.git
```

### Install Python
1. Install Python [Click me](https://www.python.org/downloads/) !!

### Install Nodejs
1. Install From [download here](https://nodejs.org/en) !!

### OLLAMA download
1. Download and install ollama [click Here](https://ollama.com/download/windows) !!

2. Open Terminal or Command prompt and type 
``` 
ollama pull bge-m3
``` 

### Config .env file
1. see [.envExample](https://github.com/santapong/CapStone-Project/blob/main/.envExample)
2. Require Parameter.
```
PYTHONPATH = "Your project directory"

LANGSMITH_API_KEY = "Your Langsmith API key"
TYPHOON_API_KEY = "Your Typhoon API key"
GOOGLE_CSE_ID = "GOOGLE Custom Search"
GOOGLE_API_KEY = "Google API Key"

```

LANGSMITH_API_KEY >> [Get Key](https://docs.smith.langchain.com/administration/how_to_guides/organization_management/create_account_api_key)
TYPHOON_API_KEY >> [Get Key](https://playground.opentyphoon.ai/api-key) 
GOOGLE_CSE_ID >> [Get Key](https://developers.google.com/custom-search/v1/introduction)
GOOGLE_API_KEY >> [Get Key](https://developers.google.com/maps/documentation/javascript/get-api-key#create-api-keys)

## For backend.

### Install uv

1. Installing uv

##### For Window
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

##### For Linux/MacOs
via curl
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```
via wget
```
wget -qO- https://astral.sh/uv/install.sh | sh
```

2. debug uv 

```
uv --version
# uv x.x.x >> example [ uv 5.3.0 ]
```

3. Sync dependecy from project.toml in this project

```
cd path/to/this/project
uv sync --no-group dev
```
PS. uv's document [click me](https://docs.astral.sh/uv/getting-started/installation/)

## For frontend.
1. go to frontend path
```
cd ../capstone/frontend
```

2. install package
```
npm install # If Error occur just run it again
```

3. run frontend server
```
npm run dev
```

## Error
1. Execution policy. ( Window )

```
# (Powershell) 
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser 
```

## Thank you
[Typhoon ai](https://opentyphoon.ai/)
[Prompt Engineer Guide](https://www.promptingguide.ai/introduction/settings)
[Langchain](https://python.langchain.com/docs/introduction/)