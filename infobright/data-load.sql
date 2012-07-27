LOAD DATA INFILE '/home/alex/Development/SnowPlow/input-data.txt'
INTO TABLE events
FIELDS TERMINATED BY '\t' ENCLOSED BY 'NULL' 
LINES TERMINATED BY '\n' ;