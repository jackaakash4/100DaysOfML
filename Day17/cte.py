--CTE POWER(Common Table Expressions)

WITH cleaned_data AS (
    SELECT ...
    )

SELECT * 
FROM cleaned_data

--MULTIPLE CTE
WITH step1 AS (
        SELECT ...
    ),

step2 AS (
        SELECT ...
        FROM step1
    ),

step3 AS (
        SELECT ...
        FROM step2
    ),

SELECT *
FROM step3


