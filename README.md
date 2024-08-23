# Chroma - Python Code Samples
Chroma is the AI-native open-source vector database.


## Running Chroma in docker

### Step 1: Setup chroma into docker
```bash
docker compose up -d
```

### Step 2: Import sample data into chroma server
```bash
python .\demo\ChromaDbServerDataPreparation.py
```


### Step 3: Running query in Client Mode
```bash
python .\demo\ChromaDbServerClientQuerySample.py
```



