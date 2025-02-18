# CapStone-Project
## Abstract
This project is a part of Capstone project in Automation Engineering. That has a Goal that to create Automation Gen AI for answer question about subject and knowledge of Automation in KMITL.
## Diagram


## Backend information
#### API endpoint
```
# Document

# Inference

# Dashboard
```
#### Server port
```
# API port
```


## Frontend information
#### Endpoints
```
# Dashboard

# Showcase
```


## Download repository
1. Install git bash [Click me](https://git-scm.com/downloads)
2. Git clone repository
```
git clone https://github.com/santapong/CapStone-Project.git
```
## Setup Backend
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

2. Check uv us exist
```
uv --version
# uv x.x.x >> example [ uv 5.3.0 ]
```

3. Sync dependecy from project.toml in this project

```
cd path/to/this/project
uv sync --no-group dev
```

PS. uv  document if get error >>> [Click me](https://docs.astral.sh/uv/getting-started/installation/)

## Install OLLAMA
1. Download and install ollama Click [Here](https://ollama.com/download/windows) !!

2. Pull embedding model from ollama 
``` 
ollama pull bge-m3
```

checking model

```
ollama list

# NAME             ID              SIZE      MODIFIED     
# bge-m3:latest    790764642607    1.2 GB    XXX ago  
```

## Setup Frontend
1. You need node.js to use ```npm``` Install >> [Node.js](https://nodejs.org/en)

2. Get to frontend directory
```
cd project-repository/capstone/frontend
```

3. Install dependencies
```
npm install
```

4. Launch frontend server.
```
npm run dev
```

## .env setup
```

#-------------------- Python ENV --------------------#
# Setup python PATH
PYTHONPATH='project/path'

# User Agent for Webbase. ( Using for Webbaseloadder )
USER_AGENT='myagent'

# Logging config
LOG_PATH='capstone/backend/logs/logs.log'
LOG_NAME=''
LOG_FORMAT='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_LEVEL='INFO'

# Database login
# DATABASE_USERNAME=
# DATABASE_PASSWORD=
# DATABASE_PORT=
# DATABASE_NAME=
# DATABASE_URL=

# Database adjustment
DATABASE_CREATE=True

# Vector Database
EMBEDDING_MODEL="bge-m3"
PERSIST_DIR='database/vector_database'

# LangSmith
LANGSMITH_TRACING="true"
LANGSMITH_API_KEY="langsmith-api-key"

# LLM Model
LLM_MODEL='typhoon-model'
MODEL_BASE_URL='https://api.opentyphoon.ai/v1'
# LLM_MODEL=''

# TYPHOON API
TYPHOON_API_KEY="typhoon-api-key"

#---------------- VITE ENV ----------------#
# Dashboard Defualt
VITE_API_URL=''

# Frontend database (Only Query)
PRISMA_DATABASE_URL=''
```
## Reference
Thank you for LLM API.  [Typhoon AI](https://opentyphoon.ai/)
Thank you for Prompt and RAG knowledge. [Prompt Engineer Guide](https://www.promptingguide.ai/introduction/settings)