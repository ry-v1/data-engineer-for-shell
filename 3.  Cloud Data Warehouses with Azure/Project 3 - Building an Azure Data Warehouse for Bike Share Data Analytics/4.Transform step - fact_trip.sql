-- DROP TABLE IF EXISTS fact_trip

CREATE TABLE fact_trip
WITH (HEAP, DISTRIBUTION = ROUND_ROBIN)  
AS 
SELECT 
    trip_id,
    t.rider_id                                              AS rider_id,
    CONVERT(Datetime, SUBSTRING(start_at, 1, 19), 120)      AS start_at,
    CONVERT(Datetime, SUBSTRING(ended_at, 1, 19), 120)      AS ended_at,
    start_station_id,
    end_station_id,
    rideable_type,
    DATEDIFF(year, 
        CONVERT(DATE, SUBSTRING(birthday, 1, 10), 23),
        CONVERT(DATE, SUBSTRING(start_at, 1, 10), 23)
        )                                                   AS rider_age_at_trip_start,
    DATEDIFF(mi, 
        CONVERT(Datetime, SUBSTRING(start_at, 1, 19), 120),
        CONVERT(Datetime, SUBSTRING(ended_at, 1, 19), 120)
        )                                                   AS duration_minutes
FROM dbo.staging_trip t
JOIN dbo.staging_rider r
    ON t.rider_id = r.rider_id

SELECT TOP 10 * FROM fact_trip