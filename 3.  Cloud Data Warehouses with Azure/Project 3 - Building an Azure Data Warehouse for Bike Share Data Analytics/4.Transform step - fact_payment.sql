DROP TABLE fact_payment

CREATE TABLE fact_payment
WITH (HEAP, DISTRIBUTION = ROUND_ROBIN)  
AS 
SELECT
    payment_id, 
    rider_id, 
    CONVERT(DATE, SUBSTRING(payment_date, 1, 10), 23) AS payment_date,
    CAST(amount AS money) AS amount
FROM staging_payment
;