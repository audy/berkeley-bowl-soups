soups.csv:
	sqlite3 -header -csv soups.sqlite 'select * from soups;' > soups.csv
