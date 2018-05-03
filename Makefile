soups.csv:
	sqlite3 -csv soups.sqlite 'select * from soups;' > soups.csv
