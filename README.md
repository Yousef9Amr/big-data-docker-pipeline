# Big Data Assignment1 - Docker Pipeline

## Project Overview
This project creates a Docker-based pipeline for processing and analyzing a dataset with Python functions scripts.

## Directory Structure
bd-a1/ ├── Dockerfile ├── train_titanic.csv ├── load.py ├── dpre.py ├── eda.py ├── vis.py ├── model.py ├── service-result/


## Instructions

### Step 1: Build Docker Image
```bash
docker build -t bd-a1-image .

### Step 2: Run Docker Container
docker run -it --name bd-a1-container bd-a1-image

### Step 3: Copy Files into the Container
docker cp train_titanic.csv bd-a1-container:/home/doc-bd-a1/
docker cp load.py bd-a1-container:/home/doc-bd-a1/
docker cp dpre.py bd-a1-container:/home/doc-bd-a1/
docker cp eda.py bd-a1-container:/home/doc-bd-a1/
docker cp vis.py bd-a1-container:/home/doc-bd-a1/
docker cp model.py bd-a1-container:/home/doc-bd-a1/

### Step 4: Run Scripts Inside the Container
python3 /home/doc-bd-a1/load.py /home/doc-bd-a1/train_titanic.csv
python3 /home/doc-bd-a1/dpre.py
python3 /home/doc-bd-a1/eda.py
python3 /home/doc-bd-a1/vis.py
python3 /home/doc-bd-a1/model.py

### Step 5: Copy Output Files to Local Machine
docker cp bd-a1-container:/home/doc-bd-a1/res_dpre.csv ./service-result/
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-1.txt ./service-result/
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-2.txt ./service-result/
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-3.txt ./service-result/
docker cp bd-a1-container:/home/doc-bd-a1/vis.png ./service-result/
docker cp bd-a1-container:/home/doc-bd-a1/k.txt ./service-result/

### Step 6: Stop the Container
docker stop bd-a1-container
