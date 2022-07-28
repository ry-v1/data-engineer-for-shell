DROP TABLE dim_station

CREATE TABLE dim_station
WITH (HEAP, DISTRIBUTION = ROUND_ROBIN)  
AS 
SELECT
	station_id,
	name,
	latitude,
	longitude
FROM staging_station r
;
