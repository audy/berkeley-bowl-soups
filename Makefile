default: soups.csv soups.tidy.csv

soups.csv:
	sqlite3 -header -csv soups.sqlite 'select * from soups;' > soups.csv

soups.tidy.csv:
	./tidy-dump.py soups.sqlite > soups-tidy.csv
