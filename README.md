# Background
This repository implements a flask app to compute the reverse complement of either
1. FASTA formated DNA sequence(s)
2. Raw DNA sequence

# Requirements
1. Docker installed (if not, instruction link here:)

# Instructions
1. Run
```
docker build . --tag <CONTAINER_NAME>
docker run -p 1234:1234 <CONTAINER_NAME>
```
2. Open up in a browser `localhost:1234`
