SELECT 
    MONTH(START_DATE) AS MONTH,
    CAR_ID,
    COUNT(*) AS RECORDS
FROM (
    SELECT *,
           COUNT(*) OVER (PARTITION BY CAR_ID) AS TOTAL_RENTALS
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
) AS SUB
WHERE TOTAL_RENTALS >= 5
GROUP BY MONTH(START_DATE), CAR_ID
ORDER BY MONTH ASC, CAR_ID DESC;
