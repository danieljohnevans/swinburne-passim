# swinburne-passim

### To run:

0. Ensure that `Passim` is installed and the path is correct. May need to reinstall `sbt` Use this [guide](https://programminghistorian.org/en/lessons/detecting-text-reuse-with-passim) if necessary.

1. First navigate to desired directory, replace `data/txt` and `data/sgml` navigate to `/code/` and run `main.py` to generate `passim_in.json`

2. Navigate up and create schema with `json-df-schema passim_in.json > Passim.schema.orig`

3. Once data is in proper format run `Passim` with:
```
SPARK_SUBMIT_ARGS='--master local[12] --driver-memory 8G --executor-memory 4G' passim --schema-path='Passim.schema.orig' --n 4 passim_in.json passim_output/
```
