## Getting Started

**Running the template**

Create a new virtualenv and install deps

```
pip install -r requirements.txt 
```

Create new directory for model

```
mkdir models
```

Download and save model from TF Hub

```
python scripts/download.py
```

Create a .env file with the following ENV vars

```
REST_API_PORT=8501
MODEL_NAME="REPLACE_WITH_MODEL_NAME"
MODEL_BASE_PATH="REPLACE_WITH_MODEL_PATH"
```

Start Nginx and TFServing containers with

```
docker-compose up
```

You can retrieve the models metadata by visiting 

```
localhost:8080/v1/models/REPLACE_WITH_MODEL_NAME/metadata
```
