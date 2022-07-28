DROP TABLE dim_dates
;
CREATE TABLE dim_dates (
    date_key datetime,
    year int,
    quarter int,
    month int,
    day int,
    weekday int,
    hour int
)
;
DECLARE @StartDate DATETIME
DECLARE @EndDate DATETIME
SET @StartDate = (SELECT MIN(TRY_CONVERT(datetime, LEFT(start_at, 19))) FROM staging_trip)
SET @EndDate = DATEADD(year, 10, (SELECT MAX(TRY_CONVERT(datetime, left(start_at, 19))) FROM staging_trip))

WHILE @StartDate <= @EndDate
      BEGIN
             INSERT INTO [dim_dates]
             SELECT
                   @StartDate,
                   DATEPART(year, @StartDate),
                   DATEPART(quarter, @StartDate),
                   DATEPART(month, @StartDate),
                   DATEPART(day, @StartDate),
                   DATEPART(weekday, @StartDate),
                   DATEPART(HOUR, @StartDate)

             SET @StartDate = DATEADD(dd, 1, @StartDate)
      END
;
SELECT top 10 * FROM dim_dates