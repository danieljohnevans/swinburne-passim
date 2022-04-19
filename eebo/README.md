### What

This is adopted from the accompanying code for the [ProgrammingHistorian lesson on passim](https://programminghistorian.org/en/lessons/detecting-text-reuse-with-passim). Code is [here](https://github.com/impresso/PH-Passim-tutorial).


- Python code to transform EEBO-TCP and txt is in `code`
- Data is in `data`:
	- `sgml` contains the original EEBO TCP files in SGML
	- `txt` contains the textual content of the SGML files 
- `ref` contains the 1904 Swinburne Anthology of Poetry 
- The already-prepared input file for passim is in this directory: `passim_in.json`. Due to size restrictions on Github's side, it is limited to 200 books picked randomly. A full compressed version is available as `passim_in.json.gz`.

### How-to

If you're only interested in trying out passim, simply use `passim_in.json`. If you want to play around with the code: 

- `python3 main.py` will transform SGML files into TXT if needed, and then create a `passim_in.json` file with all the books. 
- `python3 main.py INTEGER` (where `INTEGER` is an integer) will do as above, but will limit the number of books in the final `json` to whatever integer you specify.

### To run:

1. First navigate to /code/ and run `main.py`

2. Once data is in proper format run `Passim` with:
```
PARK_SUBMIT_ARGS='--master local[12] --driver-memory 3G --executor-memory 3G' Passim --n 4 --schema-path="Passim.schema" "passim_in.json" "passim-output/"
```

### References

Data from EEBO-TCP:
- EEBO-TCP. 2003-2019. Early English Books Online. eebo.chadwyck.com & https://www.textcreationpartnership.org/

Data from Gutenberg:
- http://www.gutenberg.org/ebooks/10


