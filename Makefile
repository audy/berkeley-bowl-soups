default: soups.csv soups.tidy.csv Rplots.pdf

soups.csv:
	sqlite3 -header -csv soups.sqlite 'select * from soups;' > soups.csv

soups.tidy.csv:
	./tidy-dump.py soups.sqlite soups-tidy.csv

Rplots.pdf:
	Rscript soups-analysis.R
