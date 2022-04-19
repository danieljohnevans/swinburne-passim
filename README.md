# swinburne-passim

### To run:

1. First navigate to desired directory, navigate to `/code/` and run `main.py` to generate `passim_in.json`

2. Navigate up and create schema with `json-df-schema passim_in.json > Passim.schema.orig`

3. Once data is in proper format run `Passim` with:
```
PARK_SUBMIT_ARGS='--master local[12] --driver-memory 3G --executor-memory 3G' Passim --n 4 --schema-path="Passim.schema" "passim_in.json" "passim-output/"
```
