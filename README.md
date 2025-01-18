# CapStone-Project
### Note
1. Can answer with Image, Vedio and link to learn more.
2. Have genre to search.
3. Have summery Dashboard. ( Only Deverloper )

## Abstract
This project is a part of Capstone project in Automation Engineering. That has a Goal that to create Automation Gen AI for answer question about subject and knowledge of Automation in KMITL.
## Diagram

## Backend using Python

## Frontend using Javascript React + Vite

## Setup Project
### Download Project repository
1. Install git bash [Click me](https://git-scm.com/downloads)
2. Git clone repository
```
git clone https://github.com/santapong/CapStone-Project.git
```

### Install Python
1. Install Python [Click me](https://www.python.org/downloads/)
2. Add Python.exe to Environment path. (only Windows) 

### Install uv

1. Installing uv

#### For Window
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### For Linux/MacOs
via curl
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```
via wget
```
wget -qO- https://astral.sh/uv/install.sh | sh
```

#### Install on python

```
pip install uv 
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
PS. uv's document [Click me](https://docs.astral.sh/uv/getting-started/installation/)

## OLLAMA download
1. Download and install ollama Click [Here](https://ollama.com/download/windows) !!

2. Open Terminal or Command prompt and type ``` ollama run llama3.2 ``` ( We use llama3.2 in this Project )

## Oauth2-proxy setup ( Docker )
Document [Read more !!](https://oauth2-proxy.github.io/oauth2-proxy/)

## Datasets
Coming Soon

## Docker

## Kubernetes

## Other

## Reference
[Prompt Engineer Guide](https://www.promptingguide.ai/introduction/settings)