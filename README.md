# Chroma - Python Code Samples
Chroma is the AI-native open-source vector database.


## Running Chroma in docker

### Setup Chroma in docker
```bash
docker compose up -d
```

Check with chroma is running

1. Check api heartbeat: Go to browser with url http://localhost:8000/api/v1
![Heartbeat](https://github.com/stefchui/ChromaSample/blob/main/images/heartbeat%20check.png?raw=true)
2. Check first setup collection content: Go to browser with url http://localhost:8000/api/v1/collections
![Collections](https://github.com/stefchui/ChromaSample/blob/main/images/first%20setup%20check.png?raw=true)


## Runing python codes with Chroma Server

### Step 1: Install external packages / libraries
```bash
pip install -r .\requirements.txt
```
### Step 2: Import sample data into chroma server
```bash
python .\demo\ChromaDbServerDataPreparation.py
```
Check after data import: Go to browser with url http://localhost:8000/api/v1/collections
![NewDataCollections](https://github.com/stefchui/ChromaSample/blob/main/images/data%20insertion%20check.png?raw=true)
### Step 3: Running query in Client Mode
```bash
python .\demo\ChromaDbServerClientQuerySample.py
```
Result when query completed
![Result](https://github.com/stefchui/ChromaSample/blob/main/images/final%20result.png?raw=true)

