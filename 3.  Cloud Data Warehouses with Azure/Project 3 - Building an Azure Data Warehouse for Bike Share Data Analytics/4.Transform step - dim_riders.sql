DROP TABLE dim_riders

CREATE TABLE dim_riders
WITH (HEAP, DISTRIBUTION = ROUND_ROBIN)  
AS 
SELECT
	rider_id,
	first_name,
	last_name,
	address,
	CONVERT(DATE, SUBSTRING(birthday, 1, 10), 23) 				AS birthday,
	CONVERT(DATE, SUBSTRING(account_start_date, 1, 10), 23) 	AS account_start_date,
	CONVERT(DATE, SUBSTRING(account_end_date, 1, 10), 23) 		AS account_end_date,
    DATEDIFF(year, 
        CONVERT(DATE, SUBSTRING(birthday, 1, 10), 23),
        CONVERT(DATE, SUBSTRING(account_start_date, 1, 10), 23)
        ) 														AS rider_age_at_account_start,
	is_member
FROM staging_rider r
;
